---
url: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/
title: Bypass Cache on Cookie \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:42.664158+00:00
---

# Bypass Cache on Cookie · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration[Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)

  4. /[Examples](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/)
  5. /Bypass Cache on Cookie



# Bypass Cache on Cookie

Bypass Cache on Cookie

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

If you are migrating from Page Rules and you want to keep Page Rules behavior, you need to create two specific rules before creating this rule. For more details refer to [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/).

[Create a cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/) to bypass cache for requests containing cookie `test_cookie` for any hostname containing `example.com`:

  * **When incoming requests match** : Custom filter expression

    * Using the Expression Builder:  
`Hostname contains "example.com" AND Cookie contains "test-cookie"`
    * Using the Expression Editor:  
`(http.host contains "example.com" and http.cookie contains "test-cookie")`
  * **Then** :

    * **Cache eligibility** : Bypass cache



[PreviousBrowser Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/browser-cache-ttl/)[NextCache by Device Type](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-device-type/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/cache-rules/examples/bypass-cache-on-cookie.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
