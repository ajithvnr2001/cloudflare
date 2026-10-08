---
url: https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/
title: Load shedding \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:03.686533+00:00
---

# Load shedding · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Load shedding



# Load shedding

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStep 1 — Identify at-risk endpointsStep 2 — Shed default traffic from a pool Configure via dashboard Configure via APIStep 3 — Monitor trafficStep 4 — Shed additional traffic (optional)Step 5 — Disable load sheddingAdditional notes Shedding policies Fallback pools Pools in multiple load balancers

Use load shedding to prevent an at-risk endpoint from [becoming unhealthy](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/) and starting the failover process.

Once you configure load shedding on a pool, that pool will begin diverting traffic to other pools according to your load shedding settings and the load balancer's [steering policy](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/).

## Step 1 — Identify at-risk endpoints

Using your internal metrics, identify endpoints at risk of reaching their failure threshold.

  * If your endpoint is seeing increased traffic but is not yet at risk of failure, start with Step 2.
  * If your endpoint is about to fail, start with Step 4.



## Step 2 — Shed default traffic from a pool

Once you have identified an at-risk endpoint, shed a small amount of **Default** traffic from that endpoint's pool. This traffic is not affiliated with existing [Session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/) sessions.

Configure load shedding via the dashboard or the API.

### Configure via dashboard

To enable load shedding for a specific pool via the dashboard:

  1. Go to **Load Balancing**.
  2. Select the **Pools** tab.
  3. On a pool, select **Edit**.
  4. Open the **Configure Load Shedding** dropdown.
  5. For **Default traffic** , select a **Policy** and a **Shed %** :



Policy options

When shedding **Default traffic** , you have two **Policy** options:

  * **Random** : Randomly sheds the percentage of requests specified in the _Shed %_. Distributes traffic more accurately, but may cause requests from the same IP to hit different endpoints.
  * **IP hash** : Sheds the percentage of IP address hash space specified in the _Shed %_. Ensures requests from the same IP will hit the same endpoint, but may shed a significantly higher or lower percentage of requests.



For more guidance on choosing a policy, refer to Shedding policies.

Shed %

When choosing a **Shed %** , start with a small percentage and increase gradually. Particularly if you choose the IP hash shedding policy, you might shed more traffic than expected.

### Configure via API

To enable load shedding for a specific pool via the API, [update the values](https://developers.cloudflare.com/api/resources/load_balancers/subresources/pools/methods/update/) for the pool's `load_shedding` object.

Example request

Requestbash
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/load_balancers/pools/{pool_id}" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data-binary '{
      "load_shedding": {
        "default_percent": 20,
        "default_policy": "random",
        "session_percent": 0,
        "session_policy": "hash"
      }
    }'

For more guidance on choosing a shedding policy, see Shedding policies.

## Step 3 — Monitor traffic

Once you have started shedding default traffic, evaluate the effects by reviewing the [**Overview** metrics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) in Load Balancing analytics. Based on these numbers and your internal metrics, you will know whether you need to divert additional traffic from the pool.

If you see increased traffic to a pool, you may need to shed additional traffic. Pools shed a percentage of total traffic, so any increase in total traffic will also increase the traffic reaching your pool.

## Step 4 — Shed additional traffic (optional)

If you need to shed additional pool traffic:

  1. Follow the steps outlined in Step 2. 
     * In the dashboard, increase the **Shed %** for **Default traffic** and/or **Session affinity traffic**.
     * For the API, increase the value for `default_percent` and/or `session_percent`.



Since shedding **Session Affinity traffic** will disrupt [existing sessions](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/) and may degrade the customer experience, only enable this option if your pool is in imminent danger of becoming unhealthy or your pool has a high percentage of traffic related to existing sessions. For more guidance, see Shedding policies.

## Step 5 — Disable load shedding

Once an endpoint is no longer at risk, remove load shedding from the pool.

To remove load shedding in the dashboard, perform the same steps as Configure load shedding via the dashboard but set the **Shed %** to `0` for both **Default traffic** and **Session affinity traffic**.

To remove load shedding via the API, perform the same steps as Configure load shedding via the API but set the `load_shedding` object to `null`.

## Additional notes

### Shedding policies

For **Default traffic** , you have two choices for shedding policy.

A _Random_ policy:

  * Randomly sheds the percentage of requests specified in the _Shed %_.
  * Distributes traffic more accurately because it sheds at the request level.
  * May cause requests from the same IP to hit different endpoints, potentially leading to cache misses, inconsistent latency, or session disruption for [DNS-only load balancers](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing).



An _IP hash_ policy:

  * Sheds the percentage of IP address hash space specified in the _Shed %_.
  * Ensures requests from the same IP will hit the same endpoint, which will increase cache hits, provide consistent latency, and preserve sessions.
  * Can over- or under-shed requests, since hashing does not guarantee a perfectly even IP distribution and individual IPs may be responsible for different percentages of your requests.



Choose a _Random_ policy when you want a more accurate distribution of raw requests and an _IP hash_ policy when you want to prevent a single IP from flapping between different endpoints.

For **Session Affinity traffic** , you can only use an _IP hash_ policy since these requests relate to existing sessions. Only increase the _Shed %_ if you are comfortable disrupting [existing sessions](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/).

### Fallback pools

If all pools within a load balancer have _Load shedding_ enabled, some traffic will go to the fallback pool. To prevent any traffic from reaching the fallback pool, ensure at least one pool within the load balancer **does not** have load shedding enabled.

### Pools in multiple load balancers

If you enable load shedding on a pool, it will shed the same percentage of traffic across all your load balancers. If you need an endpoint to shed different percentages of traffic for different load balancers, put that endpoint in multiple pools.

[PreviousPerform planned maintenance](https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/)[NextDNS persistence](https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/load-shedding.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
