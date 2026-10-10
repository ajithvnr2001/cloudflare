---
url: https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/
title: Gemini Omni Flash 1.1 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:13.862256+00:00
---

# Gemini Omni Flash 1.1 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini Omni Flash 1.1

Text-to-Video • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/gemini-omni-1.1-flash`

  * Third-party



High-performance multimodal video generation and editing model with conversational controls and generated audio.

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
      'google/gemini-omni-1.1-flash',
      {
        text: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
        aspect_ratio: '16:9',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.1-flash",
      "input": {
        "text": "A marble rolling fast on a chain reaction style track, continuous smooth shot.",
        "aspect_ratio": "16:9",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.1-flash/text-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Portrait city** — Generate a portrait-format cinematic city scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.1-flash',
      {
        text: 'A futuristic city with neon lights and flying cars, cinematic camera movement and atmospheric haze.',
        aspect_ratio: '9:16',
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.1-flash",
      "input": {
        "text": "A futuristic city with neon lights and flying cars, cinematic camera movement and atmospheric haze.",
        "aspect_ratio": "9:16",
        "resolution": "720p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.1-flash/portrait-city.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Mountain sunrise** — Generate a high-resolution landscape nature scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.1-flash',
      {
        text: 'A drone shot flying over a mountain landscape at sunrise, golden light reflecting across a misty valley.',
        aspect_ratio: '16:9',
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.1-flash",
      "input": {
        "text": "A drone shot flying over a mountain landscape at sunrise, golden light reflecting across a misty valley.",
        "aspect_ratio": "16:9",
        "resolution": "1080p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.1-flash/mountain-sunrise.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Chain reaction** — Generate a low-resolution landscape action scene
    
    
    const response = await env.AI.run(
      'google/gemini-omni-1.1-flash',
      {
        text: 'A marble rolling quickly along a wooden track, knocking through a playful chain reaction in one continuous shot.',
        aspect_ratio: '16:9',
        resolution: '360p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-omni-1.1-flash",
      "input": {
        "text": "A marble rolling quickly along a wooden track, knocking through a playful chain reaction in one continuous shot.",
        "aspect_ratio": "16:9",
        "resolution": "360p"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/google/gemini-omni-1.1-flash/chain-reaction.mp4"
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

Input[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-omni-1.1-flash/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
