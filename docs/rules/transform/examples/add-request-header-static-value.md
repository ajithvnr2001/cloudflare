---
url: https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/
title: Add request header with a static value \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.556214+00:00
---

# Add request header with a static value · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Add request header with a static value



# Add request header with a static value

Create a request header transform rule to add an `X-Source` HTTP header to the request with a static value (`Cloudflare`).

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-request-header-static-value/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule adds a header named `X-Source` with a static value (`Cloudflare`) to the HTTP request:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/en/")

Selected operation under **Modify request header** : _Set static_

**Header name** : `X-Source`

**Value** : `Cloudflare`

[PreviousAdd a wildcard CORS response header](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/)[NextNormalize encoded slashes in URL path](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/add-request-header-static-value.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
