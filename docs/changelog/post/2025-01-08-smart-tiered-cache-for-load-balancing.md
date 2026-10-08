---
url: https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/
title: Smart Tiered Cache optimizes Load Balancing Pools \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:00.704765+00:00
---

# Smart Tiered Cache optimizes Load Balancing Pools · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 8, 2025

## Smart Tiered Cache optimizes Load Balancing Pools

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now achieve higher cache hit rates and reduce origin load when using [Load Balancing](https://developers.cloudflare.com/load-balancing/) with [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/). Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.

#### How it works

When you use [Load Balancing](https://developers.cloudflare.com/load-balancing/) with [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/), Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:

  * **Consistent cache location** : All origins in the pool share the same Upper Tier cache.
  * **Higher HIT rates** : Requests for the same content hit the cache more frequently.
  * **Reduced origin requests** : Fewer requests reach your origin servers.
  * **Improved performance** : Faster response times for cache HITs.



#### Example workflow
    
    
    Load Balancing Pool: api-pool
    ├── Origin 1: api-1.example.com
    ├── Origin 2: api-2.example.com
    └── Origin 3: api-3.example.com
        ↓
    Selected Upper Tier: [Optimal data center based on pool performance]

#### Get started

To get started, enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) on your zone and configure your [Load Balancing Pool](https://developers.cloudflare.com/load-balancing/).
