---
url: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/
title: MiniMax Hailuo 2.3 Fast (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:13.138383+00:00
---

# MiniMax Hailuo 2.3 Fast (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Hailuo 2.3 Fast

Text-to-Video • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`minimax/hailuo-2.3-fast`

  * Third-party
  * Zero data retention



A lower-latency version of Hailuo 2.3 that preserves core motion quality, visual consistency, and stylization while enabling faster iteration.

Model Info|   
---|---  
Terms and License| [link ↗](https://hailuoai.com/terms)  
More information| [link ↗](https://hailuoai.com/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.032
  * 6s @768p$0.19
  * 10s @768p$0.32
  * 6s @1080p$0.33

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3-fast',
      {
        prompt: 'Gentle movement and subtle animation, natural-looking motion',
        duration: 6,
        fast_pretreatment: false,
        first_frame_image:
          'https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg',
        prompt_optimizer: true,
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3-fast",
      "input": {
        "prompt": "Gentle movement and subtle animation, natural-looking motion",
        "duration": 6,
        "fast_pretreatment": false,
        "first_frame_image": "https://replicate.delivery/xezq/MQpUhqkESIIQDlWUxtNcsznZLfUTmhEbCV3vdAZGHGPwwaMLA/tmpgl4gvv5n.jpeg",
        "prompt_optimizer": true,
        "resolution": "768P"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "status": "Success",
        "task_id": "388514752192863",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/eff40703-0339-4d1d-b66a-db050e878038/output.mp4"
      },
      "state": "Completed"
    }

## Examples

**High Resolution I2V** — Animate a photo in 1080P
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3-fast',
      {
        prompt: 'Camera slowly pans across the scene with cinematic depth of field',
        duration: 6,
        fast_pretreatment: false,
        first_frame_image:
          'https://replicate.delivery/xezq/IeNNble3XUqhpUZTd3CkYTUf8EgkFU1fl1Jnyive3B26MsGzC/tmp51dpln4i.jpeg',
        prompt_optimizer: true,
        resolution: '1080P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3-fast",
      "input": {
        "prompt": "Camera slowly pans across the scene with cinematic depth of field",
        "duration": 6,
        "fast_pretreatment": false,
        "first_frame_image": "https://replicate.delivery/xezq/IeNNble3XUqhpUZTd3CkYTUf8EgkFU1fl1Jnyive3B26MsGzC/tmp51dpln4i.jpeg",
        "prompt_optimizer": true,
        "resolution": "1080P"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "status": "Success",
        "task_id": "388515984507205",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/2b6251d2-d4ae-4d58-b12f-2609c50fadc2/output.mp4"
      },
      "state": "Completed"
    }

**Fast Processing** — Quick I2V with fast pretreatment enabled
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3-fast',
      {
        prompt: 'Hair blowing in the wind, eyes blinking naturally',
        duration: 6,
        fast_pretreatment: true,
        first_frame_image:
          'https://replicate.delivery/xezq/jfh37lJpnDQhaKcAfCrxSCEh7HA7lv5cCWmJW284tYXwh1YWA/tmpw2i437qe.jpeg',
        prompt_optimizer: true,
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3-fast",
      "input": {
        "prompt": "Hair blowing in the wind, eyes blinking naturally",
        "duration": 6,
        "fast_pretreatment": true,
        "first_frame_image": "https://replicate.delivery/xezq/jfh37lJpnDQhaKcAfCrxSCEh7HA7lv5cCWmJW284tYXwh1YWA/tmpw2i437qe.jpeg",
        "prompt_optimizer": true,
        "resolution": "768P"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "status": "Success",
        "task_id": "388515980755024",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/b64303a0-0227-4d42-983a-dcaec397b6b1/output.mp4"
      },
      "state": "Completed"
    }

## Parameters

first_frame_image

`string`requiredURL or base64 data URI of the first frame image

prompt

`string`maxLength: 2000

prompt_optimizer

`boolean`requireddefault: true

fast_pretreatment

`boolean`requireddefault: false

▶duration

`one of`required

resolution

`string`requireddefault: 768Penum: 768P, 1080P

video

`string`format: uri

task_id

`string`

status

`string`enum: Preparing, Queueing, Processing, Success, Fail

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3-fast/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
