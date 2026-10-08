---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/
title: Error codes \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.008134+00:00
---

# Error codes · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as an AI owner
  5. /Error codes



# Error codes

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Pay per crawl error responses include a `crawler-error` header with a specific error code. The following table provides a complete reference of all possible error codes:

Error Code | HTTP Status | What to do  
---|---|---  
`CrawlerForbidden` | 403 | The site owner has blocked your crawler. You cannot access this content.  
`StrongAuthRequired` | 400 | Include valid Web Bot Auth headers with strong authentication in your request.  
`InvalidSignature` | 400 | Include both `signature-input` and `signature` headers in your request. Refer to [Web Bot Auth documentation](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/).  
`InvalidCrawlerPriceValue` | 400 | Check that your `crawler-exact-price` or `crawler-max-price` header value is properly formatted (for example, `USD 0.01`).  
`MissingCrawlerPrice` | 402 | Include either `crawler-exact-price` or `crawler-max-price` header in your request.  
`PaymentFailed` | 403 | Verify your payment processing is configured correctly in Pay Per Crawl settings. Contact Cloudflare support if the issue persists.  
`InvalidCrawlerExactPrice` | 402 | Update your `crawler-exact-price` to match the `crawler-price` value from the response header.  
`InvalidCrawlerMaxPrice` | 402 | Increase your `crawler-max-price` to meet or exceed the `crawler-price` value from the response header.  
`ConflictingPriceHeaders` | 400 | Use only one price header per request. Remove either `crawler-max-price` or `crawler-exact-price`.  
`InvalidContentPrice` | 502 | The origin returned an invalid price. This is a site owner configuration issue. Try again later or contact the site owner.  
`InternalError` | 500 | A server error occurred. Retry your request with exponential backoff.  
  
[PreviousCrawl pages](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/)[NextPay Per Crawl FAQ](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
