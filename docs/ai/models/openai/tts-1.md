---
url: https://developers.cloudflare.com/ai/models/openai/tts-1/
title: TTS-1 (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:08.144058+00:00
---

# TTS-1 (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/tts-1/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# TTS-1

Text-to-Speech • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/tts-1`

  * Third-party
  * Zero data retention



OpenAI's text-to-speech model optimized for real-time use with low latency.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://platform.openai.com/docs/guides/text-to-speech)  
Zero data retention| Yes  
Pricing| 

  * Per character$0.000015

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/tts-1',
      {
        response_format: 'mp3',
        speed: 1,
        text: 'Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.',
        voice: 'alloy',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/tts-1",
      "input": {
        "response_format": "mp3",
        "speed": 1,
        "text": "Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.",
        "voice": "alloy"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/simple-speech.mp3"
      },
      "state": "Completed"
    }

## Examples

**Different Voice** — Use the Nova voice for a different tone
    
    
    const response = await env.AI.run(
      'openai/tts-1',
      {
        response_format: 'mp3',
        speed: 1,
        text: 'The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.',
        voice: 'nova',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/tts-1",
      "input": {
        "response_format": "mp3",
        "speed": 1,
        "text": "The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.",
        "voice": "nova"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/different-voice.mp3"
      },
      "state": "Completed"
    }

**Narration** — Slower narration style with the Onyx voice
    
    
    const response = await env.AI.run(
      'openai/tts-1',
      {
        response_format: 'mp3',
        speed: 0.85,
        text: 'In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.',
        voice: 'onyx',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/tts-1",
      "input": {
        "response_format": "mp3",
        "speed": 0.85,
        "text": "In the beginning, the universe was a singularity of infinite density. Then, in a fraction of a second, it expanded into everything we know today.",
        "voice": "onyx"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/narration.mp3"
      },
      "state": "Completed"
    }

**Echo Voice** — Use the Echo voice for a deeper tone
    
    
    const response = await env.AI.run(
      'openai/tts-1',
      {
        response_format: 'mp3',
        speed: 1,
        text: 'Welcome back to the podcast. Today we are going to talk about the future of artificial intelligence and its impact on creative work.',
        voice: 'echo',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/tts-1",
      "input": {
        "response_format": "mp3",
        "speed": 1,
        "text": "Welcome back to the podcast. Today we are going to talk about the future of artificial intelligence and its impact on creative work.",
        "voice": "echo"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/echo-voice.mp3"
      },
      "state": "Completed"
    }

**Fast Playback** — Speed up speech for quick listening
    
    
    const response = await env.AI.run(
      'openai/tts-1',
      {
        response_format: 'mp3',
        speed: 1.5,
        text: 'This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent, user growth exceeded expectations, and infrastructure costs remain stable.',
        voice: 'shimmer',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/tts-1",
      "input": {
        "response_format": "mp3",
        "speed": 1.5,
        "text": "This is a fast-paced summary of the key findings from the quarterly report. Revenue is up fifteen percent, user growth exceeded expectations, and infrastructure costs remain stable.",
        "voice": "shimmer"
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/openai__tts-1/fast-playback.mp3"
      },
      "state": "Completed"
    }

## Parameters

text

`string`requiredmaxLength: 4096The text to generate audio for. Maximum length is 4096 characters.

voice

`string`requireddefault: alloyenum: alloy, echo, fable, onyx, nova, shimmerThe voice to use when generating the audio. Defaults to alloy.

response_format

`string`requireddefault: mp3enum: mp3, opus, wav, aac, flacThe output format for the audio. Supported formats are mp3, opus, wav, aac and flac.

speed

`number`requireddefault: 1minimum: 0.25maximum: 4The speed of the generated audio. Select a value from 0.25 to 4.0. 1.0 is the default.

audio

`string`URL to the generated audio file

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/tts-1/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/tts-1/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/tts-1/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/tts-1/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
