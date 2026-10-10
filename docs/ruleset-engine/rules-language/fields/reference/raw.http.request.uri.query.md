---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/
title: raw.http.request.uri.query \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:29.815452+00:00
---

# raw.http.request.uri.query · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Uri.Query



# raw.http.request.uri.query

`raw.http.request.uri.query``String`

The entire query string without the `?` delimiter and without any transformation.

This is the raw field version of the [`http.request.uri.query`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.query/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note** : This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
