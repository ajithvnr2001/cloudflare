---
url: https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/
title: Filter Durable Objects metrics by object ID or name \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.751591+00:00
---

# Filter Durable Objects metrics by object ID or name · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 12, 2026

## Filter Durable Objects metrics by object ID or name

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now filter the **Metrics** tab for a Durable Objects namespace by an individual Durable Object's [ID](https://developers.cloudflare.com/durable-objects/api/id/) or [name](https://developers.cloudflare.com/durable-objects/api/id/#name) in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) ![The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2936,height=1482,format=webp/_astro/durable-objects-metrics-dashboard.BFZTyhWU.png)

Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.

Metrics are powered by the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/), so standard analytics behavior such as ingestion delay and [sampling](https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/) applies.

For more information, refer to [Metrics and analytics](https://developers.cloudflare.com/durable-objects/observability/metrics-and-analytics/).
