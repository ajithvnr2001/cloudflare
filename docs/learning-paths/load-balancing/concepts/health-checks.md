---
url: https://developers.cloudflare.com/learning-paths/load-balancing/concepts/health-checks/
title: Monitors and health checks \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:49.514476+00:00
---

# Monitors and health checks · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/concepts/health-checks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/)
  5. /Monitors and health checks



# Monitors and health checks

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/health-checks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works

There's more to a load balancer than just distributing traffic, however.

After all, what good would it be if your load balancer and pools send a request to a server that's offline? Or one that's already overloaded with traffic? Ideally, your load balancer should only forward requests that a server can take care of.

That's where another part of the load balancing equation comes in: monitors and health checks.
    
    
        flowchart RL
          accTitle: Load balancing monitor flow
          accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.
          Monitor -- Health Monitor ----> Endpoint2
          Endpoint2 -- Response ----> Monitor
          subgraph Pool
          Endpoint1((Endpoint 1))
          Endpoint2((Endpoint 2))
          end
    

## How it works

A monitor issues health checks periodically to evaluate the health of each server within a pool.

Requests issued by a monitor at regular interval and — depending on the monitor settings — return a **pass** or **fail** value to make sure an endpoint is still able to receive traffic.

Each health monitor request is trying to answer two questions:

  1. **Is the endpoint offline?** : Does the endpoint respond to the health monitor request at all? If so, does it respond quickly enough (as specified in the monitor's **Timeout** field)?
  2. **Is the endpoint working as expected?** : Does the endpoint respond with the expected HTTP response codes? Does it include specific information in the response body?



If the answer to either of these questions is "No", then the endpoint fails the health monitor request.

This system of request and response ensures that a load balancer knows which servers can handle incoming requests.

[PreviousComponents of a load balancer](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/load-balancer-components/)[NextRouting traffic](https://developers.cloudflare.com/learning-paths/load-balancing/concepts/routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/concepts/health-checks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
