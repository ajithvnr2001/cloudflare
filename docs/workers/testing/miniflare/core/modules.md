---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/modules/
title: Modules \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.600484+00:00
---

# Modules · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/modules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Modules



# Modules

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/modules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnabling ModulesModule Rules Default Rules

  * [Modules Reference](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/)



## Enabling Modules

Miniflare supports both the traditional `service-worker` and the newer `modules` formats for writing workers. To use the `modules` format, enable it with:
    
    
    const mf = new Miniflare({
    	modules: true,
    });

You can then use `modules` worker scripts like the following:
    
    
    export default {
    	async fetch(request, env, ctx) {
    		// - `request` is the incoming `Request` instance
    		// - `env` contains bindings, KV namespaces, Durable Objects, etc
    		// - `ctx` contains `waitUntil` and `passThroughOnException` methods
    		return new Response("Hello Miniflare!");
    	},
    	async scheduled(controller, env, ctx) {
    		// - `controller` contains `scheduledTime` and `cron` properties
    		// - `env` contains bindings, KV namespaces, Durable Objects, etc
    		// - `ctx` contains the `waitUntil` method
    		console.log("Doing something scheduled...");
    	},
    };

String scripts via the `script` option are supported using the `modules` format, but you cannot import other modules using them. You must use a script file via the `scriptPath` option for this.

## Module Rules

Miniflare supports all module types: `ESModule`, `CommonJS`, `Text`, `Data` and `CompiledWasm`. You can specify additional module resolution rules as follows:
    
    
    const mf = new Miniflare({
    	modulesRules: [
    		{ type: "ESModule", include: ["**/*.js"], fallthrough: true },
    		{ type: "Text", include: ["**/*.txt"] },
    	],
    });

### Default Rules

The following rules are automatically added to the end of your modules rules list. You can override them by specifying rules matching the same `globs`:
    
    
    [
    	{ type: "ESModule", include: ["**/*.mjs"] },
    	{ type: "CommonJS", include: ["**/*.js", "**/*.cjs"] },
    ];

[PreviousFetch Events](https://developers.cloudflare.com/workers/testing/miniflare/core/fetch/)[NextMultiple Workers](https://developers.cloudflare.com/workers/testing/miniflare/core/multiple-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/modules.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
