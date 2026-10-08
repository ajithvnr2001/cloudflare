---
url: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json
title: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:21.256009+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/@cf/meta/llama-guard-3-8b/schema-output.json

{"type":"object","contentType":"application/json","properties":{"response":{"oneOf":[{"type":"string","description":"The generated text response from the model."},{"type":"object","description":"The json response parsed from the generated text response from the model.","properties":{"safe":{"type":"boolean","description":"Whether the conversation is safe or not."},"categories":{"type":"array","description":"A list of what hazard categories predicted for the conversation, if the conversation is deemed unsafe.","items":{"type":"string","description":"Hazard category classname, from S1 to S14."}}}}]},"usage":{"type":"object","description":"Usage statistics for the inference request","properties":{"prompt_tokens":{"type":"number","description":"Total number of tokens in input","default":0},"completion_tokens":{"type":"number","description":"Total number of tokens in output","default":0},"total_tokens":{"type":"number","description":"Total number of input and output tokens","default":0}}}}}
