---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/
title: Cerebras \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.024695+00:00
---

# Cerebras · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Cerebras



# Cerebras

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointPrerequisitesExamples cURLOpenAI-Compatible Endpoint

[Cerebras ↗︎](https://inference-docs.cerebras.ai/) offers developers a low-latency solution for AI model inference.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras

## Prerequisites

When making requests to Cerebras, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Cerebras API token.
  * The name of the Cerebras model you want to use.



## Examples

### cURL

Example fetch requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cerebras/chat/completions \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer CEREBRAS_TOKEN' \
     --data '{
        "model": "gpt-oss-120b",
        "messages": [
            {
                "role": "user",
                "content": "What is Cloudflare?"
            }
        ]
    }'

## OpenAI-Compatible Endpoint

You can also access Cerebras models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    "model": "cerebras/{model}"
    }

[PreviousCartesia](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/)[NextCohere](https://developers.cloudflare.com/ai-gateway/usage/providers/cohere/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/cerebras.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
