---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/
title: Rewrite path of moved section of a website \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.947736+00:00
---

# Rewrite path of moved section of a website · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite path of moved section of a website



# Rewrite path of moved section of a website

Create a URL rewrite rule (part of Transform Rules) to rewrite everything under `/blog/<PATH>` to `/marketing/<PATH>`.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-moved-section/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To rewrite everything under `/blog/<PATH>` to `/marketing/<PATH>`, create a new URL rewrite rule and define a dynamic URL path rewrite using [wildcard pattern parameters](https://developers.cloudflare.com/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters):

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `https://<YOUR_HOSTNAME>/blog/*`



**Then rewrite the path and/or query**

  * **Target path** : [`/`] `blog/*`
  * **Rewrite to** : [`/`] `marketing/${1}`



Make sure to replace `<YOUR_HOSTNAME>` with your actual hostname and adjust the example paths according to your setup.

[PreviousRewrite path of archived blog posts](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-archived-posts/)[NextRewrite URL query string](https://developers.cloudflare.com/rules/transform/examples/rewrite-url-string-visitors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-moved-section.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
