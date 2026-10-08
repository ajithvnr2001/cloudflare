#!/usr/bin/env python3
"""Incremental update: crawl only new docs without recrawling existing ones.
Compares live sitemaps vs docs/_index.jsonl, fetches only missing URLs.
Usage:
  python3 update_incremental.py --check-only   # list what is new, no fetch
  python3 update_incremental.py                # fetch new only
  python3 update_incremental.py --force URL    # refetch single URL
"""
import argparse, json, os, re, pathlib, asyncio, sys
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crawl_cloudflare as C

DOCS = C.OUT_ROOT
STATE = C.STATE_FILE

def canon_dev(u):
    abs_u, _ = urldefrag(urljoin("https://developers.cloudflare.com", u.strip()))
    from urllib.parse import urlparse as up
    p = up(abs_u); path = p.path
    if path.endswith("/index.md"): path = path[:-len("/index.md")] + "/"
    elif path.endswith("/index"): path = path[:-len("/index")] + "/"
    elif path in ("/index.md", "/index"): path = "/"
    elif path.endswith(".md"): path = path[:-3] + ("" if path[:-3].endswith("/") else "/")
    c = f"{p.scheme}://{p.netloc}{path}"
    if not c.endswith("/") and "." not in c.rsplit("/", 1)[-1]: c += "/"
    return c

async def live_sitemap_urls():
    import httpx, xml.etree.ElementTree as ET
    out = {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        # developers
        r = await c.get("https://developers.cloudflare.com/sitemap-0.xml", timeout=30); r.raise_for_status()
        locs = re.findall(r"<loc>([^<]+)</loc>", r.text)
        out["developers"] = sorted({canon_dev(u) for u in locs if C.normalize_url(u)})
        # blog
        r = await c.get("https://blog.cloudflare.com/sitemap-posts.xml", timeout=30); r.raise_for_status()
        bloc = re.findall(r"<loc>([^<]+)</loc>", r.text)
        bset = set()
        for u in bloc:
            abs_u, _ = urldefrag(urljoin("https://blog.cloudflare.com", u))
            p = urlparse(abs_u); cc = f"{p.scheme}://{p.netloc}{p.path}"
            if not cc.endswith("/") and "." not in cc.rsplit("/", 1)[-1]: cc += "/"
            n = C.normalize_url(cc)
            if n and ".json" not in n and "`" not in n: bset.add(n)
        out["blog"] = sorted(bset)
        # www (regex, includes xhtml alternates -> dedupe via canon)
        r = await c.get("https://www.cloudflare.com/sitemap.xml", timeout=30); r.raise_for_status()
        wloc = re.findall(r"<loc>([^<]+)</loc>", r.text)
        out["www"] = sorted({C.normalize_url(u) for u in wloc if C.normalize_url(u)})
        out["www"] = [u for u in out["www"] if u]
    return out

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--force", default=None, help="refetch single URL")
    ap.add_argument("--concurrency", type=int, default=10)
    a = ap.parse_args()
    idx = [json.loads(l) for l in open(DOCS / "_index.jsonl")]
    indexed = set(r["url"] for r in idx)
    # encoding-aware set for %40cf vs @cf dupes
    from urllib.parse import unquote
    indexed_dec = {unquote(u) for u in indexed}
    live = await live_sitemap_urls()
    print({k: len(v) for k, v in live.items()}, f"indexed={len(indexed)}")
    new = {}
    for k, urls in live.items():
        miss = [u for u in urls if u not in indexed and unquote(u) not in indexed_dec and ".json" not in u and "`" not in u]
        new[k] = miss
        print(f"{k}: live={len(urls)} new={len(miss)}")
        for u in miss[:20]: print(f"  NEW: {u}")
        if len(miss) > 20: print(f"  ... +{len(miss)-20} more")
    total_new = sum(len(v) for v in new.values())
    if a.force:
        targets = [canon_dev(a.force) if "developers" in a.force else C.normalize_url(a.force)]
        print(f"force: {targets}")
    else:
        targets = [u for v in new.values() for u in v]
    if a.check_only or not targets:
        print("check-only" if a.check_only else "no new docs — all up to date")
        return
    print(f"fetching {len(targets)} new docs...")
    st = json.load(open(STATE)); visited_state, failed = st.get("visited", {}), st.get("failed", {})
    from datetime import datetime, timezone
    idx_f = open(DOCS / "_index.jsonl", "a", encoding="utf-8")
    sem = asyncio.Semaphore(a.concurrency)
    ok = fail = 0
    async def one(url):
        nonlocal ok, fail
        async with sem:
            try:
                data = await C.fetch_one(url)
                rel = C.url_to_relpath(url); fp = DOCS / rel
                fp.parent.mkdir(parents=True, exist_ok=True)
                fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                fp.write_text(fm + data["markdown"], encoding="utf-8")
                mr = pathlib.Path("_meta") / rel.with_suffix(".json")
                (DOCS / mr).parent.mkdir(parents=True, exist_ok=True)
                (DOCS / mr).write_text(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"], "fetched_at": datetime.now(timezone.utc).isoformat()}, indent=2))
                visited_state[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                ok += 1; print(f"[new] {url} -> {rel}")
            except Exception as e:
                failed[url] = str(e)[:300]; fail += 1; print(f"[fail] {url}: {e}")
    await asyncio.gather(*(one(u) for u in targets))
    idx_f.close()
    try:
        if C._crawler is not None: await C._crawler.close()
    except Exception: pass
    open(STATE, "w").write(json.dumps({"visited": visited_state, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
    print(f"done: ok={ok} fail={fail}")

if __name__ == "__main__":
    asyncio.run(main())
