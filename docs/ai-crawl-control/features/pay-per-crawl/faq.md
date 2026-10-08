---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/faq/
title: Pay Per Crawl FAQ \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:25.885714+00:00
---

# Pay Per Crawl FAQ · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

Features

  4. /Pay Per Crawl
  5. /Pay Per Crawl FAQ



# Pay Per Crawl FAQ

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFrequently asked questions for site owners Can I set different prices for different AI crawlers?Frequently asked questions for AI bot operators Will I be charged for re-crawling the same page? Am I charged for error responses? What user agent should I use?

## Frequently asked questions for site owners

### Can I set different prices for different AI crawlers?

No. Pay per crawl allows you to configure different actions (Block, Charge, or Allow) for each crawler, but you can only set a single price that applies to all crawlers configured with the "Charge" option.

## Frequently asked questions for AI bot operators

### Will I be charged for re-crawling the same page?

Yes. Every time your AI crawler accesses content on a website protected with pay per crawl, it will incur the cost set by the site owner. You should implement mechanisms within your crawler to track expenditure and enforce any spending limits you want to set.

Some paths are always free to crawl. These paths are: `/robots.txt`, `/sitemap.xml`, `/security.txt`, `/.well-known/security.txt`, `/crawlers.json`.

### Am I charged for error responses?

No. Charging events are only triggered for successful HTTP response codes. Error responses are not billed, even if you have sent the `crawler-exact-price` or `crawler-max-price` headers.

### What user agent should I use?

Use the standard user agents associated with your AI crawler that you have onboarded to Cloudflare and identified through Web Bot Auth.

[PreviousError codes](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/)[NextAI Crawl Control with Cloudflare WAF](https://developers.cloudflare.com/ai-crawl-control/configuration/ai-crawl-control-with-waf/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
