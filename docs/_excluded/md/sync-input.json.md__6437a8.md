---
url: https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json
title: https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:12.639873+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/baai/bge-m3/sync-input.json

{"title":"Input Query and Contexts","properties":{"query":{"type":"string","minLength":1,"description":"A query you wish to perform against the provided contexts. If no query is provided the model with respond with embeddings for contexts"},"contexts":{"type":"array","items":{"type":"object","properties":{"text":{"type":"string","minLength":1,"description":"One of the provided context content"}}},"description":"List of provided contexts. Note that the index in this array is important, as the response will refer to it."},"truncate_inputs":{"type":"boolean","default":false,"description":"When provided with too long context should the model error out or truncate the context to fit?"}},"required":["contexts"]}
