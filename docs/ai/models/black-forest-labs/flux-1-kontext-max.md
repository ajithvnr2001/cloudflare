---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/
title: FLUX.1 Kontext [max] (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:16.768163+00:00
---

# FLUX.1 Kontext [max] (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.1 Kontext [max]

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-1-kontext-max`

  * Third-party



FLUX.1 Kontext [max] is Black Forest Labs' highest-quality Kontext model for text-to-image generation and context-aware image editing.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://docs.bfl.ml/api-reference/models/edit-or-create-an-image-with-flux1-kontext-\[max\])  
Pricing| 

  * Per image$0.08

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-1-kontext-max',
      {
        prompt:
          'A lone warrior in bloodstained samurai armor stands before a pagoda engulfed in flames, cinematic dark fantasy realism',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-1-kontext-max",
      "input": {
        "prompt": "A lone warrior in bloodstained samurai armor stands before a pagoda engulfed in flames, cinematic dark fantasy realism"
      }
    }'

![Maximum Quality Generation](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/maximum-quality-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/maximum-quality-generation.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Reproducible Generation** — Use a seed and PNG output for reproducible image generation.
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-1-kontext-max',
      {
        prompt:
          'A detailed oil painting portrait of a Renaissance nobleman with an intricate lace collar',
        seed: 42,
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-1-kontext-max",
      "input": {
        "prompt": "A detailed oil painting portrait of a Renaissance nobleman with an intricate lace collar",
        "seed": 42,
        "output_format": "png"
      }
    }'

![Reproducible Generation](https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/reproducible-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-1-kontext-max/reproducible-generation.png"
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

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-1-kontext-max/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
