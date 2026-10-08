---
url: https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/
title: Wan 2.7 I2V (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:51.065045+00:00
---

# Wan 2.7 I2V (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# Wan 2.7 I2V

Image-to-Video • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/wan-2.7-i2v`

  * Third-party
  * Zero data retention



Alibaba's Wan 2.7 image-to-video model that generates videos from a reference image with optional text prompts. Supports 720P and 1080P output with durations from 2 to 15 seconds.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.alibabacloud.com/help/en/legal)  
More information| [link ↗](https://wan.video/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.10
  * @720p (per second)$0.10
  * @1080p (per second)$0.15

  
  
## Usage
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.7-i2v',
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
      "model": "alibaba/wan-2.7-i2v",
      "input": {
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png",
        "prompt": "A gentle camera push-in on the scene with soft ambient lighting"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/wan-2.7-i2v/simple-image-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**High Resolution** — Generate at 1080P with a longer duration
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.7-i2v',
      {
        image:
          'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png',
        prompt: 'Subject begins rapping confidently, head bobbing to the beat',
        duration: 10,
        resolution: '1080P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.7-i2v",
      "input": {
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png",
        "prompt": "Subject begins rapping confidently, head bobbing to the beat",
        "duration": 10,
        "resolution": "1080P"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/wan-2.7-i2v/high-resolution.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**With Negative Prompt** — Guide generation away from unwanted artifacts
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.7-i2v',
      {
        image:
          'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png',
        prompt: 'Subject slowly turns their head and smiles',
        duration: 5,
        negative_prompt: 'blurry, distorted face, extra limbs',
        resolution: '720P',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.7-i2v",
      "input": {
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png",
        "prompt": "Subject slowly turns their head and smiles",
        "duration": 5,
        "negative_prompt": "blurry, distorted face, extra limbs",
        "resolution": "720P"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/wan-2.7-i2v/with-negative-prompt.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Reproducible Output** — Use a fixed seed for reproducibility
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.7-i2v',
      {
        image:
          'https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png',
        prompt: 'Camera orbits slowly around the subject under streetlamp light',
        duration: 8,
        resolution: '720P',
        seed: 42,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.7-i2v",
      "input": {
        "image": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png",
        "prompt": "Camera orbits slowly around the subject under streetlamp light",
        "duration": 8,
        "resolution": "720P",
        "seed": 42
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/alibaba/wan-2.7-i2v/reproducible-output.mp4"
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

`integer`minimum: 2maximum: 15

seed

`integer`minimum: 0maximum: 2147483647

watermark

`boolean`

video

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.7-i2v/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
