---
url: https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/
title: Billing for SQLite Storage \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:31.856524+00:00
---

# Billing for SQLite Storage · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 12, 2025

## Billing for SQLite Storage

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).

To view your SQLite storage usage, go to the **Durable Objects** page

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.

Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to [SQLite storage pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend) announced in September 2024 with the [public beta ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/). Developers on the Workers Free plan will not be charged.

Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur [charges for requests and duration](https://developers.cloudflare.com/durable-objects/platform/pricing/#compute-billing), and no changes are being made to compute billing.

For more information about SQLite storage pricing and limits, refer to the [Durable Objects pricing documentation](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend).
