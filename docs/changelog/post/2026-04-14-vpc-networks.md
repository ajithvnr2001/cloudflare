---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/
title: VPC Networks and Cloudflare Mesh support now in public beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.529840+00:00
---

# VPC Networks and Cloudflare Mesh support now in public beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-vpc-networks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## VPC Networks and Cloudflare Mesh support now in public beta

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing [VPC Service](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/) bindings, which scope each binding to a specific host and port.

You can bind to a [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) by `tunnel_id` to reach any service on the network where that tunnel is running, or bind to your [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) network using `cf1:network` to reach any Mesh node, client device, or subnet route in your account:
    
    
    {
      "vpc_networks": [
        {
          "binding": "MESH",
          "network_id": "cf1:network",
          "remote": true
        }
      ]
    }
    
    
    [[vpc_networks]]
    binding = "MESH"
    network_id = "cf1:network"
    remote = true

At runtime, `fetch()` routes through the network to reach the service at the IP and port you specify:
    
    
    const response = await env.MESH.fetch("http://10.0.1.50:8080/api/data");

For configuration options and examples, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and [Connect Workers to Cloudflare Mesh](https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/).
