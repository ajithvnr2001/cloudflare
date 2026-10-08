---
url: https://developers.cloudflare.com/rules/transform/examples/remove-response-header/
title: Remove a response header \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.983546+00:00
---

# Remove a response header · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/remove-response-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Remove a response header



# Remove a response header

Create a response header transform rule (part of Transform Rules) to remove the `cf-connecting-ip` HTTP header from the response.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/remove-response-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule removes the `cf-connecting-ip` header from the HTTP response:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/private/")

Selected operation under **Modify response header** : _Remove_

**Header name** : `cf-connecting-ip`

[PreviousRemove a request header](https://developers.cloudflare.com/rules/transform/examples/remove-request-header/)[NextRewrite blog archive URLs](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/remove-response-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
