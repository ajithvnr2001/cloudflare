---
url: https://developers.cloudflare.com/ai/models/@cf/baai/bge-large-en-v1.5/sync-input.json
title: https://developers.cloudflare.com/ai/models/@cf/baai/bge-large-en-v1.5/sync-input.json
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:11.128788+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/baai/bge-large-en-v1.5/sync-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/baai/bge-large-en-v1.5/sync-input.json

{"properties":{"text":{"oneOf":[{"type":"string","description":"The text to embed","minLength":1},{"type":"array","description":"Batch of text values to embed","items":{"type":"string","description":"The text to embed","minLength":1},"maxItems":100}]},"pooling":{"type":"string","enum":["mean","cls"],"default":"mean","description":"The pooling method used in the embedding process. `cls` pooling will generate more accurate embeddings on larger inputs - however, embeddings created with cls pooling are not compatible with embeddings generated with mean pooling. The default pooling method is `mean` in order for this to not be a breaking change, but we highly suggest using the new `cls` pooling for better accuracy."}},"required":["text"]}
