---
url: https://developers.cloudflare.com/ai/models/@cf/meta/llama-3.3-70b-instruct-fp8-fast/batch-output.json
title: https://developers.cloudflare.com/ai/models/@cf/meta/llama-3.3-70b-instruct-fp8-fast/batch-output.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:21.190160+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/meta/llama-3.3-70b-instruct-fp8-fast/batch-output.json

> Source: https://developers.cloudflare.com/ai/models/@cf/meta/llama-3.3-70b-instruct-fp8-fast/batch-output.json

{"type":"object","contentType":"application/json","properties":{"response":{"type":"string","description":"The generated text response from the model"},"usage":{"type":"object","description":"Usage statistics for the inference request","properties":{"prompt_tokens":{"type":"number","description":"Total number of tokens in input","default":0},"completion_tokens":{"type":"number","description":"Total number of tokens in output","default":0},"total_tokens":{"type":"number","description":"Total number of input and output tokens","default":0}}},"tool_calls":{"type":"array","description":"An array of tool calls requests made during the response generation","items":{"type":"object","properties":{"arguments":{"type":"object","description":"The arguments passed to be passed to the tool call request"},"name":{"type":"string","description":"The name of the tool to be called"}}}}},"required":["response"]}
