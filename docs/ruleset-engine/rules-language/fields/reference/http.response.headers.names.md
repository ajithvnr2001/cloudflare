---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.names/
title: http.response.headers.names \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:31.515961+00:00
---

# http.response.headers.names · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.names/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Response.Headers.Names



# http.response.headers.names

`http.response.headers.names``Array<String>`

The names of the headers in the HTTP response.

The names are not pre-processed and retain the original case used in the response.

The order of header names is not guaranteed but will match [`http.response.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/).

Duplicate headers are listed multiple times.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



**Note** : The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Example value:
    
    
    ["content-type"]

Example usage:
    
    
    any(http.response.headers.names[*] == "content-type")

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
