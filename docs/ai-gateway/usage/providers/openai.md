---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
title: OpenAI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.638912+00:00
---

# OpenAI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/openai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /OpenAI



# OpenAI

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointExamples OpenAI SDK

[OpenAI ↗︎](https://openai.com/about/) helps you build with GPT models.

## Endpoint

**Base URL**
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai

When making requests to OpenAI, replace `https://api.openai.com/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai`.

**Chat completions endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions`

**Responses endpoint**

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses`

## Examples

### OpenAI SDK

With Key in Request
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "YOUR_OPENAI_API_KEY",
    	defaultHeaders: {
    		"cf-aig-authorization": `Bearer {cf_api_token}`,
    	},
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
    });
    
    const response = await client.chat.completions.create({
    	model: "gpt-4o-mini",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "YOUR_OPENAI_API_KEY",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
    });
    
    const response = await client.chat.completions.create({
    	model: "gpt-4o-mini",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });

With Stored Keys (BYOK) / Unified Billing
    
    
    import OpenAI from "openai";
    
    const client = new OpenAI({
    	apiKey: "{cf_api_token}",
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
    });
    
    // Ensure your OpenAI API key is stored with BYOK
    // or Unified Billing has credits
    const response = await client.chat.completions.create({
    	model: "gpt-4o-mini",
    	messages: [{ role: "user", content: "Hello, world!" }],
    });

### cURL

Responses API with API Key in Request
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
      --header 'Authorization: Bearer {OPENAI_API_KEY}' \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
      	"model": "gpt-5.1",
      	"input": [
        	{
          	"role": "user",
          	"content": "Write a one-sentence bedtime story about a unicorn."
        	}
      	]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
      --header 'Authorization: Bearer {OPENAI_API_KEY}' \
      --header 'Content-Type: application/json' \
      --data '{
      	"model": "gpt-5.1",
      	"input": [
        	{
          	"role": "user",
          	"content": "Write a one-sentence bedtime story about a unicorn."
        	}
      	]
      }'

Chat Completions with API Key in Request
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
      --header 'Authorization: Bearer {OPENAI_API_KEY}' \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "gpt-4o-mini",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
      --header 'Authorization: Bearer {OPENAI_API_KEY}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "gpt-4o-mini",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

Responses API with Stored Keys (BYOK) / Unified Billing
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
      	"model": "gpt-5.1",
      	"input": [
        	{
          	"role": "user",
          	"content": "Write a one-sentence bedtime story about a unicorn."
        	}
      	]
      }'

Chat Completions with Stored Keys (BYOK) / Unified Billing
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \
      --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "gpt-4o-mini",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

[PreviousMistral AI](https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/)[NextOpenRouter](https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/openai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
