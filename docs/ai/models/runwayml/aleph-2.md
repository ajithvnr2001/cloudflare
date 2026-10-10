---
url: https://developers.cloudflare.com/ai/models/runwayml/aleph-2/
title: RunwayML Aleph 2 (RunwayML) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:06.870094+00:00
---

# RunwayML Aleph 2 (RunwayML) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/runwayml/aleph-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![RunwayML logo](https://developers.cloudflare.com/_astro/runway.Cq8Cjov4.svg)

# RunwayML Aleph 2

Text-to-Video • RunwayML

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`runwayml/aleph-2`

  * Third-party



RunwayML's video editing model. Edit one frame to update your whole video, make changes across multiple shots, and work with up to 30 seconds of video. Supports keyframe-guided editing for precise control over specific moments in the clip.

Model Info|   
---|---  
Terms and License| [link ↗](https://runwayml.com/terms-of-use)  
More information| [link ↗](https://runwayml.com/)  
Pricing| 

  * Default (per second)$0.336

  
  
## Usage
    
    
    const response = await env.AI.run(
      'runwayml/aleph-2',
      {
        prompt: 'Transform the scene into a golden-hour sunset with warm lighting',
        video_uri: 'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "runwayml/aleph-2",
      "input": {
        "prompt": "Transform the scene into a golden-hour sunset with warm lighting",
        "video_uri": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://dnznrvs05pmza.cloudfront.net/7449093b-e574-41a5-8308-05e4692fa652.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Keyframe-Guided Edit** — Edit a video using a reference image anchored to the first frame of the output
    
    
    const response = await env.AI.run(
      'runwayml/aleph-2',
      {
        prompt: 'Edit the video to match the provided reference frame',
        video_uri: 'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4',
        prompt_images: [
          {
            uri: 'https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg',
            position: 'first',
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "runwayml/aleph-2",
      "input": {
        "prompt": "Edit the video to match the provided reference frame",
        "video_uri": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/nature-close-up.mp4",
        "prompt_images": [
          {
            "uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg",
            "position": "first"
          }
        ]
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://dnznrvs05pmza.cloudfront.net/cd7388fe-09d6-4b16-afc5-24bb315eaf14.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Timed Keyframe Edit** — Place a guidance image at a specific timestamp within the input video using keyframes[].seconds
    
    
    const response = await env.AI.run(
      'runwayml/aleph-2',
      {
        prompt: 'Change the background to a futuristic cityscape at night',
        video_uri: 'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4',
        keyframes: [
          {
            uri: 'https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg',
            seconds: 2.0,
          },
        ],
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "runwayml/aleph-2",
      "input": {
        "prompt": "Change the background to a futuristic cityscape at night",
        "video_uri": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/simple-text-to-video.mp4",
        "keyframes": [
          {
            "uri": "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_(cropped).jpg",
            "seconds": 2.0
          }
        ]
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://dnznrvs05pmza.cloudfront.net/a7e054fa-1cf2-4265-a35c-518b8c4d6a1a.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Content Moderation Override** — Edit a video featuring public figures with relaxed content moderation
    
    
    const response = await env.AI.run(
      'runwayml/aleph-2',
      {
        prompt: 'Make the background a dramatic stormy sky',
        video_uri: 'https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4',
        content_moderation: {
          public_figure_threshold: 'low',
        },
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "runwayml/aleph-2",
      "input": {
        "prompt": "Make the background a dramatic stormy sky",
        "video_uri": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/runwayml__gen-4.5/cinematic-scene.mp4",
        "content_moderation": {
          "public_figure_threshold": "low"
        }
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "video": "https://dnznrvs05pmza.cloudfront.net/ea5b1ccd-3dd6-43c3-86e3-5ed720849e92.mp4"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`requiredminLength: 1maxLength: 1000Text prompt describing the edit to apply to the input video

video_uri

`string`requiredHTTPS URL, Runway URI, or data URI of the source video to edit (≤30 seconds)

▶keyframes[]

`array`minItems: 1maxItems: 5Timed guidance images placed at specific points in the input video. Each entry has a uri and either seconds (absolute timestamp) or at (fractional position). Up to 5.

▶prompt_images[]

`array`minItems: 1maxItems: 5Image keyframes for guiding the edit at specific points in the output video. Up to 5.

seed

`integer`minimum: 0maximum: 4294967295Random seed for reproducible results

▶content_moderation{}

`object`Settings that affect the behavior of the content moderation system

duration

`number`exclusiveMinimum: 0Duration of the source video in seconds. Used for billing only — not sent to RunwayML. Provide this so the gateway can compute per-second video cost accurately.

video

`string`format: uriURL to the edited video

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/runwayml/aleph-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/runwayml/aleph-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/runwayml/aleph-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/runwayml/aleph-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
