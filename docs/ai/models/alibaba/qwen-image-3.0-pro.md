---
url: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/
title: Qwen Image 3.0 Pro (Alibaba) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:50.905593+00:00
---

# Qwen Image 3.0 Pro (Alibaba) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Alibaba logo](https://developers.cloudflare.com/_astro/alibaba.BK31NAJz.svg)

# Qwen Image 3.0 Pro

Text-to-Image • Alibaba

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`alibaba/qwen-image-3.0-pro`

  * Third-party



Alibaba's Qwen Image 3.0 Pro generates images from text prompts with a focus on complex layout generation, small-text precision, and multilingual font rendering. Supports up to 6 image variants per call, negative prompts, seed control, and optional prompt rewriting.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.alibabacloud.com/help/en/legal)  
More information| [link ↗](https://www.alibabacloud.com/en/solutions/generative-ai/qwen)  
Pricing| 

  * Per image$0.04
  * output size 1k$0.04
  * output size 2k$0.07
  * Default (per second)$0.04

  
  
## Usage
    
    
    const response = await env.AI.run(
      'alibaba/qwen-image-3.0-pro',
      { prompt: 'A golden retriever puppy playing in autumn leaves' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/qwen-image-3.0-pro",
      "input": {
        "prompt": "A golden retriever puppy playing in autumn leaves"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/simple-generation.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/simple-generation.png"
        ]
      },
      "state": "Completed"
    }

## Examples

**Multiple Variants** — Generate several image variants from a single call
    
    
    const response = await env.AI.run(
      'alibaba/qwen-image-3.0-pro',
      { prompt: 'A minimalist logo for a coffee roastery, line art style, single color', n: 4 },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "alibaba/qwen-image-3.0-pro",
      "input": {
        "prompt": "A minimalist logo for a coffee roastery, line art style, single color",
        "n": 4
      }
    }'

![Multiple Variants](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-0.png)![Multiple Variants](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-1.png)![Multiple Variants](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-2.png)![Multiple Variants](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-3.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-0.png",
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-1.png",
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-2.png",
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/multiple-variants-3.png"
        ]
      },
      "state": "Completed"
    }

**Negative Prompt** — Guide generation away from unwanted elements
    
    
    const response = await env.AI.run(
      'alibaba/qwen-image-3.0-pro',
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
      "model": "alibaba/qwen-image-3.0-pro",
      "input": {
        "prompt": "A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar",
        "negative_prompt": "modern clothing, photograph, blurry, low quality"
      }
    }'

![Negative Prompt](https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/negative-prompt.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/alibaba/qwen-image-3.0-pro/negative-prompt.png"
        ]
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`required

size

`string`requireddefault: 1024x1024pattern: ^\d+x\d+$

negative_prompt

`string`maxLength: 500

n

`integer`minimum: 1maximum: 6

seed

`integer`minimum: 0maximum: 2147483647

watermark

`boolean`

prompt_extend

`boolean`

prompt_extend_mode

`string`enum: direct, agent

▶images[]

`array`minItems: 1format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/alibaba/qwen-image-3.0-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
