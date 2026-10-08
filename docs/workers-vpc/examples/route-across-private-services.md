---
url: https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/
title: Route to private services from Workers \u00b7 Cloudflare Workers VPC
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:08.320313+00:00
---

# Route to private services from Workers · Cloudflare Workers VPC

> Source: https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers VPC](https://developers.cloudflare.com/workers-vpc/)
  3. /Examples
  4. /Route to private services from Workers



# Route to private services from Workers

Last updated Apr 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create the VPC Services2\. Configure your Worker3\. Implement the Worker4\. Deploy and testNext steps

This example shows how to use Workers VPC to create a centralized gateway that routes requests based on URL paths, provides authentication and rate limiting, and load balances across internal services.

## Prerequisites

  * Multiple private APIs or services running in your VPC/virtual network (we'll use a user service and orders service)
  * Cloudflare Tunnel configured and running (follow the [Get Started guide](https://developers.cloudflare.com/workers-vpc/get-started/#2-set-up-cloudflare-tunnel) to set up or [create a tunnel from the dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels))
  * Workers account with Workers VPC access



## 1\. Create the VPC Services

First, create services for your internal APIs using hostnames:
    
    
    # Create user service
    npx wrangler vpc service create user-service \
      --type http \
      --tunnel-id <YOUR_TUNNEL_ID> \
      --hostname user-api.internal.example.com
    
    # Create orders service
    npx wrangler vpc service create order-service \
      --type http \
      --tunnel-id <YOUR_TUNNEL_ID> \
      --hostname orders-api.internal.example.com

Note the service IDs returned for the next step.

## 2\. Configure your Worker

Update your Wrangler configuration file:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "api-gateway",
    	"main": "src/index.js",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"vpc_services": [
    		{
    			"binding": "USER_SERVICE",
    			"service_id": "<YOUR_USER_SERVICE_ID>"
    		},
    		{
    			"binding": "ORDER_SERVICE",
    			"service_id": "<YOUR_ORDER_SERVICE_ID>"
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "api-gateway"
    main = "src/index.js"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[vpc_services]]
    binding = "USER_SERVICE"
    service_id = "<YOUR_USER_SERVICE_ID>"
    
    [[vpc_services]]
    binding = "ORDER_SERVICE"
    service_id = "<YOUR_ORDER_SERVICE_ID>"

## 3\. Implement the Worker

In your Workers code, use the VPC Service bindings to route requests to the appropriate services:

index.jsjs
    
    
    export default {
    	async fetch(request, env, ctx) {
    		const url = new URL(request.url);
    
    		// Route to internal services
    		if (url.pathname.startsWith('/api/users')) {
    			const response = await env.USER_SERVICE.fetch("https://user-api.internal.example.com" + url.pathname);
    			return response;
    		} else if (url.pathname.startsWith('/api/orders')) {
    			const response = await env.ORDER_SERVICE.fetch("https://orders-api.internal.example.com" + url.pathname);
    			return response;
    		}
    
    		return new Response('Not Found', { status: 404 });
    	},
    };

## 4\. Deploy and test

Now, you can deploy and test your Worker:
    
    
    npx wrangler deploy
    
    
    # Test user service requests
    curl https://api-gateway.workers.dev/api/users
    
    # Test orders service requests
    curl https://api-gateway.workers.dev/api/orders

## Next steps

  * Add [authentication and authorization](https://developers.cloudflare.com/workers/examples/auth-with-headers/)
  * Implement [rate limiting](https://developers.cloudflare.com/durable-objects/api/)
  * Set up [monitoring and alerting](https://developers.cloudflare.com/analytics/analytics-engine/)
  * Explore [other examples](https://developers.cloudflare.com/workers-vpc/examples/)



[PreviousConnect Workers to Cloudflare Mesh](https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/)[NextOverview](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-vpc/examples/route-across-private-services.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
