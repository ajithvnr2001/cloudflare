#!/usr/bin/env python3
"""Coder: incremental update without recrawling.
Compares live sitemaps to docs/_index.jsonl, prints/fetches only NEW urls.
Usage:
  python3 coder_update.py --check-only
  python3 coder_update.py --run --concurrency 10
"""
import argparse, pathlib, json, re, asyncio, pathlib, sys
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guide_code.coder_scrape import scrape
import crawl_cloudflare as C

DOCS = pathlib.Path("/data/opencode/cloudflare/docs")

async def live():
    import httpx
    out = {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        r = await c.get("https://developers.cloudflare.com/sitemap-0.xml"); r.raise_for_status()
        out["dev"] = {C.normalize_url(u) for u in re.findall(r"<loc>([^<]+)</loc>", r.text) if C.normalize_url(u)}
        r = await c.get("https://blog.cloudflare.com/sitemap-posts.xml"); r.raise_for_status()
        out["blog"] = {C.normalize_url(urljoin("https://blog.cloudflare.com", u)) for u in re.findall(r"<loc>([^<]+)</loc>", r.text) if C.normalize_url(urljoin("https://blog.cloudflare.com", u))}
        r = await c.get("https://www.cloudflare.com/sitemap.xml"); r.raise_for_status()
        out["www"] = {C.normalize_url(u) for u in re.findall(r"<loc>([^<]+)</loc>", r.text) if C.normalize_url(u)}
    return out

async def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check-only", action="store_true"); ap.add_argument("--run", action="store_true"); ap.add_argument("--concurrency", type=int, default=10)
    a = ap.parse_args()
    indexed = {json.loads(l)["url"] for l in open(DOCS/"_index.jsonl")}
    from urllib.parse import unquote
    idec = {unquote(u) for u in indexed}
    lv = await live()
    new = [u for vs in lv.values() for u in vs if u not in indexed and unquote(u) not in idec and ".json" not in u and "`" not in u]
    print({k: len(v) for k, v in lv.items()}, f"indexed={len(indexed)} new={len(new)}")
    for u in new[:20]: print(" NEW:", u)
    if a.check_only or not a.run or not new: return
    sem = asyncio.Semaphore(a.concurrency); idx = open(DOCS/"_index.jsonl", "a")
    async def one(u):
        async with sem:
            md, title, method = await scrape(u)
            rel = C.url_to_relpath(u); (DOCS/rel).parent.mkdir(parents=True, exist_ok=True)
            (DOCS/rel).write_text(md)
            idx.write(json.dumps({"url": u, "file": str(rel), "title": title, "method": method})+"\n")
            print("[ok]", u)
    await asyncio.gather(*(one(u) for u in new)); idx.close()

if __name__ == "__main__": asyncio.run(main())
