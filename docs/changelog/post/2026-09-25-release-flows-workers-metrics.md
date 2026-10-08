---
url: https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/
title: See every release and gradual deployment on Workers Metrics charts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.384179+00:00
---

# See every release and gradual deployment on Workers Metrics charts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2026

## See every release and gradual deployment on Workers Metrics charts

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-release-flows-workers-metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/) charts now show every release in the selected time range, including the full progression of [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/). This makes it easier to correlate changes in memory, CPU time, errors, or latency with the code that was serving traffic.

![Memory usage chart showing a gradual deployment as a shaded rollout band](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-memory-usage.C5rkO7VY.png)

A gradual deployment appears as a single rollout across the chart, with shading that increases as more traffic moves to the new version. Hover over a rollout to see the previous and new versions, the rollout duration, and the traffic percentage configured at each step.

![Invocations chart showing traffic shifting from the previous version to the new version during a gradual deployment](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1350,format=webp/_astro/2026-09-25-release-flow-invocations.BvQMAKnw.png)

Use these annotations to:

  * **Find when a regression started** — See which traffic percentage was configured when errors, latency, CPU time, or wall time changed.
  * **Compare rollout stages** — Check whether a metric changed as more traffic moved to the new version.
  * **Confirm rollbacks** — Rollbacks appear as separate release events, so you can check whether metrics recovered after a rollback.



Direct deployments that send 100% of traffic to a single version still appear as individual markers. Nearby direct deployments are grouped to reduce visual clutter. Versions that are only uploaded, or only configured at 0%, do not appear on metrics charts.

To view release annotations, open the **Metrics** tab for your [Worker ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics).
