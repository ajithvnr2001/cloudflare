---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/
title: Proximity steering \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.953532+00:00
---

# Proximity steering · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)

  4. /[Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/)
  5. /Proximity



# Proximity

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to add proximity steeringHow to add proximity steering

**Proximity steering** routes visitors or internal services to the closest physical data center.

To use proximity steering on a load balancer, you first need to add GPS coordinates to each pool.

## When to add proximity steering

  * For new pools, add GPS coordinates when you create a pool.
  * For existing pools, add GPS coordinates when [managing pools](https://developers.cloudflare.com/load-balancing/pools/create-pool/#edit-a-pool) or in the **Add Traffic steering** step of [creating a load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/).



## How to add proximity steering

To add coordinates when creating or editing a pool:

  1. Click the _Configure coordinates for Proximity Steering_ dropdown.
  2. Enter the latitude and longitude or drag a marker on the map.
  3. Select **Save**.



Warning:

For accurate proximity steering, add GPS coordinates to all pools within the same load balancer.

[PreviousDynamic](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/)[NextLeast Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
