---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/
title: FLUX.2 [max] (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.494590+00:00
---

# FLUX.2 [max] (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.2 [max]

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-2-max`

  * Third-party



FLUX.2 [max] is Black Forest Labs' highest-quality image model — top editing consistency, strongest prompt following, and grounding search for visualizations of real-time information.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://blackforestlabs.ai/)  
Pricing| 

  * First output megapixel$0.07
  * Per additional output megapixel$0.03
  * Per input megapixel$0.03

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-max',
      {
        prompt:
          'A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.',
        height: 2048,
        width: 1440,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-max",
      "input": {
        "prompt": "A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.",
        "height": 2048,
        "width": 1440
      }
    }'

![High Resolution Scene](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/high-resolution-scene.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/high-resolution-scene.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Hex Color Control** — Exact color control via hex codes — useful for brand-consistent imagery
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-max',
      {
        prompt:
          'A vase on a table in living room, the color of the vase is a gradient of color, starting with color #02eb3c and finishing with color #edfa3c. The flowers inside the vase have the color #ff0088',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-max",
      "input": {
        "prompt": "A vase on a table in living room, the color of the vase is a gradient of color, starting with color #02eb3c and finishing with color #edfa3c. The flowers inside the vase have the color #ff0088"
      }
    }'

![Hex Color Control](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/hex-color-control.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/hex-color-control.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Image Editing** — Single-reference image editing — relight or restage a product photo
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-max',
      {
        prompt: 'Place this product onto a minimalist marble countertop with soft window light',
        input_images: [
          'https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-max",
      "input": {
        "prompt": "Place this product onto a minimalist marble countertop with soft window light",
        "input_images": [
          "https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg"
        ]
      }
    }'

![Image Editing](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/image-editing.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-max/image-editing.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText prompt for image generation or editing.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Optional seed for reproducible generation.

width

`integer`minimum: 64maximum: 9007199254740991Width of the generated image in pixels (minimum 64). Omit to let BFL pick.

height

`integer`minimum: 64maximum: 9007199254740991Height of the generated image in pixels (minimum 64). Omit to let BFL pick.

safety_tolerance

`integer`minimum: 0maximum: 5Tolerance for input/output moderation. 0 is the strictest, 5 the most permissive. Defaults to 2.

output_format

`string`enum: jpeg, png, webpOutput image format. Defaults to jpeg.

▶input_images[]

`array`maxItems: 8Up to 8 reference images for editing or multi-image composition. Each entry is an HTTPS URL or a data:image/...;base64,... URI.

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-max/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
