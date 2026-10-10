---
url: https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/
title: APO caches more crawler and bot traffic again \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.078836+00:00
---

# APO caches more crawler and bot traffic again · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 27, 2026

## APO caches more crawler and bot traffic again

[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit `Accept: text/html` header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (`cf-cache-status: DYNAMIC`) instead of the cache.

APO now caches these requests again. No action is needed. If you added a Transform Rule to set `Accept: text/html` as a workaround, you can remove it.

For details on how APO decides what to cache, refer to [About APO](https://developers.cloudflare.com/automatic-platform-optimization/about/).
