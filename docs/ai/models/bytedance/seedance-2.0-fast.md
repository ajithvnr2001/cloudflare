---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/
title: Seedance 2.0 Fast (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:54.180634+00:00
---

# Seedance 2.0 Fast (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 2.0 Fast

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedance-2.0-fast`

  * Third-party



Faster variant of ByteDance's Seedance 2.0 video model. Trades some quality for speed while sharing the same multimodal architecture. Supports text-to-video, image-to-video, native audio generation, multimodal references (images, videos, audio), video editing, and video extension.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedance)  
Pricing| 

  * Default (per second)$0.12
  * @480p video input (per second)$0.132
  * @720p video input (per second)$0.286
  * @480p non-video input (per second)$0.06
  * @720p non-video input (per second)$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-fast',
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
      "model": "bytedance/seedance-2.0-fast",
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
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/quick-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Portrait Video** — Vertical video for social media
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-fast',
      {
        prompt: 'A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field',
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
      "model": "bytedance/seedance-2.0-fast",
      "input": {
        "prompt": "A barista pouring latte art in a cozy coffee shop, close-up with shallow depth of field",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/portrait-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Virtual Avatar Reference** — Use a virtual character avatar from the trusted asset library
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-fast',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt: 'The scene gently animates with subtle motion',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '720p',
        use_virtual_avatar: true,
        generate_audio: false,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.0-fast",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "The scene gently animates with subtle motion",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p",
        "use_virtual_avatar": true,
        "generate_audio": false
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-fast/virtual-avatar-reference.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredmaxLength: 2000Text prompt describing the video to generate

image

`string`Reference image (HTTP(S) URL or base64 data URI) for image-to-video

reference_video

`string`Reference video (HTTP(S) URL or base64 data URI) for style/motion guidance

last_frame_image

`string`Reference image (HTTP(S) URL or base64 data URI) for last-frame guidance. Only works if an image start frame is also given.

▶reference_images[]

`array`maxItems: 4Reference images (1-4, HTTP(S) URLs or base64 data URIs) to guide video generation for characters, avatars, clothing, or environments. Cannot be used with first/last frame images.

duration

`integer`requireddefault: 5minimum: 4maximum: 12Video duration in seconds

resolution

`string`requireddefault: 720penum: 480p, 720pVideo resolution

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, 9:21Video aspect ratio. Ignored if an image is used.

fps

`number`requireddefault: 24const: 24Frame rate (frames per second)

camera_fixed

`boolean`requireddefault: falseWhether to fix camera position

generate_audio

`boolean`Whether to generate audio with the video

watermark

`boolean`requireddefault: falseWhether to add a watermark to the output video

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation

use_virtual_avatar

`boolean`requireddefault: falseRoute image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
