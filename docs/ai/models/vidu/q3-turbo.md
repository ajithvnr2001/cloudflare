---
url: https://developers.cloudflare.com/ai/models/vidu/q3-turbo/
title: Vidu Q3 Turbo (Vidu) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:06.369574+00:00
---

# Vidu Q3 Turbo (Vidu) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/vidu/q3-turbo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Vidu logo](https://developers.cloudflare.com/_astro/vidu.CcN5bM2x.svg)

# Vidu Q3 Turbo

Text-to-Video • Vidu

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`vidu/q3-turbo`

  * Third-party
  * Zero data retention



Vidu Q3 Turbo is a faster version of Vidu Q3 optimized for lower latency video generation while maintaining audio support and up to 16-second clips.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.vidu.com/terms)  
More information| [link ↗](https://www.vidu.com/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.06
  * @540p (per second)$0.04
  * @720p (per second)$0.06
  * @1080p (per second)$0.07

  
  
## Usage
    
    
    const response = await env.AI.run(
      'vidu/q3-turbo',
      { prompt: 'A cat lazily stretching on a sunlit windowsill', duration: 5, resolution: '720p' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-turbo",
      "input": {
        "prompt": "A cat lazily stretching on a sunlit windowsill",
        "duration": 5,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_28/tasks/26/0417/05/942602832110972928/creation-01/video.mp4"
      },
      "state": "Completed"
    }

## Examples

**High Resolution** — Generate at 1080p
    
    
    const response = await env.AI.run(
      'vidu/q3-turbo',
      {
        prompt:
          'Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background',
        duration: 5,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-turbo",
      "input": {
        "prompt": "Close-up of a hummingbird feeding from a vibrant red flower, slow motion with soft bokeh background",
        "duration": 5,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_44/tasks/26/0417/05/942602894400569344/creation-01/video.mp4"
      },
      "state": "Completed"
    }

**Portrait Video** — Vertical video for mobile viewing
    
    
    const response = await env.AI.run(
      'vidu/q3-turbo',
      {
        prompt: 'A waterfall cascading down mossy rocks in a tropical jungle, mist rising',
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
      "model": "vidu/q3-turbo",
      "input": {
        "prompt": "A waterfall cascading down mossy rocks in a tropical jungle, mist rising",
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
        "video": "https://video.cf.vidu.com/infer_48/tasks/26/0417/05/942603057143758848/creation-01/video.mp4"
      },
      "state": "Completed"
    }

**Extended Duration** — Longer video clip
    
    
    const response = await env.AI.run(
      'vidu/q3-turbo',
      {
        prompt:
          'Timelapse of clouds rolling over a mountain peak from sunrise to sunset, dramatic lighting',
        duration: 16,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-turbo",
      "input": {
        "prompt": "Timelapse of clouds rolling over a mountain peak from sunrise to sunset, dramatic lighting",
        "duration": 16,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_84/tasks/26/0417/06/942603162785705984/creation-01/video.mp4"
      },
      "state": "Completed"
    }

**Low Resolution Fast Preview** — Quick preview at 540p
    
    
    const response = await env.AI.run(
      'vidu/q3-turbo',
      {
        prompt: 'A sailboat gliding across calm ocean waters at sunset',
        duration: 3,
        resolution: '540p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "vidu/q3-turbo",
      "input": {
        "prompt": "A sailboat gliding across calm ocean waters at sunset",
        "duration": 3,
        "resolution": "540p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://video.cf.vidu.com/infer_68/tasks/26/0417/06/942603796612128768/creation-01/video.mp4"
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

Input[](https://developers.cloudflare.com/ai/models/vidu/q3-turbo/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/vidu/q3-turbo/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/vidu/q3-turbo/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/vidu/q3-turbo/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
