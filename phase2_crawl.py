#!/usr/bin/env python3
"""Phase 2: recrawl 73 missing + deep blog/www subdomain crawl. Reuses phase-1 fetchers."""
import asyncio, json, re, pathlib, sys
from urllib.parse import urlparse
sys.path.insert(0, "/data/opencode/cloudflare")
import crawl_cloudflare as C

DOCS = C.OUT_ROOT
BLOCKED_HOSTS = {"community.cloudflare.com", "dash.cloudflare.com", "support.cloudflare.com", "radar.cloudflare.com"}

async def load_seeds():
    seeds = []
    # 1. missing 71+2
    try:
        miss = [l.strip() for l in open("/tmp/phase2_missing.txt") if l.strip()]
        # drop blocked dash http variants? keep but will fast-fail
        seeds += miss
        print(f"[phase2] missing seeds {len(miss)}")
    except Exception as e: print("missing load err", e)
    # 2. blog posts
    import httpx, xml.etree.ElementTree as ET
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        for sm_url, name in [
            ("https://blog.cloudflare.com/sitemap-posts.xml", "blog-posts"),
            ("https://www.cloudflare.com/sitemap.xml", "www"),
        ]:
            try:
                r = await c.get(sm_url, timeout=30); r.raise_for_status()
                root = ET.fromstring(r.text)
                ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = [e.find("s:loc", ns).text for e in root.findall("s:url", ns) if e.find("s:loc", ns) is not None]
                # www sitemap uses different ns? fallback regex
                if not locs:
                    locs = re.findall(r"<loc>([^<]+)</loc>", r.text)
                print(f"[phase2] {name}: {len(locs)} sitemap urls")
                for u in locs:
                    n = C.normalize_url(u)
                    if n and ".json" not in n and "`" not in n and "%60" not in n:
                        seeds.append(n)
            except Exception as e: print(f"[phase2] {name} failed: {e}")
    # dedupe, drop already-indexed/excluded/sitemap-junk
    idx_urls = set(json.loads(l)["url"] for l in open(DOCS / "_index.jsonl"))
    excl_urls = set(r["url"] for r in json.loads(open(DOCS / "_excluded" / "reasons.json").read()))
    out, seen = [], set()
    for u in seeds:
        if u in seen or u in idx_urls or u in excl_urls: continue
        if ".json" in u or "`" in u or "%60" in u: continue
        seen.add(u); out.append(u)
    print(f"[phase2] total seeds {len(seeds)} -> todo {len(out)} (skip indexed {len(seeds)-len(out)})")
    return out

async def fetch_fast(url):
    host = urlparse(url).netloc
    if host in BLOCKED_HOSTS:
        # fast fail: try scrapling once, no crawl4ai 25s retry
        try:
            r = await asyncio.to_thread(C.scrapling_fetch_sync, url)
            html = r["html"]; main_html, pt = C.extract_main_content_html(html, url)
            md = f"# {r['title'] or pt or url}\n\n> Source: {url}\n\n" + C.scrapegraph_markdown(main_html, url)
            return {"url": url, "title": r["title"] or pt or url, "html": html, "markdown": md, "links": r["links"], "method": "scrapling+scrapegraph"}
        except Exception as e:
            raise RuntimeError(f"blocked-host fast-fail {host}: {e}")
    return await C.fetch_one(url)

async def main(concurrency=15, max_pages=12000):
    seeds = await load_seeds()
    queue = asyncio.Queue()
    queued = set()
    for u in seeds:
        if u not in queued:
            await queue.put((u, 0)); queued.add(u)
    visited = {json.loads(l)["url"]: True for l in open(DOCS / "_index.jsonl")}
    st = json.load(open("/data/opencode/cloudflare/crawl_state.json"))
    failed = st.get("failed", {}); visited_state = st.get("visited", {})
    idx_f = open(DOCS / "_index.jsonl", "a", encoding="utf-8")
    sem = asyncio.Semaphore(concurrency)
    stats = {"ok": 0, "fail": 0}
    from datetime import datetime, timezone
    async def worker():
        while True:
            try: url, depth = queue.get_nowait()
            except asyncio.QueueEmpty: return
            if url in visited:
                queue.task_done(); continue
            if len(visited) >= max_pages + 9325:  # cap new pages
                queue.task_done(); continue
            rel = C.url_to_relpath(url); fpath = DOCS / rel
            if fpath.exists() and fpath.stat().st_size > 500:
                visited[url] = True; queue.task_done(); continue
            async with sem:
                try:
                    data = await fetch_fast(url)
                    fpath.parent.mkdir(parents=True, exist_ok=True)
                    fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                    fpath.write_text(fm + data["markdown"], encoding="utf-8")
                    meta_rel = pathlib.Path("_meta") / (rel.with_suffix(".json"))
                    (DOCS / meta_rel).parent.mkdir(parents=True, exist_ok=True)
                    (DOCS / meta_rel).write_text(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"], "fetched_at": datetime.now(timezone.utc).isoformat(), "html_len": len(data.get("html","")), "md_len": len(data.get("markdown","")), "depth": depth, "phase": 2}, indent=2))
                    visited[url] = True; visited_state[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                    idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                    stats["ok"] += 1
                    for href in data.get("links", [])[:500]:
                        n = C.normalize_url(href, base=url)
                        if not n or n in visited or n in queued: continue
                        if ".json" in n or "`" in n or "%60" in n: continue
                        nh = urlparse(n).netloc
                        if nh in BLOCKED_HOSTS: continue  # don't expand blocked
                        if nh != "developers.cloudflare.com" and nh != urlparse(url).netloc and depth+1 > 2: continue
                        if len(queued) > max_pages: break
                        queued.add(n); await queue.put((n, depth+1))
                    if stats["ok"] % 100 == 0:
                        print(f"[phase2 progress] ok={stats['ok']} fail={stats['fail']} queue={queue.qsize()} total_visited={len(visited)}", flush=True)
                        open("/data/opencode/cloudflare/crawl_state.json","w").write(json.dumps({"visited": visited_state, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
                except Exception as e:
                    failed[url] = str(e)[:300]; stats["fail"] += 1
                finally: queue.task_done()
    tasks = [asyncio.create_task(worker()) for _ in range(concurrency)]
    while True:
        await asyncio.sleep(2)
        if queue.empty():
            await asyncio.sleep(4)
            if queue.empty(): break
    for t in tasks: t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    idx_f.close()
    try:
        if C._crawler is not None: await C._crawler.close()
    except Exception: pass
    open("/data/opencode/cloudflare/crawl_state.json","w").write(json.dumps({"visited": visited_state, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
    print(f"[phase2 done] ok={stats['ok']} fail={stats['fail']} total_visited={len(visited)}")

if __name__ == "__main__":
    asyncio.run(main())
