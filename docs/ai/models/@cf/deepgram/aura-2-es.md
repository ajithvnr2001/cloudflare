---
url: https://developers.cloudflare.com/ai/models/%40cf/deepgram/aura-2-es/
title: aura-2-es (Deepgram) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:22.986292+00:00
---

# aura-2-es (Deepgram) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/deepgram/aura-2-es/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Deepgram logo](https://developers.cloudflare.com/_astro/deepgram.BYzW8KfF.svg)

# aura-2-es

Text-to-Speech • Deepgram

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/deepgram/aura-2-es`

  * Cloudflare-hosted
  * Batch
  * Partner
  * Real-time



Aura-2 is a context-aware text-to-speech (TTS) model that applies natural pacing, expressiveness, and fillers based on the context of the provided text. The quality of your text input directly impacts the naturalness of the audio output.

Model Info|   
---|---  
Terms and License| [link ↗](https://deepgram.com/terms)  
Batch| Yes  
Partner| Yes  
Real-time| Yes  
Unit Pricing| $0.03 per 1k characters  
  
## Parameters

speaker

`string`default: aquilaenum: sirio, nestor, carina, celeste, alvaro, diana, aquila, selena, estrella, javierSpeaker used to produce the audio.

encoding

`string`enum: linear16, flac, mulaw, alaw, mp3, opus, aacEncoding of the output audio.

container

`string`enum: none, wav, oggContainer specifies the file format wrapper for the output audio. The available options depend on the encoding type..

text

`string`The text content to be converted to speech

sample_rate

`number`Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable

bit_rate

`number`The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.

The binding returns a `ReadableStream` with the audio in MPEG format (check the model's output schema). 

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-es/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-es/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-es/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/deepgram/aura-2-es/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
