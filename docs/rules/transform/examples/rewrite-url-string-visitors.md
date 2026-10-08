---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/
title: Rewrite URL query string \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.184460+00:00
---

# Rewrite URL query string · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite URL query string



# Rewrite URL query string

Create a transform rule to rewrite the request path from `/blog` to `/blog?sort-by=date`.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite a request to the `/blog` path to `/blog?sort-by=date`, create a URL rewrite rule with the following settings:

Text in **Expression Editor** :
    
    
    http.request.uri.path == "/blog"

Text after **Query** > **Rewrite to** > _Static_ :
    
    
    sort-by=date

Additionally, set the path rewrite action of the same rule to _Preserve_ so that the URL path does not change.

[PreviousRewrite path of moved section of a website](https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/)[NextSet a response header with the current bot score](https://developers.cloudflare.com/rules/transform/examples/set-response-header-bot-score/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-url-string-visitors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
