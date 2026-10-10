---
url: https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/
title: Improved support for running multiple Workers with `wrangler dev` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.547947+00:00
---

# Improved support for running multiple Workers with `wrangler dev` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 23, 2025

## Improved support for running multiple Workers with `wrangler dev`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can run multiple Workers in a single dev command by passing multiple config files to `wrangler dev`:
    
    
    wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc

Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use [Service Bindings ↗︎](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) and [Tail Workers ↗︎](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) in local development, when running separate wrangler dev sessions.

Now, the following works as expected:
    
    
    # Terminal 1: Run your application that includes both Web and API workers
    wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc
    
    # Terminal 2: Run your auth worker separately
    wrangler dev --config ./auth/wrangler.jsonc

These Workers can now communicate with each other across separate dev commands, regardless of your development setup.

./api/src/index.tsjs
    
    
    export default {
    	async fetch(request, env) {
    		// This service binding call now works across dev commands
    		const authorized = await env.AUTH.isAuthorized(request);
    
    		if (!authorized) {
    			return new Response("Unauthorized", { status: 401 });
    		}
    
    		return new Response("Hello from API Worker!", { status: 200 });
    	},
    };

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.
