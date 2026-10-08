---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/
title: Grok Imagine Video (xAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:08.420652+00:00
---

# Grok Imagine Video (xAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Imagine Video

Text-to-Video • xAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-imagine-video`

  * Third-party
  * Zero data retention



xAI's video generation model. Generates, edits, and extends videos from text and image inputs with native synchronized audio including dialogue, sound effects, and music. Supports multiple creative modes (normal, fun, custom).

Model Info|   
---|---  
Terms and License| [link ↗](https://x.ai/legal/terms-of-service)  
More information| [link ↗](https://docs.x.ai/developers/models/grok-imagine-video)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.05
  * @480p (per second)$0.05
  * @720p (per second)$0.07

  
  
## Usage
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-video',
      {
        prompt: 'A golden retriever running through a field of sunflowers on a sunny day',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-video",
      "input": {
        "prompt": "A golden retriever running through a field of sunflowers on a sunny day",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/xai/grok-imagine-video/simple-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Portrait Video** — Vertical video for social media
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-video',
      {
        prompt: 'Slow-motion close-up of ink drops blooming through water against a black background',
        aspect_ratio: '9:16',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-video",
      "input": {
        "prompt": "Slow-motion close-up of ink drops blooming through water against a black background",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/xai/grok-imagine-video/portrait-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Cinematic Landscape** — Widescreen cinematic shot at extended duration
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-video',
      {
        prompt:
          'A wide drone shot over snow-covered mountain peaks at sunrise, dramatic lighting with low clouds',
        aspect_ratio: '16:9',
        duration: 10,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-video",
      "input": {
        "prompt": "A wide drone shot over snow-covered mountain peaks at sunrise, dramatic lighting with low clouds",
        "aspect_ratio": "16:9",
        "duration": 10,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/xai/grok-imagine-video/cinematic-landscape.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

_operation

`string`enum: generate, edit, extend

prompt

`string`

duration

`integer`minimum: 1maximum: 15

aspect_ratio

`string`enum: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3

resolution

`string`enum: 480p, 720p

size

`string`enum: 848x480, 1696x960, 1280x720, 1920x1080

▶image{}

`object`

▶video{}

`object`

▶reference_images[]

`array`maxItems: 10

▶output{}

`object`

user

`string`

video

`string`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
