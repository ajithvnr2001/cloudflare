---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/
title: Grok Imagine Image Quality (xAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:08.315832+00:00
---

# Grok Imagine Image Quality (xAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Imagine Image Quality

Text-to-Image • xAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-imagine-image-quality`

  * Third-party
  * Zero data retention



xAI's higher-fidelity text-to-image model optimized for sharper details, more accurate compositions, and stronger text rendering. Supports image editing via reference images and masks. Trades speed for quality compared to grok-imagine-image. Default output at 2k resolution.

Model Info|   
---|---  
Terms and License| [link ↗](https://x.ai/legal/terms-of-service)  
More information| [link ↗](https://docs.x.ai/developers/models/grok-imagine-image-quality)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.05
  * Per input image$0.01

  
  
## Usage
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-quality',
      { prompt: 'A golden retriever puppy playing in autumn leaves' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-quality",
      "input": {
        "prompt": "A golden retriever puppy playing in autumn leaves"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/simple-generation.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/simple-generation.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**High Quality Portrait** — High-quality portrait-orientation render at 2K resolution
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-quality',
      {
        prompt:
          'A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures',
        aspect_ratio: '3:4',
        quality: 'high',
        resolution: '2k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-quality",
      "input": {
        "prompt": "A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures",
        "aspect_ratio": "3:4",
        "quality": "high",
        "resolution": "2k"
      }
    }'

![High Quality Portrait](https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/high-quality-portrait.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/high-quality-portrait.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Cinematic Widescreen** — Widescreen cinematic composition
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-quality',
      {
        prompt:
          'A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting',
        aspect_ratio: '16:9',
        quality: 'high',
        resolution: '2k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-quality",
      "input": {
        "prompt": "A neon-lit cyberpunk figure standing in the rain beneath a holographic billboard, cinematic lighting",
        "aspect_ratio": "16:9",
        "quality": "high",
        "resolution": "2k"
      }
    }'

![Cinematic Widescreen](https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/cinematic-widescreen.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/cinematic-widescreen.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Medium Quality Landscape** — Balanced quality landscape render
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-quality',
      {
        prompt:
          'A panoramic view of the northern lights over a snowy mountain range, vivid greens and purples dancing across the sky',
        aspect_ratio: '16:9',
        quality: 'medium',
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-quality",
      "input": {
        "prompt": "A panoramic view of the northern lights over a snowy mountain range, vivid greens and purples dancing across the sky",
        "aspect_ratio": "16:9",
        "quality": "medium",
        "resolution": "1k"
      }
    }'

![Medium Quality Landscape](https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/medium-quality-landscape.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/medium-quality-landscape.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Square Low Quality Draft** — Fast, rough draft for iteration
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-image-quality',
      {
        prompt: 'A quiet Japanese garden in morning mist with a stone lantern and koi pond',
        aspect_ratio: '1:1',
        quality: 'low',
        resolution: '1k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-image-quality",
      "input": {
        "prompt": "A quiet Japanese garden in morning mist with a stone lantern and koi pond",
        "aspect_ratio": "1:1",
        "quality": "low",
        "resolution": "1k"
      }
    }'

![Square Low Quality Draft](https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/square-low-quality-draft.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/xai/grok-imagine-image-quality/square-low-quality-draft.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`required

n

`integer`minimum: 1maximum: 10

aspect_ratio

`string`enum: 1:1, 3:4, 4:3, 9:16, 16:9, 2:3, 3:2, 9:19.5, 19.5:9, 9:20, 20:9, 1:2, 2:1, auto

quality

`string`enum: low, medium, high

resolution

`string`enum: 1k, 2k

response_format

`string`enum: url, b64_json

user

`string`

▶image{}

`object`

▶images[]

`array`maxItems: 10

▶mask{}

`object`

image

`string`Generated image. Either a base64 data URI (`data:image/png;base64,...`) or an `https://` URL, depending on the upstream `response_format` (defaults to base64).

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-image-quality/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
