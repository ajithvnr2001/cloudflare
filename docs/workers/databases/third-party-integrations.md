---
url: https://developers.cloudflare.com/workers/databases/third-party-integrations/
title: 3rd Party Integrations \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:17.550006+00:00
---

# 3rd Party Integrations · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/databases/third-party-integrations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Databases
  4. /3rd Party Integrations



# 3rd Party Integrations

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/databases/third-party-integrations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundDatabase credentialsDatabase limitsPopular providers

## Background

Connect to databases by configuring connection strings and credentials as [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) in your Worker.

Connecting to a regional database from a Worker?

If your Worker is connecting to a regional database, you can reduce your query latency by using [Hyperdrive](https://developers.cloudflare.com/hyperdrive) and [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/) which are both included in any Workers plan. Hyperdrive will pool your databases connections globally across Cloudflare's network. Smart Placement will monitor your application to run your Workers closest to your backend infrastructure when this reduces the latency of your Worker invocations. Learn more about [how Smart Placement works](https://developers.cloudflare.com/workers/configuration/placement/).

## Database credentials

When you rotate or update database credentials, you must update the corresponding [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) in your Worker. Use the [`wrangler secret put`](https://developers.cloudflare.com/workers/wrangler/commands/general/#secret) command to update secrets securely or update the secret directly in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/settings).

## Database limits

You can connect to multiple databases by configuring separate sets of secrets for each database connection. Use descriptive secret names to distinguish between different database connections (for example, `DATABASE_URL_PROD` and `DATABASE_URL_STAGING`).

## Popular providers

  * [Neon](https://developers.cloudflare.com/workers/databases/third-party-integrations/neon/)
  * [PlanetScale](https://developers.cloudflare.com/workers/databases/third-party-integrations/planetscale/)
  * [Supabase](https://developers.cloudflare.com/workers/databases/third-party-integrations/supabase/)
  * [Turso](https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/)
  * [Upstash](https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/)
  * [Xata](https://developers.cloudflare.com/workers/databases/third-party-integrations/xata/)



[PreviousHyperdrive ↗︎](https://developers.cloudflare.com/hyperdrive/)[NextNeon](https://developers.cloudflare.com/workers/databases/third-party-integrations/neon/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/databases/third-party-integrations/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
