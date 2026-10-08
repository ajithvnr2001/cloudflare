---
url: https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/
title: 40-60% Faster D1 Worker API Requests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:02.259125+00:00
---

# 40-60% Faster D1 Worker API Requests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 7, 2025

## 40-60% Faster D1 Worker API Requests

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-07-d1-faster-query/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Users making [D1](https://developers.cloudflare.com/d1/) requests via the [Workers API](https://developers.cloudflare.com/d1/worker-api/) can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.

![D1 Worker API latency](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4437,height=1754,format=webp/_astro/faster-d1-worker-api.4S7VSUdP.png)

_p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement._

This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 [location hints](https://developers.cloudflare.com/d1/configuration/data-location/#provide-a-location-hint) can be used to influence the geographic location of a database.

For more details on how D1 removed redundant round trips, see the D1 specific release note [entry](https://developers.cloudflare.com/d1/platform/release-notes/#2025-01-07).
