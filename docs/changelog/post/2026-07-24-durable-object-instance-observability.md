---
url: https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/
title: Filter Durable Object logs and traces by instance ID \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.598211+00:00
---

# Filter Durable Object logs and traces by instance ID · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 24, 2026

## Filter Durable Object logs and traces by instance ID

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-24-durable-object-instance-observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) and [OpenTelemetry](https://developers.cloudflare.com/observability/export/opentelemetry/) spans for [Durable Object](https://developers.cloudflare.com/durable-objects/) requests include the Durable Object instance ID.

Use `$workers.durableObjectId` to filter logs for a specific instance. Root and child spans include the same ID in `cloudflare.durable_object.id`.

![Query Builder filtering traces by Durable Object instance ID](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2000,height=666,format=webp/_astro/2026-07-24-durable-object-trace-filter.DW-BwlKL.png)

Use these fields to isolate a specific instance and correlate its logs and traces.

For more information, refer to [Durable Objects metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/) and [Workers tracing spans and attributes](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/).
