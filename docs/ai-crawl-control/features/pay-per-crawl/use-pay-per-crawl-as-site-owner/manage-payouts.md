---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/
title: Manage payouts \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.795669+00:00
---

# Manage payouts · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as a site owner
  5. /Manage payouts



# Manage payouts

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a new Stripe accountBilling lifecycle Limitations
    
    
    graph LR
    A[Enable in<br>account settings] --> B[Set a pay per <br/>crawl price ]
    B --> C[Select crawlers<br>to charge]
    C --> D[Monitor<br>activity]
    D --> E[Manage<br>payouts]:::highlight
    classDef highlight fill:#F6821F,color:white
    
    click A "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/"
    click B "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/"
    click C "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/"
    click D "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/"
    

When you're ready to receive payments for your accrued crawler activity, connect your Cloudflare account to Stripe. This step can be completed at any time after enabling pay per crawl.

## Create a new Stripe account

A person with **Administrator** or **Super Administrator** access must set up the Stripe connection:

  1. In the Cloudflare dashboard, go to **Manage Account** > **Settings**.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Select **Pay Per Crawl**.

  3. In the **Stripe account** section, select **Connect**.

  4. Select **Continue to Stripe**.

  5. Complete Stripe's onboarding process, including:

     * Basic business information
     * Bank account details for payouts



Pay Per Crawl Stripe account required

You must create a dedicated Cloudflare Stripe Connect account through the dashboard. Pre-existing Stripe accounts are not compatible with this feature.

## Billing lifecycle

Cloudflare manages the complete billing lifecycle:

  1. **Charge initiation** : AI crawlers indicate payment intent via request headers
  2. **Charge recording** : A charge event is recorded upon successful content delivery (HTTP 200 response)
  3. **Aggregation** : Cloudflare aggregates and reconciles all recorded charges
  4. **Payout** : Monthly payments to publishers in good standing



### Limitations

  * Your accrued balance is not currently visible in the dashboard. You can request balance updates from your Cloudflare team.
  * Payouts are subject to settlement periods and minimum payout thresholds.



[PreviousMonitor activity](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/)[NextAdvanced configuration](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
