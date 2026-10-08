---
url: https://developers.cloudflare.com/ai/models/pruna/p-image/
title: P-Image (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:04.877690+00:00
---

# P-Image (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-image/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Image

Text-to-Image • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-image/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-image`

  * Third-party



Pruna's P-Image is an ultra-fast text-to-image model with automatic prompt enhancement and 2-stage refinement, combining exceptional speed with high-quality output and flexible aspect ratios.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Per image$0.005

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-image',
      {
        prompt: 'A majestic lion standing on a rocky cliff at sunset, photorealistic, 4k',
        aspect_ratio: '16:9',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image",
      "input": {
        "prompt": "A majestic lion standing on a rocky cliff at sunset, photorealistic, 4k",
        "aspect_ratio": "16:9"
      }
    }'

![Lion at Sunset](https://examples.aig.cloudflare.com/pruna/p-image/lion-at-sunset.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image/lion-at-sunset.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Reading Nook** — Square-format generation with prompt upsampling.
    
    
    const response = await env.AI.run(
      'pruna/p-image',
      {
        prompt: 'A cozy reading nook by a rainy window, warm lighting, detailed illustration',
        aspect_ratio: '1:1',
        prompt_upsampling: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image",
      "input": {
        "prompt": "A cozy reading nook by a rainy window, warm lighting, detailed illustration",
        "aspect_ratio": "1:1",
        "prompt_upsampling": true
      }
    }'

![Reading Nook](https://examples.aig.cloudflare.com/pruna/p-image/reading-nook.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image/reading-nook.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText description of the image to generate. The model automatically enhances prompts for better results.

aspect_ratio

`string`requireddefault: 16:9enum: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, customAspect ratio for the image. Use "custom" with width/height for exact dimensions.

width

`integer`minimum: 256maximum: 1440multipleOf: 16Custom width in pixels (256-1440, multiple of 16). Only used when aspect_ratio="custom".

height

`integer`minimum: 256maximum: 1440multipleOf: 16Custom height in pixels (256-1440, multiple of 16). Only used when aspect_ratio="custom".

lora_weights

`string`Load LoRA weights. Supports HuggingFace URLs in the format huggingface.co/<owner>/<model-name>[/<file.safetensors>].

lora_scale

`number`requireddefault: 0.5minimum: -1maximum: 3How strongly the LoRA should be applied (-1 to 3).

hf_api_token

`string`HuggingFace API token for accessing private LoRAs. This credential is forwarded verbatim to Pruna. It is only written to gateway request-body logs when the gateway-level collectLogPayload debug flag is explicitly enabled — it never appears in structured analytics logs.

prompt_upsampling

`boolean`requireddefault: falseUpsample the prompt with an LLM for enhanced results.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable_safety_checker

`boolean`requireddefault: falseDisable safety checker for generated images.

image

`string`format: uriPresigned URL for the generated image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-image/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-image/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
