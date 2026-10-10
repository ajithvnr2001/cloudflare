---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/
title: New WebSocket Analytics Logpush dataset \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.332868+00:00
---

# New WebSocket Analytics Logpush dataset · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## New WebSocket Analytics Logpush dataset

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now push per-connection WebSocket analytics to any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) using the new `websocket_analytics` dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.

Key fields include:

  * **`ConnectionCloseReason`** — why the connection ended: `peerReset`, `peerNoError`, `timedOut`, `upstreamReset`, `protocolViolation`, `unspecifiedError`, or `none`.
  * **`ConnectionCloseSource`** — which side initiated the close: `upstream`, `downstream`, `me`, or `both`.
  * **`ConnectionTransportCloseCode`** — the TLS alert code or TCP-level close code for additional precision.
  * **`RayID`** — correlate WebSocket connection events with your existing HTTP Request logs.



The dataset also includes directional byte counts (`BytesSentClient`, `BytesReceivedClient`, `BytesSentOrigin`, `BytesReceivedOrigin`), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.

This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (`ConnectionCloseReason == "peerReset"`) grouped by host and data center — directly in your existing log analysis tools.

For the full list of available fields, refer to [WebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/).
