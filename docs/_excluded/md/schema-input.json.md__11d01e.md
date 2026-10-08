---
url: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-input.json
title: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:32.856017+00:00
---

# https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/bria/fibo-generate-1.5/schema-input.json

{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"prompt":{"description":"Text prompt. Use alone, with `images` as a reference, or with `structured_prompt` to refine a previous result.","type":"string","minLength":1},"images":{"description":"One reference image: a public URL or base64-encoded image data (a `data:` URI prefix is accepted).","minItems":1,"maxItems":1,"type":"array","items":{"type":"string","minLength":1}},"structured_prompt":{"description":"Structured (VGL) prompt as a JSON string, as returned by a previous result. Recreates that image with the same `seed`; add `prompt` to refine it. Cannot be combined with `images`.","type":"string","minLength":1},"resolution":{"description":"Output resolution. 4MP adds about 30 seconds of latency. Default 1MP.","type":"string","enum":["1MP","4MP"]},"aspect_ratio":{"description":"Output aspect ratio. Default 1:1.","type":"string","enum":["1:1","2:3","3:2","3:4","4:3","4:5","5:4","9:16","16:9"]},"seed":{"description":"Seed for reproducible results. Pass the seed of a previous result with its `structured_prompt` to recreate or refine it.","type":"integer","minimum":-9007199254740991,"maximum":9007199254740991},"output_type":{"description":"Output image format. Default png.","type":"string","enum":["png","jpeg"]},"ip_signal":{"description":"When true, the result carries a `warning` if the text input may reference IP-protected content. Default false.","type":"boolean"},"prompt_content_moderation":{"description":"Reject the request if the prompt fails content moderation. Default true.","type":"boolean"},"visual_input_content_moderation":{"description":"Reject the request if the reference image fails content moderation. Default true.","type":"boolean"},"visual_output_content_moderation":{"description":"Fail the request if the generated image fails content moderation. Default true.","type":"boolean"}},"additionalProperties":false}
