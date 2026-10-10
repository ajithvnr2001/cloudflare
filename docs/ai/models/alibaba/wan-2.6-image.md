---
url: https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/
title: Wan 2.6 Image (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:18.768123+00:00
---

# Wan 2.6 Image (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# Wan 2.6 Image

Text-to-Image • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/wan-2.6-image`

  * Third-party
  * Zero data retention



Alibaba's Wan 2.6 text-to-image model generating images from text prompts with optional negative prompts and customizable dimensions.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.alibabacloud.com/help/en/legal)  
More information| [link ↗](https://wan.video/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.03

  
  
## Usage
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.6-image',
      { prompt: 'A golden retriever puppy playing in autumn leaves' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.6-image",
      "input": {
        "prompt": "A golden retriever puppy playing in autumn leaves"
      }
    }'

![Simple Generation](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/simple-generation.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/66/20260417/c057796c/32701268-BbftSa6r_189314ac1a36.png"
      },
      "state": "Completed"
    }

## Examples

**Custom Dimensions** — Specify image size in WxH format
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.6-image',
      {
        prompt:
          'A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground',
        size: '1024x768',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.6-image",
      "input": {
        "prompt": "A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground",
        "size": "1024x768"
      }
    }'

![Custom Dimensions](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/custom-dimensions.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/35/20260417/c057796c/3257252-vy1GbNI6_bc223e38c5b4.png"
      },
      "state": "Completed"
    }

**Square Format** — Square image for social media or product photos
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.6-image',
      {
        prompt:
          'A sleek wireless headphone on a minimalist white marble surface with soft studio lighting',
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.6-image",
      "input": {
        "prompt": "A sleek wireless headphone on a minimalist white marble surface with soft studio lighting",
        "size": "1024x1024"
      }
    }'

![Square Format](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/square-format.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/84/20260417/c057796c/18355039-RFkWcHgG_0dcb1c1d6d95.png"
      },
      "state": "Completed"
    }

**Negative Prompt** — Guide generation away from unwanted elements
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.6-image',
      {
        prompt: 'A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar',
        negative_prompt: 'modern clothing, photograph, blurry, low quality',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.6-image",
      "input": {
        "prompt": "A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar",
        "negative_prompt": "modern clothing, photograph, blurry, low quality"
      }
    }'

![Negative Prompt](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/negative-prompt.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/53/20260417/c057796c/26097304-eVhNm6uS_edc041cd5e2b.png"
      },
      "state": "Completed"
    }

**Portrait Format** — Tall vertical image for portraits
    
    
    const response = await env.AI.run(
      'alibaba/wan-2.6-image',
      {
        prompt: 'An elegant Art Deco poster featuring a jazz singer under a spotlight',
        size: '768x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/wan-2.6-image",
      "input": {
        "prompt": "An elegant Art Deco poster featuring a jazz singer under a spotlight",
        "size": "768x1024"
      }
    }'

![Portrait Format](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/portrait-format.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/5a/20260417/c057796c/79957405-YTXQsRY6_8d8a6631f1d6.png"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`required

size

`string`pattern: ^\d+x\d+$

negative_prompt

`string`

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/wan-2.6-image/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
