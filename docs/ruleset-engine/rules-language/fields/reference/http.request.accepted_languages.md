---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/
title: http.request.accepted_languages \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:09.500745+00:00
---

# http.request.accepted_languages · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.accepted_languages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Accepted_languages



# http.request.accepted_languages

`http.request.accepted_languages``Array<String>`

List of language tags provided in the [`Accept-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language) HTTP request header.

Language tags are sorted by weight (`;q=<weight>`, with a default weight of `1`) in descending order.

If the HTTP header is not present in the request or is empty, `http.request.accepted_languages[0]` will return a "[missing value](https://developers.cloudflare.com/ruleset-engine/rules-language/values/#notes)", which the [`concat()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) function will handle as an empty string.

If the HTTP header includes the language tag `*` it will not be stored in the array.

**Note** : This field is only available in [Transform Rules](https://developers.cloudflare.com/rules/transform/).

Example usage:
    
    
    # Example 1: Request with header "Accept-Language: fr-CH, fr;q=0.8, en;q=0.9, de;q=0.7, *;q=0.5".
    # In this case:
    http.request.accepted_languages[0] ==> "fr-CH"
    http.request.accepted_languages    ==> ["fr-CH", "en", "fr", "de"]
    
    # Example 2: Request without an `Accept-Language` HTTP header and a URI of "https://www.example.com/my-path".
    # In this case:
    concat("/", http.request.accepted_languages[0], http.request.uri.path) ==> "//my-path"

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
