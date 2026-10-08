---
url: https://developers.cloudflare.com/ai/models/%40cf/deepgram/flux/
title: flux (Deepgram) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:44.960773+00:00
---

# flux (Deepgram) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/deepgram/flux/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Deepgram logo](https://developers.cloudflare.com/_astro/deepgram.BYzW8KfF.svg)

# flux

Automatic Speech Recognition • Deepgram

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/deepgram/flux/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/deepgram/flux`

  * Cloudflare-hosted
  * Partner
  * Real-time



Flux is the first conversational speech recognition model built specifically for voice agents.

Model Info|   
---|---  
Terms and License| [link ↗](https://deepgram.com/terms)  
Partner| Yes  
Real-time| Yes  
Unit Pricing| $0.0077 per audio minute (websocket)  
  
## Parameters

encoding

`string`enum: linear16Encoding of the audio stream. Currently only supports raw signed little-endian 16-bit PCM.

sample_rate

`string`pattern: ^[0-9]+$Sample rate of the audio stream in Hz.

eager_eot_threshold

`string`End-of-turn confidence required to fire an eager end-of-turn event. When set, enables EagerEndOfTurn and TurnResumed events. Valid Values 0.3 - 0.9.

eot_threshold

`string`default: 0.7End-of-turn confidence required to finish a turn. Valid Values 0.5 - 0.9.

eot_timeout_ms

`string`default: 5000pattern: ^[0-9]+$A turn will be finished when this much time has passed after speech, regardless of EOT confidence.

keyterm

`string`Keyterm prompting can improve recognition of specialized terminology. Pass multiple keyterm query parameters to boost multiple keyterms.

mip_opt_out

`string`default: falseenum: true, falseOpts out requests from the Deepgram Model Improvement Program. Refer to Deepgram Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip

tag

`string`Label your requests for the purpose of identification during usage reporting

request_id

`string`The unique identifier of the request (uuid)

sequence_id

`integer`minimum: 0Starts at 0 and increments for each message the server sends to the client.

event

`string`enum: Update, StartOfTurn, EagerEndOfTurn, TurnResumed, EndOfTurnThe type of event being reported.

turn_index

`integer`minimum: 0The index of the current turn

audio_window_start

`number`Start time in seconds of the audio range that was transcribed

audio_window_end

`number`End time in seconds of the audio range that was transcribed

transcript

`string`Text that was said over the course of the current turn

▶words[]

`array`The words in the transcript

end_of_turn_confidence

`number`Confidence that no more speech is coming in this turn

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/deepgram/flux/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/deepgram/flux/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/deepgram/flux/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/deepgram/flux/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
