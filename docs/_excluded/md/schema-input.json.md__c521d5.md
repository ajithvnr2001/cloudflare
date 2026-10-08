---
url: https://developers.cloudflare.com/ai/models/openai/gpt-image-1.5/schema-input.json
title: https://developers.cloudflare.com/ai/models/openai/gpt-image-1.5/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:42.683635+00:00
---

# https://developers.cloudflare.com/ai/models/openai/gpt-image-1.5/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/openai/gpt-image-1.5/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"type":"string","description":"Text prompt describing the image to generate or edit"},"images":{"description":"Input images for image editing, 1-16 entries. Each entry is base64-encoded (raw string or data:image/{png|jpeg|webp};base64,... URI).","maxItems":16,"type":"array","items":{"type":"string"}},"quality":{"description":"Quality of the generated image","type":"string","enum":["low","medium","high","auto"]},"size":{"description":"Size of the generated image","type":"string","enum":["256x256","512x512","1024x1024","1792x1024","1024x1792"]},"style":{"description":"Style of the generated image","type":"string","enum":["vivid","natural"]}},"required":["prompt"],"additionalProperties":{}}
