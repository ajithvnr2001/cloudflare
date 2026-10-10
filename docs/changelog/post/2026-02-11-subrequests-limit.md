---
url: https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/
title: Workers are no longer limited to 1000 subrequests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.055617+00:00
---

# Workers are no longer limited to 1000 subrequests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-11-subrequests-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 11, 2026

## Workers are no longer limited to 1000 subrequests

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more `fetch()` calls or requests to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as open websockets on [Durable Objects](https://developers.cloudflare.com/durable-objects) or long-running [Workflows](https://developers.cloudflare.com/workflows), as these could often exceed this limit and error.

By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this limit can be increased up to 10 million by setting the new `subrequests` limit in your Wrangler configuration file.
    
    
    {
    	"limits": {
    		"subrequests": 50000,
    	},
    }
    
    
    [limits]
    subrequests = 50_000

Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.

To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.
    
    
    {
    	"limits": {
    		"subrequests": 10,
    		"cpu_ms": 1000,
    	},
    }
    
    
    [limits]
    subrequests = 10
    cpu_ms = 1_000

For more information, refer to the [Wrangler configuration documentation for limits](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and [subrequest limits](https://developers.cloudflare.com/workers/platform/limits/#subrequests).
