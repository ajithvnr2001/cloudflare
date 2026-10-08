---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers/
title: raw.http.response.headers \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:14.464356+00:00
---

# raw.http.response.headers · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Response.Headers



# raw.http.response.headers

`raw.http.response.headers``Map<Array<String>>`

The HTTP response headers without any transformation represented as a Map (or associative array).

This is the raw field version of the [`http.response.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers/) field. Raw fields, prefixed with `raw.`, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Example value:
    
    
    {"server": ["nginx"]}

Example usage:
    
    
    any(raw.http.response.headers["server"][*] == "nginx")

Categories: 

  * Response
  * Headers
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
