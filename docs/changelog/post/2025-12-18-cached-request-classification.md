---
url: https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/
title: Improved accuracy of cached request classification in analytics \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.642792+00:00
---

# Improved accuracy of cached request classification in analytics · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## Improved accuracy of cached request classification in analytics

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.

Previously, requests were classified as "cached" based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.

The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in [HTTP Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/), so only requests genuinely served from cache are counted as cached.

**What changed:**

  * **Zone Overview** — Cache ratios now reflect actual cache performance.
  * **HTTP Analytics** — No change. HTTP Analytics already used the correct classification logic.
  * **Historical data** — This fix applies to new requests only. Previously logged data is not retroactively updated.


