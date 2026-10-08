---
url: https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/
title: Stream OpenAI API Responses \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:24.193805+00:00
---

# Stream OpenAI API Responses · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Examples](https://developers.cloudflare.com/workers/examples/)
  4. /Openai Sdk Streaming



# Stream OpenAI API Responses

Use the OpenAI v4 SDK to stream responses from OpenAI.

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/openai-sdk-streaming)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

In order to run this code, you must install the OpenAI SDK by running `npm i openai`.

Note

For analytics, caching, rate limiting, and more, you can also send requests like this through Cloudflare's [AI Gateway](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/).
    
    
    import OpenAI from "openai";
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const openai = new OpenAI({
    			apiKey: env.OPENAI_API_KEY,
    		});
    
    		// Create a TransformStream to handle streaming data
    		let { readable, writable } = new TransformStream();
    		let writer = writable.getWriter();
    		const textEncoder = new TextEncoder();
    
    		ctx.waitUntil(
    			(async () => {
    				const stream = await openai.chat.completions.create({
    					model: "gpt-4o-mini",
    					messages: [{ role: "user", content: "Tell me a story" }],
    					stream: true,
    				});
    
    				// loop over the data as it is streamed and write to the writable
    				for await (const part of stream) {
    					writer.write(
    						textEncoder.encode(part.choices[0]?.delta?.content || ""),
    					);
    				}
    				writer.close();
    			})(),
    		);
    
    		// Send the readable back to the browser
    		return new Response(readable);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import { Hono } from "hono";
    import { streamText } from "hono/streaming";
    import OpenAI from "openai";
    
    interface Env {
    	OPENAI_API_KEY: string;
    }
    
    const app = new Hono<{ Bindings: Env }>();
    
    app.get("*", async (c) => {
    	const openai = new OpenAI({
    		apiKey: c.env.OPENAI_API_KEY,
    	});
    
    	const chatStream = await openai.chat.completions.create({
    		model: "gpt-4o-mini",
    		messages: [{ role: "user", content: "Tell me a story" }],
    		stream: true,
    	});
    
    	return streamText(c, async (stream) => {
    		for await (const message of chatStream) {
    			await stream.write(message.choices[0].delta.content || "");
    		}
    		stream.close();
    	});
    });
    
    export default app;

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/examples/openai-sdk-streaming.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
