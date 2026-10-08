---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/
title: Mistral AI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.792830+00:00
---

# Mistral AI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Mistral AI



# Mistral AI

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesURL structureExamples cURL Use @mistralai/mistralai package with JavaScriptOpenAI-Compatible Endpoint

[Mistral AI ↗︎](https://mistral.ai) helps you build quickly with Mistral's advanced AI models.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral

## Prerequisites

When making requests to the Mistral AI, you will need:

  * AI Gateway Account ID
  * AI Gateway gateway name
  * Mistral AI API token
  * Mistral AI model name



## URL structure

Your new base URL will use the data above in this structure: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/`.

Then you can append the endpoint you want to hit, for example: `v1/chat/completions`

So your final URL will come together as: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions`.

## Examples

### cURL

Example fetch requestbash
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral/v1/chat/completions \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer MISTRAL_TOKEN' \
     --data '{
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

### Use `@mistralai/mistralai` package with JavaScript

If you are using the `@mistralai/mistralai` package, you can set your endpoint like this:

JavaScript examplejs
    
    
    import { Mistral } from "@mistralai/mistralai";
    
    const client = new Mistral({
    	apiKey: MISTRAL_TOKEN,
    	serverURL: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/mistral`,
    });
    
    await client.chat.create({
    	model: "mistral-large-latest",
    	messages: [
    		{
    			role: "user",
    			content: "What is Cloudflare?",
    		},
    	],
    });

## OpenAI-Compatible Endpoint

You can also access Mistral models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "mistral/{model}"
    }

[PreviousIdeogram](https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/)[NextOpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/mistral.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
