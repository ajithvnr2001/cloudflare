---
url: https://developers.cloudflare.com/ai/models/pruna/p-image-edit/
title: P-Image-Edit (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:08.503636+00:00
---

# P-Image-Edit (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-image-edit/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Image-Edit

Image-to-Image • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-image-edit`

  * Third-party



Pruna's P-Image-Edit edits and composes 1-5 reference images with text instructions. It supports complex compositions, style transfers, and targeted edits with flexible output aspect ratios.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Per image$0.01

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-image-edit',
      {
        prompt: 'Transform the subject into a watercolor painting style with vibrant colors',
        images: ['https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg'],
        aspect_ratio: '1:1',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image-edit",
      "input": {
        "prompt": "Transform the subject into a watercolor painting style with vibrant colors",
        "images": [
          "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg"
        ],
        "aspect_ratio": "1:1"
      }
    }'

![Watercolor Style](https://examples.aig.cloudflare.com/pruna/p-image-edit/watercolor-style.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image-edit/watercolor-style.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText instruction describing the desired edit or composition.

▶images[]

`array`requiredminItems: 1maxItems: 5Array of 1-5 reference images. Each entry is an HTTP(S) URL or a base64 data URI (data:image/...;base64,...).

turbo

`boolean`requireddefault: trueRun faster with additional optimizations. For complicated tasks, it is recommended to turn this off.

aspect_ratio

`string`requireddefault: match_input_imageenum: match_input_image, 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3Output aspect ratio.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed for reproducible generation.

disable_safety_checker

`boolean`requireddefault: falseDisable safety checker for generated images.

image

`string`format: uriPresigned URL for the edited image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-image-edit/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-edit/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-image-edit/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-edit/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
