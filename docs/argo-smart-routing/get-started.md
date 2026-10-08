---
url: https://developers.cloudflare.com/argo-smart-routing/get-started/
title: Get started \u00b7 Cloudflare Argo Smart Routing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.894310+00:00
---

# Get started · Cloudflare Argo Smart Routing docs

> Source: https://developers.cloudflare.com/argo-smart-routing/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/)
  3. /Get started



# Get started

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/argo-smart-routing/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBillingEnable Tiered Cache

Smart Shield

This functionality is now offered as part of Cloudflare's origin server safeguard, Smart Shield. [Learn more](https://developers.cloudflare.com/smart-shield/).

Argo Smart Routing speeds up your global traffic by routing requests across the fastest network paths available.

To enable [Argo Smart Routing ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/traffic) in the dashboard:

  1. In the Cloudflare dashboard, go to the **Argo Smart Routing** page.

[ Go to **Argo Smart Routing** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/traffic)
  2. For **Argo Smart Routing** , switch the toggle to **On**.

  3. Provide your billing information.

     * If you do not have a [billing profile](https://developers.cloudflare.com/billing/get-started/create-billing-profile/), enter your billing information.

     * If you have a billing profile, confirm your billing information.




To enable or disable Argo Smart Routing with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/edit/) request with the `value` parameter set to your desired setting (`"on"` or `"off"`).

You will need to already have a [billing profile](https://developers.cloudflare.com/billing/get-started/create-billing-profile/) on your account to enable Argo Smart Routing.

Note

Enterprise customers can preview this product as a [non-contract service](https://developers.cloudflare.com/billing/understand/preview-services/), which provides full access, free of metered usage fees, limits, and certain other restrictions.

## Billing

If Cloudflare mitigates attacks on your site - whether through DDoS protection, the WAF, or other mechanisms - that traffic will not be included in any charges for Argo Smart Routing.

Since this is a service with [usage-based billing](https://developers.cloudflare.com/billing/understand/usage-based-billing/), Cloudflare recommends that you set up usage-based billing notifications to avoid unexpected bills.

To set up those notifications:

  1. In the Cloudflare dashboard, go to the **Notifications** page.

[ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. On **Alert Type** of **Usage Based Billing** , click **Select**.

  3. Fill out the following information:

     * **Name**
     * **Product**
     * **Notification limit** (exact metric will vary based on product)
     * **Notification email**

Note

All plans can send alerts through [webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/). Business and higher plans can also use [PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/).

  4. Select **Save**.




## Enable Tiered Cache

[Cache](https://developers.cloudflare.com/cache/) works by storing a copy of website content at Cloudflare's data centers. [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) organizes these data centers into a hierarchy based on location. This behavior allows Cloudflare to deliver content from data centers closest to your visitor.

When used together, Argo Smart Routing optimizes the network path between Cloudflare data centers and your origin, while Tiered Cache reduces the number of requests that reach your origin. For more information, refer to [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/).

[PreviousOverview](https://developers.cloudflare.com/argo-smart-routing/)[NextAnalytics](https://developers.cloudflare.com/argo-smart-routing/analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/argo-smart-routing/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
