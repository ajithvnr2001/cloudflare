---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/
title: Restart a Hyperdrive configuration from the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.447602+00:00
---

# Restart a Hyperdrive configuration from the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## Restart a Hyperdrive configuration from the dashboard

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.

Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.

To restart, select your Hyperdrive configuration in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com), go to the **Settings** tab, and select **Restart** under **Danger zone**. Restarting requires the [**Hyperdrive Admin** role](https://developers.cloudflare.com/fundamentals/manage-members/roles/). After a restart, the **Settings** tab shows when the configuration was last manually restarted.

![The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=468,format=webp/_astro/dashboard-restart-danger-zone.D1h69zVU.png)

Caution

Restarting drops all active connections in the pool and forces them to be re-established. In-flight queries may see brief errors while the pool rebuilds.

For more information, refer to [Connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).
