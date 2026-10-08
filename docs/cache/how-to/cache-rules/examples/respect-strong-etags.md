---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/
title: Respect Strong ETags \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.226199+00:00
---

# Respect Strong ETags · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Respect Strong ETags



# Respect Strong ETags

Respect Strong ETags

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to respect strong ETags for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Respect strong ETags 
      * **Use strong ETag headers** : On



[PreviousQuery String Sort](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/)[NextMigration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/respect-strong-etags.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
