---
url: https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/
title: View total SQLite storage for Durable Object namespaces \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.054142+00:00
---

# View total SQLite storage for Durable Object namespaces · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 20, 2026

## View total SQLite storage for Durable Object namespaces

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-20-durable-objects-total-storage-metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new **Total storage** chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.

![The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1436,height=846,format=webp/_astro/durable-objects-total-storage.Cr_F72Yz.png)[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/#total-storage).
