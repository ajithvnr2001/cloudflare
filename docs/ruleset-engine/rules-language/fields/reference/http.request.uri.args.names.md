---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.names/
title: http.request.uri.args.names \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:31.934056+00:00
---

# http.request.uri.args.names · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.names/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Uri.Args.Names



# http.request.uri.args.names

`http.request.uri.args.names``Array<String>`

The names of the arguments in the HTTP URI query string.

When a name repeats, the array contains multiple items in the order that they appear in the request.

The names are not pre-processed and retain the original case used in the request.

  * **Decoding** : No decoding performed
  * **Non-ASCII** : Preserved



Example value:
    
    
    ["search"]

Example usage:
    
    
    any(http.request.uri.args.names[*] == "search")

Categories: 

  * Request
  * URI



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
