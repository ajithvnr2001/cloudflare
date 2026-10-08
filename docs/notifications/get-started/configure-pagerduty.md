---
url: https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/
title: Configure PagerDuty \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.572632+00:00
---

# Configure PagerDuty · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Notifications](https://developers.cloudflare.com/notifications/)
  3. /[Get started](https://developers.cloudflare.com/notifications/get-started/)
  4. /Configure PagerDuty



# Configure PagerDuty

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConnect PagerDutyEdit or disconnect PagerDuty

Note

PagerDuty is available if your account has at least one zone on a Business or higher plan.

Cloudflare supports routing alerts to PagerDuty, so you can use the same service definitions and escalation paths you already have configured. When an alert fires, Cloudflare sends it to all PagerDuty services configured for that alert. PagerDuty then handles de-duping, rate limiting, and escalation based on your service configuration.

To use PagerDuty, you need a [PagerDuty account ↗︎](https://www.pagerduty.com/sign-up/) with User, Admin, Manager, Global Admin, or Account Owner permissions.

## Connect PagerDuty

  1. In the Cloudflare dashboard, go to **Alerts** > **Destinations**.

[ Go to **Alerts** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. In the **Connected notification services** card, select **Connect**.

  3. Log in to your [PagerDuty account ↗︎](https://www.pagerduty.com/) to connect it to your Cloudflare account.

  4. Choose the services you want to use and select **Connect**.

  5. The browser will navigate back to your Cloudflare dashboard. Select **Continue**.




Your connected PagerDuty services will appear in the **Connected notification services** card.

## Edit or disconnect PagerDuty

To change which PagerDuty services are connected, you need to disconnect and reconnect:

  1. In the Cloudflare dashboard, go to **Alerts** > **Destinations**.

[ Go to **Alerts** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. In the **Connected notification services** card, select **View** on the PagerDuty service you want to disconnect.

  3. Select **Disconnect** > **Confirm**.

  4. Make your changes in [PagerDuty ↗︎](https://www.pagerduty.com/).

  5. [Reconnect PagerDuty](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/).




Note

Disconnecting PagerDuty disables any alerts currently routed to it. If PagerDuty was the only destination for an alert, that alert will have no destination until you reconfigure it.

[PreviousConfigure alerts](https://developers.cloudflare.com/notifications/get-started/)[NextConfigure webhooks](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/get-started/configure-pagerduty.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
