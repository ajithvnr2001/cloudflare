---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/
title: Least Outstanding Requests steering - Steering policies \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.928886+00:00
---

# Least Outstanding Requests steering - Steering policies · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)

  4. /[Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/)
  5. /Least Outstanding Requests



# Least Outstanding Requests

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure via the APILimitations

**Least Outstanding Requests steering** allows you to route traffic to pools that currently have the lowest number of outstanding requests.

This steering policy selects a pool by taking into consideration `random_steering` weights, as well as each pool's number of in-flight requests. Pools with more pending requests are weighted proportionately less in relation to others.

Least Outstanding Requests steering is best to use if your pools are easily overwhelmed by a spike in concurrent requests. This steering method lends itself to applications that value server health above latency, geographic alignment, or other metrics. It takes into account the [pool's health status](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#how-a-pool-becomes-unhealthy), [adaptive routing](https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/), and [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/).

## Configure via the API

Load Balancersjson
    
    
    {
      "steering_policy": "least_outstanding_requests"
    }

Refer to the [API documentation](https://developers.cloudflare.com/api/resources/load_balancers/methods/update/) for more information on the load balancer configuration.

Note

Least Outstanding Requests steering can also be configured on a pool as a [local traffic steering policy](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/least-outstanding-requests-pools/), taking into account outstanding request counts and weights for endpoints within the pool.

## Limitations

Least Outstanding Requests steering can be configured for [DNS-only load balancers](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing), but is only supported in a no-operation form. For DNS-only load balancers, all pool outstanding request counts are considered to be zero, meaning traffic is served solely based on `random_steering` weights.

Although it is configurable, it is not recommended to use Least Outstanding Requests steering for DNS-only load balancers due to its partial support.

[PreviousProximity](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/)[NextOverview](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
