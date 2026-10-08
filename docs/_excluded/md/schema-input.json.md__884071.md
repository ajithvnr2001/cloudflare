---
url: https://developers.cloudflare.com/ai/models/@cf/leonardo/lucid-origin/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/leonardo/lucid-origin/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:18.760020+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/leonardo/lucid-origin/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/leonardo/lucid-origin/schema-input.json

{"type":"object","properties":{"prompt":{"type":"string","minLength":1,"description":"A text description of the image you want to generate."},"guidance":{"type":"number","default":4.5,"minimum":0,"maximum":10,"description":"Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt"},"seed":{"type":"integer","minimum":0,"description":"Random seed for reproducibility of the image generation"},"height":{"type":"integer","minimum":0,"maximum":2500,"default":1120,"description":"The height of the generated image in pixels"},"width":{"type":"integer","minimum":0,"maximum":2500,"default":1120,"description":"The width of the generated image in pixels"},"num_steps":{"type":"integer","minimum":1,"maximum":40,"description":"The number of diffusion steps; higher values can improve quality but take longer"},"steps":{"type":"integer","minimum":1,"maximum":40,"description":"The number of diffusion steps; higher values can improve quality but take longer"}},"required":["prompt"]}
