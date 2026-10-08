---
url: https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/
title: Durable Objects can use up to ten Dynamic Workers concurrently \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:11.457525+00:00
---

# Durable Objects can use up to ten Dynamic Workers concurrently · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 28, 2026

## Durable Objects can use up to ten Dynamic Workers concurrently

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) can have up to ten distinct [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.

Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.

For more information, refer to [Dynamic Workers limits](https://developers.cloudflare.com/dynamic-workers/platform/limits/).
