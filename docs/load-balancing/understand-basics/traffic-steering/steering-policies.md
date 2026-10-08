---
url: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/
title: Global traffic steering policies \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:07.772069+00:00
---

# Global traffic steering policies · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /…

Concepts

  4. /[Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/)
  5. /Global traffic steering



# Global traffic steering

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEDNS Client Subnet (ECS) support

Global traffic steering policies decide how a load balancer routes traffic to attached and healthy pools.

  


  * [Standard](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/)
  * [Geo](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/)
  * [Dynamic](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/)
  * [Proximity](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/)
  * [Least Outstanding Requests](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/)



## EDNS Client Subnet (ECS) support

EDNS Client Subnet (ECS)  support provides customers with more control over location-based steering during gray-clouded DNS resolutions and can be used for proximity or geo (country) steering.

Customers can configure their load balancer using the `location_strategy` parameter, which includes the properties `prefer_ecs` and `mode`.

`prefer_ecs` determines whether the ECS geolocation should be preferred as the authoritative location.

Type | Description  
---|---  
`"always"` | Always prefers ECS.  
`"never"` | Never prefers ECS.  
`"proximity"` | Prefers ECS only when `steering_policy="proximity"`.  
`"geo"` | Prefers ECS only when `steering_policy="geo"` and only supports country-level steering.  
  
`mode` determines the authoritative location when ECS is not preferred, does not exist in the request, or its geolocation lookup is unsuccessful.

Type | Description  
---|---  
`"pop"` | Uses the Cloudflare PoP location.  
`"resolver_ip"` | Uses the DNS resolver geolocation data. If the geolocation lookup is unsuccessful, it uses the Cloudflare PoP location.  
  
Note

ECS support applies to DNS-only load balancers.

[PreviousPool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/)[NextStandard](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/understand-basics/traffic-steering/steering-policies/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
