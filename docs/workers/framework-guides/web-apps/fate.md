---
url: https://developers.cloudflare.com/workers/framework-guides/web-apps/fate/
title: fate \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T11:09:28.506924+00:00
---

# fate · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/fate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Framework guides

  4. /Web applications
  5. /fate



# fate

Last updated Oct 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/web-apps/fate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesDeploy a new fate application on WorkersLive updatesDatabase migrationsNext steps

[ _fate_ ↗︎](https://fate.technology/) is a modern data client for the web inspired by [Relay ↗︎](https://relay.dev/) and [GraphQL ↗︎](https://graphql.org/). It combines view composition, normalized caching, data masking, Async React features, and type-safe data fetching.

Deploy fate directly to your own Cloudflare account with [Void ↗︎](https://fate.technology/integrations/void). The Void template includes the app, [D1 database](https://developers.cloudflare.com/d1/), Drizzle migrations, Better Auth, and live updates through `void-fate` and `void/live`.

## Prerequisites

You need Node.js 24+ and [Vite+ ↗︎](https://viteplus.dev/guide/).

## Deploy a new fate application on Workers

  1. **Create a new fate app with Vite+.**
         
         vp create fate -- my-app --template void
         cd my-app

Add `--framework vue` to the create command to use Vue instead of React.

  2. **Set up Void local files, seed the local database, and prepare fate client support.**
         
         vp run dev:setup

  3. **Start the app.**
         
         vp run dev

The app runs at `http://localhost:6001`.

  4. **Deploy directly to your own Cloudflare account.**

From the project root:
         
         vp exec void deploy --platform cloudflare

Void signs you into Cloudflare when needed, lets you select your account, provisions resources, applies checked-in database migrations, and deploys the app. It saves resource IDs in the root `wrangler.jsonc`; commit that updated config for subsequent deployments. A Void platform account is not required.




## Live updates

The template includes the `VOID_LIVE` [Durable Object binding](https://developers.cloudflare.com/durable-objects/) and its class migration. Keep them in `wrangler.jsonc` so live subscriptions can receive updates across requests. RPC requests use `/fate`, and live updates use `/fate-live`.

## Database migrations

After changing your database schema or auth configuration, run `vp run db:generate`, review and commit the generated migrations, then deploy. The migrations must include the Better Auth schema used in production.

See [Void's Cloudflare deployment guide ↗︎](https://void.cloud/integrations/cloudflare) for custom domains, secrets, and CI configuration.

## Next steps

  * [fate documentation ↗︎](https://fate.technology/guide/getting-started)
  * [Void integration ↗︎](https://fate.technology/integrations/void)
  * [Cloudflare integration ↗︎](https://fate.technology/integrations/cloudflare)



[PreviousVike](https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/)[NextAnalog](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/web-apps/fate.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
