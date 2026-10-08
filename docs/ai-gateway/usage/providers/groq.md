---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/groq/
title: Groq \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.540219+00:00
---

# Groq · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/groq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Groq



# Groq

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/groq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExamples cURL Use Groq SDK with JavaScriptOpenAI-Compatible Endpoint

[Groq ↗︎](https://groq.com/) delivers high-speed processing and low-latency performance.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq

## URL structure

When making requests to [Groq ↗︎](https://groq.com/), replace `https://api.groq.com/openai/v1` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq`.

## Prerequisites

When making requests to Groq, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Groq API token.
  * The name of the Groq model you want to use.



## Examples

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/groq/chat/completions \
      --header 'Authorization: Bearer {groq_api_key}' \
      --header 'Content-Type: application/json' \
      --data '{
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ],
        "model": "llama3-8b-8192"
    }'

### Use Groq SDK with JavaScript

If using the [`groq-sdk` ↗︎](https://www.npmjs.com/package/groq-sdk), set your endpoint like this:

JavaScriptjs
    
    
    import Groq from "groq-sdk";
    
    const apiKey = env.GROQ_API_KEY;
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/groq`;
    
    const groq = new Groq({
    	apiKey,
    	baseURL,
    });
    
    const messages = [{ role: "user", content: "What is Cloudflare?" }];
    const model = "llama3-8b-8192";
    
    const chatCompletion = await groq.chat.completions.create({
    	messages,
    	model,
    });

## OpenAI-Compatible Endpoint

You can also access Groq models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "groq/{model}"
    }

[PreviousGoogle Vertex AI](https://developers.cloudflare.com/ai-gateway/usage/providers/vertex/)[NextHuggingFace](https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/groq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
