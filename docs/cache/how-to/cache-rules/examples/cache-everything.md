---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/
title: Cache Level (Cache Everything) \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:43.727660+00:00
---

# Cache Level (Cache Everything) · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Cache Level (Cache Everything)



# Cache Level (Cache Everything)

Cache Level (Cache Everything)

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to adjust cache level for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com"`
    * Using the Expression Editor:  
`(http.host contains "example.com")`
  * **Then** :

    * **Cache eligibility** : Eligible for cache



Caution

This option caches all HTML regardless of the presence of dynamic content. If you use this approach to cache pages containing dynamic content, visitors may receive information not intended for them. To avoid caching dynamic content, you can add a condition to the rule's matching criteria to prevent it from matching that content. Some examples include:

  * Checking for the presence of a cookie.
  * Negative matching against known dynamic content file paths.
  * Negative matching against dynamic content extensions (or lack of an extension).



[PreviousCache Everything while ignoring query strings](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything-ignore-query-strings/)[NextCache TTL by status code](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/cache-everything.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
