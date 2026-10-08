---
url: https://developers.cloudflare.com/learning-paths/load-balancing/planning/session-affinity/
title: Session affinity \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.208925+00:00
---

# Session affinity · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/planning/session-affinity/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Planning your load balancer](https://developers.cloudflare.com/learning-paths/load-balancing/planning/)
  5. /Session affinity



# Session affinity

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/planning/session-affinity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works

When you enable session affinity, your load balancer directs all requests from a particular end user to a specific endpoint. This continuity preserves information about the user session — such as items in their shopping cart — that might otherwise be lost if requests were spread out among multiple servers.

Session affinity can also help reduce network requests, leading to savings for customers with usage-based billing.

Note

Session Affinity is only supported by Public Load Balancers.

## How it works

Session affinity automatically directs requests from the same client to the same endpoint:

  1. When a client makes its first request, Cloudflare sets a `__cflb` cookie on the client (to track the associated endpoint).
  2. Subsequent requests by the same client are forwarded to that endpoint for the duration of the cookie and as long as the endpoint remains healthy.
  3. If the cookie expires or the endpoint becomes unhealthy, Cloudflare sets a new cookie tracking the new failover endpoint.


    
    
        flowchart LR
          accTitle: Session affinity process
          accDescr: Session affinity directs requests from the same client to the same server.
         A[Client] --Request--> B{<code>__cflb</code> cookie set?}
         B -->|Yes| C[Route to previous endpoint]
         C --> O2
         B ---->|No| E[Follow normal routing]
         E --> O2
         E --Set <code>__cflb</code> cookie--> A
         subgraph P1 [Pool 1]
            O1[Endpoint 1]
            O2[Endpoint 2]
         end
    

  


All cookie-based sessions default to 23 hours unless you set a custom session _Time to live_ (TTL).

The session cookie is secure when [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/) is enabled. Additionally, HttpOnly is always enabled for the cookie to prevent cross-site scripting attacks.

[PreviousTypes of load balancers](https://developers.cloudflare.com/learning-paths/load-balancing/planning/types-load-balancers/)[NextEndpoint steering policies](https://developers.cloudflare.com/learning-paths/load-balancing/planning/origin-steering-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/planning/session-affinity.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
