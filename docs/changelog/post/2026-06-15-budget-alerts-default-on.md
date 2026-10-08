---
url: https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/
title: Budget alerts now on by default for Pay-as-you-go accounts \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.021040+00:00
---

# Budget alerts now on by default for Pay-as-you-go accounts · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 20, 2026

## Budget alerts now on by default for Pay-as-you-go accounts

[Billing](https://developers.cloudflare.com/billing/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.

We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.

The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.

Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.

Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.

You can change the threshold, add additional alerts, or remove the default alert entirely from **Manage Account** > **Billing** > **Billable Usage** , or from your Notifications settings. If you already configured your own budget alert, nothing changes.

Enterprise contract accounts are not in scope.

For more information, refer to the [Budget alerts documentation](https://developers.cloudflare.com/billing/manage/budget-alerts/).
