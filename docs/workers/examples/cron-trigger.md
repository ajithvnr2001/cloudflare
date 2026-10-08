---
url: https://developers.cloudflare.com/workers/examples/cron-trigger/
title: Setting Cron Triggers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:22.010474+00:00
---

# Setting Cron Triggers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/cron-trigger/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Cron Trigger



# Setting Cron Triggers

Set a Cron Trigger for your Worker.

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/cron-trigger/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet Cron Triggers in WranglerTest Cron Triggers using Wrangler
    
    
    export default {
    	async scheduled(controller, env, ctx) {
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
    		console.log("cron processed");
    	},
    };
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def scheduled(self, controller, env, ctx):
      			print("cron processed")
    
    
    import { Hono } from "hono";
    
    interface Env {}
    
    // Create Hono app
    const app = new Hono<{ Bindings: Env }>();
    
    // Regular routes for normal HTTP requests
    app.get("/", (c) => c.text("Hello World!"));
    
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
    		console.log("cron processed");
    
    		// You could also perform actions like:
    		// - Fetching data from external APIs
    		// - Updating KV or Durable Object storage
    		// - Running maintenance tasks
    		// - Sending notifications
    	},
    };

## Set Cron Triggers in Wrangler

Refer to [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for more information on how to add a Cron Trigger.

If you are deploying with Wrangler, set the cron syntax (once per hour as shown below) by adding this to your Wrangler file:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "worker",
    	// ...
    	"triggers": {
    		"crons": [
    			"0 * * * *"
    		]
    	}
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "worker"
    
    [triggers]
    crons = [ "0 * * * *" ]

You also can set a different Cron Trigger for each [environment](https://developers.cloudflare.com/workers/wrangler/environments/) in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). You need to put the `[triggers]` table under your chosen environment. For example:
    
    
    {
    	"env": {
    		"dev": {
    			"triggers": {
    				"crons": [
    					"0 * * * *"
    				]
    			}
    		}
    	}
    }
    
    
    [env.dev.triggers]
    crons = [ "0 * * * *" ]

## Test Cron Triggers using Wrangler

The recommended way of testing Cron Triggers is using Wrangler.

Cron Triggers can be tested using Wrangler by passing in the `--test-scheduled` flag to [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev). This will expose a `/cdn-cgi/local/scheduled` route which can be used to test using a HTTP request. To simulate different cron patterns, a `cron` query parameter can be passed in.
    
    
    npx wrangler dev --test-scheduled
    
    curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*" # Python Workers

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/cron-trigger.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
