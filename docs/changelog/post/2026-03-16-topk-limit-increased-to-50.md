---
url: https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/
title: Return up to 50 query results with values or metadata \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.443195+00:00
---

# Return up to 50 query results with values or metadata · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 16, 2026

## Return up to 50 query results with values or metadata

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set `topK` up to `50` when a Vectorize query returns values or full metadata. This raises the previous limit of `20` for queries that use `returnValues: true` or `returnMetadata: "all"`.

Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the [Vectorize API reference](https://developers.cloudflare.com/vectorize/reference/client-api/) for query options and current `topK` limits.
