---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/
title: FLUX Video Upscale (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:53.674107+00:00
---

# FLUX Video Upscale (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX Video Upscale

video-to-video • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-video-upscale`

  * Third-party



FLUX Video Upscale increases video resolution with a precise mode for source-faithful results and a creative mode for stronger detail enhancement. It accepts clips up to 20 seconds and preserves audio.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://docs.bfl.ml/flux_tools/flux_video_upscale)  
Pricing| 

  * Precise (per megapixel-second)$0.07
  * Creative (per megapixel-second)$0.10

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-video-upscale',
      {
        input_video: 'https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4',
        upscale_factor: 2,
        creativity: 0,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-video-upscale",
      "input": {
        "input_video": "https://replicate.delivery/pbxt/PetLEVcclEkT5H9A3tYETZyAMT5GE2Sa4m6sQqPDpj8vgHga/animatediff.B572L3lv.mp4",
        "upscale_factor": 2,
        "creativity": 0
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/precise-video-upscale.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Creative Video Upscale** — Enhance fine detail in a source clip using creative mode.
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-video-upscale',
      {
        input_video: 'https://replicate.delivery/xezq/q1XccP3m8V4HMBNDY3LBkaiKjPdJ6e7t74ICqq2wbfWHJNFXA/tmpq8inl7pd.mp4',
        upscale_factor: 2,
        creativity: 1,
        prompt: 'A cinematic travel video with detailed natural scenery and crisp texture',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-video-upscale",
      "input": {
        "input_video": "https://replicate.delivery/xezq/q1XccP3m8V4HMBNDY3LBkaiKjPdJ6e7t74ICqq2wbfWHJNFXA/tmpq8inl7pd.mp4",
        "upscale_factor": 2,
        "creativity": 1,
        "prompt": "A cinematic travel video with detailed natural scenery and crisp texture"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/black-forest-labs/flux-video-upscale/creative-video-upscale.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

input_video

`string`requiredHTTP(S) URL or base64-encoded MP4 video, up to 20 seconds and 50MB.

upscale_factor

`number`minimum: 1.5maximum: 3Output scale relative to the source resolution, from 1.5x to 3x.

▶creativity

`one of`

prompt

`string`Optional description of the clip to guide creative detail enhancement.

safety_tolerance

`integer`minimum: 0maximum: 4Moderation strictness, from 0 (strictest) to 4.

video

`string`format: uriSigned URL to the upscaled MP4. Download promptly before it expires.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-video-upscale/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
