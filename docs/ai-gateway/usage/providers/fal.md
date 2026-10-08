---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/fal/
title: Fal AI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:34.329494+00:00
---

# Fal AI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/fal/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Fal AI



# Fal AI

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/usage/providers/fal/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointURL structurePrerequisitesDefault synchronous API cURL exampleCustom target URLs cURL example with custom target URLWebSocket APIJavaScript SDK integration JavaScript SDK example

[Fal AI ↗︎](https://fal.ai/) provides access to 600+ production-ready generative media models through a single, unified API. The service offers the world's largest collection of open image, video, voice, and audio generation models, all accessible with one line of code.

## Endpoint
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal

## URL structure

When making requests to Fal AI, replace `https://fal.run` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal`.

## Prerequisites

When making requests to Fal AI, ensure you have the following:

  * Your AI Gateway Account ID.
  * Your AI Gateway gateway name.
  * An active Fal AI API token.
  * The name of the Fal AI model you want to use.



## Default synchronous API

By default, requests to the Fal AI endpoint will hit the synchronous API at `https://fal.run/<path>`.

### cURL example
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal/fal-ai/fast-sdxl \
      --header 'Authorization: Key {fal_ai_token}' \
      --header 'Content-Type: application/json' \
      --data '{
        "prompt": "Make an image of a cat flying an aeroplane"
      }'

## Custom target URLs

If you need to hit a different target URL, you can supply the entire Fal target URL in the `x-fal-target-url` header.

### cURL example with custom target URL
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal \
      --header 'Authorization: Bearer {fal_ai_token}' \
      --header 'x-fal-target-url: https://queue.fal.run/fal-ai/bytedance/seedream/v4/edit' \
      --header 'Content-Type: application/json' \
      --data '{
        "prompt": "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
        ]
      }'

## WebSocket API

Fal AI also supports real-time interactions through WebSockets. For WebSocket connections and examples, see the [Realtime WebSockets API documentation](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/#fal-ai).

## JavaScript SDK integration

The `x-fal-target-url` format is compliant with the Fal SDKs, so AI Gateway can be easily passed as a `proxyUrl` in the SDKs.

### JavaScript SDK example
    
    
    import { fal } from "@fal-ai/client";
    
    fal.config({
      credentials: "{fal_ai_token}", // OR pass a cloudflare api token if using BYOK on AI Gateway
      proxyUrl: "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/fal"
    });
    
    const result = await fal.subscribe("fal-ai/bytedance/seedream/v4/edit", {
      "input": {
        "prompt": "Dress the model in the clothes and hat. Add a cat to the scene and change the background to a Victorian era building.",
        "image_urls": [
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_2.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_3.png",
          "https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_4.png"
        ]
      }
    });
    
    console.log(result.data.images[0]);

[PreviousElevenLabs](https://developers.cloudflare.com/ai-gateway/usage/providers/elevenlabs/)[NextGoogle AI Studio](https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/fal.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
