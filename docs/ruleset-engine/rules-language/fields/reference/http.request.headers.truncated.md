---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/
title: http.request.headers.truncated \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.834207+00:00
---

# http.request.headers.truncated · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Headers.Truncated



# http.request.headers.truncated

`http.request.headers.truncated``Boolean`

Indicates whether the HTTP request contains too many headers.

When `true`, [`http.request.headers`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/), [`http.request.headers.names`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/), and [`http.request.headers.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.values/) may not contain all of the headers sent in the HTTP request.

Categories: 

  * Request
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
