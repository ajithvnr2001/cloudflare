# Guide: scrape + update Cloudflare docs (coder end-to-end)

Folder: `/data/opencode/cloudflare/` · Docs: `docs/` (**21,256 md, 813M, verified 0 new**) · Full crawler: `crawl_cloudflare.py`, `phase2_crawl.py` · Updater: `update_incremental.py`

## 1. Scrape one page (all 3 libs)
`guide_code/coder_scrape.py` = Scrapling → Crawl4AI → ScrapeGraphAI.
```bash
python3 guide_code/coder_scrape.py https://developers.cloudflare.com/workers/ /tmp/workers.md
python3 guide_code/coder_scrape.py https://blog.cloudflare.com/agentic-web /tmp/blog.md
```
Flow: `Fetcher.get(stealthy_headers=True)` (`coder_scrape.py:19`) → keep `<main>/<article>` → `scrapegraph-ai/utils/convert_to_md.py::convert_to_md` → fallback `AsyncWebCrawler(CacheMode.BYPASS)` (`coder_scrape.py:34`). Verified: 5,420 chars via `scrapling+scrapegraph`.

## 2. Full crawl (done, reproducible)
```bash
python3 crawl_cloudflare.py --max-pages 15000 --concurrency 15   # developers 8729/8729
python3 phase2_crawl.py                                          # blog 7972/7972 + www 907/907
```
Seeds = `sitemap-0.xml` + `llms.txt`→`llms-full.txt` + sitemap-posts/www; `normalize_url()` canonicalizes `/index.md`→`/`, skips `.json`/backtick/binary, allows `*.cloudflare.com` (`crawl_cloudflare.py:80`). Saves `docs/<path>.md` + `_meta/*.json`, appends `_index.jsonl`. Current: dev 9143, blog 10735, www 1326.

## 3. Update without recrawling (incremental)
```bash
python3 update_incremental.py --check-only   # diff live sitemaps vs _index.jsonl (last: new=0)
python3 update_incremental.py                # fetch only NEW (prev run: 6 blog i18n, 6/6 ok)
python3 update_incremental.py --force <URL>  # refetch one changed page
# coder minimal version:
python3 guide_code/coder_update.py --check-only
python3 guide_code/coder_update.py --run --concurrency 10
```
Live set − indexed set (encoding-aware `%40cf`/`@cf`) = targets; existing files never touched (`update_incremental.py:40`). State in `crawl_state.json`.

## 4. Verify (all green)
```bash
python3 update_incremental.py --check-only   # expect dev/blog/www new=0
cat docs/_manifest.json                      # 21256 docs, 100% sitemaps, junk 0
```
Blocked (expected): `community/dash/support/radar` 403/JS-challenge → `failed`. Junk → `docs/_excluded/`.

## 5. Cron
`0 2 * * * cd /data/opencode/cloudflare && python3 update_incremental.py >> update.log 2>&1`
