---
url: https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/
title: Wan 3.0 Video (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:18.212425+00:00
---

# Wan 3.0 Video (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# Wan 3.0 Video

Text-to-Video • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/wan-3.0`

  * Third-party



Alibaba's Wan 3.0 text-to-video model. Generates cinematic videos from text prompts with adaptive aspect ratio, 480P, 720P, or 1080P resolution, and configurable duration.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.alibabacloud.com/help/en/legal)  
More information| [link ↗](https://www.alibabacloud.com/help/en/model-studio/models)  
Pricing| 

  * Default (per second)$0.05
  * @480p (per second)$0.05
  * @720p (per second)$0.10
  * @1080p (per second)$0.20

  
  
## Usage
    
    
    const response = await env.AI.run(
      'alibaba/wan-3.0',
      {
        prompt:
          'A kitten running across a rooftop under the moonlight, city neon lights flickering in the distance, cinematic quality, smooth camera movement.',
        resolution: '480P',
        ratio: 'adaptive',
        duration: 5,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-3.0",
      "input": {
        "prompt": "A kitten running across a rooftop under the moonlight, city neon lights flickering in the distance, cinematic quality, smooth camera movement.",
        "resolution": "480P",
        "ratio": "adaptive",
        "duration": 5
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/wan-3.0/adaptive-480p-text-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 2500

resolution

`string`enum: 480P, 720P, 1080P

ratio

`string`enum: adaptive, 16:9, 9:16, 1:1, 4:3, 3:4

duration

`integer`minimum: 1maximum: 15

video

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-3.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
