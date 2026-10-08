---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/
title: Perplexity \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.978178+00:00
---

# Perplexity · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Perplexity



# Perplexity

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesExamples cURL Use Perplexity through OpenAI SDK with JavaScriptOpenAI-Compatible Endpoint

[Perplexity ↗︎](https://www.perplexity.ai/) is an AI powered answer engine.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai

## Prerequisites

When making requests to Perplexity, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Perplexity API token.
  * The name of the Perplexity model you want to use.



## Examples

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai/chat/completions \
         --header 'accept: application/json' \
         --header 'content-type: application/json' \
         --header 'Authorization: Bearer {perplexity_token}' \
         --data '{
          "model": "mistral-7b-instruct",
          "messages": [
            {
              "role": "user",
              "content": "What is Cloudflare?"
            }
          ]
        }'

### Use Perplexity through OpenAI SDK with JavaScript

Perplexity does not have their own SDK, but they have compatibility with the OpenAI SDK. You can use the OpenAI SDK to make a Perplexity call through AI Gateway as follows:

JavaScriptjs
    
    
    import OpenAI from "openai";
    
    const apiKey = env.PERPLEXITY_API_KEY;
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/perplexity-ai`;
    
    const perplexity = new OpenAI({
    	apiKey,
    	baseURL,
    });
    
    const model = "mistral-7b-instruct";
    const messages = [{ role: "user", content: "What is Cloudflare?" }];
    const maxTokens = 20;
    
    const chatCompletion = await perplexity.chat.completions.create({
    	model,
    	messages,
    	max_tokens: maxTokens,
    });

## OpenAI-Compatible Endpoint

You can also access Perplexity models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "perplexity/{model}"
    }

[PreviousParallel](https://developers.cloudflare.com/ai-gateway/usage/providers/parallel/)[NextReplicate](https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/perplexity.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
