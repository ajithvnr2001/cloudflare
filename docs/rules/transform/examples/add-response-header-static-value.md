---
url: https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/
title: Add a response header with a static value \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.872451+00:00
---

# Add a response header with a static value · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Add a response header with a static value



# Add a response header with a static value

Create a response header transform rule to add a `set-cookie` HTTP header to the response with a static value (`cookiename=value`).

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule adds a header named `set-cookie` with a static value (`cookiename=value`) to the HTTP response:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/en/")

Selected operation under **Modify response header** : _Add_

**Header name** : `set-cookie`

**Value** : `cookiename=value`

This rule would keep any existing `set-cookie` headers already present in the HTTP response.

[PreviousAdd a request header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/)[NextAdd a wildcard CORS response header](https://developers.cloudflare.com/rules/transform/examples/add-cors-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/add-response-header-static-value.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
