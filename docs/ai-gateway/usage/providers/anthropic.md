---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/
title: Anthropic \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:33.027693+00:00
---

# Anthropic · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Anthropic



# Anthropic

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointExamples cURL Anthropic SDKOpenAI-Compatible Endpoint

[Anthropic ↗︎](https://www.anthropic.com/) helps build reliable, interpretable, and steerable AI systems.

## Endpoint

**Base URL**
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic

## Examples

### cURL

With API Key in Request
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'x-api-key: {anthropic_api_key}' \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'x-api-key: {anthropic_api_key}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'

With Stored Keys (BYOK) / Unified Billing
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'

### Anthropic SDK

With Key in Request
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    
    const anthropic = new Anthropic({
    	apiKey: "{ANTHROPIC_API_KEY}",
    	baseURL,
    	defaultHeaders: {
    		Authorization: `Bearer {cf_api_token}`,
    	},
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    
    const anthropic = new Anthropic({
    	apiKey: "{ANTHROPIC_API_KEY}",
    	baseURL,
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });

With Stored Keys (BYOK) / Unified Billing
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    
    const anthropic = new Anthropic({
    	apiKey: "placeholder", // Ignored by AI Gateway when using BYOK or Unified Billing, but the SDK requires a value.
    	baseURL,
    	defaultHeaders: {
    		Authorization: `Bearer {cf_api_token}`,
    	},
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });

Note

When using BYOK or Unified Billing, do not set `x-api-key` in `defaultHeaders`. AI Gateway supplies the Anthropic key for you, and adding your own `x-api-key` header will cause the request to fail. The `apiKey` value in the example is a placeholder to satisfy the Anthropic SDK, which requires either the `apiKey` option or the `ANTHROPIC_API_KEY` environment variable to be set.

## OpenAI-Compatible Endpoint

You can also access Anthropic models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    	"model": "anthropic/{model}"
    }

[PreviousAmazon Bedrock](https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/)[NextAzure OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/anthropic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
