---
url: https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/
title: Video Remove Background 3.0 (bria) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:16.160128+00:00
---

# Video Remove Background 3.0 (bria) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



b

# Video Remove Background 3.0

video-to-video • bria

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`bria/v-rmbg-3.0`

  * Third-party



Bria's video background removal replaces the background of a clip up to 60 seconds long with a solid color or with transparency. Transparent output needs the mov_proresks (ProRes) preset. Frame rate and audio are preserved, and the output resolution matches the input unless auto_zoom crops to the subject.

Model Info|   
---|---  
Terms and License| [link ↗](https://bria.ai/terms-of-use)  
More information| [link ↗](https://docs.bria.ai/video-editing/editing/remove-background)  
Pricing| 

  * Default (per second)$0.0225

  
  
## Usage
    
    
    const response = await env.AI.run(
      'bria/v-rmbg-3.0',
      {
        video:
          'https://labs-assets.bria.ai/sandbox-example-inputs/5586521-uhd_3840_2160_25fps_original.mp4',
        background_color: 'White',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "bria/v-rmbg-3.0",
      "input": {
        "video": "https://labs-assets.bria.ai/sandbox-example-inputs/5586521-uhd_3840_2160_25fps_original.mp4",
        "background_color": "White"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/bria/v-rmbg-3.0/white-background.mp4"
      }
    }

## Parameters

video

`string`requiredformat: uriPublic URL of the input video: MP4, MOV, WEBM, AVI, or GIF, up to 60 seconds and 16000x16000.

background_color

`string`enum: Transparent, Black, White, Gray, Red, Green, Blue, Yellow, Cyan, Magenta, OrangeColor that replaces the removed background; set it explicitly. Transparent needs the mov_proresks preset: with any other preset Bria uses Black and returns a `warning`.

output_container_and_codec

`string`enum: mp4_h264, mp4_h265, mov_h265, mov_proresksOutput container and codec. Default mp4_h264. mov_proresks (ProRes) is the preset that keeps transparency.

auto_zoom

`boolean`Crop once to the subject for the whole video. Output resolution and aspect ratio may change, and processing is slower. Default false.

preserve_audio

`boolean`Keep the input audio track. Default true.

spill_suppression

`number`minimum: 0maximum: 1Strength of green-fringe removal for green-screen footage, from 0 (off) to 1. Default 0.

video

`string`format: uriURL of the processed video.

warning

`string`Present when Bria adjusted the request, such as a Transparent background with a preset that has no alpha channel.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/bria/v-rmbg-3.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
