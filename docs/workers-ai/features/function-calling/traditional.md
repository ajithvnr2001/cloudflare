---
url: https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/
title: Traditional function calling \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:58.137850+00:00
---

# Traditional function calling · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /…

Features

  4. /[Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)
  5. /Traditional



# Traditional

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This page shows how you can do traditional function calling, as defined by industry standards. Workers AI also offers [embedded function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/), which is drastically easier than traditional function calling.

With traditional function calling, you define an array of tools with the name, description, and tool arguments. The example below shows how you would pass a tool called `getWeather` in an inference request to a model.

Traditional function calling examplejs
    
    
    const response = await env.AI.run("@hf/nousresearch/hermes-2-pro-mistral-7b", {
    	messages: [
    		{
    			role: "user",
    			content: "what is the weather in london?",
    		},
    	],
    	tools: [
    		{
    			name: "getWeather",
    			description: "Return the weather for a latitude and longitude",
    			parameters: {
    				type: "object",
    				properties: {
    					latitude: {
    						type: "string",
    						description: "The latitude for the given location",
    					},
    					longitude: {
    						type: "string",
    						description: "The longitude for the given location",
    					},
    				},
    				required: ["latitude", "longitude"],
    			},
    		},
    	],
    });
    
    return new Response(JSON.stringify(response.tool_calls));

The LLM will then return a JSON object with the required arguments and the name of the tool that was called. You can then pass this JSON object to make an API call.
    
    
    [
    	{
    		"arguments": { "latitude": "51.5074", "longitude": "-0.1278" },
    		"name": "getWeather"
    	}
    ]

For a working example on how to do function calling, take a look at our [demo app ↗︎](https://github.com/craigsdennis/lightbulb-moment-tool-calling/blob/main/src/index.ts).

[PreviousTroubleshooting](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/troubleshooting/)[NextJSON Mode](https://developers.cloudflare.com/workers-ai/features/json-mode/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/features/function-calling/traditional.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
