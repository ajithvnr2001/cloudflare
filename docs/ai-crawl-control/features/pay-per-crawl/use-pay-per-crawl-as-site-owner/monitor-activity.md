---
url: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/
title: Monitor activity \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.847056+00:00
---

# Monitor activity · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /…

FeaturesPay Per Crawl

  4. /Use pay per crawl as a site owner
  5. /Monitor activity



# Monitor activity

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView crawler activityAdditional considerations Robots.txt management Ongoing optimizationAdditional resources
    
    
    graph LR
    A[Enable in<br>account settings] --> B[Set a pay per <br/>crawl price ]
    B --> C[Select crawlers<br>to charge]
    C --> D[Monitor<br>activity]:::highlight
    D --> E[Manage<br>payouts]
    classDef highlight fill:#F6821F,color:white
    
    click A "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/"
    click B "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/"
    click C "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/"
    click E "/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/"
    

After configuring pay per crawl, monitor crawler activity to understand how AI crawlers interact with your content, and track your earnings.

## View crawler activity

  1. Go to **AI Crawl Control**.

[ Go to **AI Crawl Control** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ai)
  2. Go to the **Metrics** tab to view detailed analytics.




The metrics help you understand:

  * Which crawlers are accessing your content
  * How often they are being charged
  * Request patterns and trends
  * Robots.txt violations



For detailed information about available metrics, refer to [View AI Crawl Control metrics](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/#view-the-metrics-tab).

Balance visibility

Your accrued earnings balance is not currently visible in the dashboard. You can request balance updates from your Cloudflare team.

## Additional considerations

### Robots.txt management

Consider updating your `robots.txt` file to clearly indicate which pages should remain off-limits, even if AI crawlers are willing to pay for access.

### Ongoing optimization

Do the following to ensure you are using pay per crawl most effectively:

  * Review crawler activity regularly to identify patterns
  * Adjust pricing based on demand and content value
  * Modify crawler actions (charge, allow, block) as needed
  * Monitor for any unusual or unwanted crawler behavior



## Additional resources

  * [Pay Per Crawl FAQs](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/faq)
  * [Analyze AI traffic](https://developers.cloudflare.com/ai-crawl-control/features/analyze-ai-traffic/)



[PreviousSelect crawlers to charge](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/)[NextManage payouts](https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
