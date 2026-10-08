---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/
title: Rewrite path of archived blog posts \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.032431+00:00
---

# Rewrite path of archived blog posts · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite path of archived blog posts



# Rewrite path of archived blog posts

Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/news/2012/...` URI paths to `/archive/news/2012/...`.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite all requests to `/news/2012/...` to `/archive/news/2012/...` you must add a reference to the content of the original URL. Create a new URL rewrite rule and define a dynamic URL path rewrite using [wildcard pattern parameters](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters):

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `https://<YOUR_HOSTNAME>/news/2012/*`



**Then rewrite the path and/or query**

  * **Target path** : [`/`] `news/2012/*`
  * **Rewrite to** : [`/`] `archive/news/2012/${1}`



Make sure to replace `<YOUR_HOSTNAME>` with your actual hostname and adjust the example paths according to your setup.

[PreviousRewrite path for object storage bucket](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/)[NextRewrite path of moved section of a website](https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-path-archived-posts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
