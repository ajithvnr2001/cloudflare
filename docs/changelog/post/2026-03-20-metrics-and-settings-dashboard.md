---
url: https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/
title: Observability for Workers VPC Services \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.010796+00:00
---

# Observability for Workers VPC Services · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 20, 2026

## Observability for Workers VPC Services

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-20-metrics-and-settings-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Each VPC Service now has a **Metrics** tab so you can monitor connection health and debug failures without leaving the dashboard.

![Workers VPC Metrics dashboard showing connections, latency, and errors charts](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3336,height=3204,format=webp/_astro/2026-03-20-metrics-dashboard.6kfnbqQd.png)

  * **Connections** — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).
  * **Latency** — Track connection and DNS resolution latency trends.
  * **Errors** — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.



You can also view and edit your VPC Service configuration, host details, and port assignments from the **Settings** tab.

For a full list of error codes and what they mean, refer to [Troubleshooting](https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/).
