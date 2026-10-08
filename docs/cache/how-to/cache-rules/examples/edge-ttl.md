---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/
title: Edge Cache TTL \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:43.957695+00:00
---

# Edge Cache TTL · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Edge Cache TTL



# Edge Cache TTL

Edge Cache TTL

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to adjust edge cache TTL for caching resources on Cloudflare edge to one day, for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Edge TTL 
      * Ignore cache-control header and use this TTL 
        * **Input time-to-live (TTL)** : _1 day_



[PreviousCustom Cache Key](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/)[NextOrigin Cache Control](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/edge-ttl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
