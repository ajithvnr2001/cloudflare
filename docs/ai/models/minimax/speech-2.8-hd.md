---
url: https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/
title: MiniMax Speech 2.8 HD (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:12.485055+00:00
---

# MiniMax Speech 2.8 HD (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Speech 2.8 HD

Text-to-Speech • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`minimax/speech-2.8-hd`

  * Third-party
  * Zero data retention



MiniMax Speech 2.8 HD focuses on studio-grade audio generation with emotion control, multilingual support (40+ languages), and voice cloning.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.minimaxi.com/terms)  
More information| [link ↗](https://www.minimaxi.com/)  
Zero data retention| Yes  
Pricing| 

  * Per character$0.0001

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/speech-2.8-hd',
      {
        format: 'mp3',
        pitch: 0,
        speed: 1,
        text: 'Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-2.8-hd",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "speed": 1,
        "text": "Hello! Welcome to Cloudflare AI Gateway. Let me show you what we can do.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/simple-speech.mp3"
      },
      "state": "Completed"
    }

## Examples

**Custom Voice** — Use a specific voice and adjust speed
    
    
    const response = await env.AI.run(
      'minimax/speech-2.8-hd',
      {
        format: 'mp3',
        pitch: 0,
        speed: 0.9,
        text: 'The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-2.8-hd",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "speed": 0.9,
        "text": "The weather today is sunny with a high of 72 degrees. Perfect for a walk in the park.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/custom-voice.mp3"
      },
      "state": "Completed"
    }

**With Emotion** — Apply emotional tone to speech
    
    
    const response = await env.AI.run(
      'minimax/speech-2.8-hd',
      {
        emotion: 'happy',
        format: 'mp3',
        pitch: 0,
        speed: 1,
        text: "Congratulations! You've just won the grand prize! This is absolutely incredible news!",
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-2.8-hd",
      "input": {
        "emotion": "happy",
        "format": "mp3",
        "pitch": 0,
        "speed": 1,
        "text": "Congratulations! You'\''ve just won the grand prize! This is absolutely incredible news!",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/with-emotion.mp3"
      },
      "state": "Completed"
    }

**High Sample Rate** — Studio quality at 44.1kHz sample rate
    
    
    const response = await env.AI.run(
      'minimax/speech-2.8-hd',
      {
        format: 'mp3',
        pitch: 0,
        sample_rate: 44100,
        speed: 1,
        text: 'This recording is generated at studio quality sample rate for the highest possible audio fidelity.',
        voice_id: 'English_expressive_narrator',
        volume: 1,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/speech-2.8-hd",
      "input": {
        "format": "mp3",
        "pitch": 0,
        "sample_rate": 44100,
        "speed": 1,
        "text": "This recording is generated at studio quality sample rate for the highest possible audio fidelity.",
        "voice_id": "English_expressive_narrator",
        "volume": 1
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/minimax__speech-2.8-hd/high-sample-rate.mp3"
      },
      "state": "Completed"
    }

## Parameters

text

`string`requiredmaxLength: 10000The text to convert to speech. Maximum 10,000 characters.

voice_id

`string`requireddefault: English_expressive_narratorThe voice ID to use for synthesis

speed

`number`requireddefault: 1minimum: 0.5maximum: 2Speech speed (0.5 to 2)

volume

`number`requireddefault: 1minimum: 0maximum: 10Speech volume (0 to 10)

pitch

`integer`requireddefault: 0minimum: -12maximum: 12Pitch adjustment (-12 to 12)

emotion

`string`enum: happy, sad, angry, fearful, disgusted, surprised, calm, fluentEmotion control for synthesized speech

format

`string`requireddefault: mp3enum: mp3, flac, wavOutput audio format

▶sample_rate

`one of`

audio

`string`URL to the generated audio file

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/speech-2.8-hd/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
