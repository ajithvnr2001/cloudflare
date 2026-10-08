---
url: https://developers.cloudflare.com/ai/models/recraft/recraftv3/
title: Recraft V3 (Recraft) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:05.090214+00:00
---

# Recraft V3 (Recraft) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/recraft/recraftv3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Recraft logo](https://developers.cloudflare.com/_astro/recraft.BhhnJczi.svg)

# Recraft V3

Text-to-Image • Recraft

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/recraft/recraftv3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`recraft/recraftv3`

  * Third-party
  * Zero data retention



Recraft V3 is the previous-generation text-to-image model from Recraft, well-suited to design-quality compositions, brand-aware imagery, and accurate text rendering.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.recraft.ai/terms)  
More information| [link ↗](https://www.recraft.ai/)  
Zero data retention| Yes  
Pricing| 

  * Per image$0.04

  
  
## Usage
    
    
    const response = await env.AI.run(
      'recraft/recraftv3',
      { prompt: 'A minimalist logo of a mountain range with a sun rising behind it' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv3",
      "input": {
        "prompt": "A minimalist logo of a mountain range with a sun rising behind it"
      }
    }'

![Simple Generation](https://examples.aig.cloudflare.com/recraft/recraftv3/simple-generation.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv3/simple-generation.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Scene Composition** — Generate a complex compositional scene
    
    
    const response = await env.AI.run(
      'recraft/recraftv3',
      {
        prompt: 'A cozy cabin in the woods surrounded by tall pine trees, smoke rising from the chimney',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv3",
      "input": {
        "prompt": "A cozy cabin in the woods surrounded by tall pine trees, smoke rising from the chimney"
      }
    }'

![Scene Composition](https://examples.aig.cloudflare.com/recraft/recraftv3/scene-composition.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv3/scene-composition.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Custom Size** — Specify output dimensions
    
    
    const response = await env.AI.run(
      'recraft/recraftv3',
      {
        prompt: 'A flat illustration of a workspace with a laptop, coffee cup, and potted plant',
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv3",
      "input": {
        "prompt": "A flat illustration of a workspace with a laptop, coffee cup, and potted plant",
        "size": "1024x1024"
      }
    }'

![Custom Size](https://examples.aig.cloudflare.com/recraft/recraftv3/custom-size.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv3/custom-size.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**With Color Controls** — Guide generation with specific brand colors
    
    
    const response = await env.AI.run(
      'recraft/recraftv3',
      {
        prompt: 'An abstract geometric pattern suitable for a tech company brand identity',
        controls: { colors: [{ rgb: [255, 107, 53] }, { rgb: [0, 43, 91] }] },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv3",
      "input": {
        "prompt": "An abstract geometric pattern suitable for a tech company brand identity",
        "controls": {
          "colors": [
            {
              "rgb": [
                255,
                107,
                53
              ]
            },
            {
              "rgb": [
                0,
                43,
                91
              ]
            }
          ]
        }
      }
    }'

![With Color Controls](https://examples.aig.cloudflare.com/recraft/recraftv3/with-color-controls.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv3/with-color-controls.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Background Color** — Set a specific background color
    
    
    const response = await env.AI.run(
      'recraft/recraftv3',
      {
        prompt: 'A clean icon of a lightning bolt',
        controls: { background_color: { rgb: [245, 245, 245] } },
        size: '1024x1024',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "recraft/recraftv3",
      "input": {
        "prompt": "A clean icon of a lightning bolt",
        "controls": {
          "background_color": {
            "rgb": [
              245,
              245,
              245
            ]
          }
        },
        "size": "1024x1024"
      }
    }'

![Background Color](https://examples.aig.cloudflare.com/recraft/recraftv3/background-color.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/recraft/recraftv3/background-color.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
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

Input[](https://developers.cloudflare.com/ai/models/recraft/recraftv3/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/recraft/recraftv3/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/recraft/recraftv3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
