---
url: https://developers.cloudflare.com/ai/models/vidu/q3-pro/
title: Vidu Q3 Pro (Vidu) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:06.828174+00:00
---

# Vidu Q3 Pro (Vidu) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/vidu/q3-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Vidu logo](https://developers.cloudflare.com/_astro/vidu.CcN5bM2x.svg)

# Vidu Q3 Pro

Text-to-Video • Vidu

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/vidu/q3-pro/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`vidu/q3-pro`

  * Third-party
  * Zero data retention



Vidu Q3 Pro is a high-quality video generation model supporting text-to-video, image-to-video, and start/end-frame-to-video workflows with audio and up to 16-second clips.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.vidu.com/terms)  
More information| [link ↗](https://www.vidu.com/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.125
  * @540p (per second)$0.05
  * @720p (per second)$0.125
  * @1080p (per second)$0.15

  
  
## Usage
    
    
    const response = await env.AI.run(
      'vidu/q3-pro',
      {
        prompt: 'A golden retriever running through a sunlit meadow in slow motion',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-pro",
      "input": {
        "prompt": "A golden retriever running through a sunlit meadow in slow motion",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_64/tasks/26/0417/05/942597991691198464/creation-01/video.mp4"
      },
      "state": "Completed"
    }

## Examples

**Portrait Aspect Ratio** — Vertical video for social media
    
    
    const response = await env.AI.run(
      'vidu/q3-pro',
      {
        prompt:
          'A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling',
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
      "model": "vidu/q3-pro",
      "input": {
        "prompt": "A busy street in Tokyo at night with neon signs reflecting on wet pavement, rain falling",
        "aspect_ratio": "9:16",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_88/tasks/26/0417/05/942598607041753088/creation-01/video.mp4"
      },
      "state": "Completed"
    }

**Silent Video** — Generate video without audio
    
    
    const response = await env.AI.run(
      'vidu/q3-pro',
      {
        audio: false,
        prompt: 'Abstract paint swirls slowly mixing in water, vivid blues and golds',
        duration: 8,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-pro",
      "input": {
        "audio": false,
        "prompt": "Abstract paint swirls slowly mixing in water, vivid blues and golds",
        "duration": 8,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_76/tasks/26/0417/05/942599305355595776/creation-01/final_video.mp4"
      },
      "state": "Completed"
    }

**Square Format** — Square video for product demos or social posts
    
    
    const response = await env.AI.run(
      'vidu/q3-pro',
      {
        prompt:
          'A sleek wireless headphone rotating on a pedestal with soft studio lighting and a white background',
        aspect_ratio: '1:1',
        duration: 5,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-pro",
      "input": {
        "prompt": "A sleek wireless headphone rotating on a pedestal with soft studio lighting and a white background",
        "aspect_ratio": "1:1",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_40/tasks/26/0417/05/942599364482723840/creation-01/video.mp4"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`maxLength: 5000Text prompt describing what should appear in the video

start_image

`string`Start image for video generation. Use alone for image-to-video, or with end_image for start/end-to-video. Accepts public URL or Base64 data URI (data:image/png;base64,...)

end_image

`string`End image for start/end-to-video generation. Must be used together with start_image. Accepts public URL or Base64 data URI (data:image/png;base64,...)

duration

`integer`requireddefault: 5minimum: 1maximum: 16Video duration in seconds (1-16)

resolution

`string`requireddefault: 720penum: 540p, 720p, 1080pVideo resolution

audio

`boolean`Enable audio-video synchronization. Default: true for Q3 models. When false, outputs silent video

aspect_ratio

`string`enum: 16:9, 9:16, 3:4, 4:3, 1:1Video aspect ratio (text-to-video only). Default: 16:9

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/vidu/q3-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/vidu/q3-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/vidu/q3-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/vidu/q3-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
