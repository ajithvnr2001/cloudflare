---
url: https://developers.cloudflare.com/load-balancing/understand-basics/health-details/
title: How endpoints and pools become unhealthy \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.037219+00:00
---

# How endpoints and pools become unhealthy · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/health-details/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /Concepts
  4. /How endpoints and pools become unhealthy



# How endpoints and pools become unhealthy

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDynamic load balancingHow an endpoint becomes unhealthyHow a pool becomes unhealthy Traffic distribution Fallback poolsHow a load balancer becomes unhealthy

When we talk about dynamic load balancing, that means your load balancer only directs requests to endpoints that can handle the traffic.

But how does your load balancer _know_ which endpoints can handle the traffic? We determine that through a system of monitors, health monitors, and pools.

* * *

## Dynamic load balancing

Dynamic load balancing happens through a combination of [pools](https://developers.cloudflare.com/load-balancing/pools/), [monitors](https://developers.cloudflare.com/load-balancing/monitors/), and health checks.
    
    
        flowchart RL
          accTitle: Load balancing monitor flow
          accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.
          Monitor -- Health Monitor ----> Endpoint2
          Endpoint2 -- Response ----> Monitor
          subgraph Pool
          Endpoint1((Endpoint 1))
          Endpoint2((Endpoint 2))
          end
    

* * *

## How an endpoint becomes unhealthy

Health checks are requests issued by a monitor at regular interval and — depending on the monitor settings — return a **pass** or **fail** value to make sure an endpoint is still able to receive traffic.

Each health monitor request is trying to answer two questions:

  1. **Is the endpoint offline?** : Does the endpoint respond to the health monitor request at all? If so, does it respond quickly enough (as specified in the monitor's **Timeout** field)?
  2. **Is the endpoint working as expected?** : Does the endpoint respond with the expected HTTP response codes? Does it include specific information in the response body?



If the answer to either of these questions is "No", then the endpoint fails the health monitor request.

For each option selected in a pool's **Health Monitor Regions** , Cloudflare sends health monitor requests from three separate data centers in that region.

![Health monitor requests come from three data centers within each selected region.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=467,height=497,format=webp/_astro/health-check-component.wo0_f7k-.png)

If the majority of data centers for that region pass the health monitor requests, that region is considered healthy. If the majority of regions is healthy, then the endpoint itself will be considered healthy.

Note

If **Health Monitor Regions** for a pool is set to **All Data Centers (Enterprise)** , pool health is determined by a majority of data centers.

Load balancing analytics and logs will only show global health changes.

For greater accuracy and consistency when changing endpoint health status, you can also set the `consecutive_up` and `consecutive_down` parameters via the [Create Monitor API endpoint](https://developers.cloudflare.com/api/resources/load_balancers/subresources/monitors/methods/create/). To change from healthy to unhealthy, an endpoint will have to be marked healthy a consecutive number of times (specified by `consecutive_down`). The same applies — from unhealthy to healthy — for `consecutive_up`.

* * *

## How a pool becomes unhealthy

When an individual endpoint becomes unhealthy, that may affect the health status of any associated pools (visible in the dashboard):

  * **Healthy** : All endpoints are healthy.
  * **Degraded** : At least one endpoint is unhealthy, but the pool is still considered healthy and could be receiving traffic.
  * **Critical** : The pool has fallen below the number of available endpoints specified in its **Health Threshold** and will not receive traffic from your load balancer (unless other pools are also unhealthy and this pool is marked as the **Fallback Pool**).
  * **Health unknown** : There are either no monitors attached to pool endpoints or the monitors have not yet determined endpoint health.
  * **No health** : Reserved for your load balancer's **Fallback Pool**.



Note

  1. When no monitor is attached to a pool, the health status is not considered during steering.
  2. Origins are considered down when monitoring is enabled, but the health status is still unknown.
  3. If there are no monitors, a fallback pool is still required, but it will only be used if all the default pools have origins with FQDN addresses that cannot be resolved.



### Traffic distribution

When a pool reaches **Critical** health, your load balancer will begin diverting traffic according to its [Traffic steering policy](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/):

  * **Off** :

    * If the active pool becomes unhealthy, traffic goes to the next pool in order.
    * If an inactive pool becomes unhealthy, traffic continues to go to the active pool (but would skip over the unhealthy pool in the failover order).
  * **All other methods** : Traffic is distributed across all remaining pools according to the traffic steering policy.




### Fallback pools

This pool is meant to be the pool of last resort, meaning that its health is not taken into account when directing traffic.

Fallback pools are important because traffic still might be coming to your load balancer even when all the pools are unreachable (disabled or unhealthy). Your load balancer needs somewhere to route this traffic, so it will send it to the fallback pool.

* * *

## How a load balancer becomes unhealthy

When one or more pools become unhealthy, your load balancer might also show a different status in the dashboard:

  * **Healthy** : All pools are healthy.
  * **Degraded** : At least one pool is unhealthy, but traffic is not yet going to the Fallback Pool.
  * **Critical** : All pools are unhealthy and traffic is going to the Fallback Pool.



If a load balancer reaches **Critical** health and the pool serving as your fallback pool is also disabled:

  * If Cloudflare proxies your hostname, you will see a 530 HTTP/1016 Origin DNS failure.
  * If Cloudflare does not proxy your hostname, you will see the SOA record.



[PreviousLeast Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/least-outstanding-requests-pools/)[NextProxy status](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/health-details.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
