---
url: https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/
title: Next steps \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.678645+00:00
---

# Next steps · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Load Balancing

  4. /[Setup](https://developers.cloudflare.com/learning-paths/load-balancing/setup/)
  5. /Next steps



# Next steps

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsage-based notificationsAdditional configuration options

Your load balancer should be receiving production traffic (and you can confirm this by reviewing the [analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/)).

Though your product is officially set up, you may want to consider the following suggestions.

## Usage-based notifications

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




## Additional configuration options

You may want to further customize how your load balancer routes traffic or integrate your load balancer with other Cloudflare products:

  * [Cloudflare Tunnel (published applications)](https://developers.cloudflare.com/load-balancing/additional-options/cloudflare-tunnel/)
  * [Spectrum](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/)
  * [Perform planned maintenance](https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/)
  * [Load shedding](https://developers.cloudflare.com/load-balancing/additional-options/load-shedding/)
  * [DNS persistence](https://developers.cloudflare.com/load-balancing/additional-options/dns-persistence/)
  * [Load Balancing with the China Network](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/)
  * [Override HTTP Host headers](https://developers.cloudflare.com/load-balancing/additional-options/override-http-host-headers/)
  * [CNAME flattening for endpoints](https://developers.cloudflare.com/load-balancing/additional-options/cname-flattening/)
  * [Custom load balancing rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/)
  * [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/)
  * [Additional DNS records](https://developers.cloudflare.com/load-balancing/additional-options/additional-dns-records/)



[PreviousRoute production traffic](https://developers.cloudflare.com/learning-paths/load-balancing/setup/production-traffic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/load-balancing/setup/next-steps.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
