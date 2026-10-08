---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/
title: FLUX.2 [flex] (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.395073+00:00
---

# FLUX.2 [flex] (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX.2 [flex]

Text-to-Image • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-2-flex`

  * Third-party



FLUX.2 [flex] is Black Forest Labs' fine-grained control variant of FLUX.2 — exposes tunable inference steps, guidance, and prompt upsampling for typography-heavy and production workflows.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://blackforestlabs.ai/)  
Pricing| 

  * First output megapixel$0.05
  * Per additional output megapixel$0.05
  * Per input megapixel$0.05

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-flex',
      {
        prompt:
          "Samsung Galaxy S25 Ultra product advertisement, 'Ultra-strong titanium' headline, close-up of phone edge showing titanium frame, dark gradient background, clean minimalist tech aesthetic",
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-flex",
      "input": {
        "prompt": "Samsung Galaxy S25 Ultra product advertisement, '\''Ultra-strong titanium'\'' headline, close-up of phone edge showing titanium frame, dark gradient background, clean minimalist tech aesthetic"
      }
    }'

![Typography & Design](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/typography-design.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/typography-design.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**High Detail Generation** — Crank steps and guidance for maximum detail when latency is not the priority
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-flex',
      {
        prompt: 'A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar',
        guidance: 7.5,
        steps: 50,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-flex",
      "input": {
        "prompt": "A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar",
        "guidance": 7.5,
        "steps": 50
      }
    }'

![High Detail Generation](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/high-detail-generation.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/high-detail-generation.jpeg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Fast Draft** — Fast draft with prompt upsampling disabled — preserves the literal prompt
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-2-flex',
      { prompt: 'A simple line sketch of a mountain landscape', prompt_upsampling: false, steps: 10 },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-2-flex",
      "input": {
        "prompt": "A simple line sketch of a mountain landscape",
        "prompt_upsampling": false,
        "steps": 10
      }
    }'

![Fast Draft](https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/fast-draft.jpeg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/black-forest-labs/flux-2-flex/fast-draft.jpeg"
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

prompt_upsampling

`boolean`Whether BFL should expand short prompts before generation. Defaults to true on flex.

guidance

`number`minimum: 1.5maximum: 10Classifier-free guidance scale (1.5–10). Higher values follow the prompt more strictly at the cost of realism.

steps

`integer`minimum: 1maximum: 50Number of denoising steps (1–50). Higher steps yield more detail at the cost of latency.

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-2-flex/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
