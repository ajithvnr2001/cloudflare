---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/
title: Nano Banana 2 Lite (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:57.218396+00:00
---

# Nano Banana 2 Lite (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Nano Banana 2 Lite

Text-to-Image • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/nano-banana-2-lite`

  * Third-party
  * Zero data retention



Google's fastest Gemini image generation model for rapid image creation and iteration.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 65,536 tokens  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://deepmind.google/technologies/imagen/)  
Zero data retention| Yes  
Pricing| 

  * Input (per 1M tokens)$0.25
  * Output (per 1M tokens)$30.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/nano-banana-2-lite',
      {
        prompt:
          'A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design',
        aspect_ratio: '16:9',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2-lite",
      "input": {
        "prompt": "A playful concept sketch of a compact solar-powered delivery robot rolling through a leafy neighborhood, bright morning light, clean product design",
        "aspect_ratio": "16:9"
      }
    }'

![Concept Sketch](https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2-lite/concept-sketch.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Product Render** — Create a square PNG product image
    
    
    const response = await env.AI.run(
      'google/nano-banana-2-lite',
      {
        prompt:
          'A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style',
        aspect_ratio: '1:1',
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2-lite",
      "input": {
        "prompt": "A studio product render of translucent wireless earbuds in a frosted glass charging case, soft gradient background, premium advertising style",
        "aspect_ratio": "1:1",
        "output_format": "png"
      }
    }'

![Product Render](https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2-lite/product-render.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`required

▶image_input[]

`array`maxItems: 3

aspect_ratio

`string`enum: match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

output_format

`string`enum: jpg, png

resolution

`string`enum: 1K, 2K, 4K

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2-lite/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
