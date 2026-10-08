---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/
title: Cache TTL by status code \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:43.861389+00:00
---

# Cache TTL by status code · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Cache TTL by status code



# Cache TTL by status code

Cache TTL by status code

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to cache responses with status code between `200` and `599` for one day for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Edge TTL 
      * Use cache-control header if present, use default Cloudflare caching behavior if not
      * **Status code TTL** : 
        * **Scope** : _Range_
        * **From** : _200_
        * **To** : _599_
        * **Duration** : _1 day_



[PreviousCache Level (Cache Everything)](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/)[NextCustom Cache Key](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/cache-ttl-by-status-code.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
