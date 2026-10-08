---
url: https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/
title: Perform planned maintenance \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:04.538096+00:00
---

# Perform planned maintenance · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Perform planned maintenance



# Perform planned maintenance

Last updated Jul 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginGradual rotationImmediate rotation

When you change application settings or add new assets, you will likely want to make these changes on one endpoint at a time. Going endpoint by endpoint reduces the risk of changes and ensures a more consistent user experience.

To take endpoints out of rotation gradually (important for session-based load balancing), enable endpoint drain on your load balancer. This option is only available for [proxied load balancers (orange-clouded)](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/).

To direct traffic away from your endpoint immediately, adjust settings on the pool or monitor.

Note

If you want to divert traffic from an endpoint to prevent it from becoming unhealthy, use [Load Shedding](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/) instead.

Existing connections are not terminated

When an endpoint becomes unhealthy, Cloudflare Load Balancing stops routing **new** requests to it. However, existing connections (including long-lived WebSocket connections) are **not** terminated — they remain open until they close naturally.

If you need graceful connection draining, use endpoint drain to proactively take endpoints out of rotation before maintenance, rather than relying on health check failures alone.

## Before you begin

Before disabling any endpoint, review the settings for any affected load balancers and pools.

If a pool falls below its **Health Threshold** , it will be considered **Unhealthy** and — depending on the load balancer setup and steering policy — a load balancer may begin routing traffic away from that pool.

## Gradual rotation

Note

Endpoint drain is only available for [proxied load balancers (orange-clouded)](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/).

With [session-based load balancing](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/), it is important to direct all requests from a particular end user to a specific endpoint. Otherwise, information about the user session — such as items in their shopping cart — may be lost and lead to negative business outcomes.

To remove an endpoint from rotation while still preserving session continuity, set up **Endpoint drain** on a load balancer:

  1. On a new or existing load balancer, go to the **Hostname** step.
  2. Make sure you have enabled **Session Affinity**.
  3. For **Endpoint drain duration** , enter a time in seconds. If this value is less than the **Session TTL** value, you will affect existing sessions. ![Example configuration of session affinity with endpoint drain](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1002,height=491,format=webp/_astro/session-affinity-3.Cv_ZhLzx.png)
  4. Save your changes to the load balancer.
  5. Click **Manage Pools**.
  6. Disable an endpoint. Your load balancer will gradually drain sessions from that endpoint.
  7. On your load balancer, expand your pools to find the disabled endpoint. You will see the estimated **Drain Time** counting down. ![Example showing load balancer draining in progress](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=802,height=275,format=webp/_astro/session-affinity-4.DC0RLZtj.png)
  8. When a drain is **Complete** , there are no longer any connections to that endpoint. ![Example showing load balancer draining complete](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=802,height=275,format=webp/_astro/session-affinity-5.BAgwGz7x.png)
  9. Perform your required maintenance or upgrades.
  10. To bring your endpoint back online, re-enable the endpoint.



## Immediate rotation

To direct traffic away from an endpoint immediately:

  1. Do one of the following actions: 
     * On the endpoint's [monitor](https://developers.cloudflare.com/load-balancing/monitors/), update the monitor settings so the endpoint will fail health monitor requests, such as putting an incorrect value for the **Response Body** or **Response Code**.
     * On the pool, disable the endpoint.
     * On the pool, set the [endpoint weight](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights) to `0` (though traffic may still reach the endpoint if it is included in multiple pools).
  2. Monitor [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to make sure no requests are reaching the pool. 
     * If you are using [DNS-only load balancing (gray-clouded)](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/), changes may be delayed due to DNS resolver caching.
  3. Perform your required maintenance or upgrades.
  4. Undo the changes you made in **Step 1**.



[PreviousSpectrum](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/)[NextLoad shedding](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/planned-maintenance.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
