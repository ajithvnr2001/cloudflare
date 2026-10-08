---
url: https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/
title: Vectorize indexes now support up to 10 million vectors \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.835007+00:00
---

# Vectorize indexes now support up to 10 million vectors · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 23, 2026

## Vectorize indexes now support up to 10 million vectors

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.

Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the [Vectorize limits documentation](https://developers.cloudflare.com/vectorize/platform/limits/) for complete details.
