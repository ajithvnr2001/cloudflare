---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/
title: Custom Cache Key \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.265127+00:00
---

# Custom Cache Key · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Custom Cache Key



# Custom Cache Key

Custom Cache Key

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to set a custom cache key for all query string parameters, for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Cache key 
      * **Query string** : All query string parameters



Refer to [cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/) for more information on possible settings when configuring a custom cache key.

[PreviousCache TTL by status code](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/)[NextEdge Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/custom-cache-key.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
