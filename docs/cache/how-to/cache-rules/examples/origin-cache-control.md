---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/
title: Origin Cache Control \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.024123+00:00
---

# Origin Cache Control · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Origin Cache Control



# Origin Cache Control

Origin Cache Control

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to determine edge cache behavior for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Origin Cache Control 
      * **Enable Origin Cache Control** : Off



[PreviousEdge Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/)[NextQuery String Sort](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/origin-cache-control.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
