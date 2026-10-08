---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/
title: OpenRouter \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.881291+00:00
---

# OpenRouter · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /OpenRouter



# OpenRouter

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExamples cURL Use OpenAI SDK with JavaScript

[OpenRouter ↗︎](https://openrouter.ai/) is a platform that provides a unified interface for accessing and using large language models (LLMs).

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter

## URL structure

When making requests to [OpenRouter ↗︎](https://openrouter.ai/), replace `https://openrouter.ai/api/v1/chat/completions` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/chat/completions`.

## Prerequisites

When making requests to OpenRouter, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active OpenRouter API token or a token from the original model provider.
  * The name of the OpenRouter model you want to use.



## Examples

### cURL

Requestbash
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/v1/chat/completions \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer OPENROUTER_TOKEN' \
     --data '{
        "model": "openai/gpt-5-mini",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

### Use OpenAI SDK with JavaScript

If you are using the OpenAI SDK with JavaScript, you can set your endpoint like this:

JavaScriptjs
    
    
    import OpenAI from "openai";
    
    const openai = new OpenAI({
    	apiKey: env.OPENROUTER_TOKEN,
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/openrouter",
    });
    
    try {
    	const chatCompletion = await openai.chat.completions.create({
    		model: "openai/gpt-5-mini",
    		messages: [{ role: "user", content: "What is Cloudflare?" }],
    	});
    
    	const response = chatCompletion.choices[0].message;
    
    	return new Response(JSON.stringify(response));
    } catch (e) {
    	return new Response(e);
    }

[PreviousOpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/)[NextParallel](https://developers.cloudflare.com/ai-gateway/usage/providers/parallel/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/openrouter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
