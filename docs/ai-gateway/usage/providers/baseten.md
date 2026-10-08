---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/baseten/
title: Baseten \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:33.095264+00:00
---

# Baseten · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/baseten/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Baseten



# Baseten

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/baseten/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesOpenAI-compatible chat completions API cURL Use OpenAI SDK with JavaScriptOpenAI-Compatible EndpointModel-specific endpoints cURL Use with JavaScript

[Baseten ↗︎](https://www.baseten.co/) provides infrastructure for building and deploying machine learning models at scale. Baseten offers access to various language models through a unified chat completions API.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten

## Prerequisites

When making requests to Baseten, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Baseten API token.
  * The name of the Baseten model you want to use.



## OpenAI-compatible chat completions API

Baseten provides an OpenAI-compatible chat completions API for supported models.

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten/v1/chat/completions \
      --header 'Authorization: Bearer {baseten_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "model": "openai/gpt-oss-120b",
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ]
      }'

### Use OpenAI SDK with JavaScript

JavaScriptjs
    
    
    import OpenAI from "openai";
    
    const apiKey = "{baseten_api_token}";
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/baseten`;
    
    const openai = new OpenAI({
      apiKey,
      baseURL,
    });
    
    const model = "openai/gpt-oss-120b";
    const messages = [{ role: "user", content: "What is Cloudflare?" }];
    
    const chatCompletion = await openai.chat.completions.create({
      model,
      messages,
    });
    
    console.log(chatCompletion);

## OpenAI-Compatible Endpoint

You can also access Baseten models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "baseten/{model}"
    }

## Model-specific endpoints

For models that don't use the OpenAI-compatible API, you can access them through their specific model endpoints.

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/baseten/model/{model_id} \
      --header 'Authorization: Bearer {baseten_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "prompt": "What is Cloudflare?",
        "max_tokens": 100
      }'

### Use with JavaScript

JavaScriptjs
    
    
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const basetenApiToken = "{baseten_api_token}";
    const modelId = "{model_id}";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/baseten`;
    
    const response = await fetch(`${baseURL}/model/${modelId}`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${basetenApiToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt: "What is Cloudflare?",
        max_tokens: 100,
      }),
    });
    
    const result = await response.json();
    console.log(result);

[PreviousAzure OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/)[NextCartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/baseten.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
