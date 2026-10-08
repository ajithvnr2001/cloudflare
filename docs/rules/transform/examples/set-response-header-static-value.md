---
url: https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/
title: Set response header with a static value \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.626731+00:00
---

# Set response header with a static value · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Set response header with a static value



# Set response header with a static value

Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response to a static value (`Cloudflare`).

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule sets a header named `X-Source` to a static value (`Cloudflare`) in the HTTP response:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/en/")

Selected operation under **Modify response header** : _Set static_

**Header name** : `X-Source`

**Value** : `Cloudflare`

This rule would overwrite any existing `X-Source` headers already present in the HTTP response.

[PreviousSet a response header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/)[NextOverview](https://developers.cloudflare.com/rules/url-forwarding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/set-response-header-static-value.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
