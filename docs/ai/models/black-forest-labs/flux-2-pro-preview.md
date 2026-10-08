---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/
title: FLUX.2 [pro] (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.564752+00:00
---

# FLUX.2 [pro] (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.2 [pro]

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-2-pro-preview`

  * Third-party



FLUX.2 [pro] Preview is Black Forest Labs' recommended default for production image generation and editing — tracks the latest [pro] weights with strong multi-reference support.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://blackforestlabs.ai/)  
Pricing| 

  * First output megapixel$0.03
  * Per additional output megapixel$0.015
  * Per input megapixel$0.015

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-pro-preview',
      {
        prompt:
          'A serene mountain landscape at golden hour, soft diffused light filtering through clouds',
        height: 1024,
        width: 1024,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-pro-preview",
      "input": {
        "prompt": "A serene mountain landscape at golden hour, soft diffused light filtering through clouds",
        "height": 1024,
        "width": 1024
      }
    }'

![Simple Prompt](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/simple-prompt.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Multi-Reference Editing** — Multi-reference editing — combine two reference images in a single composition
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-pro-preview',
      {
        prompt: 'Combine the subjects of these images into a single editorial fashion scene',
        input_images: [
          'https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg',
          'https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-pro-preview",
      "input": {
        "prompt": "Combine the subjects of these images into a single editorial fashion scene",
        "input_images": [
          "https://replicate.delivery/xezq/jCypj4MeXYUiRyq7nfgm8z1OvFZF81wh4FznutDsZOuJz0YWA/tmp1iukn307.jpg",
          "https://replicate.delivery/xezq/0lxxNQSg3NabCZrDiQVAPGVmjP1Q2dd7TgYCOTfI9LpyZaMLA/tmp89gopylq.jpg"
        ]
      }
    }'

![Multi-Reference Editing](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/multi-reference-editing.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Reproducible PNG Output** — Seeded generation with PNG output for downstream editing pipelines
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-pro-preview',
      { prompt: 'A pastel watercolor of a koi pond at sunrise', output_format: 'png', seed: 1337 },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-pro-preview",
      "input": {
        "prompt": "A pastel watercolor of a koi pond at sunrise",
        "output_format": "png",
        "seed": 1337
      }
    }'

![Reproducible PNG Output](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-pro-preview/reproducible-png-output.png"
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

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-pro-preview/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
