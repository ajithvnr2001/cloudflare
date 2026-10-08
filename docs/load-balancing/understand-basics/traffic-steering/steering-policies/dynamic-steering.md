---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/
title: Dynamic steering \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.796761+00:00
---

# Dynamic steering · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)

  4. /[Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/)
  5. /Dynamic



# Dynamic

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Dynamic steering** uses health monitor data to identify the fastest pool for a given Cloudflare Region or data center.

Dynamic steering creates Round Trip Time (RTT) profiles based on an exponential weighted moving average (EWMA) of RTT to determine the fastest pool. If there is no current RTT data for your pool in a region or colocation center, Cloudflare directs traffic to the pools in failover order.

RTT values are collected each time a health probe request is made and based on the response from the endpoint to the monitor request. When a request is made, Cloudflare inspects the RTT data and uses it to sort pools by their RTT values.

When enabling Dynamic steering the first time for a pool, allow 10 minutes for the change to take effect while Cloudflare builds an RTT profile for that pool.

For TCP health monitors, calculated latency may not reflect the true latency to the endpoint if you are terminating TCP at a cloud provider edge location.

The diagram below shows how Cloudflare would route traffic to the pool with the lowest EWMA among three regions: Eastern North America, Europe, and Australia. In this case, the ENAM pool is selected because it has the lowest RTT.

![Dynamic steering routes traffic to the fastest available pool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=960,height=973,format=webp/_astro/traffic-steering-2.CEeFHZfg.png)

Note

To ensure dynamic steering works as expected, the [Health Monitor Region](https://developers.cloudflare.com/load-balancing/monitors/#health-monitor-regions) must be set to **All Regions**. The Enterprise-only **All Data Centers** option is also a viable alternative.

[PreviousGeo](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/)[NextProximity](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
