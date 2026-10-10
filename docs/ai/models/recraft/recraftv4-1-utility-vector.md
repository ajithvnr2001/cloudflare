---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/
title: Recraft V4.1 Utility SVG (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:07.340295+00:00
---

# Recraft V4.1 Utility SVG (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Utility SVG

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-utility-vector`

  * Third-party
  * Zero data retention



Generate production-ready SVG vector graphics from text prompts with a general-purpose model suited for a wide range of design and illustration tasks.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.08

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-vector',
      { prompt: 'A simple flat icon of a calendar with a date marked' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-vector",
      "input": {
        "prompt": "A simple flat icon of a calendar with a date marked"
      }
    }'

![Simple Icon](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/simple-icon.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/simple-icon.jpg"
      },
      "state": "Completed"
    }

## Examples

**App Icon** — Mobile app icon in vector format
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-vector',
      { prompt: 'A clean app icon featuring a magnifying glass over a document', size: '1024x1024' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-vector",
      "input": {
        "prompt": "A clean app icon featuring a magnifying glass over a document",
        "size": "1024x1024"
      }
    }'

![App Icon](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/app-icon.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/app-icon.jpg"
      },
      "state": "Completed"
    }

**Illustration** — Vector illustration for general use
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-vector',
      {
        prompt:
          'A flat vector illustration of a team of people collaborating around a table with laptops',
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-vector",
      "input": {
        "prompt": "A flat vector illustration of a team of people collaborating around a table with laptops",
        "size": "1024x1024"
      }
    }'

![Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/illustration.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/illustration.jpg"
      },
      "state": "Completed"
    }

**With Brand Colors** — Vector with specific color palette
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-vector',
      {
        prompt: 'A simple shield icon representing protection and security',
        controls: {
          background_color: { rgb: [245, 245, 245] },
          colors: [{ rgb: [34, 139, 87] }, { rgb: [255, 255, 255] }],
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-vector",
      "input": {
        "prompt": "A simple shield icon representing protection and security",
        "controls": {
          "background_color": {
            "rgb": [
              245,
              245,
              245
            ]
          },
          "colors": [
            {
              "rgb": [
                34,
                139,
                87
              ]
            },
            {
              "rgb": [
                255,
                255,
                255
              ]
            }
          ]
        }
      }
    }'

![With Brand Colors](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/with-brand-colors.jpg)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-vector/with-brand-colors.jpg"
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

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-vector/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
