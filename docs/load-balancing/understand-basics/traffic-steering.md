---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/
title: Traffic steering \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.355200+00:00
---

# Traffic steering · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /Concepts
  4. /Traffic steering



# Traffic steering

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When requests come to your load balancer, it distributes them across your pools and endpoints according to four factors:

  1. [Pool and endpoint health](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/): Traffic decisions start with which pools and endpoints are available and should receive traffic.
  2. [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/): The preferred way to define new API-managed location routing. A matched pool set can replace pool selection and provide its own steering policy, weights, and fallback pool.
  3. [Global traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/): Policies set on your [load balancer](https://developers.cloudflare.com/load-balancing/load-balancers/) that route traffic to attached and available pools.
  4. [Local traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/): These are policies set on each [pool](https://developers.cloudflare.com/load-balancing/pools/) that route traffic to available endpoints within the pool.



When a pool or endpoint becomes unhealthy, your load balancer and pools redistribute traffic according to these same policies.

[PreviousLoad Balancing components](https://developers.cloudflare.com/load-balancing/understand-basics/load-balancing-components/)[NextPool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
