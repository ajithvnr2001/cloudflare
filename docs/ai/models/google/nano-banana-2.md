---
url: https://developers.cloudflare.com/ai/models/google/nano-banana-2/
title: Nano Banana 2 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:57.423173+00:00
---

# Nano Banana 2 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/nano-banana-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Nano Banana 2

Text-to-Image • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/google/nano-banana-2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/nano-banana-2`

  * Third-party
  * Zero data retention



Google's second-generation image generation model with improved quality and speed.

Model Info|   
---|---  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://deepmind.google/technologies/imagen/)  
Zero data retention| Yes  
Pricing| 

  * Input (per 1M tokens)$0.50
  * Output (per 1M tokens)$60.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/nano-banana-2',
      {
        prompt:
          'A futuristic cyberpunk city at night with towering skyscrapers, neon signs in Japanese and English, flying cars, and rain-slicked streets reflecting colorful lights',
        aspect_ratio: '16:9',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2",
      "input": {
        "prompt": "A futuristic cyberpunk city at night with towering skyscrapers, neon signs in Japanese and English, flying cars, and rain-slicked streets reflecting colorful lights",
        "aspect_ratio": "16:9"
      }
    }'

![Futuristic City](https://examples.aig.cloudflare.com/google/nano-banana-2/futuristic-city.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2/futuristic-city.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Abstract Art** — Modern abstract expressionist painting
    
    
    const response = await env.AI.run(
      'google/nano-banana-2',
      {
        prompt:
          'An abstract expressionist painting with bold splashes of cobalt blue, crimson red, and gold leaf accents on a large canvas',
        aspect_ratio: '1:1',
        output_format: 'jpg',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2",
      "input": {
        "prompt": "An abstract expressionist painting with bold splashes of cobalt blue, crimson red, and gold leaf accents on a large canvas",
        "aspect_ratio": "1:1",
        "output_format": "jpg"
      }
    }'

![Abstract Art](https://examples.aig.cloudflare.com/google/nano-banana-2/abstract-art.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2/abstract-art.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**With Google Search** — Use web search grounding for current events
    
    
    const response = await env.AI.run(
      'google/nano-banana-2',
      {
        prompt: 'An illustration of the latest Mars rover exploring the Martian surface',
        aspect_ratio: '16:9',
        google_search: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2",
      "input": {
        "prompt": "An illustration of the latest Mars rover exploring the Martian surface",
        "aspect_ratio": "16:9",
        "google_search": true
      }
    }'

![With Google Search](https://examples.aig.cloudflare.com/google/nano-banana-2/with-google-search.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2/with-google-search.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**High Resolution Portrait** — 4K portrait with specific aspect ratio
    
    
    const response = await env.AI.run(
      'google/nano-banana-2',
      {
        prompt:
          'A professional studio portrait of a woman with dramatic side lighting, wearing elegant jewelry',
        aspect_ratio: '3:4',
        output_format: 'jpg',
        resolution: '4K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/nano-banana-2",
      "input": {
        "prompt": "A professional studio portrait of a woman with dramatic side lighting, wearing elegant jewelry",
        "aspect_ratio": "3:4",
        "output_format": "jpg",
        "resolution": "4K"
      }
    }'

![High Resolution Portrait](https://examples.aig.cloudflare.com/google/nano-banana-2/high-resolution-portrait.jpg)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/google/nano-banana-2/high-resolution-portrait.jpg"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`required

▶image_input[]

`array`maxItems: 3

aspect_ratio

`string`enum: match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9

output_format

`string`enum: jpg, png

resolution

`string`enum: 1K, 2K, 4K

google_search

`boolean`

image_search

`boolean`

image

`string`format: uri

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/nano-banana-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
