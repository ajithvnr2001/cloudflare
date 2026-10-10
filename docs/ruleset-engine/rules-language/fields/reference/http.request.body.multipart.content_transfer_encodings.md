---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.content_transfer_encodings/
title: http.request.body.multipart.content_transfer_encodings \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:37:33.068695+00:00
---

# http.request.body.multipart.content_transfer_encodings · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.content_transfer_encodings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Body.Multipart.Content_transfer_encodings



# http.request.body.multipart.content_transfer_encodings

`http.request.body.multipart.content_transfer_encodings``Array<Array<String>>`

List of `Content-Transfer-Encoding` headers for each part in the multipart body.

Requires a Cloudflare Enterprise plan.

Example value:
    
    
    [["quoted-printable"], ["base64"]]

Example usage:
    
    
    any(http.request.body.multipart.content_transfer_encodings[*][0] == "binary")

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
