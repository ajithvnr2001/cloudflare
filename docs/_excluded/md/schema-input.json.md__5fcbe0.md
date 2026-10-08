---
url: https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json
title: https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:25.071986+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/qwen/qwen3-embedding-0.6b/schema-input.json

{"type":"object","properties":{"queries":{"oneOf":[{"type":"string","description":"A single query string","minLength":1},{"type":"array","description":"An array of query strings","items":{"type":"string","minLength":1},"maxItems":32}]},"instruction":{"type":"string","default":"Given a web search query, retrieve relevant passages that answer the query","description":"Optional instruction for the task"},"documents":{"oneOf":[{"type":"string","description":"A single document string","minLength":1},{"type":"array","description":"An array of document strings","items":{"type":"string","minLength":1},"maxItems":32}]},"text":{"oneOf":[{"type":"string","description":"Alias for documents: a single text string","minLength":1},{"type":"array","description":"Alias for documents: an array of text strings","items":{"type":"string","minLength":1},"maxItems":32}]}}}
