---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/
title: http.request.body.size \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:32.921739+00:00
---

# http.request.body.size · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Body.Size



# http.request.body.size

`http.request.body.size``Number`

The total size of the HTTP request body (in bytes).

This field may have a value larger than the one returned by `len(http.request.body.raw)`, since the [`http.request.body.raw`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/) field only considers the request body up to a maximum size that varies according to your Cloudflare plan.

Requires a Cloudflare Enterprise plan.

Categories: 

  * Request
  * Body



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
