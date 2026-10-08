---
url: https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/
title: P-Image Try-On (Pruna AI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:04.803785+00:00
---

# P-Image Try-On (Pruna AI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Pruna AI logo](https://developers.cloudflare.com/_astro/prunaai.Bv7D31UF.svg)

# P-Image Try-On

Image-to-Image • Pruna AI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`pruna/p-image-try-on`

  * Third-party



Pruna's P-Image Try-On virtually fits one or more garments onto a person's photo. Provide a photo of a person plus garment reference images and the model realistically dresses the person in the provided garments.

Tip

**70% off P-Image-Try-On:** Save 70% on all inference with P-Image-Try-On until Sunday, 21 June at 11:59 PM CEST

Model Info|   
---|---  
More information| [link ↗](https://docs.api.pruna.ai/guides/quickstart)  
Pricing| 

  * Per image$0.015
  * Per input image$0.008

  
  
## Usage
    
    
    const response = await env.AI.run(
      'pruna/p-image-try-on',
      {
        person_image:
          'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
        garment_images: [
          'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/cloth/04469_00.jpg',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image-try-on",
      "input": {
        "person_image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
        "garment_images": [
          "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/cloth/04469_00.jpg"
        ]
      }
    }'

![Single Garment](https://examples.aig.cloudflare.com/pruna/p-image-try-on/single-garment.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image-try-on/single-garment.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Turbo PNG** — Faster generation with turbo optimizations, returning a PNG.
    
    
    const response = await env.AI.run(
      'pruna/p-image-try-on',
      {
        person_image:
          'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg',
        garment_images: [
          'https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/cloth/09163_00.jpg',
        ],
        turbo: true,
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "pruna/p-image-try-on",
      "input": {
        "person_image": "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/human/00121_00.jpg",
        "garment_images": [
          "https://huggingface.co/spaces/yisol/IDM-VTON/resolve/main/example/cloth/09163_00.jpg"
        ],
        "turbo": true,
        "output_format": "png"
      }
    }'

![Turbo PNG](https://examples.aig.cloudflare.com/pruna/p-image-try-on/turbo-png.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/pruna/p-image-try-on/turbo-png.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

person_image

`string`requiredImage of the person to dress. A publicly reachable HTTP(S) URL or a base64 data URI (data:image/...;base64,...).

▶garment_images[]

`array`requiredminItems: 1maxItems: 11Garment reference images to fit onto the person. Each entry is an HTTP(S) URL or a base64 data URI. Up to 6 recommended, up to 11 supported.

prompt

`string`requireddefault: Experimental guidance for non-flatlay garment images, e.g. which garment from which image to use.

seed

`integer`minimum: -9007199254740991maximum: 9007199254740991Random seed. Leave unset for a random seed.

turbo

`boolean`requireddefault: falseRun faster with additional optimizations. Not recommended for more than 4 garments.

output_format

`string`requireddefault: jpgenum: webp, jpg, pngFormat of the saved output image.

output_quality

`integer`requireddefault: 95minimum: 0maximum: 100Quality for jpg/webp outputs, from 0 to 100.

reference_pose

`string`Optional reference pose image (HTTP(S) URL or data URI). When provided, the person is reposed to match this reference before virtual try-on.

preserve_input_size

`boolean`requireddefault: trueReturn the output at the original input resolution.

image

`string`format: uriPresigned URL for the generated try-on image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/pruna/p-image-try-on/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
