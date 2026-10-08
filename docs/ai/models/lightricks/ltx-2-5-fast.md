---
url: https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/
title: LTX-2.5 Fast (lightricks) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:58.249036+00:00
---

# LTX-2.5 Fast (lightricks) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



l

# LTX-2.5 Fast

Text-to-Video • lightricks

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`lightricks/ltx-2-5-fast`

  * Third-party



Lightricks LTX-2.5 Fast is a fast video generation model for text-to-video and image-to-video workflows, with synchronized audio, configurable duration, resolution, and frame rate.

Model Info|   
---|---  
More information| [link ↗](https://docs.ltx.io/api-documentation/api-reference/video-generation/text-to-video)  
Pricing| 

  * Default (per second)$0.09
  * @720p (per second)$0.09
  * @1080p (per second)$0.15
  * @2k (per second)$0.19
  * @4k (per second)$0.37

  
  
## Usage
    
    
    const response = await env.AI.run(
      'lightricks/ltx-2-5-fast',
      {
        prompt: 'A cinematic aerial shot of ocean waves at sunset',
        duration: 8,
        resolution: '1920x1080',
        fps: 24,
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "lightricks/ltx-2-5-fast",
      "input": {
        "prompt": "A cinematic aerial shot of ocean waves at sunset",
        "duration": 8,
        "resolution": "1920x1080",
        "fps": 24,
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/text-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Image-to-Video** — Animate a reference image with a final frame
    
    
    const response = await env.AI.run(
      'lightricks/ltx-2-5-fast',
      {
        prompt: 'The camera moves forward while the trees sway in the wind',
        image_uri:
          'https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg',
        last_frame_uri:
          'https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg',
        duration: 8,
        resolution: '1920x1080',
        fps: 24,
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "lightricks/ltx-2-5-fast",
      "input": {
        "prompt": "The camera moves forward while the trees sway in the wind",
        "image_uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
        "last_frame_uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
        "duration": 8,
        "resolution": "1920x1080",
        "fps": 24,
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/lightricks/ltx-2-5-fast/image-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 10000Text prompt describing the video

image_uri

`string`format: uriHTTPS URI for the first frame

last_frame_uri

`string`format: uriHTTPS URI for the last frame

▶duration

`one of`required

resolution

`string`requireddefault: 1920x1080enum: 1280x720, 720x1280, 1920x1080, 1080x1920, 2560x1440, 1440x2560, 3840x2160, 2160x3840

▶fps

`one of`required

generate_audio

`boolean`requireddefault: true

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/lightricks/ltx-2-5-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
