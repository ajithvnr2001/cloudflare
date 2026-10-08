---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.names/
title: raw.http.response.headers.names \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:14.529680+00:00
---

# raw.http.response.headers.names · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.names/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Response.Headers.Names



# raw.http.response.headers.names

`raw.http.response.headers.names``Array<String>`

The names of the headers in the HTTP response without any transformation.

This is the raw field version of the [`http.response.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.names/) field. Raw fields, prefixed with `raw.`, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Example value:
    
    
    ["content-type"]

Example usage:
    
    
    any(raw.http.response.headers.names[*] == "content-type")

Categories: 

  * Response
  * Headers
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
