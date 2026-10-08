---
url: https://developers.cloudflare.com/changelog/post/2026-05-01-dynamic-workflows/
title: Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.139288+00:00
---

# Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-01-dynamic-workflows/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 1, 2026

## Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-01-dynamic-workflows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use [`@cloudflare/dynamic-workflows` ↗︎](https://github.com/cloudflare/dynamic-workflows) to run a [Workflow](https://developers.cloudflare.com/workflows/) inside a [Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/), ensuring durable execution for code that is loaded at runtime.

The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.

The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.

Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.

This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:

  * **SaaS platforms** where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.
  * **AI agent frameworks** where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.
  * **Multi-tenant job systems** where each customer submits their own processing logic and every step persists progress and retries on failure.


    
    
    import {
    	createDynamicWorkflowEntrypoint,
    	DynamicWorkflowBinding,
    	wrapWorkflowBinding,
    	type WorkflowRunner,
    } from "@cloudflare/dynamic-workflows";
    
    export { DynamicWorkflowBinding };
    
    interface Env {
    	WORKFLOWS: Workflow;
    	LOADER: WorkerLoader;
    }
    
    function loadTenant(env: Env, tenantId: string) {
    	return env.LOADER.get(tenantId, async () => ({
    		compatibilityDate: "2026-01-01",
    		mainModule: "index.js",
    		modules: { "index.js": await fetchTenantCode(tenantId) },
    		// The Dynamic Worker uses this exactly like a real Workflow binding;
    		// every create() is tagged with { tenantId } automatically.
    		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },
    	}));
    }
    
    // The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.
    export const DynamicWorkflow = createDynamicWorkflowEntrypoint<Env>(
    	async ({ env, metadata }) => {
    		const stub = loadTenant(env, metadata.tenantId as string);
    		return stub.getEntrypoint("TenantWorkflow") as unknown as WorkflowRunner;
    	},
    );
    
    export default {
    	fetch(request: Request, env: Env) {
    		const tenantId = request.headers.get("x-tenant-id")!;
    		return loadTenant(env, tenantId).getEntrypoint().fetch(request);
    	},
    };

For a full walkthrough, refer to the [Dynamic Workflows guide](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/).
