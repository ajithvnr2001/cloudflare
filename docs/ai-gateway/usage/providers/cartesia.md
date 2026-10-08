---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/
title: Cartesia \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:33.930495+00:00
---

# Cartesia · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Cartesia



# Cartesia

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/cartesia/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL StructurePrerequisitesExample cURL

[Cartesia ↗︎](https://docs.cartesia.ai/) provides advanced text-to-speech services with customizable voice models.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia

## URL Structure

When making requests to Cartesia, replace `https://api.cartesia.ai/v1` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia`.

## Prerequisites

When making requests to Cartesia, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Cartesia API token.
  * The model ID and voice ID for the Cartesia voice model you want to use.



## Example

### cURL

Requestbash
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/cartesia/tts/bytes \
      --header 'Content-Type: application/json' \
      --header 'Cartesia-Version: 2024-06-10' \
      --header 'X-API-Key: {cartesia_api_token}' \
      --data '{
        "transcript": "Welcome to Cloudflare - AI Gateway!",
        "model_id": "sonic-english",
        "voice": {
            "mode": "id",
            "id": "694f9389-aac1-45b6-b726-9d9369183238"
        },
        "output_format": {
            "container": "wav",
            "encoding": "pcm_f32le",
            "sample_rate": 44100
        }
    }

[PreviousBaseten](https://developers.cloudflare.com/ai-gateway/usage/providers/baseten/)[NextCerebras](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/cartesia.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
