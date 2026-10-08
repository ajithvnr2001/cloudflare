---
url: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/
title: Grok Imagine Video 1.5 Preview (xAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:08.355013+00:00
---

# Grok Imagine Video 1.5 Preview (xAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![xAI logo](https://developers.cloudflare.com/_astro/xai.2Y8IhZGx.svg)

# Grok Imagine Video 1.5 Preview

Image-to-Video • xAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`xai/grok-imagine-video-1.5-preview`

  * Third-party
  * Zero data retention



xAI's next-generation video generation model. Generates, edits, and extends videos from text and image inputs. Supports multiple aspect ratios and resolutions with improved quality over the previous generation.

Model Info|   
---|---  
Terms and License| [link ↗](https://x.ai/legal/terms-of-service)  
More information| [link ↗](https://docs.x.ai/developers/models/grok-imagine-video)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.08
  * @480p (per second)$0.08
  * @720p (per second)$0.14

  
  
## Usage
    
    
    const response = await env.AI.run(
      'xai/grok-imagine-video-1.5-preview',
      {
        prompt: 'Generate a slow and serene time-lapse',
        image: { url: 'https://docs.x.ai/assets/api-examples/video/milkyway-still.png' },
        duration: 12,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "xai/grok-imagine-video-1.5-preview",
      "input": {
        "prompt": "Generate a slow and serene time-lapse",
        "image": {
          "url": "https://docs.x.ai/assets/api-examples/video/milkyway-still.png"
        },
        "duration": 12
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/xai/grok-imagine-video-1.5-preview/image-to-video.mp4"
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

Input[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/xai/grok-imagine-video-1.5-preview/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
