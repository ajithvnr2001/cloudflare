---
url: https://developers.cloudflare.com/ai/models/minimax/music-2.6/
title: MiniMax Music 2.6 (MiniMax) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:58.500577+00:00
---

# MiniMax Music 2.6 (MiniMax) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/minimax/music-2.6/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![MiniMax logo](https://developers.cloudflare.com/_astro/minimax.B0Y99aoe.svg)

# MiniMax Music 2.6

Music Generation • MiniMax

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/minimax/music-2.6/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`minimax/music-2.6`

  * Third-party
  * Zero data retention



MiniMax's music generation model that creates full-length songs with vocals from text prompts and lyrics, or instrumental tracks. Supports BPM/key control and auto-generated lyrics.

Model Info|   
---|---  
Terms and License| [link ↗](https://www.minimaxi.com/terms)  
More information| [link ↗](https://www.minimaxi.com/)  
Zero data retention| Yes  
Pricing| 

  * Per track$0.15
  * Per lyrics generation$0.01

  
  
## Usage
    
    
    const response = await env.AI.run(
      'minimax/music-2.6',
      {
        prompt: 'An upbeat electronic dance track with a catchy synth melody and driving beat',
        is_instrumental: false,
        lyrics_optimizer: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/music-2.6",
      "input": {
        "prompt": "An upbeat electronic dance track with a catchy synth melody and driving beat",
        "is_instrumental": false,
        "lyrics_optimizer": true
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092034-QxSPMzdbiRxBSbDb.mp3"
      },
      "state": "Completed"
    }

## Examples

**With Lyrics** — Generate a song with custom lyrics
    
    
    const response = await env.AI.run(
      'minimax/music-2.6',
      {
        prompt: 'A warm acoustic folk ballad with fingerpicked guitar and gentle vocals',
        is_instrumental: false,
        lyrics:
          'Walking down a dusty road\nWith the sunset painting gold\nEvery step a story told\nOf the places I call home',
        lyrics_optimizer: false,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/music-2.6",
      "input": {
        "prompt": "A warm acoustic folk ballad with fingerpicked guitar and gentle vocals",
        "is_instrumental": false,
        "lyrics": "Walking down a dusty road\nWith the sunset painting gold\nEvery step a story told\nOf the places I call home",
        "lyrics_optimizer": false
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417091919-YiIxwmvIqXtREDcu.mp3"
      },
      "state": "Completed"
    }

**Instrumental** — Generate instrumental music without vocals
    
    
    const response = await env.AI.run(
      'minimax/music-2.6',
      {
        prompt: 'A calm lo-fi hip hop instrumental with vinyl crackle and mellow piano chords',
        is_instrumental: true,
        lyrics_optimizer: false,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/music-2.6",
      "input": {
        "prompt": "A calm lo-fi hip hop instrumental with vinyl crackle and mellow piano chords",
        "is_instrumental": true,
        "lyrics_optimizer": false
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092057-LOwvBOOdyGvAyHkQ.mp3"
      },
      "state": "Completed"
    }

**High Quality Audio** — Specify audio format and sample rate
    
    
    const response = await env.AI.run(
      'minimax/music-2.6',
      {
        prompt: 'An orchestral cinematic score building to an epic crescendo with full symphony',
        format: 'wav',
        is_instrumental: false,
        lyrics_optimizer: true,
        sample_rate: 44100,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/music-2.6",
      "input": {
        "prompt": "An orchestral cinematic score building to an epic crescendo with full symphony",
        "format": "wav",
        "is_instrumental": false,
        "lyrics_optimizer": true,
        "sample_rate": 44100
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092208-UGTfqDggHaemCDAW.wav"
      },
      "state": "Completed"
    }

**Auto-Generated Lyrics** — Let the model generate lyrics from the prompt
    
    
    const response = await env.AI.run(
      'minimax/music-2.6',
      {
        prompt: 'A cheerful pop song about a summer road trip with friends',
        is_instrumental: false,
        lyrics_optimizer: true,
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "minimax/music-2.6",
      "input": {
        "prompt": "A cheerful pop song about a summer road trip with friends",
        "is_instrumental": false,
        "lyrics_optimizer": true
      }
    }'
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "audio": "https://minimax-algeng-chat-tts-us.oss-us-east-1.aliyuncs.com/music%2Fprod%2Ftts-20260417092245-UlqOBbhqSXtRPopt.mp3"
      },
      "state": "Completed"
    }

## Parameters

prompt

`string`requiredmaxLength: 2000Description of the music style, mood, and scenario

lyrics

`string`minLength: 1maxLength: 3500Song lyrics, using \n to separate lines

▶sample_rate

`one of`

▶bitrate

`one of`

format

`string`enum: mp3, wavAudio format

lyrics_optimizer

`boolean`requireddefault: falseAutomatically generate lyrics based on the prompt description

is_instrumental

`boolean`requireddefault: falseGenerate instrumental music (no vocals)

audio

`string`format: uriURL to the generated audio file

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/minimax/music-2.6/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
