---
url: https://developers.cloudflare.com/workers-ai/models/nova-3/
title: nova-3 (Deepgram) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:05.704275+00:00
---

# nova-3 (Deepgram) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/nova-3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![Deepgram logo](https://developers.cloudflare.com/_astro/deepgram.BYzW8KfF.svg)

# nova-3

Automatic Speech Recognition • Deepgram

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/nova-3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/deepgram/nova-3`

  * Cloudflare-hosted
  * Batch
  * Partner
  * Real-time



Transcribe audio using Deepgram’s speech-to-text model

Model Info|   
---|---  
Terms and License| [link ↗](https://deepgram.com/terms)  
Batch| Yes  
Partner| Yes  
Real-time| Yes  
Unit Pricing| $0.0052 per audio minute, $0.0092 per audio minute (websocket)  
  
Note

The [pricing of this model](https://developers.cloudflare.com/workers-ai/platform/pricing) is different based on transport. Transport-based pricing does not apply to all models.

  * WebSocket: $0.0092 per audio minute output (836.36 neurons per audio minute output)
  * Regular HTTP: $0.0052 per audio minute output (472.73 neurons per audio minute output)



## Parameters

▶audio{}

`object`required

custom_topic_mode

`string`enum: extended, strictSets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param.

custom_topic

`string`Custom topics you want the model to detect within your input audio or text if present Submit up to 100

custom_intent_mode

`string`enum: extended, strictSets how the model will interpret intents submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in addition those submitted using the custom_intents param

custom_intent

`string`Custom intents you want the model to detect within your input audio if present

detect_entities

`boolean`Identifies and extracts key entities from content in submitted audio

detect_language

`boolean`Identifies the dominant language spoken in submitted audio

diarize

`boolean`Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0

dictation

`boolean`Identify and extract key entities from content in submitted audio

encoding

`string`enum: linear16, flac, mulaw, amr-nb, amr-wb, opus, speex, g729Specify the expected encoding of your submitted audio

extra

`string`Arbitrary key-value pairs that are attached to the API response for usage in downstream processing

filler_words

`boolean`Filler Words can help transcribe interruptions in your audio, like 'uh' and 'um'

keyterm

`string`Key term prompting can boost or suppress specialized terminology and brands.

keywords

`string`Keywords can boost or suppress specialized terminology and brands.

language

`string`The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available.

measurements

`boolean`Spoken measurements will be converted to their corresponding abbreviations.

mip_opt_out

`boolean`Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip.

mode

`string`enum: general, medical, financeMode of operation for the model representing broad area of topic that will be talked about in the supplied audio

multichannel

`boolean`Transcribe each audio channel independently.

numerals

`boolean`Numerals converts numbers from written format to numerical format.

paragraphs

`boolean`Splits audio into paragraphs to improve transcript readability.

profanity_filter

`boolean`Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely.

punctuate

`boolean`Add punctuation and capitalization to the transcript.

redact

`string`Redaction removes sensitive information from your transcripts.

replace

`string`Search for terms or phrases in submitted audio and replaces them.

search

`string`Search for terms or phrases in submitted audio.

sentiment

`boolean`Recognizes the sentiment throughout a transcript or text.

smart_format

`boolean`Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability.

topics

`boolean`Detect topics throughout a transcript or text.

utterances

`boolean`Segments speech into meaningful semantic units.

utt_split

`number`Seconds to wait before detecting a pause between words in submitted audio.

channels

`number`The number of channels in the submitted audio

interim_results

`boolean`Specifies whether the streaming endpoint should provide ongoing transcription updates as more audio is received. When set to true, the endpoint sends continuous updates, meaning transcription results may evolve over time. Note: Supported only for webosockets.

endpointing

`string`Indicates how long model will wait to detect whether a speaker has finished speaking or pauses for a significant period of time. When set to a value, the streaming endpoint immediately finalizes the transcription for the processed time range and returns the transcript with a speech_final parameter set to true. Can also be set to false to disable endpointing

vad_events

`boolean`Indicates that speech has started. You'll begin receiving Speech Started messages upon speech starting. Note: Supported only for webosockets.

utterance_end_ms

`boolean`Indicates how long model will wait to send an UtteranceEnd message after a word has been transcribed. Use with interim_results. Note: Supported only for webosockets.

▶results{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/nova-3/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nova-3/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/nova-3/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/nova-3/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
