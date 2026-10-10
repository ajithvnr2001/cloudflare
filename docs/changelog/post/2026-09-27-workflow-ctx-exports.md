---
url: https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/
title: Call Workflows declared in `exports` through `ctx.exports` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.424261+00:00
---

# Call Workflows declared in `exports` through `ctx.exports` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 27, 2026

## Call Workflows declared in `exports` through `ctx.exports`

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A Worker can now call the Workflows it declares in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of its Wrangler configuration through [`ctx.exports`](https://developers.cloudflare.com/workers/runtime-apis/context/#exports). You no longer need a `workflows` binding to call a Workflow from the Worker that defines it.

Each Workflow is keyed by class name, and has the same API as a Workflow binding:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env, ctx) {
    		const instance = await ctx.exports.MyWorkflow.create({
    			params: { name: "World" },
    		});
    		return Response.json({ id: instance.id });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const instance = await ctx.exports.MyWorkflow.create({
    			params: { name: "World" },
    		});
    		return Response.json({ id: instance.id });
    	},
    } satisfies ExportedHandler<Env>;

A `workflows` binding and a `workflow` export with the same `name` share their instances. You can move a Workflow from a binding to an export without losing its instances.

`wrangler dev`, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), and the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) run Workflows on `ctx.exports` locally. Local development requires Wrangler 4.142.0, `@cloudflare/vite-plugin` 1.61.0, or `@cloudflare/vitest-plugin` 1.3.0 or above.

In Vitest, `introspectWorkflow()` and `introspectWorkflowInstance()` still need a Workflow binding. To introspect a Workflow declared in `exports`, add a [test-only binding](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#introspect-workflows-declared-in-exports) to it.

For more information, refer to [Call a Workflow through `ctx.exports`](https://developers.cloudflare.com/workflows/build/workers-api/#call-a-workflow-through-ctxexports).
