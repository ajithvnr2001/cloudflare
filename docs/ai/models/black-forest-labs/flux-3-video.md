---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/
title: FLUX 3 Video (Black Forest Labs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:16.691179+00:00
---

# FLUX 3 Video (Black Forest Labs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Black Forest Labs logo](https://developers.cloudflare.com/_astro/blackforestlabs.Ccs-Y4-D.svg)

# FLUX 3 Video

Text-to-Video • Black Forest Labs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`black-forest-labs/flux-3-video`

  * Third-party



FLUX 3 Video is Black Forest Labs' video generation model. It generates video from a text prompt (t2v), animates one or more reference images (i2v), or continues an existing clip (v2v), with synchronized audio, up to fhd resolution, and 5-20 second durations.

Model Info|   
---|---  
Terms and License| [link ↗](https://blackforestlabs.ai/terms-of-service/)  
More information| [link ↗](https://blackforestlabs.ai/)  
Pricing| 

  * hd$0.17
  * fhd$0.29
  * v2v hd$0.41
  * v2v fhd$0.53
  * hd draft$0.06
  * v2v hd draft$0.12

  
  
## Usage
    
    
    const response = await env.AI.run(
      'black-forest-labs/flux-3-video',
      {
        mode: 't2v',
        prompt:
          'A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.',
        resolution: 'hd',
        duration: 5,
        generate_audio: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "black-forest-labs/flux-3-video",
      "input": {
        "mode": "t2v",
        "prompt": "A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.",
        "resolution": "hd",
        "duration": 5,
        "generate_audio": true
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://examples.aig.cloudflare.com/black-forest-labs/flux-3-video/text-to-video.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

▶Option 1{}

object

▶Option 2{}

object

▶Option 3{}

object

video

`string`format: uriSigned URL to the generated mp4 (24fps, with audio by default). Expires ~2 hours after ready — download promptly.

draft_cache

`string`Draft-mode cache bundle URL, only present for draft: true requests.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
