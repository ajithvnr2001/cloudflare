---
url: https://developers.cloudflare.com/changelog/post/2025-06-18-remote-bindings-beta/
title: Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.604751+00:00
---

# Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-18-remote-bindings-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 18, 2025

## Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-18-remote-bindings-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Today [we announced the public beta ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) of [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) for local development. With remote bindings, you can now connect to deployed resources like [R2 buckets](https://developers.cloudflare.com/r2/) and [D1 databases](https://developers.cloudflare.com/d1/) while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.

#### Example configuration

To enable remote mode, add `"experimental_remote" : true` to each binding that you want to rely on a remote resource running on Cloudflare:
    
    
    {
    	"name": "my-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    
    	"r2_buckets": [
    		{
    			"bucket_name": "screenshots-bucket",
    			"binding": "screenshots_bucket",
    			"experimental_remote": true,
    		},
    	],
    }
    
    
    name = "my-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[r2_buckets]]
    bucket_name = "screenshots-bucket"
    binding = "screenshots_bucket"
    experimental_remote = true

When remote bindings are configured, your Worker **still executes locally** , but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.

**You can try out remote bindings for local development today with:**

  * [Wrangler v4.20.3](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Use the `wrangler dev --x-remote-bindings` command.
  * The [Cloudflare Vite Plugin](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Refer to the documentation for how to enable in your Vite config.
  * The [Cloudflare Vitest Plugin](https://developers.cloudflare.com/workers/local-development/#remote-bindings): Refer to the documentation for how to enable in your Vitest config.



**Have feedback?** Join the discussion in our [beta announcement ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9660) to share feedback or report any issues.
