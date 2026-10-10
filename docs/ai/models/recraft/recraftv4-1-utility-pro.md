---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/
title: Recraft V4.1 Utility Pro (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:07.426630+00:00
---

# Recraft V4.1 Utility Pro (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V4.1 Utility Pro

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv4-1-utility-pro`

  * Third-party
  * Zero data retention



Recraft V4.1 Utility Pro is a general-purpose text-to-image model producing high-resolution 2048px+ output for a wide range of production and print use cases.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.25

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-pro',
      {
        prompt:
          'A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-pro",
      "input": {
        "prompt": "A detailed illustrated map of an imaginary fantasy island with labeled landmarks, mountains, and forests"
      }
    }'

![Print-Ready Illustration](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/print-ready-illustration.png"
      },
      "state": "Completed"
    }

## Examples

**Large Format Art** — Large canvas general-purpose image
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-pro',
      {
        prompt:
          'A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky',
        size: '2048x2048',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-pro",
      "input": {
        "prompt": "A wide panoramic landscape of rolling green hills with a river winding through the valley under a bright blue sky",
        "size": "2048x2048"
      }
    }'

![Large Format Art](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/large-format-art.png"
      },
      "state": "Completed"
    }

**Marketing Asset** — High-resolution marketing visual with controlled colors
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-pro',
      {
        prompt: 'A clean, modern banner illustration of a smartphone displaying a productivity app',
        controls: {
          background_color: { rgb: [250, 250, 255] },
          colors: [{ rgb: [100, 200, 150] }, { rgb: [20, 20, 60] }],
        },
        size: '2048x2048',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-pro",
      "input": {
        "prompt": "A clean, modern banner illustration of a smartphone displaying a productivity app",
        "controls": {
          "background_color": {
            "rgb": [
              250,
              250,
              255
            ]
          },
          "colors": [
            {
              "rgb": [
                100,
                200,
                150
              ]
            },
            {
              "rgb": [
                20,
                20,
                60
              ]
            }
          ]
        },
        "size": "2048x2048"
      }
    }'

![Marketing Asset](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/marketing-asset.png"
      },
      "state": "Completed"
    }

**Technical Diagram** — High-resolution technical or infographic illustration
    
    
    const response = await env.AI.run(
      'recraft/recraftv4-1-utility-pro',
      {
        prompt:
          'A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv4-1-utility-pro",
      "input": {
        "prompt": "A clean technical diagram showing the layers of a cloud computing architecture with labeled tiers"
      }
    }'

![Technical Diagram](https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png)
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "image": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-utility-pro/technical-diagram.png"
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

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-utility-pro/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
