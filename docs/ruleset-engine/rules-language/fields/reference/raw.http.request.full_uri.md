---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.full_uri/
title: raw.http.request.full_uri \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:13.874668+00:00
---

# raw.http.request.full_uri · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.full_uri/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Request.Full_uri



# raw.http.request.full_uri

`raw.http.request.full_uri``String`

The raw full URI as received by the web server without any transformation.

The value will not include the `#fragment` part, which is not sent to web servers.

This is the raw field version of the [`http.request.full_uri`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.full_uri/) field. Raw fields, prefixed with `raw.`, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.

**Note** : This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.

Categories: 

  * Request
  * URI
  * Raw fields



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
