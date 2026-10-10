---
url: https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/
title: Smart Tiered Cache automatically optimizes R2 caching \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.773228+00:00
---

# Smart Tiered Cache automatically optimizes R2 caching · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2024

## Smart Tiered Cache automatically optimizes R2 caching

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now reduce latency and lower R2 egress costs automatically when using [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) with [R2](https://developers.cloudflare.com/r2/). Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.

#### How it works

When you enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) for zones using [R2](https://developers.cloudflare.com/r2/) as an origin, Cloudflare automatically:

  1. **Identifies your R2 bucket location** : Determines the geographical region where your R2 bucket is stored.
  2. **Selects an optimal Upper Tier** : Chooses a data center close to your bucket as the common Upper Tier cache.
  3. **Routes requests efficiently** : All cache misses in edge locations route through this Upper Tier before reaching R2.



#### Benefits

  * **Automatic optimization** : No manual configuration required.
  * **Lower egress costs** : Fewer requests to R2 reduce egress charges.
  * **Improved hit ratio** : Common Upper Tier increases cache efficiency.
  * **Reduced latency** : Upper Tier proximity to R2 minimizes fetch times.



#### Get started

To get started, enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) on your zone using R2 as an origin.
