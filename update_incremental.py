#!/usr/bin/env python3
"""Incremental update: crawl new docs AND refetch pages updated upstream.
Compares live sitemaps vs docs/_index.jsonl (new URLs) plus sitemap
<lastmod> vs _meta fetched_at (changed pages, newest-first, capped).
Usage:
  python3 update_incremental.py --check-only   # list new + stale, no fetch
  python3 update_incremental.py                # fetch new + refresh stale
  python3 update_incremental.py --force URL    # refetch single URL
"""
import argparse, json, os, re, pathlib, asyncio, sys
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crawl_cloudflare as C

DOCS = C.OUT_ROOT
STATE = C.STATE_FILE
REFRESH_CAP = 0  # 0 = no cap: refresh ALL stale pages per run (newest first)

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
    lastmod = {}  # canon url -> sitemap lastmod string
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        # developers
        r = await c.get("https://developers.cloudflare.com/sitemap-0.xml", timeout=30); r.raise_for_status()
        locs = re.findall(r"<loc>([^<]+)</loc>", r.text)
        out["developers"] = sorted({canon_dev(u) for u in locs if C.normalize_url(u)})
        for u, d in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", r.text):
            n = canon_dev(u)
            if n and (n not in lastmod or d > lastmod[n]): lastmod[n] = d
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
        for u, d in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", r.text):
            abs_u, _ = urldefrag(urljoin("https://blog.cloudflare.com", u))
            p = urlparse(abs_u); cc = f"{p.scheme}://{p.netloc}{p.path}"
            if not cc.endswith("/") and "." not in cc.rsplit("/", 1)[-1]: cc += "/"
            n = C.normalize_url(cc)
            if n and (n not in lastmod or d > lastmod[n]): lastmod[n] = d
        # www (regex, includes xhtml alternates -> dedupe via canon)
        r = await c.get("https://www.cloudflare.com/sitemap.xml", timeout=30); r.raise_for_status()
        wloc = re.findall(r"<loc>([^<]+)</loc>", r.text)
        out["www"] = sorted({C.normalize_url(u) for u in wloc if C.normalize_url(u)})
        out["www"] = [u for u in out["www"] if u]
    return out, lastmod

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
    live, lastmod = await live_sitemap_urls()
    print({k: len(v) for k, v in live.items()}, f"indexed={len(indexed)}")
    new = {}
    for k, urls in live.items():
        miss = [u for u in urls if u not in indexed and unquote(u) not in indexed_dec and ".json" not in u and "`" not in u]
        new[k] = miss
        print(f"{k}: live={len(urls)} new={len(miss)}")
        for u in miss[:20]: print(f"  NEW: {u}")
        if len(miss) > 20: print(f"  ... +{len(miss)-20} more")
    total_new = sum(len(v) for v in new.values())
    # stale: sitemap lastmod newer than our _meta fetched_at (newest first, capped)
    stale = []
    for mfile in (DOCS / "_meta").rglob("*.json"):
        try:
            m = json.loads(mfile.read_text())
        except Exception:
            continue
        u, fa = m.get("url"), m.get("fetched_at")
        d = lastmod.get(u) if u else None
        if not u or not fa or not d:
            continue
        if u in set(sum(new.values(), [])):
            continue
        try:
            from datetime import datetime as _dt
            if _dt.fromisoformat(d.replace("Z", "+00:00")) > _dt.fromisoformat(fa):
                stale.append((d, u))
        except Exception:
            pass
    stale.sort(reverse=True)
    refresh = [u for _, u in stale] if not REFRESH_CAP else [u for _, u in stale[:REFRESH_CAP]]
    print(f"stale (sitemap newer than fetched): {len(stale)}, refreshing newest {len(refresh)}")
    for d, u in stale[:10]: print(f"  STALE {d} {u}")
    if not a.check_only:
        # daily verification stamp (committed even when nothing new)
        from datetime import datetime as _dt, timezone as _tz
        _now = _dt.now(_tz.utc)
        _stamp = {"date": _now.strftime("%F"), "at": _now.isoformat(),
                  "new": {k: len(v) for k, v in new.items()},
                  "refreshed": len(refresh), "stale_total": len(stale),
                  "total_index": len(indexed)}
        (DOCS / "_last_verified.json").write_text(json.dumps(_stamp, indent=2))
        try:
            _mp = DOCS / "_manifest.json"
            _m = json.loads(_mp.read_text()) if _mp.exists() else {}
            _m["last_verified"] = _stamp["date"]
            _m["generated_at"] = _stamp["at"]
            _mp.write_text(json.dumps(_m, indent=2))
        except Exception as e:
            print("stamp manifest skip:", e)
        print(f"stamped {_stamp['date']} (new={total_new} refresh={len(refresh)})")
    if a.force:
        targets = [canon_dev(a.force) if "developers" in a.force else C.normalize_url(a.force)]
        print(f"force: {targets}")
        refresh_urls = set()
    else:
        targets = [u for v in new.values() for u in v] + refresh
        refresh_urls = set(refresh)
    if a.check_only or not targets:
        print("check-only" if a.check_only else "no new docs — all up to date")
        return
    print(f"fetching {len(targets)} docs ({total_new} new + {len(refresh)} refresh)...")
    st = json.load(open(STATE)) if STATE.exists() else {"visited": {}, "failed": {}}
    visited_state, failed = st.get("visited", {}), st.get("failed", {})
    from datetime import datetime, timezone
    lines = [json.loads(l) for l in open(DOCS / "_index.jsonl")]
    if len({r["url"] for r in lines}) != len(lines):  # drop dupes from legacy appends
        seen, ded = set(), []
        for r in reversed(lines):
            if r["url"] not in seen:
                seen.add(r["url"]); ded.append(r)
        lines = list(reversed(ded))
        print(f"deduped index {len(seen)} unique")
    pos = {r["url"]: i for i, r in enumerate(lines)}
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
                row = {"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}
                if url in pos:
                    lines[pos[url]] = row
                    print(f"[refresh] {url} -> {rel}")
                else:
                    pos[url] = len(lines); lines.append(row)
                    print(f"[new] {url} -> {rel}")
                ok += 1
            except Exception as e:
                failed[url] = str(e)[:300]; fail += 1; print(f"[fail] {url}: {e}")
    await asyncio.gather(*(one(u) for u in targets))
    (DOCS / "_index.jsonl").write_text("".join(json.dumps(r) + "\n" for r in lines))
    try:
        if C._crawler is not None: await C._crawler.close()
    except Exception: pass
    open(STATE, "w").write(json.dumps({"visited": visited_state, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
    print(f"done: ok={ok} fail={fail}")

if __name__ == "__main__":
    asyncio.run(main())
