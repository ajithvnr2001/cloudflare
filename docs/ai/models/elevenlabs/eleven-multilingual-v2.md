---
url: https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/
title: Eleven Multilingual v2 (ElevenLabs) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:15.514215+00:00
---

# Eleven Multilingual v2 (ElevenLabs) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ElevenLabs logo](https://developers.cloudflare.com/_astro/elevenlabs.0RXw7U95.svg)

# Eleven Multilingual v2

Text-to-Speech • ElevenLabs

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`elevenlabs/eleven-multilingual-v2`

  * Third-party



ElevenLabs' multilingual text-to-speech model for generating natural speech across many languages with ElevenLabs voices.

Model Info|   
---|---  
Terms and License| [link ↗](https://elevenlabs.io/terms)  
More information| [link ↗](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)  
Pricing| 

  * Per character$0.0001
  * Default (per second)$0.0001

  
  
## Usage
    
    
    const response = await env.AI.run(
      'elevenlabs/eleven-multilingual-v2',
      {
        text: 'Bonjour et bienvenue dans Cloudflare AI Gateway. Suivez vos requetes, vos couts et les performances de vos modeles depuis une seule interface.',
        voice_id: 'JBFqnCBsd6RMkjVDRZzb',
        language_code: 'fr',
        output_format: 'mp3_44100_128',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "elevenlabs/eleven-multilingual-v2",
      "input": {
        "text": "Bonjour et bienvenue dans Cloudflare AI Gateway. Suivez vos requetes, vos couts et les performances de vos modeles depuis une seule interface.",
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
        "language_code": "fr",
        "output_format": "mp3_44100_128"
      }
    }'
    
    
    {
      "state": "Completed",
      "result": {
        "audio": "https://examples.aig.cloudflare.com/elevenlabs/eleven-multilingual-v2/french-ai-gateway-speech.mp3"
      },
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

text

`string`requiredminLength: 1maxLength: 10000The text to convert into speech.

voice_id

`string`requiredminLength: 1The ElevenLabs voice ID to use for generation.

output_format

`string`enum: mp3_22050_32, mp3_24000_48, mp3_44100_128, mp3_44100_192, mp3_44100_32, mp3_44100_64, mp3_44100_96, opus_48000_128, opus_48000_192, opus_48000_32, opus_48000_64, opus_48000_96

language_code

`string`ISO 639-1 language code to enforce.

▶voice_settings{}

`object`

seed

`integer`minimum: 0maximum: 4294967295

previous_text

`string`

next_text

`string`

apply_text_normalization

`string`enum: auto, on, off

audio

`string`URL to the generated audio file.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/elevenlabs/eleven-multilingual-v2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
