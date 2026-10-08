---
url: https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/
title: Normalize encoded slashes in URL path \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.303282+00:00
---

# Normalize encoded slashes in URL path · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Normalize encoded slashes in URL path



# Normalize encoded slashes in URL path

Create a URL rewrite rule (part of Transform Rules) to normalize encoded forward slashes (`%2F`) in the request path to standard slashes (`/`).

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow to normalize %2F

Different web servers and applications handle encoded forward slashes (`%2F`) in URLs differently. Cloudflare follows [RFC 3986 ↗︎](https://datatracker.ietf.org/doc/html/rfc3986), which specifies that `%2F` **should not** be automatically normalized to `/` because `/` is a reserved character in URLs, and decoding it might change the intended meaning of the path.

However, many origin servers **do** automatically decode `%2F` into `/` when processing requests. If your origin server behaves this way, you may want to apply the same normalization at Cloudflare’s edge to ensure consistency in request handling, rule evaluation, and logging.

## How to normalize `%2F`

To normalize encoded forward slashes (`%2F`) to standard slashes (`/`) in the request path before [subsequent](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) rule evaluation, create a new URL rewrite rule and define a dynamic URL path rewrite using [`url_decode()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#url_decode) function:

Text in **Expression Editor** :
    
    
    (lower(raw.http.request.full_uri) wildcard "*%2f*")

Text after **Path** > **Rewrite to** > _Dynamic_ :
    
    
    url_decode(http.request.uri.path)

This transformation ensures that `%2F` is always treated as `/` in the request path. This is particularly useful when setting up rules that depend on URL path matching, as it prevents discrepancies caused by differing normalization behaviors.

[PreviousAdd request header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/)[NextRemove a request header](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/normalize-encoded-slash.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
