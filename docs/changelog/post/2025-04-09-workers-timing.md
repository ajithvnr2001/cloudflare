---
url: https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/
title: CPU time and Wall time now published for Workers Invocations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:09.459246+00:00
---

# CPU time and Wall time now published for Workers Invocations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2025

## CPU time and Wall time now published for Workers Invocations

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-workers-timing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now observe and investigate the CPU time and Wall time for every Workers Invocations.

  * For [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs), CPU time and Wall time are surfaced in the [Invocation Log](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)..
  * For [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers), CPU time and Wall time are surfaced at the top level of the [Workers Trace Events object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events).
  * For [Workers Logpush](https://developers.cloudflare.com/workers/observability/logs/logpush), CPU and Wall time are surfaced at the top level of the [Workers Trace Events object](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/workers_trace_events). All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.



You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.

![Workers Logs Wall Time Filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=652,height=436,format=webp/_astro/2025-04-09-wall-time-filter.CT-VQyTS.png)

You can also use the Workers Observability [Query Builder ↗︎](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate) to find the median CPU time and median Wall time for all of your Workers.

![Query Builder filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2650,height=1318,format=webp/_astro/2025-04-09-query-builder.CaW9IZza.png)
