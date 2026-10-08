---
url: https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/
title: Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.602625+00:00
---

# Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 17, 2026

## Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now restart, reboot, or shut down a [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) directly from the dashboard or via API.

![Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-07-17-appliance-restart-reboot-shutdown.DKqTLOh6.gif)

  * **Restart** — Restart managed services. Purges temporary and (optionally) persistent state.
  * **Reboot** — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.
  * **Shutdown** — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.



In the dashboard, go to **Networking** > **Connectors** > **Appliances** , select an appliance, then **Edit** > **Operations** to send an operation. Via API, `POST` to the `/accounts/{account_id}/magic/connectors/{connector_id}/interrupts` endpoint.

For details, refer to [Appliance operations](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/).
