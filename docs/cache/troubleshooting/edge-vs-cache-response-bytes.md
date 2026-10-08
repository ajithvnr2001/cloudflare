---
url: https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/
title: edgeResponseBytes and cacheResponseBytes discrepancy \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:46.327869+00:00
---

# edgeResponseBytes and cacheResponseBytes discrepancy · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Troubleshooting
  4. /edgeResponseBytes and cacheResponseBytes discrepancy



# edgeResponseBytes and cacheResponseBytes discrepancy

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [HTTP request logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/), `cacheResponseBytes` reflects the uncompressed response size from cache or origin. `edgeResponseBytes` reflects the final compressed response size sent to the client. Because Cloudflare applies compression (gzip, Brotli) before delivering to the client, `edgeResponseBytes` is typically smaller than `cacheResponseBytes`.

[PreviousBot Management cookie causes cache bypass in O2O setups](https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/)[NextAlways Online](https://developers.cloudflare.com/cache/troubleshooting/always-online/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/troubleshooting/edge-vs-cache-response-bytes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
