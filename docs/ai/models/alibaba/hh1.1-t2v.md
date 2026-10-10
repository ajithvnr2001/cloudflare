---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/
title: HappyHorse 1.1 T2V (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:18.971508+00:00
---

# HappyHorse 1.1 T2V (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# HappyHorse 1.1 T2V

Text-to-Video • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/hh1.1-t2v`

  * Third-party



Alibaba's HappyHorse 1.1 text-to-video model. Generates videos from a text prompt with stronger dynamic expressiveness, better visual quality, and improved instruction following over 1.0. Configurable resolution, aspect ratio, and duration (3-15s).

Model Info|   
---|---  
Terms and License| [link ↗](https://www.alibabacloud.com/help/en/legal)  
More information| [link ↗](https://modelstudio.console.alibabacloud.com/)  
Pricing| 

  * Default (per second)$0.18
  * @720p (per second)$0.14
  * @1080p (per second)$0.18

  
  
## Usage
    
    
    const response = await env.AI.run(
      'alibaba/hh1.1-t2v',
      { prompt: 'A little girl walking on the road' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/hh1.1-t2v",
      "input": {
        "prompt": "A little girl walking on the road"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/hh1.1-t2v/simple-text-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 2500

resolution

`string`enum: 720P, 1080P

ratio

`string`enum: 16:9, 9:16, 1:1, 4:3, 3:4

duration

`integer`minimum: 3maximum: 15

seed

`integer`minimum: 0maximum: 2147483647

watermark

`boolean`

video

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-t2v/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
