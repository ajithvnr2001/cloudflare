---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/
title: Use KV API \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.757037+00:00
---

# Use KV API · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)[Embedded](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/)

  4. /Examples
  5. /Use KV API



# Use KV API

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPre-RequisitesWorker codeVerify results

Interact with persistent storage to retrieve or store information enables for powerful use cases.

In this example we show how embedded function calling can interact with other resources on the Cloudflare Developer Platform with a few lines of code.

## Pre-Requisites

For this example to work, you need to provision a [KV](https://developers.cloudflare.com/kv/) namespace first. To do so, follow the [KV - Get started ](https://developers.cloudflare.com/kv/get-started/) guide.

Importantly, your Wrangler file must be updated to include the `KV` binding definition to your respective namespace.

## Worker code

Embedded function calling example with KV APIts
    
    
    import { runWithTools } from "@cloudflare/ai-utils";
    
    type Env = {
    	AI: Ai;
    	KV: KVNamespace;
    };
    
    export default {
    	async fetch(request, env, ctx) {
    		// Define function
    		const updateKvValue = async ({
    			key,
    			value,
    		}: {
    			key: string;
    			value: string;
    		}) => {
    			const response = await env.KV.put(key, value);
    			return `Successfully updated key-value pair in database: ${response}`;
    		};
    
    		// Run AI inference with function calling
    		const response = await runWithTools(
    			env.AI,
    			"@hf/nousresearch/hermes-2-pro-mistral-7b",
    			{
    				messages: [
    					{ role: "system", content: "Put user given values in KV" },
    					{ role: "user", content: "Set the value of banana to yellow." },
    				],
    				tools: [
    					{
    						name: "KV update",
    						description: "Update a key-value pair in the database",
    						parameters: {
    							type: "object",
    							properties: {
    								key: {
    									type: "string",
    									description: "The key to update",
    								},
    								value: {
    									type: "string",
    									description: "The value to update",
    								},
    							},
    							required: ["key", "value"],
    						},
    						function: updateKvValue,
    					},
    				],
    			},
    		);
    		return new Response(JSON.stringify(response));
    	},
    } satisfies ExportedHandler<Env>;

## Verify results

To verify the results, run the following command
    
    
    npx wrangler kv key get banana --binding KV --local

[PreviousTools based on OpenAPI Spec](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/)[NextAPI Reference](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/api-reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/embedded/examples/kv.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
