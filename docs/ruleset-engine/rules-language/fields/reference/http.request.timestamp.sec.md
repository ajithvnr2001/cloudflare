---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/
title: http.request.timestamp.sec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.133848+00:00
---

# http.request.timestamp.sec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Timestamp.Sec



# http.request.timestamp.sec

`http.request.timestamp.sec``Integer`

The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.

The field value is 10 digits long.

When validating HMAC tokens in an expression, pass this field as the `currentTimestamp` argument to the [`is_timed_hmac_valid_v0()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hmac-validation) validation function.

To obtain the timestamp milliseconds, use the [`http.request.timestamp.msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/) field.

Example value:
    
    
    1484063137

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
