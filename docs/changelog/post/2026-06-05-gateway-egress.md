---
url: https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/
title: Filter Workers' public Internet traffic using Gateway policies \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.130335+00:00
---

# Filter Workers' public Internet traffic using Gateway policies · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 5, 2026

## Filter Workers' public Internet traffic using Gateway policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers using a [VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) binding with `network_id: "cf1:network"` now egress to public Internet destinations through [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/). This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.

  1. [Worker](https://developers.cloudflare.com/workers/)

Calls `env.EGRESS.fetch()`

  2. [VPC binding](https://developers.cloudflare.com/workers-vpc/)↓
  3. [Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Bind via [`cf1:network`](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/)

  4. ↓
  5. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Policies applied:

[DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)[HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/)[Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/)

  6. ↓
  7. ↗Public Internet

Any public hostname or IP


[Gateway logsDNSHTTPNetwork](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/)

What you get by default:

  * **Visibility.** Worker egress shows up in Gateway [DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/), [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/), and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) logs alongside your other traffic, so you can audit what your Workers are calling and when.
  * **Enforcement.** Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.


    
    
    {
    	"vpc_networks": [
    		{
    			"binding": "EGRESS",
    			"network_id": "cf1:network",
    			"remote": true,
    		},
    	],
    }
    
    
    [[vpc_networks]]
    binding = "EGRESS"
    network_id = "cf1:network"
    remote = true
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");
    
    
    // Egress to a public destination — subject to your Gateway policies and logged
    const response = await env.EGRESS.fetch("https://api.example.com/data");

For configuration options, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/). For policy authoring, refer to [Cloudflare Gateway traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).
