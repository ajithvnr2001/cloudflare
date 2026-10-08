---
url: https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/
title: Set a response header with the current bot score \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:57.153163+00:00
---

# Set a response header with the current bot score · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Set a response header with the current bot score



# Set a response header with the current bot score

Create a response header transform rule (part of Transform Rules) to set an `X-Bot-Score` HTTP header in the response with the current bot score.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following response header transform rule sets a header named `X-Bot-Score` to the current bot score in the HTTP response:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/en/")

Selected operation under **Modify response header** : _Set dynamic_

**Header name** : `X-Bot-Score`

**Value** : `to_string(cf.bot_management.score)`

This rule would overwrite any existing `X-Bot-Score` headers already present in the HTTP response.

[PreviousRewrite URL query string](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/)[NextSet response header with a static value](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/set-response-header-bot-score.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
