---
url: https://developers.cloudflare.com/workers/examples/multiple-cron-triggers/
title: Multiple Cron Triggers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:24.085402+00:00
---

# Multiple Cron Triggers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/multiple-cron-triggers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Multiple Cron Triggers



# Multiple Cron Triggers

Set multiple Cron Triggers on three different schedules.

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/multiple-cron-triggers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTest Cron Triggers using Wrangler

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/multiple-cron-triggers)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.
    
    
    export default {
    	async scheduled(event, env, ctx) {
    		// Write code for updating your API
    		switch (event.cron) {
    			case "*/3 * * * *":
    				// Every three minutes
    				await updateAPI();
    				break;
    			case "*/10 * * * *":
    				// Every ten minutes
    				await updateAPI2();
    				break;
    			case "*/45 * * * *":
    				// Every forty-five minutes
    				await updateAPI3();
    				break;
    		}
    		console.log("cron processed");
    	},
    };
    
    
    interface Env {}
    export default {
    	async scheduled(
    		controller: ScheduledController,
    		env: Env,
    		ctx: ExecutionContext,
    	) {
    		// Write code for updating your API
    		switch (controller.cron) {
    			case "*/3 * * * *":
    				// Every three minutes
    				await updateAPI();
    				break;
    			case "*/10 * * * *":
    				// Every ten minutes
    				await updateAPI2();
    				break;
    			case "*/45 * * * *":
    				// Every forty-five minutes
    				await updateAPI3();
    				break;
    		}
    		console.log("cron processed");
    	},
    };
    
    
    import { Hono } from "hono";
    
    interface Env {}
    
    // Create Hono app
    const app = new Hono<{ Bindings: Env }>();
    
    // Regular routes for normal HTTP requests
    app.get("/", (c) => c.text("Multiple Cron Trigger Example"));
    
    // Export both the app and a scheduled function
    export default {
    	// The Hono app handles regular HTTP requests
    	fetch: app.fetch,
    
    	// The scheduled function handles Cron triggers
    	async scheduled(
    		controller: ScheduledController,
    		env: Env,
    		ctx: ExecutionContext,
    	) {
    		// Check which cron schedule triggered this execution
    		switch (controller.cron) {
    			case "*/3 * * * *":
    				// Every three minutes
    				await updateAPI();
    				break;
    			case "*/10 * * * *":
    				// Every ten minutes
    				await updateAPI2();
    				break;
    			case "*/45 * * * *":
    				// Every forty-five minutes
    				await updateAPI3();
    				break;
    		}
    		console.log("cron processed");
    	},
    };

## Test Cron Triggers using Wrangler

The recommended way of testing Cron Triggers is using Wrangler.

Cron Triggers can be tested using Wrangler by passing in the `--test-scheduled` flag to [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev). This will expose a `/cdn-cgi/local/scheduled` route which can be used to test using a HTTP request. To simulate different cron patterns, a `cron` query parameter can be passed in.
    
    
    npx wrangler dev --test-scheduled
    
    curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*" # Python Workers

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/multiple-cron-triggers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
