---
url: https://developers.cloudflare.com/ai/models/@cf/meta/m2m100-1.2b/batch-input.json
title: https://developers.cloudflare.com/ai/models/@cf/meta/m2m100-1.2b/batch-input.json
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (755 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:23:22.817513+00:00
---

# https://developers.cloudflare.com/ai/models/@cf/meta/m2m100-1.2b/batch-input.json

> Source: https://developers.cloudflare.com/ai/models/@cf/meta/m2m100-1.2b/batch-input.json


```
{"properties":{"requests":{"type":"array","description":"Batch of the embeddings requests to run using async-queue","items":{"type":"object","properties":{"text":{"type":"string","minLength":1,"description":"The text to be translated"},"source_lang":{"type":"string","default":"en","description":"The language code of the source text (e.g., 'en' for English). Defaults to 'en' if not specified"},"target_lang":{"type":"string","description":"The language code to translate the text into (e.g., 'es' for Spanish)"}},"required":["text","target_lang"]}}},"required":["requests"]}
```

