---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/
title: Use fetch() handler \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.655136+00:00
---

# Use fetch() handler · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)[Embedded](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/)

  4. /Examples
  5. /Use fetch() handler



# Use fetch() handler

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A very common use case is to provide the LLM with the ability to perform API calls via function calling.

In this example the LLM will retrieve the weather forecast for the next 5 days. To do so a `getWeather` function is defined that is passed to the LLM as tool.

The `getWeather`function extracts the user's location from the request and calls the external weather API via the Workers' [`Fetch API`](https://developers.cloudflare.com/workers/runtime-apis/fetch/) and returns the result.

Embedded function calling example with fetch()ts
    
    
    import { runWithTools } from '@cloudflare/ai-utils';
    
    type Env = {
    	AI: Ai;
    };
    
    export default {
    	async fetch(request, env, ctx) {
    		// Define function
    		const getWeather = async (args: { numDays: number }) => {
    			const { numDays } = args;
          // Location is extracted from request based on
          // https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties
          const lat = request.cf?.latitude
          const long = request.cf?.longitude
    
          // Interpolate values for external API call
    			const response = await fetch(
    				`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${long}&daily=temperature_2m_max,precipitation_sum&timezone=GMT&forecast_days=${numDays}`
    			);
    			return response.text();
    		};
    		// Run AI inference with function calling
    		const response = await runWithTools(
    			env.AI,
    			// Model with function calling support
    			'@hf/nousresearch/hermes-2-pro-mistral-7b',
    			{
    				// Messages
    				messages: [
    					{
    						role: 'user',
    						content: 'What the weather like the next 5 days? Respond as text',
    					},
    				],
    				// Definition of available tools the AI model can leverage
    				tools: [
    					{
    						name: 'getWeather',
    						description: 'Get the weather for the next [numDays] days',
    						parameters: {
    							type: 'object',
    							properties: {
    								numDays: { type: 'numDays', description: 'number of days for the weather forecast' },
    							},
    							required: ['numDays'],
    						},
    						// reference to previously defined function
    						function: getWeather,
    					},
    				],
    			}
    		);
    		return new Response(JSON.stringify(response));
    	},
    } satisfies ExportedHandler<Env>;

[PreviousGet Started](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/get-started/)[NextTools based on OpenAPI Spec](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/embedded/examples/fetch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
