---
url: https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/
title: AI Gateway consolidates monthly usage invoice line items and standardizes model names \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:11.968639+00:00
---

# AI Gateway consolidates monthly usage invoice line items and standardizes model names · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 1, 2026

## AI Gateway consolidates monthly usage invoice line items and standardizes model names

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.

For example, an invoice that previously included these separate line items:

  * `anthropic claude-haiku-4-5-20251001 Input Tokens`: 40,000 tokens at $0.000001 ($0.04)
  * `anthropic claude-haiku-4-5-20251001 Output Tokens`: 24,000 tokens at $0.000005 ($0.12)



The updated invoice includes one line item: `anthropic/claude-haiku-4.5`: $0.16.

AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent `provider/model` identifier.

For more information, refer to the [Unified Billing documentation](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) and [AI Gateway logging documentation](https://developers.cloudflare.com/ai-gateway/observability/logging/).
