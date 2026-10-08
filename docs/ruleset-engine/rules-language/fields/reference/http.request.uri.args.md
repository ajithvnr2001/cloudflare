---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/
title: http.request.uri.args \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.420088+00:00
---

# http.request.uri.args · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Uri.Args



# http.request.uri.args

`http.request.uri.args``Map<Array<String>>`

The HTTP URI arguments associated with a request represented as a Map (associative array).

When an argument repeats, the array contains multiple items in the order they appear in the request.

The values are not pre-processed and retain the original case used in the request.

  * **Decoding** : No decoding performed
  * **Non-ASCII** : Preserved



Example value:
    
    
    {"search": ["red+apples"]}

Example usage:
    
    
    any(http.request.uri.args["search"][*] == "red+apples")

Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
