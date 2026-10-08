---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.cookies/
title: http.request.cookies \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:10.783974+00:00
---

# http.request.cookies · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.cookies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Cookies



# http.request.cookies

`http.request.cookies``Map<Array<String>>`

The `Cookie` HTTP header associated with a request represented as a Map (associative array).

Requires a Cloudflare Pro, Business, or Enterprise plan.

The cookie names are URL decoded. If two cookies have the same name after decoding, their value arrays are merged.

The cookie values are not pre-processed and retain the original case used in the request.

Example value:
    
    
    { "app": ["test"] }

Example usage:
    
    
    any(http.request.cookies["app"][*] == "test")

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
