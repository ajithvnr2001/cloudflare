---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-deception-armor/
title: Cache Deception Armor \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:43.275752+00:00
---

# Cache Deception Armor · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-deception-armor/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Cache Deception Armor



# Cache Deception Armor

Cache Deception Armor

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-deception-armor/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to protect against cache deception attacks for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache
    * **Setting** : Cache key 
      * **Cache deception armor** : On



[PreviousCache by Device Type](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-device-type/)[NextCache everything for hostnames in a list](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/cache-deception-armor.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
