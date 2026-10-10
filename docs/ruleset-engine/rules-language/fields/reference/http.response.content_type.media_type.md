---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/
title: http.response.content_type.media_type \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:31.650871+00:00
---

# http.response.content_type.media_type · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Response.Content_type.Media_type



# http.response.content_type.media_type

`http.response.content_type.media_type``String`

The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's `Content-Type` header.

The field value will not include parameters such as `charset`.

Example values:

Content-Type header | Field value  
---|---  
`text/html` | `"text/html"`  
`text/html; charset=utf-8` | `"text/html"`  
`text/html+extra` | `"text/html+extra"`  
`text/html+extra; charset=utf-8` | `"text/html+extra"`  
`text/HTML` | `"text/html"`  
`text/html; charset=utf-8; other=value` | `"text/html"`  
  
**Note** : The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
