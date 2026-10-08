---
url: https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/
title: Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.683920+00:00
---

# Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 18, 2026

## Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.

Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.

[ Go to **Create a PlanetScale database** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive?modal=1&type=planetscale&step=1) ![Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=240,format=svg/_astro/planetscale-request-flow.CYsRfKtG.svg)

PlanetScale databases created from Cloudflare work with [Workers](https://developers.cloudflare.com/workers/) through [Hyperdrive](https://developers.cloudflare.com/hyperdrive/). Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.

PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard [pricing ↗︎](https://planetscale.com/pricing). You can introspect per-database billing usage via PlanetScale's [dashboard ↗︎](https://planetscale.com/docs/billing#organization-usage-and-billing-page).

When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.

To get started, refer to [PlanetScale Postgres and MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/planetscale/).
