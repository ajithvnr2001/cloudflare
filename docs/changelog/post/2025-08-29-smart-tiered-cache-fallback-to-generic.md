---
url: https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/
title: Smart Tiered Cache Fallback to Generic \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:21.105992+00:00
---

# Smart Tiered Cache Fallback to Generic · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 29, 2025

## Smart Tiered Cache Fallback to Generic

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#smart-tiered-cache) now falls back to [Generic Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) when the origin location cannot be determined, improving cache precision for your content.

Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.

#### How it works

When Smart Tiered Cache falls back to Generic Tiered Cache:

  1. **Multiple upper-tiers** : Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.
  2. **Distributed cache requests** : Lower-tier data centers can query any available upper-tier for cached content.
  3. **Improved global coverage** : Provides better cache hit ratios across geographically distributed visitors.
  4. **Automatic fallback** : Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.



#### Benefits

  * **Preserves high performance during fallback** : Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.
  * **Minimizes latency impact** : Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.
  * **Seamless experience** : No configuration changes or intervention required when fallback occurs.
  * **Improved resilience** : Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.



#### Get started

This improvement is automatically applied to all zones using [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/). No action is required on your part.
