---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/
title: Set a pay per crawl price \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:27.303051+00:00
---

# Set a pay per crawl price · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as a site owner
  5. /Set a pay per crawl price



# Set a pay per crawl price

Last updated Jul 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    graph LR
    A[Enable in<br>account settings] --> B[Set a pay per <br/>crawl price ]:::highlight
    B --> C[Select crawlers<br>to charge]
    C --> D[Monitor<br>activity]
    D --> E[Manage<br>payouts]
    classDef highlight fill:#F6821F,color:white
    
    click A "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/"
    click C "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/"
    click D "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/"
    click E "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/"
    

Once your domain's visibility is set to **Visible** in Account Settings, you can set a pay per crawl price and enable pay per crawl for that domain.

  1. Go to **AI Crawl Control**.

[ Go to **AI Crawl Control** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ai)
  2. Go to the **Payments** tab.

  3. In the **Pay Per Crawl** card, select **Enable**.

  4. Set your default per crawl price. This is the amount charged for each successful content retrieval (HTTP 200 response) by an AI crawler.

     * (Optional) To set different prices for different content, select **Enable dynamic pricing**. Refer to [Advanced configuration](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/) for details.
  5. Select **Save**.




After enabling and setting a price, the domain's status in Account Settings will change to **Enabled**.

Pricing considerations

The minimum price is $0.001 USD per crawl. Consider your content value and expected crawler volume when setting your price.

[PreviousEnable in account settings](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/)[NextSelect crawlers to charge](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
