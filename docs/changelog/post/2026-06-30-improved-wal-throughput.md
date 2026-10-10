---
url: https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/
title: Reduced end-to-end latency for vector changes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.674913+00:00
---

# Reduced end-to-end latency for vector changes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Reduced end-to-end latency for vector changes

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have greatly improved the throughput of the Vectorize [write-ahead log (WAL) ↗︎](https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal). As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.

![Vectorize p99 WAL batch end-to-end latency improved](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2542,height=1184,format=webp/_astro/vectorize-p99-wal-batch-end-to-end-latency-improvement.k8gtzlG7.png)

This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.

For more information, refer to the [Vectorize documentation](https://developers.cloudflare.com/vectorize/).
