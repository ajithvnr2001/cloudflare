---
url: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/
title: HappyHorse 1.1 R2V (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:49.909184+00:00
---

# HappyHorse 1.1 R2V (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# HappyHorse 1.1 R2V

Image-to-Video • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/hh1.1-r2v`

  * Third-party



Alibaba's HappyHorse 1.1 reference-to-video model. Takes 1-9 reference images (characters and scenes) and a prompt that choreographs them into a single video, keeping each subject's identity consistent. Supports 720P and 1080P output with durations from 3 to 15 seconds.

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
      'alibaba/hh1.1-r2v',
      {
        prompt:
          'The person in image 1 walks through the futuristic city in image 2 and meets the person in image 3.',
        images: [
          'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg',
          'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/futuristic-city.png',
          'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/high-resolution-portrait.jpg',
        ],
        duration: 8,
        ratio: '16:9',
        resolution: '1080P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/hh1.1-r2v",
      "input": {
        "prompt": "The person in image 1 walks through the futuristic city in image 2 and meets the person in image 3.",
        "images": [
          "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-5-lite/portrait-photo-0.jpeg",
          "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/futuristic-city.png",
          "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-2/high-resolution-portrait.jpg"
        ],
        "duration": 8,
        "ratio": "16:9",
        "resolution": "1080P"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/hh1.1-r2v/multi-image-reference.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 2500

▶images[]

`array`requiredminItems: 1maxItems: 9format: uri

resolution

`string`enum: 720P, 1080P

ratio

`string`enum: 16:9, 9:16, 3:4, 4:3, 1:1, 21:9, 9:21, 5:4, 4:5

duration

`integer`minimum: 3maximum: 15

seed

`integer`minimum: 0maximum: 2147483647

watermark

`boolean`

video

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/hh1.1-r2v/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
