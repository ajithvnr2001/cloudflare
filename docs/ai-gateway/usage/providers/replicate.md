---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/
title: Replicate \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:35.326416+00:00
---

# Replicate · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Replicate



# Replicate

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesExample cURL

[Replicate ↗︎](https://replicate.com/) runs and fine tunes open-source models.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate

## URL structure

When making requests to Replicate, replace `https://api.replicate.com/v1` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate`.

## Prerequisites

When making requests to Replicate, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Replicate API token. You can create one at [replicate.com/account/api-tokens ↗︎](https://replicate.com/account/api-tokens)
  * The name of the Replicate model you want to use, like `anthropic/claude-4.5-haiku` or `google/nano-banana`.



## Example

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \
      --header 'Authorization: Bearer {replicate_api_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "version": "anthropic/claude-4.5-haiku",
        "input":
          {
            "prompt": "Write a haiku about Cloudflare"
          }
        }'

[PreviousPerplexity](https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/)[NextxAI](https://developers.cloudflare.com/ai-gateway/usage/providers/grok/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/replicate.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
