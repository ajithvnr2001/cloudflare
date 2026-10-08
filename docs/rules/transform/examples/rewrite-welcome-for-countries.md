---
url: https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/
title: Rewrite page path for visitors in specific countries \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:56.568000+00:00
---

# Rewrite page path for visitors in specific countries · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)

  4. /[Examples](https://developers.cloudflare.com/rules/transform/examples/)
  5. /Rewrite page path for visitors in specific countries



# Rewrite page path for visitors in specific countries

Create two URL rewrite rules (part of Transform Rules) to rewrite the path of the welcome page for visitors in specific countries.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/examples/rewrite-welcome-for-countries/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To have a welcome page in two languages, create two URL rewrite rules with a static rewrite of the path component:

**URL rewrite rule #1**

Text in **Expression Editor** :
    
    
    http.request.uri.path == "/welcome.html" && ip.src.country == "GB"

Text after **Path** > **Rewrite to** > _Static_ :
    
    
    /welcome-gb.html

**URL rewrite rule #2**

Text in **Expression Editor** :
    
    
    http.request.uri.path == "/welcome.html" && ip.src.country == "PT"

Text after **Path** > **Rewrite to** > _Static_ :
    
    
    /welcome-pt.html

[PreviousRewrite image paths with several URL segments](https://developers.cloudflare.com/rules/transform/examples/rewrite-several-url-different-url/)[NextRewrite path for object storage bucket](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/examples/rewrite-welcome-for-countries.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
