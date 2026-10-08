---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/
title: http.request.timestamp.msec \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:12.068142+00:00
---

# http.request.timestamp.msec · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Timestamp.Msec



# http.request.timestamp.msec

`http.request.timestamp.msec``Integer`

The millisecond when Cloudflare received the request, between 0–999.

To obtain the complete timestamp, use both [`http.request.timestamp.sec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/) and [`http.request.timestamp.msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/) fields.

Example value:
    
    
    857

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
