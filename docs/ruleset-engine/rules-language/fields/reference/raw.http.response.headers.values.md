---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/
title: raw.http.response.headers.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:29.644136+00:00
---

# raw.http.response.headers.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Response.Headers.Values



# raw.http.response.headers.values

`raw.http.response.headers.values``Array<String>`

The values of the headers in the HTTP response without any transformation.

This is the raw field version of the [`http.response.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/) field. Raw fields, prefixed with `raw.`, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Example value:
    
    
    Example 1: ["application/json"]
    Example 2: ["This header value is longer than 10 bytes"]

Example usage:
    
    
    # Example 1: Check for specific header value.
    any(raw.http.response.headers.values[*] == "application/json")
    
    # Example 2: Match requests according to the specified operator and the length/size entered for the header value.
    any(len(raw.http.response.headers.values[*])[*] gt 10)

Categories: 

  * Response
  * Headers
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
