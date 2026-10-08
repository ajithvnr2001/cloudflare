---
url: https://developers.cloudflare.com/ai/models/@cf/openai/gpt-oss-20b/batch-input.json
title: https://developers.cloudflare.com/ai/models/@cf/openai/gpt-oss-20b/batch-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:23.981790+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/openai/gpt-oss-20b/batch-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/openai/gpt-oss-20b/batch-input.json

{"type":"object","title":"Responses_Async","properties":{"requests":{"type":"array","items":{"type":"object","properties":{"input":{"anyOf":[{"type":"string"},{"items":{},"type":"array"}],"description":"Responses API Input messages. Refer to OpenAI Responses API docs to learn more about supported content types"},"reasoning":{"type":"object","properties":{"effort":{"type":"string","enum":["low","medium","high"],"description":"Reasoning effort. Supported levels: low, medium, high. Reasoning cannot be disabled.","default":"medium"},"summary":{"type":"string","description":"A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model's reasoning process. One of auto, concise, or detailed.","enum":["auto","concise","detailed"]}}}},"required":["input"]}}},"required":["requests"]}
