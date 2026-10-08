---
url: https://developers.cloudflare.com/learning-paths/load-balancing/concepts/load-balancer-components/
title: Components of a load balancer \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:49.712289+00:00
---

# Components of a load balancer · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/concepts/load-balancer-components/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/)
  5. /Components of a load balancer



# Components of a load balancer

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/load-balancer-components/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works

At it's most basic, load balancing is made up of three components:

  * **Pools** : Which contain one or more endpoints.
  * **Endpoints** : Which respond to individual requests.
  * **A load balancer** : Which decides which traffic goes to each pool.



## How it works

Normally, requests to your application would go to individual servers directly.

With a load balancer, requests first go through the load balancer. Your load balancer then routes requests to specific pools.
    
    
        flowchart LR
          accTitle: Load balancing flow
          accDescr: Load balancing involves a load balancer, pools, endpoints, monitors, and health monitors.
          B[Request 1] --> A
          C[Request 2] --> A
          D[Request 3] --> A
          A[Load balancer] -- Request 1 --> P1
          A -- Request 2 --> P2
          A -- Request 3 --> P3
          subgraph P1 [Pool 1]
          Endpoint1((Endpoint 1))
          Endpoint2((Endpoint 2))
          end
          subgraph P2 [Pool 2]
          Endpoint3((Endpoint 3))
          Endpoint4((Endpoint 4))
          end
          subgraph P3 [Pool 3]
          Endpoint5((Endpoint 5))
          Endpoint6((Endpoint 6))
          end
    

  


Within each pool, requests then go to individual endpoints. And that endpoint is what responds to the request.
    
    
        flowchart LR
          accTitle: Pool traffic flow
          accDescr: When an incoming request reaches a pool, it then goes to an endpoint within the pool.
        A[Request 1] --Routed by pool--> Endpoint2
          subgraph P1 [Pool]
            Endpoint1((Endpoint 1))
            Endpoint2((Endpoint 2))
          end
    

  


This progression of load balancer --> pool --> endpoint is the core part of how a load balancer works.

[PreviousWhat is load balancing?](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/load-balancing/)[NextMonitors and health checks](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/health-checks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/concepts/load-balancer-components.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
