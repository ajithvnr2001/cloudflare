---
url: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json
title: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-08T07:23:34.399382+00:00
---

# https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json

> Source: https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/schema-output.json


```
{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"video":{"type":"string","format":"uri","description":"Signed URL to the generated mp4 (24fps, with audio by default). Expires ~2 hours after ready — download promptly."},"draft_cache":{"description":"Draft-mode cache bundle URL, only present for draft: true requests.","type":"string"}},"required":["video"],"additionalProperties":false}
```

