---
url: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:21.280311+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-input.json

{"type":"object","properties":{"messages":{"type":"array","description":"An array of message objects representing the conversation history.","items":{"type":"object","properties":{"role":{"enum":["user","assistant"],"description":"The role of the message sender must alternate between 'user' and 'assistant'."},"content":{"type":"string","description":"The content of the message as a string."}},"required":["role","content"]}},"max_tokens":{"type":"integer","default":256,"description":"The maximum number of tokens to generate in the response."},"temperature":{"type":"number","default":0.6,"minimum":0,"maximum":5,"description":"Controls the randomness of the output; higher values produce more random results."},"response_format":{"type":"object","description":"Dictate the output format of the generated response.","properties":{"type":{"type":"string","description":"Set to json_object to process and output generated text as JSON."}}}},"required":["messages"]}
