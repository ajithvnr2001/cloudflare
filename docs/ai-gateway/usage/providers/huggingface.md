---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/
title: HuggingFace \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.583604+00:00
---

# HuggingFace · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /HuggingFace



# HuggingFace

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExamples cURL Use HuggingFace.js library with JavaScript

[HuggingFace ↗︎](https://huggingface.co/) helps users build, deploy and train machine learning models.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface

## URL structure

When making requests to HuggingFace Inference API, replace `https://api-inference.huggingface.co/models/` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface`. Note that the model you're trying to access should come right after, for example `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder`.

## Prerequisites

When making requests to HuggingFace, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active HuggingFace API token.
  * The name of the HuggingFace model you want to use.



## Examples

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder \
      --header 'Authorization: Bearer {hf_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "inputs": "console.log"
    }'

### Use HuggingFace.js library with JavaScript

If you are using the HuggingFace.js library, you can set your inference endpoint like this:

JavaScriptjs
    
    
    import { HfInferenceEndpoint } from "@huggingface/inference";
    
    const accountId = "{account_id}";
    const gatewayId = "{gateway_id}";
    const model = "gpt2";
    const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/huggingface/${model}`;
    const apiToken = env.HF_API_TOKEN;
    
    const hf = new HfInferenceEndpoint(baseURL, apiToken);

[PreviousGroq](https://developers.cloudflare.com/ai-gateway/usage/providers/groq/)[NextIdeogram](https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/huggingface.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
