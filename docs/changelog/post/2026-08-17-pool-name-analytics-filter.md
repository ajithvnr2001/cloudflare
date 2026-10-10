---
url: https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/
title: Load balancing analytics now filters by pool name \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.854019+00:00
---

# Load balancing analytics now filters by pool name · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 17, 2026

## Load balancing analytics now filters by pool name

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.

Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.

The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:

  * **Requests over time** , filtering the chart series to the selected pool.
  * **Pool distribution** , showing only the selected pool segment.
  * **Top endpoints** , displaying cards for origins in the selected pool.
  * **Latency** , showing latency data for the selected pool.



The **Logs** view and health event filtering are unchanged.

To use this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same pool filter appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

For more information about analytics filters and metrics, refer to [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/).
