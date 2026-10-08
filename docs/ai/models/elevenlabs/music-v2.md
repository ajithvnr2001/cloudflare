---
url: https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/
title: ElevenLabs Music v2 (ElevenLabs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:55.325042+00:00
---

# ElevenLabs Music v2 (ElevenLabs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ElevenLabs logo](https://developers.cloudflare.com/_astro/elevenlabs.0RXw7U95.svg)

# ElevenLabs Music v2

Music Generation • ElevenLabs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`elevenlabs/music-v2`

  * Third-party



ElevenLabs Music v2 composes songs and instrumental tracks from a prompt or detailed composition plan.

Model Info|   
---|---  
Terms and License| [link ↗](https://elevenlabs.io/terms)  
More information| [link ↗](https://elevenlabs.io/docs/api-reference/music/compose)  
Pricing| 

  * output audio seconds$0.0025
  * Default (per second)$0.0025

  
  
## Usage
    
    
    const response = await env.AI.run(
      'elevenlabs/music-v2',
      {
        prompt: 'A warm cinematic ambient track with soft piano, subtle strings, and a hopeful mood',
        music_length_ms: 30000,
        force_instrumental: true,
        output_format: 'mp3_48000_192',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "elevenlabs/music-v2",
      "input": {
        "prompt": "A warm cinematic ambient track with soft piano, subtle strings, and a hopeful mood",
        "music_length_ms": 30000,
        "force_instrumental": true,
        "output_format": "mp3_48000_192"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/elevenlabs/music-v2/cinematic-instrumental.mp3"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

prompt

`string`minLength: 1

▶composition_plan{}

`object`

music_length_ms

`integer`minimum: 3000maximum: 600000

output_format

`string`enum: auto, mp3_48000_128, mp3_48000_192, mp3_48000_240, mp3_48000_320, mp3_22050_32, mp3_24000_48, mp3_44100_32, mp3_44100_64, mp3_44100_96, mp3_44100_128, mp3_44100_192, opus_48000_32, opus_48000_64, opus_48000_96, opus_48000_128, opus_48000_192

seed

`integer`minimum: 0maximum: 4294967295

force_instrumental

`boolean`

store_for_inpainting

`boolean`

sign_with_c2pa

`boolean`

audio

`string`URL to the generated music file.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/music-v2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
