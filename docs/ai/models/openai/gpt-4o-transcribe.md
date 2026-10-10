---
url: https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/
title: GPT-4o Transcribe (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:11.939817+00:00
---

# GPT-4o Transcribe (OpenAI) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# GPT-4o Transcribe

Automatic Speech Recognition • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`openai/gpt-4o-transcribe`

  * Third-party
  * Zero data retention



A speech-to-text model that uses GPT-4o to transcribe audio with improved word error rate and better language recognition compared to original Whisper models.

Model Info|   
---|---  
Terms and License| [link ↗](https://openai.com/policies/)  
More information| [link ↗](https://openai.com/)  
Zero data retention| Yes  
Pricing| 

  * Per audio minute$0.006

  
  
## Usage
    
    
    const response = await env.AI.run(
      'openai/gpt-4o-transcribe',
      { file: 'data:audio/wav;base64,<...>' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-4o-transcribe",
      "input": {
        "file": "data:audio/wav;base64,<...>"
      }
    }'
    
    
    Hello
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "text": "Hello"
      },
      "state": "Completed"
    }

## Examples

**With Language Hint** — Transcribe with a language hint for better accuracy
    
    
    const response = await env.AI.run(
      'openai/gpt-4o-transcribe',
      { file: 'data:audio/wav;base64,<...>', language: 'en' },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-4o-transcribe",
      "input": {
        "file": "data:audio/wav;base64,<...>",
        "language": "en"
      }
    }'
    
    
    Hello
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "text": "Hello"
      },
      "state": "Completed"
    }

**Guided Transcription** — Use a prompt to guide transcription style and context
    
    
    const response = await env.AI.run(
      'openai/gpt-4o-transcribe',
      {
        file: 'data:audio/wav;base64,<...>',
        prompt: 'This is a technical discussion about Kubernetes and cloud-native architecture.',
        language: 'en',
      },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-4o-transcribe",
      "input": {
        "file": "data:audio/wav;base64,<...>",
        "prompt": "This is a technical discussion about Kubernetes and cloud-native architecture.",
        "language": "en"
      }
    }'
    
    
    This is a technical discussion about Kubernetes and cloud-native architecture.
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "text": "This is a technical discussion about Kubernetes and cloud-native architecture."
      },
      "state": "Completed"
    }

**High Temperature** — Higher temperature for more varied transcription
    
    
    const response = await env.AI.run(
      'openai/gpt-4o-transcribe',
      { file: 'data:audio/wav;base64,<...>', temperature: 0.5 },
    )
    console.log(response)
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
      "model": "openai/gpt-4o-transcribe",
      "input": {
        "file": "data:audio/wav;base64,<...>",
        "temperature": 0.5
      }
    }'
    
    
    Hello, world!
    
    
    {
      "gatewayMetadata": {
        "keySource": "Unified"
      },
      "result": {
        "text": "Hello, world!"
      },
      "state": "Completed"
    }

## Parameters

file

`string`requiredThe audio file as a data URI (data:audio/...;base64,...) or HTTPS URL. Supported formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, webm.

language

`string`The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.

prompt

`string`An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language.

temperature

`number`minimum: 0maximum: 1The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Defaults to 0 if omitted.

text

`string`The transcribed text.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/openai/gpt-4o-transcribe/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
