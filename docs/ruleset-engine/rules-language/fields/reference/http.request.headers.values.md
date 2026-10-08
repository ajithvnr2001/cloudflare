---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/
title: http.request.headers.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:10.835439+00:00
---

# http.request.headers.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Headers.Values



# http.request.headers.values

`http.request.headers.values``Array<String>`

The values of the headers in the HTTP request.

The values are not pre-processed and retain the original case used in the request.

The order of header values is not guaranteed but will match [`http.request.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/).

Duplicate headers are listed multiple times.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



When the HTTP request contains too many headers, this field may not contain the values of all of the headers sent in the HTTP request. In this situation, the [`http.request.headers.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/) field will be set to `true`.

**Note** : In HTTP/2, the names of HTTP headers are always in lowercase. Recent versions of the `curl` tool [enable HTTP/2 by default](https://curl.se/docs/manpage.html#--http2) for HTTPS connections.

Example value:
    
    
    Example 1: ["application/json"]
    Example 2: ["This header value is longer than 10 bytes"]

Example usage:
    
    
    # Example 1: Check for specific header value.
    any(http.request.headers.values[*] == "application/json")
    
    # Example 2: Match requests according to the specified operator and the length/size entered for the header value.
    any(len(http.request.headers.values[*])[*] gt 10)

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
