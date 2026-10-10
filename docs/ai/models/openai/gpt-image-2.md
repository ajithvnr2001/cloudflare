---
url: https://developers.cloudflare.com/ai/models/openai/gpt-image-2/
title: GPT Image 2 (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:08.788829+00:00
---

# GPT Image 2 (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-image-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT Image 2

Text-to-Image • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-image-2`

  * Third-party
  * Zero data retention



OpenAI's next-generation image model that creates and edits images from text prompts, with support for multiple quality levels, sizes, and output formats. Note: transparent backgrounds are not supported — use openai/gpt-image-1.5 for transparent PNGs.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://openai.com/)  
Zero data retention| Yes  
Pricing| 

  * Cached input image (per 1M tokens)$2.00
  * Cached input (per 1M tokens)$1.25
  * Input image (per 1M tokens)$8.00
  * Input (per 1M tokens)$5.00
  * Output image (per 1M tokens)$30.00
  * Output (per 1M tokens)$10.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      { prompt: 'A golden retriever puppy playing in autumn leaves' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "A golden retriever puppy playing in autumn leaves"
      }
    }'

![Simple Generation](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/simple-generation.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/simple-generation.png"
      },
      "state": "Completed"
    }

## Examples

**High Quality** — Generate a high-quality detailed image
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      {
        prompt:
          'A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures',
        quality: 'high',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "A detailed botanical illustration of exotic tropical flowers with fine line work and watercolor textures",
        "quality": "high"
      }
    }'

![High Quality](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/high-quality.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/high-quality.png"
      },
      "state": "Completed"
    }

**Custom Size** — Generate a portrait-oriented image
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      {
        prompt: 'A towering redwood forest with sunbeams filtering through the canopy, misty atmosphere',
        size: '1024x1536',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "A towering redwood forest with sunbeams filtering through the canopy, misty atmosphere",
        "size": "1024x1536"
      }
    }'

![Custom Size](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/custom-size.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/custom-size.png"
      },
      "state": "Completed"
    }

**WebP Output** — Generate an image in WebP format for smaller file size
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      {
        prompt:
          'A neon-lit cyberpunk cityscape at night with rain-slicked streets and holographic billboards',
        output_format: 'webp',
        quality: 'high',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "A neon-lit cyberpunk cityscape at night with rain-slicked streets and holographic billboards",
        "output_format": "webp",
        "quality": "high"
      }
    }'

![WebP Output](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/webp-output.webp)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/webp-output.webp"
      },
      "state": "Completed"
    }

**Image Edit** — Edit an existing image by providing it in the images array as base64 (a raw string or a data:image/{png|jpeg|webp};base64,... URI). This routes the call to OpenAI's /v1/images/edits endpoint. The example uses a tiny 32x32 smiley-face PNG - real inputs are the full base64 encoding of your source image.
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      {
        prompt:
          'Transform this cartoon smiley into a photorealistic 3D clay sculpture sitting on a marble pedestal, studio lighting',
        images: [
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "Transform this cartoon smiley into a photorealistic 3D clay sculpture sitting on a marble pedestal, studio lighting",
        "images": [
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII="
        ]
      }
    }'

![Image Edit](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/image-edit.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/image-edit.png"
      },
      "state": "Completed"
    }

**Multi-Image Edit** — Compose multiple input images by passing up to 16 base64 strings in the images array. The model blends the references; useful for combining subjects, styles, or reference shots. The example pairs a smiley-face PNG with a red ball PNG.
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2',
      {
        prompt:
          'Combine these into a single photorealistic scene: a ceramic smiley-face mug next to a red rubber ball on a sunlit wooden table',
        images: [
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAhklEQVR42u2XsRHAMAgDNY73nye7OG2KgGUnGCWH76j/oTACPfnhcwIA3AoTGIFXRTADPlqjakYEDJwFWyJLAk/hrAQi4YwEouEjiVuBt+FXCVcgqntvCtjVvTUF7OremkIJlEAJ6Aikf0QSX3H6MpJYx+mBRCKSSYRSiVgucZjInGa/vY5PvB72/7IdMuAAAAAASUVORK5CYII=',
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2",
      "input": {
        "prompt": "Combine these into a single photorealistic scene: a ceramic smiley-face mug next to a red rubber ball on a sunlit wooden table",
        "images": [
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=",
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAhklEQVR42u2XsRHAMAgDNY73nye7OG2KgGUnGCWH76j/oTACPfnhcwIA3AoTGIFXRTADPlqjakYEDJwFWyJLAk/hrAQi4YwEouEjiVuBt+FXCVcgqntvCtjVvTUF7OremkIJlEAJ6Aikf0QSX3H6MpJYx+mBRCKSSYRSiVgucZjInGa/vY5PvB72/7IdMuAAAAAASUVORK5CYII="
        ]
      }
    }'

![Multi-Image Edit](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/multi-image-edit.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "BYOK"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__gpt-image-2/multi-image-edit.png"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate or edit

▶images[]

`array`maxItems: 16Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).

quality

`string`enum: low, medium, high, autoQuality of the generated image

size

`string`enum: 1024x1024, 1024x1536, 1536x1024, autoSize of the generated image

background

`string`enum: transparent, opaque, autoBackground transparency setting. Use transparent for images with no background, opaque for a solid background, or auto to let the model decide.

output_format

`string`enum: png, webp, jpegOutput format for the generated image

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
