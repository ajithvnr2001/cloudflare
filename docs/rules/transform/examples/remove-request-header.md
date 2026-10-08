---
url: https://developers.cloudflare.com/rules/transform/examples/remove-request-header/
title: Remove a request header \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.912459+00:00
---

# Remove a request header · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/remove-request-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Remove a request header



# Remove a request header

Create a request header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the request.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule removes the `cf-connecting-ip` header from the HTTP request:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/private/")

Selected operation under **Modify request header** : _Remove_

**Header name** : `cf-connecting-ip`

[PreviousNormalize encoded slashes in URL path](https://developers.cloudflare.com/rules/transform/examples/normalize-encoded-slash/)[NextRemove a response header](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/remove-request-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
