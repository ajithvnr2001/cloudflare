# Cloudflare Developer Docs — End-to-End Crawler

Crawls **https://developers.cloudflare.com/** completely (sitemap + `llms.txt` + subdomains) and saves clean markdown docs. Three stacks combined: **Scrapling** (fast fetch) → **Crawl4AI** (JS fallback) → **ScrapeGraphAI** (HTML→MD, local, no LLM key needed).

## Results (verified)

> Last verified: 2026-10-10 — see `docs/_last_verified.json` (rewritten daily by GitHub Actions).

| Scope | Coverage |
|---|---|
| developers `sitemap-0.xml` | 8730/8730 = 100% |
| blog `sitemap-posts.xml` | 7966/7966 = 100% |
| www `sitemap.xml` | 907/907 = 100% |
| Total | **21,263 md / 813M** (dev 9144, blog 10741, www 1326, +15 hosts) |

Junk 0 (697 `.json`/backtick/404 moved to `docs/_excluded/`). Blocked: `community/dash/support/radar` (403/JS-challenge, logged). Local docs excluded from git (813M) — regenerate with one command below.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install crawl4ai scrapling scrapegraphai beautifulsoup4 lxml html2text httpx
python3 -c "from crawl4ai import AsyncWebCrawler"  # browsers bundled
# optional source clones (code already imports pip packages):
git clone --depth 1 https://github.com/ScrapeGraphAI/Scrapegraph-ai tools/scrapegraph-ai
git clone --depth 1 https://github.com/unclecode/crawl4AI tools/crawl4AI
git clone --depth 1 https://github.com/D4Vinci/Scrapling tools/scrapling
```

## Run

```bash
# full crawl (resume-safe, ~25 min at --concurrency 15)
python3 crawl_cloudflare.py --max-pages 15000 --concurrency 15
# phase 2 subdomains (blog/www)
python3 phase2_crawl.py
# steady state — NEW pages + refreshes ALL sitemap-updated pages (newest first), never blind-recrawls
python3 update_incremental.py --check-only
python3 update_incremental.py
python3 update_incremental.py --force <URL>
```

Rerun is a verified no-op (5 s, visited unchanged). Cron: `0 2 * * * cd <repo> && python3 update_incremental.py >> update.log 2>&1`.

## How it works

1. **Seed**: `sitemap-index.xml` → `sitemap-0.xml` (8730) + root `llms.txt` → ~200 product `llms.txt`/`llms-full.txt` → dedupe with canonicalization (`/index.md`→`/`, `%40cf`/`@cf` aware) → ~9108 seeds.
2. **Fetch per URL**: Scrapling `Fetcher.get(stealthy_headers=True)` → keep `<main>/<article>` → ScrapeGraphAI `convert_to_md`; if thin/failed → Crawl4AI `AsyncWebCrawler` → httpx fallback. Frontmatter `url/title/method/fetched_at` + `# title` + `> Source:` header.
3. **Expand**: normalize `<a href>`, allow `*.cloudflare.com` (main unlimited depth, subdomains ≤4), cap 15000.
4. **Output**: `docs/<path>.md`, `_meta/*.json`, `_index.jsonl`, `_manifest.json`, `_llms/`, `crawl_state.json`.

## Verify

```bash
python3 update_incremental.py --check-only   # expect new=0
find docs -name '*.md' | wc -l
cat docs/_manifest.json
```

## Layout

```
crawl_cloudflare.py  phase2_crawl.py  phase2_cleanup.py  update_incremental.py
guide_code/          # coder guide + coder_scrape.py / coder_update.py (runnable)
docs/                # full crawl output (committed: 21,256 files, all <15MB)
tools/               # git-ignored optional clones
```

## Limits

- `community/dash/support` login/anti-bot walled → recorded in `failed`, not silently dropped.
- ScrapeGraphAI used for local `cleanup_html`/`convert_to_md` (its LLM graphs need keys; not required here).
