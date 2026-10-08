---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/
title: New scheduling policy for Containers to configure image and instance from Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:17.400008+00:00
---

# New scheduling policy for Containers to configure image and instance from Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## New scheduling policy for Containers to configure image and instance from Durable Objects

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) now support the `durable_object` scheduling policy in public beta. This policy lets a Durable Object select the image and instance size for a Container at runtime instead of using one centrally managed configuration for the application.

To use custom images, configure the policy and one or more named images in Wrangler:
    
    
    {
    	"containers": [
    		{
    			"class_name": "AgentComputer",
    			"scheduling_policy": "durable_object",
    			"images": {
    				"base": {
    					"dockerfile": "./container/Dockerfile",
    				},
    			},
    		},
    	],
    }
    
    
    [[containers]]
    class_name = "AgentComputer"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./container/Dockerfile"

Wrangler prepares each image and exposes its immutable reference through `ctx.container.images`. Supply that reference and an instance size when you start the Container:

src/index.jsjs
    
    
    this.ctx.container.start({
    	image: this.ctx.container.images.base,
    	enableInternet: false,
    	instance: "standard-2",
    });

src/index.tsts
    
    
    this.ctx.container.start({
    	image: this.ctx.container.images.base,
    	enableInternet: false,
    	instance: "standard-2",
    });

The `durable_object` policy also supports the new [`cloudflare/debian-trixie` Cloudflare-managed image](https://developers.cloudflare.com/containers/guides/image-management/#use-the-cloudflare-managed-image), which includes Node.js 24.20.0 on Debian Trixie slim. Start it directly without configuring a named image.

Durable Object-managed Container instances have independent lifecycles and do not participate in application-wide image rollouts.

For configuration, runtime sizing, snapshots, and update behavior, refer to [Scheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/).
