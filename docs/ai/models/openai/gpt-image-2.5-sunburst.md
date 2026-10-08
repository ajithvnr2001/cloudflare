---
url: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/
title: GPT Image 2.5 Sunburst (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:03.505740+00:00
---

# GPT Image 2.5 Sunburst (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT Image 2.5 Sunburst

Text-to-Image • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-image-2.5-sunburst`

  * Third-party



OpenAI's most capable image generation and editing model. It accepts text and image inputs and produces images with low, medium, high, xhigh, max, and auto quality settings.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)  
Pricing| 

  * Cached input image (per 1M tokens)$3.00
  * Cached input (per 1M tokens)$1.25
  * Input image (per 1M tokens)$8.00
  * Input (per 1M tokens)$5.00
  * Output image (per 1M tokens)$30.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-sunburst',
      {
        prompt:
          'A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting',
        quality: 'max',
        size: '1536x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-sunburst",
      "input": {
        "prompt": "A cutaway editorial illustration of a floating ocean research station during a storm, showing laboratories, hydroponic gardens, autonomous submersibles, and illuminated underwater cables, precise technical details, dramatic but realistic lighting",
        "quality": "max",
        "size": "1536x1024"
      }
    }'

![Technical Editorial Illustration](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/technical-editorial-illustration.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/technical-editorial-illustration.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Portrait WebP** — Generate a portrait composition in WebP format
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-sunburst',
      {
        prompt:
          'A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography',
        quality: 'xhigh',
        size: '1024x1536',
        output_format: 'webp',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-sunburst",
      "input": {
        "prompt": "A fashion portrait of an astronaut botanist in a glass greenhouse on Mars, crimson dust visible through the windows, translucent fabric, delicate blue flowers in the foreground, soft rim light, sophisticated magazine photography",
        "quality": "xhigh",
        "size": "1024x1536",
        "output_format": "webp"
      }
    }'

![Portrait WebP](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/portrait-webp.webp)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/portrait-webp.webp"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Cinematic Reference Edit** — Edit a reference image into a cinematic scene while preserving its main subject
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-sunburst',
      {
        prompt:
          "Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character's face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures",
        images: [
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
        ],
        quality: 'high',
        background: 'opaque',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-sunburst",
      "input": {
        "prompt": "Turn the reference drawing into a polished cinematic stop-motion scene. Preserve the character'\''s face and red scarf, add a miniature train platform at night, warm station lights, shallow depth of field, handcrafted felt and paper textures",
        "images": [
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII="
        ],
        "quality": "high",
        "background": "opaque"
      }
    }'

![Cinematic Reference Edit](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/cinematic-reference-edit.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-sunburst/cinematic-reference-edit.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate or edit

▶images[]

`array`maxItems: 16Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).

quality

`string`enum: low, medium, high, xhigh, max, autoQuality of the generated image

size

`string`enum: 1024x1024, 1024x1536, 1536x1024, autoSize of the generated image

background

`string`enum: transparent, opaque, autoBackground transparency setting

output_format

`string`enum: png, webp, jpegOutput format for the generated image

image

`string`format: uriURL to the generated image

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-sunburst/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
