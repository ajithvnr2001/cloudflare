---
url: https://developers.cloudflare.com/videos/set-up-cf-tunnel/
title: Set up Cloudflare Tunnel | Cloudflare Docs
method: httpx+scrapegraph (scrapling: scrapling thin content (251 chars), fallback to crawl4ai | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 632 in wrap_api_call (../../../../../opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/playwright/_impl/_connection.py):
Error: BrowserContext.new_page: Target page, context or browser has been closed

Code context:
 627           )
 628           self._api_zone.set(parsed_st)
 629           try:
 630               return await cb()
 631           except Exception as error:
 632 →             raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
 633           finally:
 634               self._api_zone.set(None)
 635   
 636       def wrap_api_call_sync(
 637           self, cb: Callable[[], Any], is_internal: bool = False, title: str = None)
fetched_at: 2026-10-10T14:37:28.807117+00:00
---

# Set up Cloudflare Tunnel | Cloudflare Docs

> Source: https://developers.cloudflare.com/videos/set-up-cf-tunnel/

# Set up Cloudflare Tunnel

Set up Cloudflare Tunnel to create a secure link between your private environment and the Cloudflare edge.
