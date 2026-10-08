---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/
title: Google AI Studio \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.495983+00:00
---

# Google AI Studio · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Google AI Studio



# Google AI Studio

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointExamples cURL @google/genaiOpenAI-Compatible Endpoint

[Google AI Studio ↗︎](https://ai.google.dev/aistudio) helps you build quickly with Google Gemini models.

## Endpoint

**Base URL:**
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio

Then you can append the endpoint you want to hit, for example: `v1/models/{model}:{generative_ai_rest_resource}`

So your final URL will come together as: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio/v1/models/{model}:{generative_ai_rest_resource}`.

## Examples

### cURL

With API Key in Request
    
    
    curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
     --header 'content-type: application/json' \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --header 'x-goog-api-key: {google_studio_api_key}' \
     --data '{
          "contents": [
              {
                "role":"user",
                "parts": [
                  {"text":"What is Cloudflare?"}
                ]
              }
            ]
          }'
    
    
    curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
     --header 'content-type: application/json' \
     --header 'x-goog-api-key: {google_studio_api_key}' \
     --data '{
          "contents": [
              {
                "role":"user",
                "parts": [
                  {"text":"What is Cloudflare?"}
                ]
              }
            ]
          }'

With Stored Keys (BYOK) / Unified Billing
    
    
    curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
     --header 'content-type: application/json' \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --data '{
          "contents": [
              {
                "role":"user",
                "parts": [
                  {"text":"What is Cloudflare?"}
                ]
              }
            ]
          }'

### `@google/genai`

If you are using the `@google/genai` package, you can set your endpoint like this:

With Key in Request
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({
      apiKey: "{google_studio_api_key}",
      httpOptions: {
    	  baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
    	  headers: {
    		  'cf-aig-authorization': 'Bearer {cf_aig_token}',
    	  }	
      }
    });
    
    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: "What is Cloudflare?",
    });
    
    console.log(response.text);
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({
      apiKey: "{google_studio_api_key}",
      httpOptions: {
    	  baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
      }
    });
    
    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: "What is Cloudflare?",
    });
    
    console.log(response.text);

With Stored Keys (BYOK) / Unified Billing
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({
      apiKey: "{cf_aig_token}",
      httpOptions: {
    	  baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
      }
    });
    
    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: "What is Cloudflare?",
    });
    
    console.log(response.text);

## OpenAI-Compatible Endpoint

You can also access Google AI Studio models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "google-ai-studio/{model}"
    }

[PreviousFal AI](https://developers.cloudflare.com/ai-gateway/usage/providers/fal/)[NextGoogle Vertex AI](https://developers.cloudflare.com/ai-gateway/usage/providers/vertex/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/google-ai-studio.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
