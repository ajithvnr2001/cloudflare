---
url: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/
title: Load Balancing actions \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:03.383980+00:00
---

# Load Balancing actions · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)

  4. /[Custom load balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/)
  5. /Actions



# Actions

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported Actions

Add **actions** to customize how your load balancer responds to certain HTTP requests.

Each load balancing rule includes one or more actions.

## Supported Actions

This table lists the actions available for Load Balancing rules. For a walkthrough, refer to [Create Load Balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/).

Action| Options| Description  
---|---|---  
 _Fixed response_|  _N/A_|  Respond to the request with an HTTP status code and an optional message.  
_Override_|  _Session affinity_|  Set the [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/) for the request. You can customize cookie behavior and session time-to-live (TTL).  
_Override_|  _Load balancer TTL_|  Customize the load balancer session time-to-live (TTL).  
_Override_|  _Steering policy_|  Update the [steering policy](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/) associated with your load balancer.  
_Override_|  _Fallback pool_|  Update the [fallback pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#off---failover) associated with your load balancer.  
_Override_|  _Pools_|  Update the [pools](https://developers.cloudflare.com/load-balancing/pools/) associated with your load balancer.  
_Override_|  _Region pools_|  Update the [region pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/) associated with your load balancer.  
_Override_|  _Country pools_|  Update the [country pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/) associated with your load balancer.  
_Override_|  _Terminates_|  Stop processing Load Balancing rules and apply the current load balancing logic to the request.  
  
[PreviousExpressions](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/expressions/)[NextSupported fields and operators](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/load-balancing-rules/actions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
