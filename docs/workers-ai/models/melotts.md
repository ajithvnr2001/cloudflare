---
url: https://developers.cloudflare.com/workers-ai/models/melotts/
title: melotts (MyShell) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:05.343013+00:00
---

# melotts (MyShell) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/melotts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![MyShell logo](https://developers.cloudflare.com/_astro/myshell.6ROagMV2.svg)

# melotts

Text-to-Speech • MyShell

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/melotts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/myshell-ai/melotts`

  * Cloudflare-hosted



MeloTTS is a high-quality multi-lingual text-to-speech library by MyShell.ai.

Model Info|   
---|---  
Unit Pricing| $0.000205 per audio minute  
  
## Parameters

prompt

`string`requiredminLength: 1A text description of the audio you want to generate

lang

`string`default: enThe speech language (e.g., 'en' for English, 'fr' for French). Defaults to 'en' if not specified

▶Option 1{}

objectcontentType: application/json

Option 2

stringcontentType: audio/mpegformat: binary

The generated audio in MP3 format

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/melotts/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/melotts/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/melotts/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/melotts/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
