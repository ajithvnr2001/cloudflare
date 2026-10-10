---
url: https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/
title: Realtime backlog metrics now available for Queues \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:39.335771+00:00
---

# Realtime backlog metrics now available for Queues · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 28, 2026

## Realtime backlog metrics now available for Queues

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Queues](https://developers.cloudflare.com/queues/), Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:

  * **`backlog_count`** — the number of unacknowledged messages in the queue
  * **`backlog_bytes`** — the total size of those messages in bytes
  * **`oldest_message_timestamp_ms`** — the timestamp of the oldest unacknowledged message



The following endpoints also now include a `metadata.metrics` object on the result field after successful message consumption:

  * `/accounts/{account_id}/queues/{queue_id}/messages/pull`
  * `/accounts/{account_id}/queues/{queue_id}/messages`
  * `/accounts/{account_id}/queues/{queue_id}/messages/batch`



#### Javascript APIs

Call `env.QUEUE.metrics()` to get realtime backlog metrics:
    
    
    const {
    	backlogCount, // number
    	backlogBytes, // number
    	oldestMessageTimestamp, // Date | undefined
    } = await env.QUEUE.metrics();

`env.QUEUE.send()` and `env.QUEUE.sendBatch()` also now return a metrics object on the response.

You can also query these fields via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) or view realtime backlog on the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/queues).

![Queues realtime backlog](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1402,height=494,format=webp/_astro/2026-04-28-queues-metrics.BYi0hgrD.png)

For more information, refer to [Queues metrics](https://developers.cloudflare.com/queues/observability/metrics/).
