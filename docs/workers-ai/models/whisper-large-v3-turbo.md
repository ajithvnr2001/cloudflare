---
url: https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/
title: whisper-large-v3-turbo (OpenAI) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:27:15.047125+00:00
---

# whisper-large-v3-turbo (OpenAI) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![OpenAI logo](https://developers.cloudflare.com/_astro/openai.BBwNKzBb.svg)

# whisper-large-v3-turbo

Automatic Speech Recognition • OpenAI

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/openai/whisper-large-v3-turbo`

  * Cloudflare-hosted
  * Batch



Whisper is a pre-trained model for automatic speech recognition (ASR) and speech translation. 

Model Info|   
---|---  
Batch| Yes  
Unit Pricing| $0.000513 per audio minute  
  
## Parameters

▶audio

`one of`required

task

`string`default: transcribeSupported tasks are 'translate' or 'transcribe'.

language

`string`The language of the audio being transcribed or translated.

vad_filter

`boolean`default: falsePreprocess the audio with a voice activity detection model.

initial_prompt

`string`A text prompt to help provide context to the model on the contents of the audio.

prefix

`string`The prefix appended to the beginning of the output of the transcription and can guide the transcription result.

beam_size

`integer`default: 5The number of beams to use in beam search decoding. Higher values may improve accuracy at the cost of speed.

condition_on_previous_text

`boolean`default: trueWhether to condition on previous text during transcription. Setting to false may help prevent hallucination loops.

no_speech_threshold

`number`default: 0.6Threshold for detecting no-speech segments. Segments with no-speech probability above this value are skipped.

compression_ratio_threshold

`number`default: 2.4Threshold for filtering out segments with high compression ratio, which often indicate repetitive or hallucinated text.

log_prob_threshold

`number`default: -1Threshold for filtering out segments with low average log probability, indicating low confidence.

hallucination_silence_threshold

`number`Optional threshold (in seconds) to skip silent periods that may cause hallucinations.

▶transcription_info{}

`object`

text

`string`The complete transcription of the audio.

word_count

`number`The total number of words in the transcription.

▶segments[]

`array`

vtt

`string`The transcription in WebVTT format, which includes timing and text information for use in subtitles.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
