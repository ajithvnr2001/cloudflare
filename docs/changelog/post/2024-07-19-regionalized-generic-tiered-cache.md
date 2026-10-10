---
url: https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/
title: Regionalized Generic Tiered Cache for higher hit ratios \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:56.183106+00:00
---

# Regionalized Generic Tiered Cache for higher hit ratios · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 19, 2024

## Regionalized Generic Tiered Cache for higher hit ratios

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now achieve higher cache hit ratios with [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache). Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.

#### How it works

Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:

  * Same content always routes to the same upper-tier data center within a region.
  * Eliminates redundant copies across multiple upper-tier caches.
  * Increases the likelihood of cache HITs for the same content.



#### Example

A popular image requested from multiple edge locations in a region:

  * **Before** : Cached at 3-4 different upper-tier data centers
  * **After** : Cached at 1 designated upper-tier data center
  * **Result** : 3-4x fewer cache MISSes, reducing origin load and improving performance



#### Get started

To get started, enable [Generic Global Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/#generic-global-tiered-cache) on your zone.
