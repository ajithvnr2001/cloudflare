---
url: https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/
title: Up to 10x faster cached queries for Hyperdrive \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.677170+00:00
---

# Up to 10x faster cached queries for Hyperdrive · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-12-11-hyperdrive-caching-at-edge/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 11, 2024

## Up to 10x faster cached queries for Hyperdrive

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.

When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.

This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.

![Hyperdrive edge caching improves average session duration for database queries](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1746,height=734,format=webp/_astro/hyperdrive-edge-caching-metrics.BR7svphB.png)

_P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period._

This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.

For more details on how Hyperdrive performs query caching, refer to the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching).
