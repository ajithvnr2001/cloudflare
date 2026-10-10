---
url: https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/
title: Capture up to 256 KB of log events in each Workers Invocation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.330348+00:00
---

# Capture up to 256 KB of log events in each Workers Invocation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-07-increase-trace-events-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2025

## Capture up to 256 KB of log events in each Workers Invocation

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.

All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted as [JSON object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events). [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs) deserializes this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers).

256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be recorded in your logs.

This limit is automatically applied to all Workers.
