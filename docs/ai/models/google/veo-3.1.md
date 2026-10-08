---
url: https://developers.cloudflare.com/ai/models/google/veo-3.1/
title: Veo 3.1 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:57.714515+00:00
---

# Veo 3.1 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/veo-3.1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Veo 3.1

Text-to-Video • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/google/veo-3.1/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/veo-3.1`

  * Third-party
  * Zero data retention



Google's latest video generation model with improved quality, motion, and audio generation.

Model Info|   
---|---  
Terms and License| [link ↗](https://ai.google.dev/gemini-api/terms)  
More information| [link ↗](https://deepmind.google/technologies/veo/)  
Zero data retention| Yes  
Pricing| 

  * Default (per second)$0.40
  * @720p (per second)$0.20
  * @1080p (per second)$0.20
  * @4k (per second)$0.40
  * @720p w/ audio (per second)$0.40
  * @1080p w/ audio (per second)$0.40
  * @4k w/ audio (per second)$0.60

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/veo-3.1',
      {
        prompt:
          'A majestic eagle soaring over snow-capped mountains, tracking shot following the bird as it glides through clouds',
        aspect_ratio: '16:9',
        duration: '8s',
        generate_audio: true,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/veo-3.1",
      "input": {
        "prompt": "A majestic eagle soaring over snow-capped mountains, tracking shot following the bird as it glides through clouds",
        "aspect_ratio": "16:9",
        "duration": "8s",
        "generate_audio": true,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/nature-documentary.mp4"
      },
      "state": "Completed"
    }

## Examples

**Urban Time-lapse** — City life time-lapse video
    
    
    const response = await env.AI.run(
      'google/veo-3.1',
      {
        prompt:
          'A time-lapse of a busy city intersection at night, car lights creating streaks, people walking in fast motion',
        aspect_ratio: '16:9',
        duration: '6s',
        generate_audio: true,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/veo-3.1",
      "input": {
        "prompt": "A time-lapse of a busy city intersection at night, car lights creating streaks, people walking in fast motion",
        "aspect_ratio": "16:9",
        "duration": "6s",
        "generate_audio": true,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/urban-time-lapse.mp4"
      },
      "state": "Completed"
    }

**Abstract Art** — Abstract motion graphics
    
    
    const response = await env.AI.run(
      'google/veo-3.1',
      {
        prompt:
          'Colorful ink drops falling into water in slow motion, creating organic swirling patterns',
        aspect_ratio: '16:9',
        duration: '6s',
        generate_audio: false,
        resolution: '720p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/veo-3.1",
      "input": {
        "prompt": "Colorful ink drops falling into water in slow motion, creating organic swirling patterns",
        "aspect_ratio": "16:9",
        "duration": "6s",
        "generate_audio": false,
        "resolution": "720p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/abstract-art.mp4"
      },
      "state": "Completed"
    }

**Food Video** — Appetizing food footage
    
    
    const response = await env.AI.run(
      'google/veo-3.1',
      {
        prompt: 'Melted chocolate being poured over fresh strawberries in slow motion, rich and glossy',
        aspect_ratio: '9:16',
        duration: '4s',
        generate_audio: true,
        resolution: '1080p',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/veo-3.1",
      "input": {
        "prompt": "Melted chocolate being poured over fresh strawberries in slow motion, rich and glossy",
        "aspect_ratio": "9:16",
        "duration": "4s",
        "generate_audio": true,
        "resolution": "1080p"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "video": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/google__veo-3.1/food-video.mp4"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`requiredText prompt describing the video to generate

image_input

`string`Base64-encoded reference image for i2v

duration

`string`requireddefault: 6senum: 4s, 6s, 8sVideo duration

aspect_ratio

`string`requireddefault: 16:9enum: 16:9, 9:16, 1:1Video aspect ratio

resolution

`string`requireddefault: 720penum: 720p, 1080pVideo resolution

generate_audio

`boolean`requireddefault: trueWhether to generate audio with the video

video

`string`format: uriURL to the generated video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/veo-3.1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/veo-3.1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/veo-3.1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/veo-3.1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
