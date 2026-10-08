---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/
title: Workers AI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:35.651279+00:00
---

# Workers AI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Workers AI



# Workers AI

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewREST APIWorkers binding

Use AI Gateway as a unified control layer for [Workers AI](https://developers.cloudflare.com/workers-ai/) requests, with analytics, logging, caching, security, and prepaid billing. To use prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), set the gateway's [Workers AI billing setting](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing) to **Unified billing**. Requests to frontier models billed with prepaid credits receive [higher rate limits](https://developers.cloudflare.com/workers-ai/platform/limits/#paid-models).

## REST API

Use the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/) to call Workers AI models. Workers AI models use the `@cf/` prefix in the model name and require the `cf-aig-gateway-id` header to specify which gateway to route through.

Request to Workers AI Kimi modelbash
    
    
    # Run `wrangler whoami` to get your account ID to replace $CLOUDFLARE_ACCOUNT_ID,
    # and `wrangler auth token` to get an auth token to replace $CLOUDFLARE_API_TOKEN.
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "cf-aig-gateway-id: default" \
      --header "Content-Type: application/json" \
      --data '{
        "model": "@cf/moonshotai/kimi-k2.6",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

## Workers binding

You can integrate Workers AI with AI Gateway using an environment binding. To include an AI Gateway within your Worker, add the gateway as an object in your Workers AI request.
    
    
    export default {
    	async fetch(request, env) {
    		const response = await env.AI.run(
    			"@cf/meta/llama-3.1-8b-instruct",
    			{
    				prompt: "Why should you use Cloudflare for your AI inference?",
    			},
    			{
    				gateway: {
    					id: "{gateway_id}",
    					skipCache: false,
    					cacheTtl: 3360,
    				},
    			},
    		);
    		return new Response(JSON.stringify(response));
    	},
    };
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const response = await env.AI.run(
    			"@cf/meta/llama-3.1-8b-instruct",
    			{
    				prompt: "Why should you use Cloudflare for your AI inference?",
    			},
    			{
    				gateway: {
    					id: "{gateway_id}",
    					skipCache: false,
    					cacheTtl: 3360,
    				},
    			},
    		);
    		return new Response(JSON.stringify(response));
    	},
    } satisfies ExportedHandler<Env>;

For a detailed step-by-step guide on integrating Workers AI with AI Gateway using a binding, refer to [Integrations in AI Gateway](https://developers.cloudflare.com/ai-gateway/integrations/aig-workers-ai-binding/).

Workers AI supports the following parameters for AI gateways:

  * `id` string 
    * Name of your existing [AI Gateway](https://developers.cloudflare.com/ai-gateway/get-started/). Must be in the same account as your Worker.
  * `skipCache` boolean(default: false) 
    * Controls whether the request should [skip the cache](https://developers.cloudflare.com/ai-gateway/features/caching/#skip-cache-cf-aig-skip-cache).
  * `cacheTtl` number 
    * Controls the [Cache TTL](https://developers.cloudflare.com/ai-gateway/features/caching/#cache-ttl-cf-aig-cache-ttl).



[PreviousUnified API (OpenAI compat)](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/)[NextAmazon Bedrock](https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/workersai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
