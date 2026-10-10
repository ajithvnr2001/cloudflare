---
url: https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/
title: Revamped Workers Metrics \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.067671+00:00
---

# Revamped Workers Metrics · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-03-workers-metrics-revamp/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 3, 2025

## Revamped Workers Metrics

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've revamped the [Workers Metrics dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/).

![Workers Metrics dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3032,height=1756,format=webp/_astro/workers-metrics.IxYk9yF0.png)

Now you can easily compare metrics across Worker versions, understand the current state of a [gradual deployment](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/), and review key Workers metrics in a single view. This new interface enables you to:

  * Drag-and-select using a graphical timepicker for precise metric selection.

![Workers Metrics graphical timepicker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1944,height=932,format=webp/_astro/metrics-graphical-timepicker.tzLlEF5U.png)

  * Use histograms to visualize cumulative metrics, allowing you to bucket and compare rates over time.
  * Focus on Worker versions by directly interacting with the version numbers in the legend.

![Workers Metrics legend selector](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2308,height=1068,format=webp/_astro/metrics-legend-selector.B2GY90Hn.png)

  * Monitor and compare active gradual deployments.
  * Track error rates across versions with grouping both by version and by invocation status.
  * Measure how [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) improves request duration.



Learn more about [metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics).
