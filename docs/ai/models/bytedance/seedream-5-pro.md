---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/
title: Seedream 5 Pro (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:15.897936+00:00
---

# Seedream 5 Pro (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedream 5 Pro

Text-to-Image • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedream-5-pro`

  * Third-party



Seedream 5 Pro is ByteDance's high-quality image generation and editing model with text prompts, up to 10 reference images, and 1K, 2K, or explicit pixel-size output controls.

Model Info|   
---|---  
More information| [link ↗](https://ark.ap-southeast.bytepluses.com/api/v3/images/generations)  
Pricing| 

  * Per image$0.045
  * Per input image$0.03
  * Default (per second)$0.045

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5-pro',
      {
        prompt:
          'Premium studio product render of a transparent mechanical wristwatch suspended above matte black stone, visible gears, sapphire reflections, razor-sharp lighting, luxury advertising style',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5-pro",
      "input": {
        "prompt": "Premium studio product render of a transparent mechanical wristwatch suspended above matte black stone, visible gears, sapphire reflections, razor-sharp lighting, luxury advertising style"
      }
    }'

![Mechanical Watch](https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/mechanical-watch-0.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/mechanical-watch-0.jpeg"
        ]
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Red Panda Bakery** — Whimsical illustrated scene with a very different visual style.
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5-pro',
      {
        prompt:
          "A cozy children's book illustration of a red panda baker frosting moon-shaped cakes inside a tiny snowy mountain bakery, soft gouache texture, warm window light",
        size: '1536x864',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5-pro",
      "input": {
        "prompt": "A cozy children'\''s book illustration of a red panda baker frosting moon-shaped cakes inside a tiny snowy mountain bakery, soft gouache texture, warm window light",
        "size": "1536x864"
      }
    }'

![Red Panda Bakery](https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/red-panda-bakery-0.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/red-panda-bakery-0.jpeg"
        ]
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Claymation Reference** — Use a reference image for a claymation-style transformation.
    
    
    const response = await env.AI.run(
      'bytedance/seedream-5-pro',
      {
        image: 'https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg',
        prompt:
          'Transform this reference into a handcrafted claymation diorama, rounded clay forms, visible fingerprints, miniature set lighting, playful stop-motion film look',
        size: '1K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-5-pro",
      "input": {
        "image": "https://ark-doc.tos-ap-southeast-1.bytepluses.com/doc_image/r2v_tea_pic1.jpg",
        "prompt": "Transform this reference into a handcrafted claymation diorama, rounded clay forms, visible fingerprints, miniature set lighting, playful stop-motion film look",
        "size": "1K"
      }
    }'

![Claymation Reference](https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/claymation-reference-0.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "images": [
          "https://examples.aig.cloudflare.com/bytedance/seedream-5-pro/claymation-reference-0.jpeg"
        ]
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`required

▶image

`one of`

size

`string`

watermark

`boolean`requireddefault: falseWhether to add an AI-generated watermark to the output image

▶images[]

`array`minItems: 1format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-5-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
