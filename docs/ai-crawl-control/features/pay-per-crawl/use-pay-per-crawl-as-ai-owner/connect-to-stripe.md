---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/connect-to-stripe/
title: Connect Stripe \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.122387+00:00
---

# Connect Stripe · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/connect-to-stripe/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as an AI owner
  5. /Connect Stripe



# Connect Stripe

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/connect-to-stripe/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBilling
    
    
    graph LR
    A[Set up your<br>Cloudflare Account] --> B[Verify your<br>AI crawler]
    B --> C[Discover<br>payable content]
    C --> D[Connect to<br>Stripe]:::highlight
    D --> E[Crawl pages]
    classDef highlight fill:#F6821F,color:white
    

Connect your Cloudflare account to Stripe to process payments. Pay per crawl uses Stripe to process payments between AI crawler owners and site owners.

  1. In the Cloudflare dashboard, go to **Manage Account** > **Settings**.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to the **Pay Per Crawl** tab.

  3. From **Connect to Stripe** , select **Connect**.

  4. Select **Continue to Stripe**.

  5. Follow the on-screen instructions to connect your Cloudflare account to a Stripe account.

Use a non-personal email address

Cloudflare recommends using a dedicated email to manage your pay per crawl account (for example, `aicrawler@company.com`).




When you successfully connect Stripe to your account, you will see a green tick ✅ next to **Stripe connection**.

Spending limits

Cloudflare is not responsible for configuring spending limits. Ensure you have configured a maximum spending limit on your AI crawler.

## Billing

Charges are recorded upon successful delivery of content that is requested with valid [crawler price headers](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#21-include-payment-headers).

Invoices are created and managed via Stripe. Crawlers are responsible for setting and enforcing their own spending limits.

[PreviousVerify your AI crawler](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/)[NextDiscover payable content](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/connect-to-stripe.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
