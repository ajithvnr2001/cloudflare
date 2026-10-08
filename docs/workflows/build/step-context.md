---
url: https://developers.cloudflare.com/workflows/build/step-context/
title: Step context \u00b7 Cloudflare Workflows docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:14.425583+00:00
---

# Step context · Cloudflare Workflows docs

> Source: https://developers.cloudflare.com/workflows/build/step-context/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workflows](https://developers.cloudflare.com/workflows/)
  3. /Build with Workflows
  4. /Step context



# Step context

Last updated Jul 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workflows/build/step-context/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWorkflowStepContext PropertiesAccess the contextExamples Adjust behavior based on retry attempt Log step metadata for observability

Every `step.do` callback receives a **context object** (`WorkflowStepContext`) as its first argument. The context gives your step code runtime information about the step itself, the current retry attempt, and the resolved configuration for that step.

## WorkflowStepContext
    
    
    type WorkflowStepContext = {
    	step: {
    		name: string;
    		count: number;
    	};
    	attempt: number;
    	config: WorkflowStepConfig;
    };

### Properties

Property | Type | Description  
---|---|---  
`step.name` | `string` | The name you passed to `step.do`.  
`step.count` | `number` | How many times `step.do` has been called with this name so far in the current Workflow run. Starts at `1` for the first call with a given name.  
`attempt` | `number` | The current attempt number (1-indexed). `1` on the first try, `2` on the first retry, and so on.  
`config` | [`WorkflowStepConfig`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig) | The resolved retry and timeout configuration for this step, including any defaults applied by the runtime.  
  
If a step config's `retries.delay` is a function, the dynamic delay is not exposed on `ctx.config.retries.delay`. The delay function receives its own context object with the current step context and the error that caused the retry.

## Access the context

Pass a parameter to your `step.do` callback to receive the context object:
    
    
    await step.do("my-step", async (ctx) => {
    	console.log(ctx.step.name); // "my-step"
    	console.log(ctx.step.count); // 1
    	console.log(ctx.attempt); // 1 on first try, 2 on first retry, etc.
    	console.log(ctx.config); // { retries: { limit: 5, ... }, timeout: "10 minutes" }
    });

The context is also available when you pass a custom `WorkflowStepConfig`:
    
    
    await step.do(
    	"call an API",
    	{
    		retries: {
    			limit: 10,
    			delay: "10 seconds",
    			backoff: "exponential",
    		},
    		timeout: "30 minutes",
    	},
    	async (ctx) => {
    		console.log(ctx.config.retries.limit); // 10
    		console.log(ctx.config.timeout); // "30 minutes"
    	},
    );

To configure delay functions, refer to [Set a dynamic retry delay](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/#set-a-dynamic-retry-delay).

## Examples

### Adjust behavior based on retry attempt

Use `ctx.attempt` to change how your step behaves on retries. For example, you might use a fallback endpoint after a certain number of retries:
    
    
    await step.do(
    	"fetch data",
    	{ retries: { limit: 5, delay: "5 seconds", backoff: "linear" } },
    	async (ctx) => {
    		const url =
    			ctx.attempt <= 3
    				? "https://api.example.com/primary"
    				: "https://api.example.com/fallback";
    
    		const response = await fetch(url);
    		if (!response.ok) {
    			throw new Error(`Request failed with status ${response.status}`);
    		}
    		return await response.json();
    	},
    );

### Log step metadata for observability

Use `ctx.step` to add structured metadata to your logs:
    
    
    await step.do("process-order", async (ctx) => {
    	console.log(
    		JSON.stringify({
    			step: ctx.step.name,
    			stepCount: ctx.step.count,
    			attempt: ctx.attempt,
    			retryLimit: ctx.config.retries?.limit,
    		}),
    	);
    
    	// Your step logic here
    });

[PreviousSleeping and retrying](https://developers.cloudflare.com/workflows/build/sleeping-and-retrying/)[NextEvents and parameters](https://developers.cloudflare.com/workflows/build/events-and-parameters/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workflows/build/step-context.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
