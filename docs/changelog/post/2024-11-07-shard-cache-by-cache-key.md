---
url: https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/
title: Shard cache using custom cache key values \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.893010+00:00
---

# Shard cache using custom cache key values · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 7, 2024

## Shard cache using custom cache key values

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by **sharding cache** using up to ten values from previously restricted headers with [custom cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/).

#### How it works

When configuring [custom cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/), you can now include values from these headers to create distinct cache entries:

  * **`accept*` headers** (for example, `accept`, `accept-encoding`, `accept-language`): Serve different cached versions based on content negotiation.
  * **`referer` header**: Cache content differently based on the referring page or site.
  * **`user-agent` header**: Maintain separate caches for different browsers, devices, or bots.



#### When to use cache sharding

  * Content varies significantly by device type (mobile vs desktop).
  * Different language or encoding preferences require distinct responses.
  * Referrer-specific content optimization is needed.



#### Example configuration
    
    
    {
      "cache_key": {
        "custom_key": {
          "header": {
            "include": ["accept-language", "user-agent"],
            "check_presence": ["referer"]
          }
        }
      }
    }

This configuration creates separate cache entries based on the `accept-language` and `user-agent` headers, while also considering whether the `referer` header is present.

#### Get started

To get started, refer to the [custom cache keys documentation](https://developers.cloudflare.com/cache/how-to/cache-keys/).

Note

While cache sharding can improve hit ratios for specific use cases, overly sharding your cache can reduce overall cache efficiency and negatively impact performance. Carefully evaluate whether sharding benefits your specific traffic patterns.
