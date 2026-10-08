---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/
title: Grok Imagine Image 2.0 (xAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:08.075598+00:00
---

# Grok Imagine Image 2.0 (xAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Imagine Image 2.0

Text-to-Image • xAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-imagine-image-2.0`

  * Third-party



xAI's Grok Imagine Image 2.0 is a precise image generation and editing model for creative work, with strong instruction following, typography, layout, and reference-image preservation.

Model Info|   
---|---  
Terms and License| [link ↗](https://x.ai/legal/terms-of-service)  
More information| [link ↗](https://docs.x.ai/developers/model-capabilities/images/generation)  
Pricing| 

  * Per image$0.04
  * Per input image$0.01

  
  
## Usage
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-2.0',
      { prompt: 'A concert poster for a synthwave band, bold retro typography, sharp small print' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-2.0",
      "input": {
        "prompt": "A concert poster for a synthwave band, bold retro typography, sharp small print"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/simple-generation.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Portrait 2K** — High-resolution image with a controlled aspect ratio
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-2.0',
      {
        aspect_ratio: '3:4',
        prompt:
          'A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures',
        quality: 'medium',
        resolution: '2k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-2.0",
      "input": {
        "aspect_ratio": "3:4",
        "prompt": "A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures",
        "quality": "medium",
        "resolution": "2k"
      }
    }'

![Portrait 2K](https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/portrait-2k.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/portrait-2k.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Low Quality Draft** — Fast low-quality draft for iteration
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-2.0',
      {
        aspect_ratio: '1:1',
        prompt: 'A quiet Japanese garden in morning mist with a stone lantern and koi pond',
        quality: 'low',
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-2.0",
      "input": {
        "aspect_ratio": "1:1",
        "prompt": "A quiet Japanese garden in morning mist with a stone lantern and koi pond",
        "quality": "low",
        "resolution": "1k"
      }
    }'

![Low Quality Draft](https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/low-quality-draft.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-2.0/low-quality-draft.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`required

aspect_ratio

`string`enum: 1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, auto

quality

`string`enum: low, medium

resolution

`string`enum: 1k, 2k

response_format

`string`enum: url, b64_json

user

`string`

▶image{}

`object`

▶images[]

`array`maxItems: 5

▶mask{}

`object`

image

`string`Generated image. Either a base64 data URI (`data:image/png;base64,...`) or an `https://` URL, depending on the upstream `response_format`.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-2.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
