---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers/
title: http.response.headers \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.851547+00:00
---

# http.response.headers · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Response.Headers



# http.response.headers

`http.response.headers``Map<Array<String>>`

The HTTP response headers represented as a Map (or associative array).

When there are repeating headers, the array includes them in the order they appear in the response. The keys convert to lowercase.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



**Note** : The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Example value:
    
    
    {"server": ["nginx"]}

Example usage:
    
    
    any(http.response.headers["server"][*] == "nginx")

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
