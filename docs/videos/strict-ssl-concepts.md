---
url: https://developers.cloudflare.com/videos/strict-ssl-concepts/
title: SSL/TLS concepts | Cloudflare Docs
method: httpx+scrapegraph (scrapling: scrapling thin content (201 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 778 in _crawl_web (../../../../../opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/crawl4ai/async_crawler_strategy.py):
Error: Failed on navigating ACS-GOTO:
Page.goto: net::ERR_ABORTED; maybe frame was detached?
Call log:
  - navigating to "https://developers.cloudflare.com/videos/strict-ssl-concepts/", waiting until "domcontentloaded"


Code context:
 773                                   tag="GOTO",
 774                                   params={"url": url},
 775                               )
 776                               response = None
 777                           else:
 778 →                             raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
 779   
 780                       # ──────────────────────────────────────────────────────────────
 781                       # Walk the redirect chain.  Playwright returns only the last
 782                       # hop, so we trace the `request.redirected_from` links until the
 783                       # first response that differs from the final one and surface its)
fetched_at: 2026-10-10T14:37:28.806363+00:00
---

# SSL/TLS concepts | Cloudflare Docs

> Source: https://developers.cloudflare.com/videos/strict-ssl-concepts/

# SSL/TLS concepts

In this video, learn the key concepts relevant to Cloudflare SSL/TLS.
