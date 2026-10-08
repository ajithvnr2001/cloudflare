---
url: https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/
title: Adaptive routing \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:06.861315+00:00
---

# Adaptive routing · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /Concepts
  4. /Adaptive routing



# Adaptive routing

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFailover across pools Enable failover across poolsHTTP/2 GOAWAY handling

Adaptive routing controls features that modify the routing of requests to pools and endpoints in response to dynamic conditions, such as during the interval between active health monitoring requests. 

Zero-downtime failover will trigger a single retry only if there is another healthy endpoint in the pool and a [521, 522, 523, 525 or 526 error code](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/) is occurring. No other error codes will trigger a zero-downtime failover operation.

## Failover across pools

When there are no healthy endpoints in the same pool, failover across pools extend the zero-downtime failover of requests to healthy endpoints in alternate pools according to the failover order defined by traffic and endpoint steering.

Geo-steering limitation

When using [geo-steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/), failover across pools only considers pools within the same geographic grouping. If your NA pool becomes unhealthy, traffic will **not** automatically fail over to your EU pool — it will go to the global fallback pool instead.

To enable cross-region failover, include the desired fallback pool as an additional pool within each region's pool list.

Alternatively, [pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/) accept a fallback pool for each location, so traffic that exhausts the pools for one location fails over to a pool you choose for that location instead of the global fallback pool.

### Enable failover across pools

  1. In the Cloudflare dashboard, go to the **Load Balancing** page.

[ Go to **Load Balancing** ↗ ](https://dash.cloudflare.com/?to=/:account/load-balancing)
  2. Navigate to your Load Balancers and select **Edit**.

  3. From **Adaptive Routing** , enable **Failover across pools**.




## HTTP/2 GOAWAY handling

When an origin sends a GOAWAY frame, Cloudflare stops sending new requests on that connection but does not mark the endpoint as unhealthy. Safe-to-retry requests (typically GET) are automatically retried on a new connection. Non-idempotent requests (such as POST or PUT) may not be retried unless the request was not yet sent on the closing connection.

[PreviousSession affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/)[NextOverview](https://developers.cloudflare.com/load-balancing/load-balancers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/adaptive-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
