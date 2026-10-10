---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-pro/
title: Nano Banana Pro (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:13.432189+00:00
---

# Nano Banana Pro (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Nano Banana Pro

Text-to-Image • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/nano-banana-pro`

  * Third-party
  * Zero data retention



Google's higher-quality image generation model with improved detail and prompt adherence.

Model Info|   
---|---  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://deepmind.google/technologies/imagen/)  
Zero data retention| Yes  
Pricing| 

  * Input (per 1M tokens)$2.00
  * Output (per 1M tokens)$120.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/nano-banana-pro',
      {
        prompt:
          'A sleek modern wireless headphone on a minimalist white marble surface with soft studio lighting and subtle shadows',
        aspect_ratio: '1:1',
        output_format: 'png',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-pro",
      "input": {
        "prompt": "A sleek modern wireless headphone on a minimalist white marble surface with soft studio lighting and subtle shadows",
        "aspect_ratio": "1:1",
        "output_format": "png"
      }
    }'

![Product Photography](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/product-photography.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/product-photography.png"
      },
      "state": "Completed"
    }

## Examples

**Fantasy Illustration** — Epic fantasy scene
    
    
    const response = await env.AI.run(
      'google/nano-banana-pro',
      {
        prompt:
          'An epic fantasy illustration of a wizard casting a spell in an ancient library, magical runes floating in the air, dust motes catching golden light streaming through stained glass windows',
        aspect_ratio: '16:9',
        image_size: '2K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-pro",
      "input": {
        "prompt": "An epic fantasy illustration of a wizard casting a spell in an ancient library, magical runes floating in the air, dust motes catching golden light streaming through stained glass windows",
        "aspect_ratio": "16:9",
        "image_size": "2K"
      }
    }'

![Fantasy Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/fantasy-illustration.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/fantasy-illustration.png"
      },
      "state": "Completed"
    }

**Architectural Visualization** — Modern architecture render
    
    
    const response = await env.AI.run(
      'google/nano-banana-pro',
      {
        prompt:
          'A photorealistic architectural visualization of a modern glass house perched on a cliff overlooking the ocean at sunset',
        aspect_ratio: '16:9',
        image_size: '4K',
        output_format: 'jpg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-pro",
      "input": {
        "prompt": "A photorealistic architectural visualization of a modern glass house perched on a cliff overlooking the ocean at sunset",
        "aspect_ratio": "16:9",
        "image_size": "4K",
        "output_format": "jpg"
      }
    }'

![Architectural Visualization](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/architectural-visualization.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/architectural-visualization.jpg"
      },
      "state": "Completed"
    }

**Character Design** — Game character concept art
    
    
    const response = await env.AI.run(
      'google/nano-banana-pro',
      {
        prompt:
          'A detailed character design sheet for a steampunk inventor, showing front view, side view, and detail callouts for mechanical arm and goggles',
        aspect_ratio: '3:2',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-pro",
      "input": {
        "prompt": "A detailed character design sheet for a steampunk inventor, showing front view, side view, and detail callouts for mechanical arm and goggles",
        "aspect_ratio": "3:2"
      }
    }'

![Character Design](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/character-design.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__nano-banana-pro/character-design.png"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`required

▶image_input[]

`array`maxItems: 3

aspect_ratio

`string`enum: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

output_format

`string`enum: jpg, png, webp

image_size

`string`enum: 1K, 2K, 4K

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/nano-banana-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/nano-banana-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
