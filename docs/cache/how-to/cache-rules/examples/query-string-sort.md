---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/
title: Query String Sort \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.171100+00:00
---

# Query String Sort · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Query String Sort



# Query String Sort

Query String Sort

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to sort query string parameters for caching purposes, for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Cache key 
      * **Sort query string** : On



[PreviousOrigin Cache Control](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/)[NextRespect Strong ETags](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/query-string-sort.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
