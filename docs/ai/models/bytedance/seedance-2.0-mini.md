---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/
title: Seedance 2.0 Mini (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:16.319789+00:00
---

# Seedance 2.0 Mini (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 2.0 Mini

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedance-2.0-mini`

  * Third-party



ByteDance's compact, cost-efficient video generation model from the Seedance 2.0 family. Supports text-to-video, image-to-video, reference video, and reference audio for background music. Ideal for high-volume workloads where speed and cost matter.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedance)  
Pricing| 

  * Default (per second)$0.09
  * @480p video input (per second)$0.084
  * @720p video input (per second)$0.182
  * @480p non-video input (per second)$0.04
  * @720p non-video input (per second)$0.09

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-mini',
      {
        prompt:
          'A cat sitting on a windowsill watching raindrops fall on the glass, cozy interior lighting',
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
      "model": "bytedance/seedance-2.0-mini",
      "input": {
        "prompt": "A cat sitting on a windowsill watching raindrops fall on the glass, cozy interior lighting",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-mini/simple-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Image to Video** — Generate video from a reference image
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-mini',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt: 'The scene slowly comes to life with gentle movement',
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
      "model": "bytedance/seedance-2.0-mini",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "The scene slowly comes to life with gentle movement",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-mini/image-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Portrait Video with Audio** — Vertical video for social media
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-mini',
      {
        prompt: 'A steaming coffee cup on a marble table, morning light streaming through a window',
        aspect_ratio: '9:16',
        duration: 5,
        resolution: '720p',
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.0-mini",
      "input": {
        "prompt": "A steaming coffee cup on a marble table, morning light streaming through a window",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p",
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-mini/portrait-video-with-audio.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Virtual Avatar Reference** — Use a virtual character avatar from the trusted asset library
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0-mini',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt: 'The scene gently animates with subtle motion',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '720p',
        use_virtual_avatar: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.0-mini",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "The scene gently animates with subtle motion",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p",
        "use_virtual_avatar": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0-mini/virtual-avatar-reference.mp4"
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

reference_audio

`string`Reference audio (HTTP(S) URL or base64 data:audio/... URI) to use as background music. Must be accompanied by a reference image or video.

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0-mini/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
