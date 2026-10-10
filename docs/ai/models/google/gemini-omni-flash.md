---
url: https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/
title: Gemini Omni Flash (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:14.032916+00:00
---

# Gemini Omni Flash (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini Omni Flash

Text-to-Video • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/gemini-omni-flash`

  * Third-party



Preview high-performance multimodal video generation and editing model with conversational controls and generated audio.

Model Info|   
---|---  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
Pricing| 

  * Input text (per 1M tokens)$1.50
  * Input image (per 1M tokens)$1.50
  * Input audio (per 1M tokens)$1.50
  * Input video (per 1M tokens)$1.50
  * Output text (per 1M tokens)$9.00
  * Reasoning (per 1M tokens)$9.00
  * Output video (per 1M tokens)$17.50
  * Default (per second)$1.50

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/gemini-omni-flash',
      {
        text: 'A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.',
        aspect_ratio: '16:9',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-flash",
      "input": {
        "text": "A school of silver fish moving through a sunlit coral reef, slow cinematic tracking shot with drifting particles.",
        "aspect_ratio": "16:9",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/underwater-reef.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Breakfast robot** — Generate a portrait-format character scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-flash',
      {
        text: 'A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.',
        aspect_ratio: '9:16',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-flash",
      "input": {
        "text": "A friendly home robot preparing breakfast in a bright modern kitchen, gentle handheld camera movement.",
        "aspect_ratio": "9:16",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/breakfast-robot.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Desert train** — Generate a high-resolution desert scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-flash',
      {
        text: 'A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.',
        aspect_ratio: '16:9',
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-flash",
      "input": {
        "text": "A vintage train crossing a vast desert at golden hour, dust glowing in the sunset as the camera sweeps alongside.",
        "aspect_ratio": "16:9",
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/desert-train.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Northern lights** — Generate a low-resolution night landscape
    
    
    const response = await env.AI.run(
      'google/gemini-omni-flash',
      {
        text: 'Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.',
        aspect_ratio: '16:9',
        resolution: '360p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-flash",
      "input": {
        "text": "Colorful northern lights dancing above a frozen lake, a small cabin glowing warmly in the foreground.",
        "aspect_ratio": "16:9",
        "resolution": "360p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-flash/northern-lights.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

text

`string`Text prompt or editing instruction

image

`string`First-frame or primary reference image

last_frame

`string`Last-frame reference image

▶reference_images[]

`array`maxItems: 10

video

`string`Reference video for editing or extension

audio

`string`Reference audio input

previous_interaction_id

`string`

aspect_ratio

`string`enum: 16:9, 9:16

resolution

`string`enum: 360p, 720p, 1080p, 4k

▶video

`one of`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-flash/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
