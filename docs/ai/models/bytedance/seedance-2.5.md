---
url: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/
title: Seedance 2.5 (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:54.908617+00:00
---

# Seedance 2.5 (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedance 2.5

Text-to-Video • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedance-2.5`

  * Third-party



ByteDance's next-generation video model with a unified multimodal reference-to-video architecture. Generates video from text, up to 30 reference images, 10 reference videos, and 10 reference audio clips — including audio-only input with no image or video required. Supports first/last-frame image-to-video, video editing, video extension, intelligent duration (including automatic selection), and adaptive aspect ratio.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedance2_5)  
Pricing| 

  * Default (per second)$0.2312
  * @480p video input (per second)$0.4304
  * @720p video input (per second)$0.9676
  * @480p non-video input (per second)$0.1028
  * @720p non-video input (per second)$0.2312

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.5',
      {
        prompt: 'A golden retriever running through a field of sunflowers on a sunny day',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.5",
      "input": {
        "prompt": "A golden retriever running through a field of sunflowers on a sunny day",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.5/simple-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Cinematic Wide Shot** — Longer cinematic video with an explicit 16:9 aspect ratio
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.5',
      {
        prompt:
          'A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog',
        aspect_ratio: '16:9',
        duration: 12,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.5",
      "input": {
        "prompt": "A dramatic drone shot flying through misty mountain peaks at sunrise, cinematic lighting with volumetric fog",
        "aspect_ratio": "16:9",
        "duration": 12,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.5/cinematic-wide-shot.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**First and Last Frame** — Generate a video that transitions between a given first-frame and last-frame image
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.5',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        last_frame_image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic2.jpg',
        prompt: 'The character slowly turns to face the camera and smiles',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.5",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "last_frame_image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic2.jpg",
        "prompt": "The character slowly turns to face the camera and smiles",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.5/first-and-last-frame.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Portrait Video with MOV Output** — Vertical video for social media, encoded as mov for higher color fidelity
    
    
    const response = await env.AI.run(
      'bytedance/seedance-2.5',
      {
        prompt: 'Abstract ink drops spreading through water, vivid colors mixing in slow motion',
        aspect_ratio: '9:16',
        duration: 5,
        resolution: '720p',
        output_format: 'mov',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedance-2.5",
      "input": {
        "prompt": "Abstract ink drops spreading through water, vivid colors mixing in slow motion",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p",
        "output_format": "mov"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bytedance/seedance-2.5/portrait-video-with-mov-output.mov"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`maxLength: 2000Text prompt describing the video to generate. Optional when at least one reference image, video, or audio clip is provided (Seedance 2.5 supports audio-only input).

image

`string`First-frame reference image (HTTP(S) URL or base64 data URI) for image-to-video

last_frame_image

`string`Last-frame reference image (HTTP(S) URL or base64 data URI). Requires a first-frame image to also be given.

▶reference_images[]

`array`maxItems: 30Reference images (0-30, HTTP(S) URLs or base64 data URIs) to guide multimodal video generation, editing, or extension.

▶reference_videos[]

`array`maxItems: 10Reference videos (0-10, HTTP(S) URLs or base64 data URIs) for style/motion guidance, video editing, or video extension. Total duration of all reference videos must not exceed 30 seconds.

▶reference_audios[]

`array`maxItems: 10Reference audio clips (0-10, HTTP(S) URLs or base64 data:audio/... URIs). Supports audio-only input (no image or video required). Total duration of all audio clips must not exceed 30 seconds.

▶duration

`one of`required

resolution

`string`requireddefault: 720penum: 480p, 720pVideo resolution

aspect_ratio

`string`requireddefault: adaptiveenum: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptiveVideo aspect ratio. "adaptive" automatically matches the aspect ratio of the provided reference image or video when applicable. First/last-frame generation always uses "adaptive"; any supplied value is overridden.

fps

`number`requireddefault: 24const: 24Frame rate (frames per second)

camera_fixed

`boolean`requireddefault: falseWhether to fix camera position. Not currently supported by the provider; has no effect.

generate_audio

`boolean`Whether to generate audio with the video

watermark

`boolean`requireddefault: falseWhether to add a watermark to the output video

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed. Passing this does not error, but reproducibility is not guaranteed and is not documented by the provider.

output_format

`string`requireddefault: mp4enum: mp4, movOutput video container format. "mp4" offers the best compatibility and smaller file size; "mov" preserves higher color fidelity for professional post-production workflows at the cost of a larger file.

use_virtual_avatar

`boolean`requireddefault: falseRoute image reference inputs (image, reference_images, last_frame_image) through ByteDance's trusted virtual avatar asset library before generation. Intended for AI-generated/virtual character avatars that would otherwise be blocked by face or deepfake detection

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
