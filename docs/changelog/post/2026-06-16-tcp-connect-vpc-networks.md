---
url: https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/
title: TCP connections via connect() over VPC Networks \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.400145+00:00
---

# TCP connections via connect() over VPC Networks · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-16-tcp-connect-vpc-networks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 16, 2026

## TCP connections via connect() over VPC Networks

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[VPC Network](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) bindings now support the [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via `fetch()`.

This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "vpc_networks": [
        {
          "binding": "PRIVATE_NETWORK",
          "network_id": "cf1:network",
          "remote": true
        }
      ]
    }
    
    
    [[vpc_networks]]
    binding = "PRIVATE_NETWORK"
    network_id = "cf1:network"
    remote = true

At runtime, use `connect()` on the binding to open a TCP socket to a private destination:
    
    
    export default {
    	async fetch(request: Request, env: Env) {
    		// Open a TCP connection to a private Redis instance
    		const socket = await env.PRIVATE_NETWORK.connect("10.0.1.50:6379");
    
    		// Write a Redis PING command
    		const writer = socket.writable.getWriter();
    		await writer.write(new TextEncoder().encode("PING\r\n"));
    		await writer.close();
    
    		return new Response(socket.readable);
    	},
    };

Note

`connect()` over VPC Networks currently supports plaintext TCP only.

For more details, refer to [VPC Networks](https://developers.cloudflare.com/workers-vpc/configuration/vpc-networks/) and the [Workers Binding API](https://developers.cloudflare.com/workers-vpc/api/).
