---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/
title: Send npm package dependency metadata with Worker uploads \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.782218+00:00
---

# Send npm package dependency metadata with Worker uploads · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 9, 2026

## Send npm package dependency metadata with Worker uploads

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now collects npm package dependency information from your project's `package.json` during [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy) and [`wrangler versions upload`](https://developers.cloudflare.com/workers/wrangler/commands/general/#upload), and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.

To opt out, set [`dependencies_instrumentation.enabled`](https://developers.cloudflare.com/workers/wrangler/configuration/#top-level-only-keys) to `false` in your Wrangler configuration file:
    
    
    {
    	"dependencies_instrumentation": {
    		"enabled": false
    	}
    }
    
    
    [dependencies_instrumentation]
    enabled = false

For more details, refer to [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#top-level-only-keys).
