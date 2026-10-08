---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/
title: Recraft V4.1 Pro SVG (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:05.143398+00:00
---

# Recraft V4.1 Pro SVG (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Pro SVG

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-pro-vector`

  * Third-party
  * Zero data retention



Generate detailed, high-resolution SVG vector graphics from text prompts with high aesthetic quality, fine geometry, scalable to any size for print and design work.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.30

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-pro-vector',
      { prompt: 'A modern minimalist logo for a cloud computing company, clean geometric shapes' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-pro-vector",
      "input": {
        "prompt": "A modern minimalist logo for a cloud computing company, clean geometric shapes"
      }
    }'

![Logo Design](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/logo-design.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/logo-design.jpg"
      },
      "state": "Completed"
    }

## Examples

**Icon Set** — Generate a vector icon
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-pro-vector',
      {
        prompt: 'A flat design icon of a rocket launching, suitable for a mobile app',
        size: '2048x2048',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-pro-vector",
      "input": {
        "prompt": "A flat design icon of a rocket launching, suitable for a mobile app",
        "size": "2048x2048"
      }
    }'

![Icon Set](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/icon-set.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/icon-set.jpg"
      },
      "state": "Completed"
    }

**Print-Ready Vector** — High-resolution vector for large-format print
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-pro-vector',
      {
        prompt:
          'An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical',
        size: '2048x2048',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-pro-vector",
      "input": {
        "prompt": "An intricate mandala pattern with floral and geometric elements, highly detailed and symmetrical",
        "size": "2048x2048"
      }
    }'

![Print-Ready Vector](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/print-ready-vector.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/print-ready-vector.jpg"
      },
      "state": "Completed"
    }

**Brand Illustration** — Vector illustration with brand colors
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-pro-vector',
      {
        prompt: 'A vector illustration of a cityscape skyline at sunset with clean lines and flat colors',
        controls: { colors: [{ rgb: [255, 87, 51] }, { rgb: [41, 50, 65] }, { rgb: [239, 239, 239] }] },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-pro-vector",
      "input": {
        "prompt": "A vector illustration of a cityscape skyline at sunset with clean lines and flat colors",
        "controls": {
          "colors": [
            {
              "rgb": [
                255,
                87,
                51
              ]
            },
            {
              "rgb": [
                41,
                50,
                65
              ]
            },
            {
              "rgb": [
                239,
                239,
                239
              ]
            }
          ]
        }
      }
    }'

![Brand Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/brand-illustration.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro-vector/brand-illustration.jpg"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`required

size

`string`

style

`string`

substyle

`string`

▶controls{}

`object`

image

`string`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro-vector/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
