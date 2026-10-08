---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/
title: Rewrite image paths with several URL segments \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.238925+00:00
---

# Rewrite image paths with several URL segments · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite image paths with several URL segments



# Rewrite image paths with several URL segments

Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/images/<FOLDER1>/<FOLDER2>/<FILENAME>` to `/img/<FILENAME>`.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite paths like `/images/<FOLDER1>/<FOLDER2>/<FILENAME>` — where `<FOLDER1>`, `<FOLDER2>`, and `<FILENAME>` can vary — to `/img/<FILENAME>`, create a URL rewrite rule with a dynamic rewrite of the path component:

Text in **Expression Editor** :
    
    
    http.request.uri.path ~ "^/images/[^/]+/[^/]+/[^/]+$"

Text after **Path** > **Rewrite to** > _Dynamic_ :
    
    
    regex_replace(http.request.uri.path, "^/images/[^/]+/[^/]+/(.+)$", "/img/${1}")

For example, this rule would rewrite the `/images/nature/animals/tiger.png` path to `/img/tiger.png`.

[PreviousRewrite blog archive URLs](https://developers.cloudflare.com/rules/transform/examples/rewrite-archive-urls-new-format/)[NextRewrite page path for visitors in specific countries](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-several-url-different-url.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
