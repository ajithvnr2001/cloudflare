---
url: https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/
title: phoenix-1.0 (Leonardo) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:05.898455+00:00
---

# phoenix-1.0 (Leonardo) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![Leonardo logo](https://developers.cloudflare.com/_astro/leonardo.JZysY-g3.svg)

# phoenix-1.0

Text-to-Image • Leonardo

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/leonardo/phoenix-1.0`

  * Cloudflare-hosted
  * Partner



Phoenix 1.0 is a model by Leonardo.Ai that generates images with exceptional prompt adherence and coherent text.

Model Info|   
---|---  
Terms and License| [link ↗](https://leonardo.ai/terms-of-service/)  
Partner| Yes  
Unit Pricing| $0.00583 per 512 by 512 tile, $0.00011 per step  
  
## Parameters

prompt

`string`requiredminLength: 1A text description of the image you want to generate.

guidance

`number`default: 2minimum: 2maximum: 10Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt

seed

`integer`minimum: 0Random seed for reproducibility of the image generation

height

`integer`default: 1024minimum: 0maximum: 2048The height of the generated image in pixels

width

`integer`default: 1024minimum: 0maximum: 2048The width of the generated image in pixels

num_steps

`integer`default: 25minimum: 1maximum: 50The number of diffusion steps; higher values can improve quality but take longer

negative_prompt

`string`minLength: 1Specify what to exclude from the generated images

The binding returns a `ReadableStream` with the output (check the model's output schema). 

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/phoenix-1.0/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
