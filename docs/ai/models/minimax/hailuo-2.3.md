---
url: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/
title: MiniMax Hailuo 2.3 (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:13.189630+00:00
---

# MiniMax Hailuo 2.3 (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Hailuo 2.3

Text-to-Video • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`minimax/hailuo-2.3`

  * Third-party
  * Zero data retention



A high-fidelity video generation model optimized for realistic human motion, cinematic VFX, expressive characters, and strong prompt and style adherence across text-to-video and image-to-video workflows.

Model Info|   
---|---  
Terms and License| [link ↗](https://hailuoai.com/terms)  
More information| [link ↗](https://hailuoai.com/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.047
  * 6s @768p$0.28
  * 10s @768p$0.56
  * 6s @1080p$0.49

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3',
      {
        prompt: 'A golden retriever playing fetch on a sandy beach at sunset',
        duration: 6,
        fast_pretreatment: false,
        prompt_optimizer: true,
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3",
      "input": {
        "prompt": "A golden retriever playing fetch on a sandy beach at sunset",
        "duration": 6,
        "fast_pretreatment": false,
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
        "task_id": "388507504709991",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/97d0c2d0-45ab-4ce8-a1f4-177401f43073/output.mp4"
      },
      "state": "Completed"
    }

## Examples

**High Resolution** — 1080P video for higher quality output
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3',
      {
        prompt:
          'A professional chef preparing sushi in a traditional Japanese kitchen, detailed close-up shots',
        duration: 6,
        fast_pretreatment: false,
        prompt_optimizer: true,
        resolution: '1080P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3",
      "input": {
        "prompt": "A professional chef preparing sushi in a traditional Japanese kitchen, detailed close-up shots",
        "duration": 6,
        "fast_pretreatment": false,
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
        "task_id": "388510158565457",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/1ee6a770-eb88-4b6a-86ea-61981f01ed65/output.mp4"
      },
      "state": "Completed"
    }

**Image to Video** — Animate a still image with I2V
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3',
      {
        prompt: 'Slowly zoom in with subtle parallax movement, gentle atmospheric motion',
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
      "model": "minimax/hailuo-2.3",
      "input": {
        "prompt": "Slowly zoom in with subtle parallax movement, gentle atmospheric motion",
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
        "task_id": "388509844320343",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/a19c7850-6f3b-47dd-b6f1-decb592a11ff/output.mp4"
      },
      "state": "Completed"
    }

**Fast Processing** — Enable fast pretreatment for quicker results
    
    
    const response = await env.AI.run(
      'minimax/hailuo-2.3',
      {
        prompt: 'Fireworks exploding over a city skyline at night, colorful reflections on water',
        duration: 6,
        fast_pretreatment: true,
        prompt_optimizer: true,
        resolution: '768P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/hailuo-2.3",
      "input": {
        "prompt": "Fireworks exploding over a city skyline at night, colorful reflections on water",
        "duration": 6,
        "fast_pretreatment": true,
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
        "task_id": "388509805367378",
        "video": "https://video-product.cdn.minimax.io/inference_output/video/2026-04-17/438b5433-5d32-4760-9564-c86da3d22aee/output.mp4"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`maxLength: 2000

first_frame_image

`string`

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

Input[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/hailuo-2.3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
