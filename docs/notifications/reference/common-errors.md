---
url: https://developers.cloudflare.com/notifications/reference/common-errors/
title: Common errors \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.845056+00:00
---

# Common errors · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/reference/common-errors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Notifications](https://developers.cloudflare.com/notifications/)
  3. /Reference
  4. /Common errors



# Common errors

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/notifications/reference/common-errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWebhook test failed with status code 400 Bad RequestDeleted users are still receiving alerts

## Webhook test failed with status code 400 Bad Request

This error can occur when you try to configure a webhook that is not currently supported, such as setting up a PagerDuty webhook. PagerDuty needs to be configured under [connected services](https://developers.cloudflare.com/notifications/get-started/configure-pagerduty/), not as a webhook.

## Deleted users are still receiving alerts

When you remove a user from your account via **Manage Account** > **Members** in the Cloudflare dashboard, their email address is not removed from existing alerts. You need to remove their email address by [editing the alert](https://developers.cloudflare.com/notifications/get-started/#manage-alerts).

[PreviousHTTP Traffic Alerts](https://developers.cloudflare.com/notifications/reference/traffic-alerts/)[NextWebhook payload schema](https://developers.cloudflare.com/notifications/reference/webhook-payload-schema/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/reference/common-errors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
