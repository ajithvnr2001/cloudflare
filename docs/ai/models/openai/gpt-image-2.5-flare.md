---
url: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/
title: GPT Image 2.5 Flare (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:03.552415+00:00
---

# GPT Image 2.5 Flare (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT Image 2.5 Flare

Text-to-Image • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-image-2.5-flare`

  * Third-party



OpenAI's fastest high-quality everyday image generation model. It accepts text and image inputs and produces images with low, medium, high, xhigh, max, and auto quality settings.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)  
Pricing| 

  * Cached input image (per 1M tokens)$3.00
  * Cached input (per 1M tokens)$1.25
  * Input image (per 1M tokens)$8.00
  * Input (per 1M tokens)$5.00
  * Output image (per 1M tokens)$30.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-flare',
      {
        prompt:
          'A premium studio product photograph of a translucent orange mechanical keyboard on a cobalt blue acrylic pedestal, a few keys glowing amber, crisp reflections, bold geometric shadows, clean commercial art direction, no logos or readable words',
        quality: 'high',
        size: '1024x1024',
        output_format: 'jpeg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-flare",
      "input": {
        "prompt": "A premium studio product photograph of a translucent orange mechanical keyboard on a cobalt blue acrylic pedestal, a few keys glowing amber, crisp reflections, bold geometric shadows, clean commercial art direction, no logos or readable words",
        "quality": "high",
        "size": "1024x1024",
        "output_format": "jpeg"
      }
    }'

![Commercial Product Scene](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/commercial-product-scene.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/commercial-product-scene.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Environmental Concept Frame** — Generate a wide environmental concept frame
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-flare',
      {
        prompt:
          'A wide establishing shot of a hidden mountain library carved into basalt cliffs, tiny figures crossing rope bridges, waterfalls disappearing into mist, late afternoon sun, grounded fantasy concept art with realistic scale',
        quality: 'xhigh',
        size: '1536x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-flare",
      "input": {
        "prompt": "A wide establishing shot of a hidden mountain library carved into basalt cliffs, tiny figures crossing rope bridges, waterfalls disappearing into mist, late afternoon sun, grounded fantasy concept art with realistic scale",
        "quality": "xhigh",
        "size": "1536x1024"
      }
    }'

![Environmental Concept Frame](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/environmental-concept-frame.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/environmental-concept-frame.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Poster Reference Edit** — Transform a reference sketch into a finished illustration
    
    
    const response = await env.AI.run(
      'openai/gpt-image-2.5-flare',
      {
        prompt:
          'Reimagine the reference as a vibrant risograph poster for a fictional night market. Keep the central market stall silhouette and hanging lantern arrangement, add layered coral, teal, and navy ink textures, imperfect registration, and a lively crowd rendered as abstract shapes',
        images: [
          'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII=',
        ],
        quality: 'medium',
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-image-2.5-flare",
      "input": {
        "prompt": "Reimagine the reference as a vibrant risograph poster for a fictional night market. Keep the central market stall silhouette and hanging lantern arrangement, add layered coral, teal, and navy ink textures, imperfect registration, and a lively crowd rendered as abstract shapes",
        "images": [
          "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnklEQVR42u2XQRLAIAgD8/839i/26qFCACm0ozPe1KwcQsAoXvgcAABxpwFowl4QWITHxW0LCBhxVngF4gKIirMQyBRnIJAtrkE8AuwWnyFEgKzfS1UA+3sWTju3BGAu7gKYIfBW+Q/AAQgBeMCkt1wVsLZjcwUYG2Z9wGLHZitWk1DEisubUYt2XB5IWkSyFqG0RSxvMZi0Gc1+Ox3fm00ZJ5mGVtkAAAAASUVORK5CYII="
        ],
        "quality": "medium",
        "output_format": "png"
      }
    }'

![Poster Reference Edit](https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/poster-reference-edit.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/openai/gpt-image-2.5-flare/poster-reference-edit.png"
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

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-image-2.5-flare/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
