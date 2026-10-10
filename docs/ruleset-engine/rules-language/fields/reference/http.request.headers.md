---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/
title: http.request.headers \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.609983+00:00
---

# http.request.headers · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Headers



# http.request.headers

`http.request.headers``Map<Array<String>>`

The HTTP request headers represented as a Map (or associative array).

The keys of the associative array are the names of HTTP request headers converted to lowercase.

When there are repeating headers, the array includes them in the order they appear in the request.

The request header values are not pre-processed and retain the original case used in the request.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



When the HTTP request contains too many headers, this field may not contain all of the headers sent in the HTTP request. In this situation, the [`http.request.headers.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/) field will be set to `true`.

Example value:
    
    
    {"content-type": ["application/json"]}

Example usage:
    
    
    any(http.request.headers["content-type"][*] == "application/json")

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
