---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/
title: http.response.headers.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:31.615734+00:00
---

# http.response.headers.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Response.Headers.Values



# http.response.headers.values

`http.response.headers.values``Array<String>`

The values of the headers in the HTTP response.

The values are not pre-processed and retain the original case used in the response.

The order of header values is not guaranteed but will match [`http.response.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.names/).

Duplicate headers are listed multiple times.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



**Note** : The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Example value:
    
    
    Example 1: ["application/json"]
    Example 2: ["This header value is longer than 10 bytes"]

Example usage:
    
    
    # Example 1: Check for specific header value.
    any(http.response.headers.values[*] == "application/json")
    
    # Example 2: Match requests according to the specified operator and the length/size entered for the header value.
    any(len(http.response.headers.values[*])[*] gt 10)

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
