---
url: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/
title: Seedream 4.5 (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:55.033851+00:00
---

# Seedream 4.5 (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# Seedream 4.5

Text-to-Image • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bytedance/seedream-4.5`

  * Third-party



Seedream 4.5 builds on 4.0 with multi-reference image support, batch generation, and sequential image generation.

Model Info|   
---|---  
More information| [link ↗](https://seed.bytedance.com/en/seedream4_5)  
Pricing| 

  * Per image$0.04

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bytedance/seedream-4.5',
      { prompt: 'A cozy reading nook with floor-to-ceiling bookshelves and a comfortable armchair' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-4.5",
      "input": {
        "prompt": "A cozy reading nook with floor-to-ceiling bookshelves and a comfortable armchair"
      }
    }'

![Simple Generation](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/simple-generation-0.jpeg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052077481386b9a8ed856c57501cfa946ce34c9865285c_0.jpeg"
        ]
      },
      "state": "Completed"
    }

## Examples

**High Resolution** — 4K quality image generation
    
    
    const response = await env.AI.run(
      'bytedance/seedream-4.5',
      {
        prompt:
          'A hyperrealistic still life painting of fresh fruit on an antique wooden table with dramatic chiaroscuro lighting',
        aspect_ratio: '4:3',
        size: '4K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-4.5",
      "input": {
        "prompt": "A hyperrealistic still life painting of fresh fruit on an antique wooden table with dramatic chiaroscuro lighting",
        "aspect_ratio": "4:3",
        "size": "4K"
      }
    }'

![High Resolution](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/high-resolution-0.jpeg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052077581386b9a8ed856c57501cfa946ce34c985dabe3_0.jpeg"
        ]
      },
      "state": "Completed"
    }

**Image-to-Image** — Edit using reference images
    
    
    const response = await env.AI.run(
      'bytedance/seedream-4.5',
      {
        prompt: 'Transform this scene into a winter wonderland with snow covering everything',
        aspect_ratio: 'match_input_image',
        image_input: [
          'https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-4.5",
      "input": {
        "prompt": "Transform this scene into a winter wonderland with snow covering everything",
        "aspect_ratio": "match_input_image",
        "image_input": [
          "https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg"
        ]
      }
    }'

![Image-to-Image](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/image-to-image-0.jpeg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052176861386b9a8ed856c57501cfa946ce34c98846458_0.jpeg"
        ]
      },
      "state": "Completed"
    }

**Sequential Generation** — Generate multiple related images
    
    
    const response = await env.AI.run(
      'bytedance/seedream-4.5',
      {
        prompt: 'A character design sheet for a fantasy warrior: front view, side view, and back view',
        aspect_ratio: '16:9',
        max_images: 3,
        sequential_image_generation: 'auto',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-4.5",
      "input": {
        "prompt": "A character design sheet for a fantasy warrior: front view, side view, and back view",
        "aspect_ratio": "16:9",
        "max_images": 3,
        "sequential_image_generation": "auto"
      }
    }'

![Sequential Generation](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/sequential-generation-0.jpeg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052291261386b9a8ed856c57501cfa946ce34c98481db1_0.jpeg"
        ]
      },
      "state": "Completed"
    }

**Multi-Image Edit** — Combine multiple reference images
    
    
    const response = await env.AI.run(
      'bytedance/seedream-4.5',
      {
        prompt: 'Combine the style of the first image with the subject from the second image',
        image_input: [
          'https://replicate.delivery/xezq/TRYcLgNMrBpPJVq09ICKXWe4Z8d6olzpK5vtQPOB8O23ZaMLA/tmpaecga26m.jpg',
          'https://replicate.delivery/xezq/1SbAc0aXYXbVD9doyrdCW78hYufVefMsaJXBrETN7Lu2npxsA/tmphvkx7emy.jpg',
        ],
        size: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bytedance/seedream-4.5",
      "input": {
        "prompt": "Combine the style of the first image with the subject from the second image",
        "image_input": [
          "https://replicate.delivery/xezq/TRYcLgNMrBpPJVq09ICKXWe4Z8d6olzpK5vtQPOB8O23ZaMLA/tmpaecga26m.jpg",
          "https://replicate.delivery/xezq/1SbAc0aXYXbVD9doyrdCW78hYufVefMsaJXBrETN7Lu2npxsA/tmphvkx7emy.jpg"
        ],
        "size": "2K"
      }
    }'

![Multi-Image Edit](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/bytedance__seedream-4.5/multi-image-edit-0.jpeg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "images": [
          "https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-4-5/0217764052323791386b9a8ed856c57501cfa946ce34c98b2f132_0.jpeg"
        ]
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`required

▶image_input[]

`array`format: uri

size

`string`enum: 2K, 4K

aspect_ratio

`string`enum: match_input_image, 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9

sequential_image_generation

`string`enum: disabled, auto

max_images

`integer`minimum: 1maximum: 15

disable_safety_checker

`boolean`

▶images[]

`array`minItems: 1format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bytedance/seedream-4.5/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
