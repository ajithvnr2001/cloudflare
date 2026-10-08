---
url: https://developers.cloudflare.com/ai/models/%40cf/bytedance/stable-diffusion-xl-lightning/
title: stable-diffusion-xl-lightning (ByteDance) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:44.674353+00:00
---

# stable-diffusion-xl-lightning (ByteDance) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/bytedance/stable-diffusion-xl-lightning/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![ByteDance logo](https://developers.cloudflare.com/_astro/bytedance.T1uiROQ6.svg)

# stable-diffusion-xl-lightning

Beta

Text-to-Image • ByteDance

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/bytedance/stable-diffusion-xl-lightning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/bytedance/stable-diffusion-xl-lightning`

  * Cloudflare-hosted



SDXL-Lightning is a lightning-fast text-to-image generation model. It can generate high-quality 1024px images in a few steps.

Model Info|   
---|---  
More information| [link ↗](https://huggingface.co/ByteDance/SDXL-Lightning)  
Beta| Yes  
Unit Pricing| $0.00 per step  
  
## Parameters

prompt

`string`requiredminLength: 1A text description of the image you want to generate

negative_prompt

`string`Text describing elements to avoid in the generated image

height

`integer`minimum: 256maximum: 2048The height of the generated image in pixels

width

`integer`minimum: 256maximum: 2048The width of the generated image in pixels

▶image[]

`array`For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values

image_b64

`string`For use with img2img tasks. A base64-encoded string of the input image

▶mask[]

`array`An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values

num_steps

`integer`default: 20maximum: 20The number of diffusion steps; higher values can improve quality but take longer

strength

`number`default: 1A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image

guidance

`number`default: 7.5Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt

seed

`integer`Random seed for reproducibility of the image generation

The binding returns a `ReadableStream` with the output (check the model's output schema). 

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/bytedance/stable-diffusion-xl-lightning/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/bytedance/stable-diffusion-xl-lightning/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/bytedance/stable-diffusion-xl-lightning/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/bytedance/stable-diffusion-xl-lightning/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
