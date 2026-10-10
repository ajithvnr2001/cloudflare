---
url: https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/
title: Use Docker Hub images with Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.704182+00:00
---

# Use Docker Hub images with Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 24, 2026

## Use Docker Hub images with Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Containers now support [Docker Hub ↗︎](https://hub.docker.com/) images. You can use a fully qualified Docker Hub image reference in your [Wrangler configuration ↗︎](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.
    
    
    {
    	"containers": [
    		{
    			// Example: docker.io/cloudflare/sandbox:0.7.18
    			"image": "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>",
    		},
    	],
    }
    
    
    [[containers]]
    image = "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>"

Containers also support private Docker Hub images. To configure credentials, refer to [Use private Docker Hub images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-docker-hub-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).
