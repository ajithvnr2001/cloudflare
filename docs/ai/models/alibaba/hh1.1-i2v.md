---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/
title: HappyHorse 1.1 I2V (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:49.421033+00:00
---

# HappyHorse 1.1 I2V (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# HappyHorse 1.1 I2V

Image-to-Video • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/hh1.1-i2v`

  * Third-party



Alibaba's HappyHorse 1.1 image-to-video model. Animates a reference image with an optional text prompt, with smoother motion, natural skin textures, and improved close-up quality over 1.0. Supports 720P and 1080P output with durations from 3 to 15 seconds.

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
      'alibaba/hh1.1-i2v',
      {
        image:
          'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png',
        prompt: 'A gentle camera push-in on the scene with soft ambient lighting',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/hh1.1-i2v",
      "input": {
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png",
        "prompt": "A gentle camera push-in on the scene with soft ambient lighting"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/hh1.1-i2v/simple-image-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

image

`string`requiredformat: uri

prompt

`string`

negative_prompt

`string`

resolution

`string`enum: 720P, 1080P

duration

`integer`minimum: 3maximum: 15

seed

`integer`minimum: 0maximum: 2147483647

watermark

`boolean`

video

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-i2v/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
