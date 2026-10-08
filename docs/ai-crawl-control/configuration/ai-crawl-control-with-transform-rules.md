---
url: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-transform-rules/
title: AI Crawl Control with Transform Rules \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:25.624271+00:00
---

# AI Crawl Control with Transform Rules · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-transform-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /Configuration
  4. /AI Crawl Control with Transform Rules



# AI Crawl Control with Transform Rules

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-transform-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExample: Add licensing terms to blocked responses

Use [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) to add `Link` headers to crawler responses — even when those crawlers are blocked. This lets you communicate terms of use or [RSL ↗︎](https://rslstandard.org/) license information.

## Example: Add licensing terms to blocked responses

**Expression:**
    
    
    (cf.bot_management.verified_bot and http.response.code eq 403)

**Header modification:**

  * **Operation:** Set static
  * **Header name:** `Link`
  * **Value:** `<https://example.com/ai-licensing-terms>; rel="license"; type="text/html"`



For more details, refer to [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/).

[PreviousAI Crawl Control with Cloudflare Bots](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/)[NextGraphQL API](https://developers.cloudflare.com/ai-crawl-control/reference/graphql-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/configuration/ai-crawl-control-with-transform-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
