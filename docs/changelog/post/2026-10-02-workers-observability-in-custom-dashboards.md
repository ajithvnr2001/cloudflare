---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/
title: Workers Observability logs and traces in Custom Dashboards \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.501685+00:00
---

# Workers Observability logs and traces in Custom Dashboards · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## Workers Observability logs and traces in Custom Dashboards

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)** , let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).
