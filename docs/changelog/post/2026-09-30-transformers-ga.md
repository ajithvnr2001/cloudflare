---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/
title: Transformers are now generally available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.004749+00:00
---

# Transformers are now generally available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Transformers are now generally available

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).
