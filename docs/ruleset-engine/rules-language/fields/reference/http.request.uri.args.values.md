---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/
title: http.request.uri.args.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:31.879515+00:00
---

# http.request.uri.args.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Uri.Args.Values



# http.request.uri.args.values

`http.request.uri.args.values``Array<String>`

The values of arguments in the HTTP URI query string.

The values are not pre-processed and retain the original case used in the request. They are in the same order as in the request.

Duplicated values are listed multiple times.

  * **Decoding** : No decoding performed
  * **Non-ASCII** : Preserved



Example value:
    
    
    ["red+apples"]

Example usage:
    
    
    any(http.request.uri.args.values[*] == "red+apples")

Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
