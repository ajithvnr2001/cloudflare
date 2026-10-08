---
url: https://developers.cloudflare.com/changelog/post/2026-09-08-per-container-observability/
title: Configure observability per container application \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:12.697894+00:00
---

# Configure observability per container application · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-08-per-container-observability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 8, 2026

## Configure observability per container application

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-08-per-container-observability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure observability for each container application when you deploy [Containers](https://developers.cloudflare.com/containers/) with [Wrangler](https://developers.cloudflare.com/workers/wrangler/). This lets you change logging for one container without changing the rest of your Worker.

If you omit `containers[].observability`, Wrangler uses the top-level `observability` setting for that container. If you set it, the container setting overrides the top-level setting.

Use `target_instance_percentage` or `target_instance_count` to apply an observability change to a subset of running instances.
    
    
    {
    	"observability": {
    		"enabled": false,
    	},
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"image": "./Dockerfile",
    			"observability": {
    				"enabled": true,
    				"target_instance_percentage": 25,
    			},
    		},
    	],
    }
    
    
    [observability]
    enabled = false
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    
      [containers.observability]
      enabled = true
      target_instance_percentage = 25

For more information about Workers Logs, refer to [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/).
