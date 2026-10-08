---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/
title: http.request.headers.names \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:11.044810+00:00
---

# http.request.headers.names · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Headers.Names



# http.request.headers.names

`http.request.headers.names``Array<String>`

The names of the headers in the HTTP request.

The names are not pre-processed and retain the original case used in the request.

The order of header names is not guaranteed but will match [`http.request.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/).

Duplicate headers are listed multiple times.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



When the HTTP request contains too many headers, this field may not contain the names of all of the headers sent in the HTTP request. In this situation, the [`http.request.headers.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/) field will be set to `true`.

**Note** : In HTTP/2, the names of HTTP headers are always in lowercase. Recent versions of the `curl` tool [enable HTTP/2 by default](https://curl.se/docs/manpage.html#--http2) for HTTPS connections.

Example value:
    
    
    ["content-type"]

Example usage:
    
    
    any(http.request.headers.names[*] == "content-type")

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
