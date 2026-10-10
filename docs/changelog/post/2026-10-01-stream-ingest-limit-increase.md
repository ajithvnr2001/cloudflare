---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/
title: Basin Pipelines ingest limit increased to 1 GB/s \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.697890+00:00
---

# Basin Pipelines ingest limit increased to 1 GB/s · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## Basin Pipelines ingest limit increased to 1 GB/s

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Each [Basin Pipelines stream](https://developers.cloudflare.com/basin-pipelines/streams/) can now ingest up to 1 GB/s, increased from 5 MB/s.

The higher per-stream limit gives high-volume application events, telemetry, and logs more room to grow without splitting ingestion across streams solely to stay within the previous limit.

For the full list of stream, sink, and pipeline limits, refer to [Basin Pipelines limits](https://developers.cloudflare.com/basin-pipelines/platform/limits/).
