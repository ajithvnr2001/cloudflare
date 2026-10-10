---
url: https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/
title: Automatic configuration for private databases on Hyperdrive \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.343167+00:00
---

# Automatic configuration for private databases on Hyperdrive · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 28, 2025

## Automatic configuration for private databases on Hyperdrive

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.

![Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1814,height=922,format=webp/_astro/hyperdrive-private-database-automatic-configuration.BT4_KLwW.png)

When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.

To create a Hyperdrive for a private database, you can follow the [Hyperdrive documentation](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/). You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.

This feature is available from the Cloudflare dashboard.
