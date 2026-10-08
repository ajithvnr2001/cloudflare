---
url: https://developers.cloudflare.com/d1/observability/billing/
title: Billing \u00b7 Cloudflare D1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:38.166196+00:00
---

# Billing · Cloudflare D1 docs

> Source: https://developers.cloudflare.com/d1/observability/billing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[D1](https://developers.cloudflare.com/d1/)
  3. /Observability
  4. /Billing



# Billing

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/d1/observability/billing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView metrics in the dashboardBilling Notifications

D1 exposes analytics to track billing metrics (rows read, rows written, and total storage) across all databases in your account.

The metrics displayed in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) are sourced from Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). You can access the metrics [programmatically](https://developers.cloudflare.com/d1/observability/metrics-analytics/#query-via-the-graphql-api) via GraphQL or HTTP client.

## View metrics in the dashboard

Total account billable usage analytics for D1 are available in the Cloudflare dashboard. To view current and past metrics for an account:

  1. In the Cloudflare dashboard, go to the **Billing** page.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  2. Go to **Billable Usage**.




From here you can view charts of your account's D1 usage on a daily or month-to-date timeframe.

Note that billable usage history is stored for a maximum of 30 days.

## Billing Notifications

Usage-based billing notifications are available within the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) for users looking to monitor their total account usage.

Notifications on the following metrics are available:

  * Rows Read
  * Rows Written



[PreviousMetrics and analytics](https://developers.cloudflare.com/d1/observability/metrics-analytics/)[NextAudit Logs](https://developers.cloudflare.com/d1/observability/audit-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/d1/observability/billing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
