---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/
title: Cache everything for hostnames in a list \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:42.767729+00:00
---

# Cache everything for hostnames in a list · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Cache everything for hostnames in a list



# Cache everything for hostnames in a list

Cache everything for hostnames in a list

Last updated Jun 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-by-hostname-list/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to cache everything for hostnames that match a [custom hostname list](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#lists-with-hostnames):

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname is in list "my_hostnames"`
    * Using the Expression Editor:  
`(http.host in $my_hostnames)`
  * **Then** :

    * **Cache eligibility** : Eligible for cache



Note

The **is in list** operator requires an Enterprise plan. You must first [create a hostname list](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/) in your account before you can reference it in a cache rule expression.

[PreviousCache Deception Armor](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-deception-armor/)[NextCache Everything while ignoring query strings](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything-ignore-query-strings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/cache-by-hostname-list.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
