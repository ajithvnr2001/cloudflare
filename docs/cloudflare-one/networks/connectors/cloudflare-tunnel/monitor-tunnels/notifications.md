---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/
title: Notifications \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:18.394548+00:00
---

# Notifications · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Monitor tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/)
  5. /Notifications



# Notifications

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage notificationsAvailable notifications

Administrators can receive an alert when Cloudflare Tunnels in an account change their health or deployment status. Notifications can be delivered via email, webhook, and third-party services.

## Manage notifications

Tunnel notifications are configured on the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/). For more information, refer to [Create a notification](https://developers.cloudflare.com/notifications/get-started/#create-an-alert).

## Available notifications

Tunnel Creation or Deletion Event

**Who is it for?**

Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

No action is needed.

Tunnel Health Alert

**Who is it for?**

Customers who want to be warned about changes in health status for their Cloudflare Tunnels.

**Other options / filters**

None.

**Included with**

All Cloudflare Zero Trust plans.

**What should you do if you receive one?**

Monitor tunnel health over time and consider deploying [`cloudflared` replicas or load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/).

**Additional information**

Refer to [Tunnel status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) to review the list of possible tunnel statuses (`Healthy`, `Inactive`, `Down` and `Degraded`).

[PreviousLog streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/)[NextMetrics](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/notifications.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
