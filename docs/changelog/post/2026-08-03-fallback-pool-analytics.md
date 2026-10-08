---
url: https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/
title: See fallback pool traffic separately in load balancing analytics \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.900431+00:00
---

# See fallback pool traffic separately in load balancing analytics · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 3, 2026

## See fallback pool traffic separately in load balancing analytics

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Load balancing analytics now shows traffic served by your [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) separately from traffic routed to the same pool by normal steering.

Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.

Fallback traffic is now labeled with the pool name followed by `(Fallback)`. A pool named `eu-west`, for example, is shown as `eu-west (Fallback)`. This label appears as its own entry in:

  * **Requests over time** , as a separate series in the chart.
  * **Pool distribution** , as a separate segment.
  * **Top endpoints** , as a separate card for the pool.



The **Latency** view and the health event **Logs** are unchanged.

To see this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same breakdown appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

Refer to [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to learn more.
