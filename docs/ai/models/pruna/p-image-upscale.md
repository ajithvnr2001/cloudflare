---
url: https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/
title: P-Image-Upscale (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:04.713171+00:00
---

# P-Image-Upscale (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Image-Upscale

Image-to-Image • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-image-upscale`

  * Third-party



Pruna's P-Image-Upscale increases image resolution using AI, targeting 1-128 megapixels with optional detail and realism enhancement for sharper, cleaner results.

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Per image (1-4 MP)$0.005
  * Per image (5-8 MP)$0.01
  * Per image (9-16 MP)$0.02
  * Per image (17-32 MP)$0.04
  * Per image (33-64 MP)$0.06
  * Per image (65-128 MP)$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-image-upscale',
      {
        image: 'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
        target: 4,
        enhance_details: true,
        output_format: 'jpg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image-upscale",
      "input": {
        "image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
        "target": 4,
        "enhance_details": true,
        "output_format": "jpg"
      }
    }'

![4MP Upscale](https://examples.aig.cloudflare.com/pruna/p-image-upscale/4mp-upscale.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image-upscale/4mp-upscale.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

image

`string`requiredInput image to upscale. A publicly reachable HTTP(S) URL or a base64 data URI (data:image/...;base64,...).

target

`integer`requireddefault: 4minimum: 1maximum: 128Target resolution in megapixels (1-128). Output is capped at 128 MP.

output_format

`string`requireddefault: jpgenum: webp, jpg, pngFormat of the output image.

output_quality

`integer`requireddefault: 80minimum: 0maximum: 100Quality when saving the output image (0-100). Not relevant for .png outputs.

enhance_details

`boolean`requireddefault: falseEnhance fine textures and small details.

enhance_realism

`boolean`requireddefault: falseImprove realism. Recommended for AI-generated images.

disable_safety_checker

`boolean`requireddefault: falseDisable safety checker for generated images.

image

`string`format: uriPresigned URL for the upscaled image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-upscale/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
