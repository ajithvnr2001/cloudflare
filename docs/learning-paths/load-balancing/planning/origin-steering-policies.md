---
url: https://developers.cloudflare.com/learning-paths/load-balancing/planning/origin-steering-policies/
title: Endpoint steering policies \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:49.965552+00:00
---

# Endpoint steering policies · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/planning/origin-steering-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Planning your load balancer](https://developers.cloudflare.com/learning-paths/load-balancing/planning/)
  5. /Endpoint steering policies



# Endpoint steering policies

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/planning/origin-steering-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPoliciesWeights Customize weights Limitations

Endpoint steering customizes how each [pool](https://developers.cloudflare.com/load-balancing/pools/) distributes requests to its associated endpoints.

These distributions are a combination of two properties:

  * The endpoint steering policy chosen for your pool.
  * The weights assigned to each endpoint.



Note

If an endpoint [becomes unhealthy](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/), your pool will also re-balance traffic according to its endpoint steering policy.

* * *

## Policies

When you [create a pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/), you have to choose an option for **Endpoint Steering**.

* * *

## Weights

The weight assigned to an endpoint controls the percentage of pool traffic sent to that endpoint. By default, all endpoints within a pool have a weight of **1**.

If you leave each endpoint with the default setting and choose a **Random** endpoint steering policy, each endpoint will receive the same percentage of traffic. If you use a **Hash** policy, that percentage will vary based on the IP distribution of your requests.

### Customize weights

To customize weights when you [create or edit a pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/), set the **Weight** to a number between 0 and 1 (expressed in increments of .01). Cloudflare will then send traffic to that pool based on a combination of your endpoint steering policy and the following formula.
    
    
    % of traffic to endpoint = endpoint weight ÷ sum of all weights in the pool

Endpoint weight example

Here’s an example applying weights to three endpoints with a **Random** endpoint steering policy:

  * **Weights:** Endpoint A = 0.25; Endpoint B = 0.25; Endpoint C = 0.50
  * **When all endpoints are healthy** , each endpoint will receive the following proportion of total traffic: A = 25%; B = 25%; C = 50%.
  * **When one endpoint is unhealthy** (such as endpoint C), each healthy endpoint will receive the following proportion of total traffic: A = 50%; B=50%.



A significant amount of traffic is required for the distribution to converge on the expected values.

An endpoint with a weight of **0** should not receive any traffic sent to that pool (though the endpoint will still receive health monitor requests).

You can also see this value in the **Percent** field when creating or editing a pool in the dashboard.

Note:

If an endpoint is used in multiple pools and has multiple weights assigned, the total traffic sent to that pool will differ from the percentage specified in each individual pool.

### Limitations

If you choose **Hash** for your **Endpoint Steering** or enable [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/), these options can affect traffic distribution.

Additionally, session affinity takes precedence over any selected weight or endpoint steering policy.

When using [DNS-only load balancing](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing), DNS resolvers may cache resolved IPs for clients and affect traffic distribution.

[PreviousSession affinity](https://developers.cloudflare.com/learning-paths/load-balancing/planning/session-affinity/)[NextServer and pool health](https://developers.cloudflare.com/learning-paths/load-balancing/planning/server-pool-health/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/planning/origin-steering-policies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
