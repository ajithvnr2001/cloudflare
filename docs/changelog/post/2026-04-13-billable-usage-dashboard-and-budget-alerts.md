---
url: https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/
title: Introducing Billable Usage dashboard and Budget alerts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.746136+00:00
---

# Introducing Billable Usage dashboard and Budget alerts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 21, 2026

## Introducing Billable Usage dashboard and Budget alerts

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.

#### Billable Usage dashboard

The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.

The dashboard displays:

  * A bar chart showing daily usage charges for your billing period
  * A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs
  * Ability to view previous billing periods



Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.

To access the dashboard, go to **Manage Account** > **Billing** > **Billable Usage**.

![Screenshot of the Billable Usage dashboard in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1033,height=757,format=webp/_astro/billable-usage-dashboard.CQvMdtrp.png)

#### Budget alerts

Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.

To configure a budget alert:

  1. Go to **Manage Account** > **Billing** > **Billable Usage**.
  2. Select **Set Budget Alert**.
  3. Enter a budget threshold amount greater than $0.
  4. Select **Create**.



Alternatively, configure alerts via **Notifications** > **Add** > **Budget Alert**.

![Create Budget Alert modal in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=315,height=374,format=webp/_astro/budget-alert-modal.BjIzGOLV.png)

You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.

Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.

For more information, refer to the [Usage based billing documentation](https://developers.cloudflare.com/billing/understand/usage-based-billing/).
