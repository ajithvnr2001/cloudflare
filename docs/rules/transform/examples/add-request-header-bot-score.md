---
url: https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/
title: Add a request header with the current bot score \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.521887+00:00
---

# Add a request header with the current bot score · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Add a request header with the current bot score



# Add a request header with the current bot score

Create a request header transform rule to add a `X-Bot-Score` HTTP header to the request with the current bot score.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/add-request-header-bot-score/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following request header transform rule adds a header named `X-Bot-Score` with the current bot score to the HTTP request:

Text in **Expression Editor** :
    
    
    starts_with(http.request.uri.path, "/en/")

Selected operation under **Modify request header** : _Set dynamic_

**Header name** : `X-Bot-Score`

**Value** : `to_string(cf.bot_management.score)`

[PreviousAdd a request header for subrequests from other zones](https://developers.cloudflare.com/rules/transform/examples/add-request-header-subrequest-other-zone/)[NextAdd a response header with a static value](https://developers.cloudflare.com/rules/transform/examples/add-response-header-static-value/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/add-request-header-bot-score.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
