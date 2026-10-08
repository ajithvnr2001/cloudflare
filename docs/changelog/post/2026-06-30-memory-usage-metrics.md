---
url: https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/
title: Track memory usage for Workers and Durable Objects in the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:00.598161+00:00
---

# Track memory usage for Workers and Durable Objects in the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2026

## Track memory usage for Workers and Durable Objects in the dashboard

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-30-memory-usage-metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now monitor how much memory your [Workers](https://developers.cloudflare.com/workers/) and [Durable Objects](https://developers.cloudflare.com/durable-objects/) consume across invocations with the new **Memory Usage** chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.

![Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1210,height=782,format=webp/_astro/2026-06-26-memory-usage.B20y2uNp.png)

Memory usage measures the V8 [isolate](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) memory at the time of each invocation, subject to the [128 MB per-isolate limit](https://developers.cloudflare.com/workers/platform/limits/#memory) — a single isolate can handle many concurrent requests and shares memory across them.

Use the Memory Usage chart to:

  * **Track memory trends** — Spot gradual increases that may indicate a memory leak before they cause `Exceeded Memory` errors.
  * **Correlate with deployments** — Deployment markers on the chart help you identify whether a new version introduced a memory regression.
  * **Right-size your Worker** — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.



For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is [hibernated or evicted](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/). This state is not preserved across eviction, hibernation, or a crash, so persist anything important to [storage](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/).

To view memory usage, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics) or [Durable Object namespace ↗︎](https://dash.cloudflare.com/?to=/:account/workers/durable-objects). For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/) using the `workersInvocationsAdaptive` dataset — the `quantiles.memoryUsageBytesP50` through `quantiles.memoryUsageBytesP999` fields return percentile values in bytes.

For local memory debugging, you can also [profile memory with DevTools](https://developers.cloudflare.com/workers/observability/dev-tools/memory-usage/) to take heap snapshots and identify specific objects causing high memory usage.
