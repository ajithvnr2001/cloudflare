---
url: https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/
title: Gemini 3.8 Flash-Lite TTS (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:14.163099+00:00
---

# Gemini 3.8 Flash-Lite TTS (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# Gemini 3.8 Flash-Lite TTS

Text-to-Speech • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`google/gemini-3.8-flash-lite-tts`

  * Third-party



Gemini 3.8 Flash-Lite TTS is a fast, cost-efficient text-to-speech model optimized for high-throughput production workloads.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 8,192 tokens  
More information| [link ↗](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts)  
Pricing| 

  * Input text (per 1M tokens)$0.50
  * Cached input (per 1M tokens)$0.125
  * Output audio (per 1M tokens)$6.00

  
  
## Usage
    
    
    const response = await env.AI.run(
      'google/gemini-3.8-flash-lite-tts',
      { text: 'Hello, welcome to Cloudflare AI Gateway!' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-3.8-flash-lite-tts",
      "input": {
        "text": "Hello, welcome to Cloudflare AI Gateway!"
      }
    }'
    
    
    {
      "audio": "https://examples.aig.cloudflare.com/google/gemini-3.8-flash-lite-tts/simple-text-to-speech.wav",
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Examples

**Expressive Pause** — Generate expressive speech with an inline vocal pause
    
    
    const response = await env.AI.run(
      'google/gemini-3.8-flash-lite-tts',
      {
        text: 'Welcome to the future of voice. <short pause> Let us build something remarkable together.',
        voice: 'Puck',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-3.8-flash-lite-tts",
      "input": {
        "text": "Welcome to the future of voice. <short pause> Let us build something remarkable together.",
        "voice": "Puck"
      }
    }'
    
    
    {
      "audio": "https://examples.aig.cloudflare.com/google/gemini-3.8-flash-lite-tts/expressive-pause.wav",
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**Narrated Passage** — Generate a longer narrated passage with a different voice
    
    
    const response = await env.AI.run(
      'google/gemini-3.8-flash-lite-tts',
      {
        text: 'At sunrise, the research team opened the observatory and watched the first light move across the valley. Every sensor came online in sequence, and the quiet room filled with the soft rhythm of discovery.',
        voice: 'Charon',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-3.8-flash-lite-tts",
      "input": {
        "text": "At sunrise, the research team opened the observatory and watched the first light move across the valley. Every sensor came online in sequence, and the quiet room filled with the soft rhythm of discovery.",
        "voice": "Charon"
      }
    }'
    
    
    {
      "audio": "https://examples.aig.cloudflare.com/google/gemini-3.8-flash-lite-tts/narrated-passage.wav",
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

**French Greeting** — Generate speech from a French greeting using a distinct voice
    
    
    const response = await env.AI.run(
      'google/gemini-3.8-flash-lite-tts',
      {
        text: "Bonjour et bienvenue. Nous sommes ravis de vous accompagner aujourd'hui.",
        voice: 'Kore',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "google/gemini-3.8-flash-lite-tts",
      "input": {
        "text": "Bonjour et bienvenue. Nous sommes ravis de vous accompagner aujourd'\''hui.",
        "voice": "Kore"
      }
    }'
    
    
    {
      "audio": "https://examples.aig.cloudflare.com/google/gemini-3.8-flash-lite-tts/french-greeting.wav",
      "gatewayMetadata": {
        "keySource": "Unified"
      }
    }

## Parameters

text

`string`requiredmaxLength: 10000The text to convert to speech. Maximum 10,000 characters.

voice

`string`enum: Zephyr, Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, SulafatThe voice to use for speech synthesis

temperature

`number`minimum: 0maximum: 2Controls randomness in generation (0-2)

topP

`number`minimum: 0maximum: 1Nucleus sampling threshold (0-1). Tokens with cumulative probability up to topP are considered

topK

`integer`exclusiveMinimum: 0maximum: 9007199254740991Only sample from the top K tokens. Smaller K = more focused, larger K = more diverse

maxOutputTokens

`integer`exclusiveMinimum: 0maximum: 9007199254740991Maximum number of tokens to generate

▶stopSequences[]

`array`Sequences where the model will stop generating further tokens

audio

`string`Base64-encoded audio data (WAV format)

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/google/gemini-3.8-flash-lite-tts/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
