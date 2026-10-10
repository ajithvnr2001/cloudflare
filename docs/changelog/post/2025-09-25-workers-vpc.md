---
url: https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/
title: Announcing Workers VPC Services (Beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.380087+00:00
---

# Announcing Workers VPC Services (Beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2025

## Announcing Workers VPC Services (Beta)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Workers VPC Services** is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.

#### What's new

  * **VPC Services** : Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax
  * **Multi-cloud Support** : Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels


    
    
    export default {
    	async fetch(request, env, ctx) {
    		// Perform application logic in Workers here
    
    		// Sample call to an internal API running on ECS in AWS using the binding
    		const response = await env.AWS_VPC_ECS_API.fetch("https://internal-host.example.com");
    
    		// Additional application logic in Workers
    		return new Response();
    	},
    };

#### Getting started

Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. [Refer to the documentation](https://developers.cloudflare.com/workers-vpc/) to get started.
