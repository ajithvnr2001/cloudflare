---
url: https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/
title: Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:20.212084+00:00
---

# Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 22, 2025

## Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.

![Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1486,height=796,format=webp/_astro/kv-hybrid-providers-performance-improvements.D6MBO22S.png)

#### Performance improvements

The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:

  * **p95 latency** : Reduced from ~150ms to ~50ms (67% decrease)
  * **p99 latency** : Reduced from ~350ms to ~250ms (29% decrease)


