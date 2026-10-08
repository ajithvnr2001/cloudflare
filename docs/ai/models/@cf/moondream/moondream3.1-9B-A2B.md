---
url: https://developers.cloudflare.com/ai/models/%40cf/moondream/moondream3.1-9B-A2B/
title: moondream3.1-9B-A2B (moondream) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:47.115486+00:00
---

# moondream3.1-9B-A2B (moondream) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/moondream/moondream3.1-9B-A2B/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



m

# moondream3.1-9B-A2B

Image-to-Text • moondream

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/moondream/moondream3.1-9B-A2B/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/moondream/moondream3.1-9B-A2B`

  * Cloudflare-hosted
  * Vision



Moondream 3 is a fast, efficient 9B mixture-of-experts vision language model (2B active parameters) that delivers frontier-level visual reasoning for tasks like object detection, pointing, OCR, and structured output.

Model Info|   
---|---  
Terms and License| [link ↗](https://moondream.ai/licenses/model/1.0)  
Vision| Yes  
Unit Pricing| $0.30 per M input tokens, $1.00 per M output tokens  
  
## Parameters

task

`string`default: queryenum: query, caption, point, detectWhich Moondream skill to run.

image

`string`Input image as a public HTTPS URL or base64 data URI. Optional for `query`; required for `caption`, `point`, and `detect`.

question

`string`default: What's in this image?Question for the `query` task.

caption_length

`string`default: normalenum: short, normal, longCaption length for the `caption` task.

target

`string`default: personObject phrase to locate for `point` and `detect` tasks (e.g. 'person wearing a red shirt').

reasoning

`boolean`default: trueEnable reasoning trace for the `query` task.

temperature

`number`default: 0.2minimum: 0maximum: 2Sampling temperature.

top_p

`number`default: 0.9minimum: 0maximum: 1Top-p (nucleus) sampling.

max_tokens

`integer`default: 8192minimum: 1maximum: 28672Max tokens to generate for `query` and `caption`.

max_objects

`integer`default: 150minimum: 1maximum: 500Max objects to return for `point` and `detect`.

stream

`boolean`default: falseReturn incremental tokens for `query` and `caption`. `point` and `detect` do not support streaming.

finish_reason

`string`Reason the generation finished.

▶metrics{}

`object`

answer

`string`Answer text for the `query` task. Null for other tasks.

caption

`string`Caption text for the `caption` task. Null for other tasks.

▶points[]

`array`Located points for the `point` task. Null for other tasks.

▶objects[]

`array`Detected bounding boxes for the `detect` task. Null for other tasks.

▶reasoning{}

`object`Reasoning trace for the `query` task when reasoning=true. Null otherwise.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/moondream/moondream3.1-9B-A2B/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/moondream/moondream3.1-9B-A2B/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/moondream/moondream3.1-9B-A2B/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/moondream/moondream3.1-9B-A2B/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
