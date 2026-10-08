---
url: https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/
title: Krea 2 Medium Turbo (krea) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:58.168948+00:00
---

# Krea 2 Medium Turbo (krea) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



k

# Krea 2 Medium Turbo

Text-to-Image • krea

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`krea/krea-2-medium-turbo`

  * Third-party



The fastest Krea 2 model, built for low-cost iteration on expressive illustrations, style-driven concepts, and rapid visual exploration. Keeps the Krea 2 style system and expressive visual range but uses a distilled sampling schedule so you can move through ideas much faster. Especially useful for expressive illustration, graphic styles, typography experiments, and quick campaign or concept directions.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.krea.ai/terms)  
More information| [link ↗](https://docs.krea.ai/api-reference/krea/krea-2-medium-turbo)  
Pricing| 

  * Default (per second)$0.015
  * Per image$0.015

  
  
## Usage
    
    
    const response = await env.AI.run(
      'krea/krea-2-medium-turbo',
      {
        prompt: 'Ice citadel, frost mages and snow beasts, in a cool, fantasy anime style.',
        aspect_ratio: '1:1',
        resolution: '1K',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "krea/krea-2-medium-turbo",
      "input": {
        "prompt": "Ice citadel, frost mages and snow beasts, in a cool, fantasy anime style.",
        "aspect_ratio": "1:1",
        "resolution": "1K"
      }
    }'

![Default](https://examples.aig.cloudflare.com/krea/krea-2-medium-turbo/default.png)
    
    
    {
      "state": "Completed",
      "result": {
        "image": "https://examples.aig.cloudflare.com/krea/krea-2-medium-turbo/default.png"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredText prompt describing the image to generate.

aspect_ratio

`string`requiredenum: 1:1, 4:3, 3:2, 16:9, 2.35:1, 4:5, 2:3, 9:16Aspect ratio of the generated image.

resolution

`string`requiredenum: 1KResolution scale.

seed

`number`Random seed for reproducible generations. Pass null or omit for a random seed.

▶styles[]

`array`Styles (typically LoRAs) to apply to the generation.

▶image_style_references[]

`array`maxItems: 10Reference images to drive the visual style (up to 10).

creativity

`string`default: lowenum: raw, low, medium, highPrompt expansion mode. `raw` disables expansion; `low`, `medium`, `high` control strength. Does not affect the K2 Intensity, Complexity, or Movement slider LoRAs.

intensity

`integer`default: 0minimum: -100maximum: 100K2 Intensity slider (-100 to 100). 0 disables the slider LoRA.

complexity

`integer`default: 0minimum: -100maximum: 100K2 Complexity slider (-100 to 100). 0 disables the slider LoRA.

movement

`integer`default: 0minimum: -100maximum: 100K2 Movement slider (-100 to 100). 0 disables the slider LoRA.

▶moodboards[]

`array`maxItems: 1Moodboard references (currently limited to one).

image

`string`format: uriPresigned URL for the generated image.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/krea/krea-2-medium-turbo/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
