---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form/
title: http.request.body.form \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.169348+00:00
---

# http.request.body.form · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.form/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Body.Form



# http.request.body.form

`http.request.body.form``Map<Array<String>>`

The HTTP request body of a form represented as a Map (or associative array).

Populated when the `Content-Type` header is `application/x-www-form-urlencoded`.

The values are not pre-processed and retain the original case used in the request.

When a field repeats, then the array contains multiple items in the order they are in the request.

The return value may be truncated if [`http.request.body.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated) is `true`.

  * **Decoding** : No decoding performed
  * **Whitespace** : Preserved
  * **Non-ASCII** : Preserved



Requires a Cloudflare Enterprise plan.

Example value:
    
    
    {username": ["admin"]}

Example usage:
    
    
    any(http.request.body.form["username"][*] == "admin")

Caution

All `http.request.body.*` fields (except [ `http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/)) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default — reach out to your account team or to Cloudflare Support to increase the limit. For users in the Free plan, the limit is 1 MB.

You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, the body fields will contain a truncated value and the [`http.request.body.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/) field will be set to `true`. The [`http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/) field will contain the full size of the request without any truncation.

The maximum body size applies only to the values of HTTP body fields — the origin server will still receive the complete request body.

Categories: 

  * Request
  * Body



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
