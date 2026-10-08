---
url: https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/
title: WebSocket reporting now includes full connection data transfer and duration \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.622829+00:00
---

# WebSocket reporting now includes full connection data transfer and duration · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2026

## WebSocket reporting now includes full connection data transfer and duration

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial `101 Switching Protocols` handshake for some WebSocket connections.

Customers with WebSocket traffic will see the correct **Data Transfer** in the dashboard and `EdgeResponseBytes` in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.

The separate [WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/) continues to provide per-connection directional byte counts, timestamps, and close details.

For more information about HTTP Traffic Analytics, refer to [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/#http-traffic).
