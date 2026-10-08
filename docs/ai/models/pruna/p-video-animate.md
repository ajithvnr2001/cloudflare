---
url: https://developers.cloudflare.com/ai/models/pruna/p-video-animate/
title: P-Video-Animate (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:04.990557+00:00
---

# P-Video-Animate (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-video-animate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Video-Animate

Image-to-Video • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-video-animate`

  * Third-party



Pruna's P-Video-Animate takes a source video and a subject reference image, then animates the referenced subject using the motion and audio from the source video.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Default (per second)$0.03
  * @720p (per second)$0.03
  * @1080p (per second)$0.06

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-video-animate',
      {
        video: 'https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4',
        image: 'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
        resolution: '720p',
        target_fps: 'original',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-video-animate",
      "input": {
        "video": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
        "image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
        "resolution": "720p",
        "target_fps": "original"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/pruna/p-video-animate/motion-transfer.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

video

`string`requiredSource RGB video (.mp4) used as the motion and audio source. HTTP(S) URL or data URI.

image

`string`requiredReference image of the subject to animate. HTTP(S) URL or data URI.

turbo

`boolean`requireddefault: falseTurbo mode: faster generation for slightly lower quality.

resolution

`string`requireddefault: 720penum: 720p, 1080pTarget resolution.

save_audio

`boolean`requireddefault: trueSave the video with audio.

ignore_audio

`boolean`requireddefault: falseIgnore source audio during generation.

target_fps

`string`requireddefault: originalenum: 24, 48, originalTarget FPS for the working video.

instruction_prompt

`string`requireddefault: Further instruction on how the reference subject should be animated.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable_safety_checker

`boolean`requireddefault: falseDisable safety checker for generated videos.

video

`string`format: uriPresigned URL for the animated video.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-video-animate/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
