---
url: https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/
title: Bot Management cookie causes cache bypass in O2O setups \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:46.218687+00:00
---

# Bot Management cookie causes cache bypass in O2O setups · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Troubleshooting
  4. /Bot Management cookie causes cache bypass in O2O setups



# Bot Management cookie causes cache bypass in O2O setups

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/troubleshooting/bot-management-o2o-cache-bypass/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Orange-to-Orange (O2O)](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/) setups — where a SaaS provider uses [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and their customer also has their own Cloudflare zone — the `__cf_bm` Bot Management cookie returned from the origin-facing Cloudflare zone can cause the eyeball-facing zone to bypass cache. This occurs because the `Set-Cookie` header in the response triggers Cloudflare's default behavior of not caching responses with `Set-Cookie`.

If you are seeing unexpectedly low cache hit rates in an O2O setup with Bot Management enabled, this may be the cause.

[PreviousInvestigate latency on tiered requests](https://developers.cloudflare.com/cache/troubleshooting/investigating-tiered-cache-latency/)[NextedgeResponseBytes and cacheResponseBytes discrepancy](https://developers.cloudflare.com/cache/troubleshooting/edge-vs-cache-response-bytes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/troubleshooting/bot-management-o2o-cache-bypass.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
