---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri/
title: raw.http.request.uri \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:29.770420+00:00
---

# raw.http.request.uri · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Uri



# raw.http.request.uri

`raw.http.request.uri``String`

The URI path and query string of the request without any transformation.

This is the raw field version of the [`http.request.uri`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note** : This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
