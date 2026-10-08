---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path/
title: raw.http.request.uri.path \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:14.236795+00:00
---

# raw.http.request.uri.path · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.path/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Uri.Path



# raw.http.request.uri.path

`raw.http.request.uri.path``String`

The raw URI path of the request without any transformation.

This is the raw field version of the [`http.request.uri.path`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note** : This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
