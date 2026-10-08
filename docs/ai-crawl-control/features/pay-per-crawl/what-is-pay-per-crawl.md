---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/
title: What is Pay Per Crawl? \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.946902+00:00
---

# What is Pay Per Crawl? · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

Features

  4. /Pay Per Crawl
  5. /What is Pay Per Crawl?



# What is Pay Per Crawl?

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is Pay Per Crawl?Additional resources

Pay per crawl beta

Pay per crawl is currently in closed beta.

To find out how to join the beta program, reach out to us at [Pay per crawl signup ↗︎](https://www.cloudflare.com/paypercrawl-signup/), or contact your account executive if you are an existing Enterprise customer.

To learn more about pay per crawl, refer to Cloudflare blog: [Introducing pay per crawl: enabling content owners to charge AI crawlers for access ↗︎](https://blog.cloudflare.com/introducing-pay-per-crawl/).

AI crawlers often consume vast amounts of web content. Some provide mutual benefit to content owners by indexing content for search engines, but others engage in activities such as content scraping without permission.

The resulting landscape leaves content owners with limited options for managing AI crawlers or receiving compensation for automated access to their intellectual property.

## What is Pay Per Crawl?

Pay per crawl is a feature of AI Crawl Control that enables site owners to control and monetize AI crawler access to content by setting a price per zone.

Each time an AI crawler requests content, they either present payment intent via request headers for successful `HTTP 200` access, or receive an `HTTP 402 Payment Required` response with pricing. Cloudflare acts as the Merchant of Record for pay per crawl and also provides the underlying technical infrastructure.

Note

If you block an AI crawler from a zone via either of Cloudflare's [WAF](https://developers.cloudflare.com/waf/) or [Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) products, those products' rulesets will override pay per crawl's "charge" feature, and the blocked crawler will not have access to the zone.

Ultimately, pay per crawl enables:

  * Site owners to take control of their content, and charge a fee every time an AI crawler accesses a page in their [Cloudflare zone](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones). For more details, refer to [use pay per crawl as a site owner](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/).
  * AI crawler owners to pay to access content on sites protected by pay per crawl. For more details, refer to [use pay per crawl as an AI owner](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/).

![Pay per crawl components](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2400,height=1122,format=webp/_astro/ai-crawl-control-pay-per-crawl-diagram.51Dvd0Od.png)

## Additional resources

Refer to the following resources.

  * [Use pay per crawl as a site owner](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/).
  * [Use pay per crawl as an AI owner](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/set-up-cloudflare-account/).
  * [AI Crawl Control with Cloudflare WAF](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-waf/).
  * [AI Crawl Control with Cloudflare Bots](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-bots/).



[PreviousDirectives](https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/)[NextEnable in account settings](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
