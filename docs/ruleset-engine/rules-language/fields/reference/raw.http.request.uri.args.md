---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args/
title: raw.http.request.uri.args \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:29.965988+00:00
---

# raw.http.request.uri.args · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Uri.Args



# raw.http.request.uri.args

`raw.http.request.uri.args``Map<Array<String>>`

The raw HTTP URI arguments associated with a request represented as a Map (associative array).

This is the raw field version of the [`http.request.uri.args`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
