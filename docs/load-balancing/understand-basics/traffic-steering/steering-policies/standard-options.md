---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/
title: Standard traffic steering policies \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:08.022344+00:00
---

# Standard traffic steering policies · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)

  4. /[Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/)
  5. /Standard



# Standard

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOff - Failover Failback behaviorRandom steering

**Standard steering** policies include **Off - Failover** and **Random**.

These are the only steering policies available to non-Enterprise customers who have not purchased **Traffic steering**.

## Off - Failover

Failover steering uses the pool order to determine failover priority (the failover order).

Failover directs traffic from unhealthy pools — determined by [health monitors](https://developers.cloudflare.com/load-balancing/monitors/) and the **Health Threshold** — to the next healthy pool in the configuration. Customers commonly use this option to set up [active - passive failover](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/#active---passive-failover).

If all pools are marked unhealthy, Load Balancing will direct traffic to the fallback pool. The default fallback pool is the last pool listed in the Load Balancing configuration.

If no monitors are attached to the load balancer, it will direct traffic to the primary pool exclusively.

### Failback behavior

In an active/standby setup, with two origin pools:

  * Traffic always routes to Pool 1 (the primary pool) unless it becomes unhealthy.
  * If Pool 1 is marked unhealthy, traffic shifts to Pool 2 (the standby pool).
  * Once Pool 1 becomes healthy again, traffic automatically shifts back to Pool 1, assuming no [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/) or other settings require subsequent requests to stay at Pool 2.



This behavior is known as failback and ensures traffic resumes normal routing when the primary pool recovers.

## Random steering

Choose **Random** to route traffic to a healthy pool at random. Customers can use this option to set up [active - active failover](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/#active---active-failover) (also known as round robin), where traffic is split equally between multiple pools.

Similar to setting Weights to direct the amount of traffic going to each endpoint, customers can also set Weights on pools via the [API's](https://developers.cloudflare.com/api/resources/load_balancers/methods/create/) `random_steering` object to determine the percentage of traffic sent to each pool.

[PreviousOverview](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/)[NextGeo](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
