---
url: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/
title: Set up alerts \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:51.784251+00:00
---

# Set up alerts · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Prevent Ddos Attacks

  4. /[Baseline DDoS protection](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/)
  5. /Set up alerts



# Set up alerts

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Another part of preparing for DDoS attacks is knowing when your application is being attacked.

Cloudflare offers notifications for DDoS attacks, which you can set up on your account.

To set up a notification:

  1. In the Cloudflare dashboard, go to the **Notifications** page.

[ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. Select **Add**.

  3. Select one of the [available DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/#alert-types) depending on your plan and services:

     * HTTP DDoS Attack Alert
     * Layer 3/4 DDoS Attack Alert
     * Advanced HTTP DDoS Attack Alert
     * Advanced Layer 3/4 DDoS Attack Alert
  4. Enter a notification name and (optionally) a description.

  5. Configure a delivery method for the notification. The available delivery methods depend on your Cloudflare plan. For more information, refer to [Cloudflare Notifications](https://developers.cloudflare.com/notifications/).

  6. If you are creating a notification for one of the advanced DDoS attack alerts, select **Next** and define the parameters that will filter the notifications you will receive.

  7. Select **Save**.




[PreviousUpdate TLS versions](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/)[NextOverview](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/advanced/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
