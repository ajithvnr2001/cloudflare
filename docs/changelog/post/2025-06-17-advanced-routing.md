---
url: https://developers.cloudflare.com/changelog/post/2025-06-17-advanced-routing/
title: Control which routes invoke your Worker script for Single Page Applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.671013+00:00
---

# Control which routes invoke your Worker script for Single Page Applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-17-advanced-routing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 17, 2025

## Control which routes invoke your Worker script for Single Page Applications

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

For those building [Single Page Applications (SPAs) on Workers](https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/#advanced-routing-control), you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The [`run_worker_first` config option](https://developers.cloudflare.com/workers/static-assets/binding/#run_worker_first) has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.

**Configuration example:**
    
    
    {
    	"name": "my-spa-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-10",
    	"main": "./src/index.ts",
    	"assets": {
    		"directory": "./dist/",
    		"not_found_handling": "single-page-application",
    		"binding": "ASSETS",
    		"run_worker_first": ["/api/*", "!/api/docs/*"]
    	}
    }
    
    
    name = "my-spa-worker"
    # Set this to today's date
    compatibility_date = "2026-10-10"
    main = "./src/index.ts"
    
    [assets]
    directory = "./dist/"
    not_found_handling = "single-page-application"
    binding = "ASSETS"
    run_worker_first = [ "/api/*", "!/api/docs/*" ]

This new routing control was done in partnership with our community and customers who provided great feedback on [our public proposal ↗︎](https://github.com/cloudflare/workers-sdk/discussions/9143). Thank you to everyone who brought forward use-cases and feedback on the design!

#### Prerequisites

To use advanced routing control with `run_worker_first`, you'll need:

  * [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) v4.20.0 and above
  * [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/get-started/) v1.7.0 and above


