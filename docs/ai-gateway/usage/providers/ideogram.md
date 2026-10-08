---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/
title: Ideogram \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.699208+00:00
---

# Ideogram · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Ideogram



# Ideogram

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesExamples cURL Use with JavaScript

[Ideogram ↗︎](https://ideogram.ai/) provides advanced text-to-image generation models with exceptional text rendering capabilities and visual quality.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram

## Prerequisites

When making requests to Ideogram, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Ideogram API key.
  * The name of the Ideogram model you want to use (e.g., `V_3`).



## Examples

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram/v1/ideogram-v3/generate \
      --header 'Api-Key: {ideogram_api_key}' \
      --header 'Content-Type: application/json' \
      --data '{
        "prompt": "A serene landscape with mountains and a lake at sunset",
        "model": "V_3"
      }'

### Use with JavaScript

JavaScriptjs
    
    
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const ideogramApiKey = "{ideogram_api_key}";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/ideogram`;
    
    const response = await fetch(`${baseURL}/v1/ideogram-v3/generate`, {
      method: "POST",
      headers: {
        "Api-Key": ideogramApiKey,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt: "A serene landscape with mountains and a lake at sunset",
        model: "V_3",
      }),
    });
    
    const result = await response.json();
    console.log(result);

[PreviousHuggingFace](https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/)[NextMistral AI](https://developers.cloudflare.com/ai-gateway/usage/providers/mistral/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/ideogram.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
