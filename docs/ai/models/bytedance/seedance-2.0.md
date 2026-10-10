---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/
title: Seedance 2.0 (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:15.963373+00:00
---

# Seedance 2.0 (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 2.0

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedance-2.0`

  * Third-party



ByteDance's next-generation video model with a unified multimodal architecture. Generates high-quality video with synchronized audio from text, images, video clips, and audio inputs. Supports multimodal references (up to 9 images, 3 videos, 3 audio files), native audio generation, video editing, video extension, intelligent duration, and adaptive aspect ratio.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedance2_0)  
Pricing| 

  * Default (per second)$0.15
  * @480p video input (per second)$0.172
  * @720p video input (per second)$0.372
  * @1080p video input (per second)$0.914
  * @4k video input (per second)$1.866
  * @480p non-video input (per second)$0.07
  * @720p non-video input (per second)$0.15
  * @1080p non-video input (per second)$0.37
  * @4k non-video input (per second)$0.78

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
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
      "model": "bytedance/seedance-2.0",
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
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/simple-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**High Resolution Cinematic** — Cinematic video in 1080p
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
      {
        prompt:
          'A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog',
        aspect_ratio: '16:9',
        duration: 10,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.0",
      "input": {
        "prompt": "A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog",
        "aspect_ratio": "16:9",
        "duration": 10,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/high-resolution-cinematic.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Image to Video** — Generate video from a reference image
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
      {
        image:
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
        prompt: 'The character begins walking forward through the scene',
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
      "model": "bytedance/seedance-2.0",
      "input": {
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=",
        "prompt": "The character begins walking forward through the scene",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/image-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Portrait Video** — Vertical video for social media
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
      {
        prompt: 'Abstract ink drops spreading through water, vivid colors mixing in slow motion',
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
      "model": "bytedance/seedance-2.0",
      "input": {
        "prompt": "Abstract ink drops spreading through water, vivid colors mixing in slow motion",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/portrait-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**4K Cinematic Video** — Generate a detailed cinematic video in 4K
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
      {
        prompt:
          'A sweeping cinematic shot of a futuristic city skyline at dusk, flying past glass towers with neon reflections and dramatic clouds',
        aspect_ratio: '16:9',
        duration: 5,
        resolution: '4k',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.0",
      "input": {
        "prompt": "A sweeping cinematic shot of a futuristic city skyline at dusk, flying past glass towers with neon reflections and dramatic clouds",
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "4k"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/4k-cinematic-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Virtual Avatar Reference** — Use a virtual character avatar from the trusted asset library
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.0',
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
      "model": "bytedance/seedance-2.0",
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
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.0/virtual-avatar-reference.mp4"
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

`array`maxItems: 4Reference images (1-4, HTTP(S) URLs or base64 data URIs) to guide video generation for characters, avatars, clothing, or environments. Cannot be used with 1080p resolution or first/last frame images.

duration

`integer`requireddefault: 5minimum: 4maximum: 12Video duration in seconds

resolution

`string`requireddefault: 720penum: 480p, 720p, 1080p, 4kVideo resolution

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

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
