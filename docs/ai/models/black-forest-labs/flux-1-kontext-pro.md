---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/
title: FLUX.1 Kontext [pro] (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.444803+00:00
---

# FLUX.1 Kontext [pro] (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.1 Kontext [pro]

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-1-kontext-pro`

  * Third-party



FLUX.1 Kontext [pro] creates and edits images from text prompts with strong character and style consistency.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://docs.bfl.ml/api-reference/models/edit-or-create-an-image-with-flux1-kontext-\[pro\])  
Pricing| 

  * Per image$0.04

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-1-kontext-pro',
      { prompt: 'A small furry elephant pet looks out from a cat house' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-1-kontext-pro",
      "input": {
        "prompt": "A small furry elephant pet looks out from a cat house"
      }
    }'

![Text to Image](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/text-to-image.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/text-to-image.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Wide Cinematic Image** — Generate a cinematic landscape using a wide aspect ratio.
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-1-kontext-pro',
      {
        prompt:
          'A remote gas station swallowed by crimson fog, green glow from overhead lights staining the asphalt, cinematic wide shot',
        input_image:
          'https://cdn.sanity.io/images/gsvmb6gz/production/3ae6ee032b85373b84934574f3ac3bb2fb792d64-2048x1365.jpg',
        aspect_ratio: '16:9',
        output_format: 'jpeg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-1-kontext-pro",
      "input": {
        "prompt": "A remote gas station swallowed by crimson fog, green glow from overhead lights staining the asphalt, cinematic wide shot",
        "input_image": "https://cdn.sanity.io/images/gsvmb6gz/production/3ae6ee032b85373b84934574f3ac3bb2fb792d64-2048x1365.jpg",
        "aspect_ratio": "16:9",
        "output_format": "jpeg"
      }
    }'

![Wide Cinematic Image](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/wide-cinematic-image.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-pro/wide-cinematic-image.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText prompt for image generation or editing.

input_image

`string`Optional base64 encoded image or URL to edit.

aspect_ratio

`string`Output aspect ratio, from 3:7 to 7:3. Defaults to 1:1.

seed

`integer | null`Optional seed for reproducible generation.

prompt_upsampling

`boolean`Whether to upsample the prompt. Defaults to false.

safety_tolerance

`integer`minimum: 0maximum: 6Moderation tolerance. 0 is strictest and 6 is most permissive.

output_format

`string`enum: jpeg, pngOutput image format. Defaults to jpeg.

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
