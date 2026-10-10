---
url: https://developers.cloudflare.com/workers-ai/models/lucid-origin/
title: lucid-origin (Leonardo) \u00b7 Cloudflare AI docs \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:27:16.031445+00:00
---

# lucid-origin (Leonardo) · Cloudflare AI docs · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/models/lucid-origin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Models



![Leonardo logo](https://developers.cloudflare.com/_astro/leonardo.JZysY-g3.svg)

# lucid-origin

Text-to-Image • Leonardo

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/leonardo/lucid-origin`

  * Cloudflare-hosted
  * Partner



Lucid Origin from Leonardo.AI is their most adaptable and prompt-responsive model to date. Whether you're generating images with sharp graphic design, stunning full-HD renders, or highly specific creative direction, it adheres closely to your prompts, renders text with accuracy, and supports a wide array of visual styles and aesthetics – from stylized concept art to crisp product mockups. 

Model Info|   
---|---  
Terms and License| [link ↗](https://leonardo.ai/terms-of-service/)  
Partner| Yes  
Unit Pricing| $0.007 per 512 by 512 tile, $0.000132 per step  
  
## Parameters

prompt

`string`requiredminLength: 1A text description of the image you want to generate.

guidance

`number`default: 4.5minimum: 0maximum: 10Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt

seed

`integer`minimum: 0Random seed for reproducibility of the image generation

height

`integer`default: 1120minimum: 0maximum: 2500The height of the generated image in pixels

width

`integer`default: 1120minimum: 0maximum: 2500The width of the generated image in pixels

num_steps

`integer`minimum: 1maximum: 40The number of diffusion steps; higher values can improve quality but take longer

steps

`integer`minimum: 1maximum: 40The number of diffusion steps; higher values can improve quality but take longer

image

`string`The generated image in Base64 format.

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/workers-ai/models/lucid-origin/schema-input.json "Open")[](https://developers.cloudflare.com/workers-ai/models/lucid-origin/schema-input.json "Download")

Output[](https://developers.cloudflare.com/workers-ai/models/lucid-origin/schema-output.json "Open")[](https://developers.cloudflare.com/workers-ai/models/lucid-origin/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
