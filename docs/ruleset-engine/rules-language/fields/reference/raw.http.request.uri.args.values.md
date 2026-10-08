---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args.values/
title: raw.http.request.uri.args.values \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:14.004402+00:00
---

# raw.http.request.uri.args.values · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.args.values/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Uri.Args.Values



# raw.http.request.uri.args.values

`raw.http.request.uri.args.values``Array<String>`

The raw values of arguments in the HTTP URI query string.

This is the raw field version of the [`http.request.uri.args.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
