---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/
title: Recraft V4.1 Utility (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:05.528165+00:00
---

# Recraft V4.1 Utility (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Utility

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-utility`

  * Third-party
  * Zero data retention



Recraft V4.1 Utility is a general-purpose text-to-image model balancing quality and flexibility for a wide range of everyday use cases at standard resolution.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.04

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility',
      { prompt: 'A friendly cartoon robot waving hello against a white background' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility",
      "input": {
        "prompt": "A friendly cartoon robot waving hello against a white background"
      }
    }'

![Simple Generation](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/simple-generation.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/simple-generation.png"
      },
      "state": "Completed"
    }

## Examples

**Product Mockup** — Generate a product concept image
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility',
      { prompt: 'A clean product photo of a white ceramic coffee mug on a wooden table' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility",
      "input": {
        "prompt": "A clean product photo of a white ceramic coffee mug on a wooden table"
      }
    }'

![Product Mockup](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/product-mockup.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/product-mockup.png"
      },
      "state": "Completed"
    }

**Custom Size** — Specify output dimensions
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility',
      {
        prompt: 'A simple banner illustration with abstract shapes and warm colors',
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility",
      "input": {
        "prompt": "A simple banner illustration with abstract shapes and warm colors",
        "size": "1024x1024"
      }
    }'

![Custom Size](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/custom-size.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/custom-size.png"
      },
      "state": "Completed"
    }

**With Color Controls** — Guide generation with specific colors
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility',
      {
        prompt: 'A flat illustration of a globe with network connections',
        controls: { colors: [{ rgb: [30, 90, 200] }, { rgb: [255, 255, 255] }] },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility",
      "input": {
        "prompt": "A flat illustration of a globe with network connections",
        "controls": {
          "colors": [
            {
              "rgb": [
                30,
                90,
                200
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

![With Color Controls](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/with-color-controls.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/with-color-controls.png"
      },
      "state": "Completed"
    }

**Background Color** — Set a specific background color
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility',
      {
        prompt: 'A simple icon of a checkmark inside a circle',
        controls: { background_color: { rgb: [240, 248, 255] } },
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility",
      "input": {
        "prompt": "A simple icon of a checkmark inside a circle",
        "controls": {
          "background_color": {
            "rgb": [
              240,
              248,
              255
            ]
          }
        },
        "size": "1024x1024"
      }
    }'

![Background Color](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/background-color.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility/background-color.png"
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

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
