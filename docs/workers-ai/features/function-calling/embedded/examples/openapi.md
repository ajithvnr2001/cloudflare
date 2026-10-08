---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/
title: Tools based on OpenAPI Spec \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:57.804954+00:00
---

# Tools based on OpenAPI Spec · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)[Embedded](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/)

  4. /Examples
  5. /Tools based on OpenAPI Spec



# Tools based on OpenAPI Spec

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Oftentimes APIs are defined and documented via [OpenAPI specification ↗︎](https://swagger.io/specification/). The Cloudflare `ai-utils` package's `createToolsFromOpenAPISpec` function creates tools from the OpenAPI spec, which the LLM can then leverage to fulfill the prompt.

In this example the LLM will describe the a Github user, based Github's API and its OpenAPI spec.

Embedded function calling example from OpenAPI Spects
    
    
    import { createToolsFromOpenAPISpec, runWithTools } from '@cloudflare/ai-utils';
    
    type Env = {
    	AI: Ai;
    };
    
    const APP_NAME = 'cf-fn-calling-example-app';
    
    export default {
    	async fetch(request, env, ctx) {
    		const toolsFromOpenAPISpec = [
    			// You can pass the OpenAPI spec link or contents directly
    			...(await createToolsFromOpenAPISpec(
    				'https://gist.githubusercontent.com/mchenco/fd8f20c8f06d50af40b94b0671273dc1/raw/f9d4b5cd5944cc32d6b34cad0406d96fd3acaca6/partial_api.github.com.json',
    				{
    					overrides: [
    						{
    							matcher: ({ url }) => {
    								return url.hostname === 'api.github.com';
    							},
    							// for all requests on *.github.com, we'll need to add a User-Agent.
    							values: {
    								headers: {
    									'User-Agent': APP_NAME,
    								},
    							},
    						},
    					],
    				}
    			)),
    		];
    
    		const response = await runWithTools(
    			env.AI,
    			'@hf/nousresearch/hermes-2-pro-mistral-7b',
    			{
    				messages: [
    					{
    						role: 'user',
    						content: 'Who is cloudflare on Github and how many repos does the organization have?',
    					},
    				],
    				tools: toolsFromOpenAPISpec,
    			}
    		);
    
    		return new Response(JSON.stringify(response));
    	},
    } satisfies ExportedHandler<Env>;

[PreviousUse fetch() handler](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/fetch/)[NextUse KV API](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/embedded/examples/openapi.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
