---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/
title: DeepSeek \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.082124+00:00
---

# DeepSeek · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /DeepSeek



# DeepSeek

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesURL structureExamples cURL with a provider key cURL with stored keys (BYOK) Use DeepSeek with JavaScriptOpenAI-Compatible Endpoint

[DeepSeek ↗︎](https://www.deepseek.com/) helps you build quickly with DeepSeek's advanced AI models.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek

## Prerequisites

When making requests to DeepSeek, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active DeepSeek AI API token.
  * The name of the DeepSeek AI model you want to use.



## URL structure

Your new base URL will use the data above in this structure:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/`.

You can then append the endpoint you want to hit, for example: `chat/completions`.

So your final URL will come together as:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions`.

## Examples

### cURL with a provider key

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
     --data '{
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

### cURL with stored keys (BYOK)

Store your DeepSeek key with [bring your own keys (BYOK)](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Then omit the `Authorization` header so AI Gateway can substitute the stored key:

Example BYOK requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
     --header 'content-type: application/json' \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --data '{
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

### Use DeepSeek with JavaScript

If you are using the OpenAI SDK, you can set your endpoint like this:

JavaScriptjs
    
    
    import OpenAI from "openai";
    
    const openai = new OpenAI({
    	apiKey: env.DEEPSEEK_TOKEN,
    	baseURL:
    		"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek",
    });
    
    try {
    	const chatCompletion = await openai.chat.completions.create({
    		model: "deepseek-chat",
    		messages: [{ role: "user", content: "What is Cloudflare?" }],
    	});
    
    	const response = chatCompletion.choices[0].message;
    
    	return new Response(JSON.stringify(response));
    } catch (e) {
    	return new Response(e);
    }

## OpenAI-Compatible Endpoint

You can also access DeepSeek models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "deepseek/{model}"
    }

[PreviousDeepgram](https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/)[NextElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/deepseek.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
