---
url: https://developers.cloudflare.com/ai/models/pruna/p-video/
title: P-Video (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:04.951147+00:00
---

# P-Video (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-video/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Video

Text-to-Video • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-video/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-video`

  * Third-party



Pruna's P-Video is a premium video generation model supporting text-to-video, image-to-video, and audio-conditioned generation up to 1080p at 24 or 48 fps, with configurable duration up to 20 seconds.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Default (per second)$0.02
  * @720p (per second)$0.02
  * @1080p (per second)$0.04
  * @720p draft (per second)$0.005
  * @1080p draft (per second)$0.01

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-video',
      {
        prompt: 'A sports car drifting through a neon-lit city at night, cinematic aerial shot',
        duration: 5,
        resolution: '720p',
        aspect_ratio: '16:9',
        draft: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-video",
      "input": {
        "prompt": "A sports car drifting through a neon-lit city at night, cinematic aerial shot",
        "duration": 5,
        "resolution": "720p",
        "aspect_ratio": "16:9",
        "draft": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/pruna/p-video/neon-city-drift.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText prompt for video generation.

image

`string`Input image to generate video from (image-to-video). HTTP(S) URL or data URI. Supports jpg, jpeg, png, webp. When provided, aspect_ratio is ignored.

audio

`string`Input audio to condition video generation. HTTP(S) URL or data URI. Supports flac, mp3, wav. When provided, duration is ignored.

duration

`integer`requireddefault: 5minimum: 1maximum: 20Duration of the video in seconds (1-20). Ignored when audio is provided.

resolution

`string`requireddefault: 720penum: 720p, 1080pVideo resolution.

▶fps

`one of`required

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 1:1Aspect ratio of the video. Ignored when an input image is provided.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

draft

`boolean`requireddefault: falseDraft mode. Generates a lower-quality preview of the video.

save_audio

`boolean`requireddefault: trueSave the video with audio.

last_frame_image

`string`Reference image for the last frame of the video. HTTP(S) URL or data URI.

prompt_upsampling

`boolean`requireddefault: trueUse prompt upsampling to enhance the prompt.

disable_safety_filter

`boolean`requireddefault: trueDisable safety filter for prompts and input images.

video

`string`format: uriPresigned URL for the generated video.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-video/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-video/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
