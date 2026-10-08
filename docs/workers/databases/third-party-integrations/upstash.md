---
url: https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/
title: Upstash \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:18.136471+00:00
---

# Upstash · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Databases

  4. /[3rd Party Integrations](https://developers.cloudflare.com/workers/databases/third-party-integrations/)
  5. /Upstash



# Upstash

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpstash for RedisUpstash QStash

[Upstash ↗︎](https://upstash.com/) is a serverless database with Redis* and Kafka API. Upstash also offers QStash, a task queue/scheduler designed for the serverless.

## Upstash for Redis

To set up an integration with Upstash:

  1. You need an existing Upstash database to connect to. [Create an Upstash database ↗︎](https://docs.upstash.com/redis#create-a-database) or [load data from an existing database to Upstash ↗︎](https://docs.upstash.com/redis/howto/connectclient).

  2. Insert some data to your Upstash database. You can add data to your Upstash database in two ways:

     * Use the CLI directly from your Upstash console.
     * Alternatively, install [redis-cli ↗︎](https://redis.io/docs/getting-started/installation/) locally and run the following commands.
    
    set GB "Ey up?"
    
    OK
    
    set US "Yo, what’s up?"
    
    OK
    
    set NL "Hoi, hoe gaat het?"
    
    OK

  3. Configure the Upstash Redis credentials in your Worker:

You need to add your Upstash Redis database URL and token as secrets to your Worker. Get these from your [Upstash Console ↗︎](https://console.upstash.com) under your database details, then add them as secrets using Wrangler:
         
         # Add the Upstash Redis URL as a secret
         npx wrangler secret put UPSTASH_REDIS_REST_URL
         # When prompted, paste your Upstash Redis REST URL
         
         # Add the Upstash Redis token as a secret
         npx wrangler secret put UPSTASH_REDIS_REST_TOKEN
         # When prompted, paste your Upstash Redis REST token

  4. In your Worker, install the `@upstash/redis`, a HTTP client to connect to your database and start manipulating data:

npmyarnpnpmbun
         
         npm i @upstash/redis
         
         yarn add @upstash/redis
         
         pnpm add @upstash/redis
         
         bun add @upstash/redis

  5. The following example shows how to make a query to your Upstash database in a Worker. The credentials needed to connect to Upstash have been added as secrets to your Worker.
         
         import { Redis } from "@upstash/redis/cloudflare";
         
         export default {
         	async fetch(request, env) {
         		const redis = Redis.fromEnv(env);
         
         		const country = request.headers.get("cf-ipcountry");
         		if (country) {
         			const greeting = await redis.get(country);
         			if (greeting) {
         				return new Response(greeting);
         			}
         		}
         
         		return new Response("Hello What's up!");
         	},
         };

Note

`Redis.fromEnv(env)` automatically picks up the default `url` and `token` names created in the integration.

If you have renamed the secrets, you must declare them explicitly like in the [Upstash basic example ↗︎](https://docs.upstash.com/redis/sdks/redis-ts/getstarted#basic-usage).




To learn more about Upstash, refer to the [Upstash documentation ↗︎](https://docs.upstash.com/redis).

## Upstash QStash

To set up an integration with Upstash QStash:

  1. Configure the [publicly available HTTP endpoint ↗︎](https://docs.upstash.com/qstash#1-public-api) that you want to send your messages to.

  2. Configure the Upstash QStash credentials in your Worker:

You need to add your Upstash QStash token as a secret to your Worker. Get your token from your [Upstash Console ↗︎](https://console.upstash.com) under QStash settings, then add it as a secret using Wrangler:
         
         # Add the QStash token as a secret
         npx wrangler secret put QSTASH_TOKEN
         # When prompted, paste your QStash token

  3. In your Worker, install the `@upstash/qstash`, a HTTP client to connect to your database QStash endpoint:

npmyarnpnpmbun
         
         npm i @upstash/qstash
         
         yarn add @upstash/qstash
         
         pnpm add @upstash/qstash
         
         bun add @upstash/qstash

  4. Refer to the [Upstash documentation on how to receive webhooks from QStash in your Cloudflare Worker ↗︎](https://docs.upstash.com/qstash/quickstarts/cloudflare-workers#3-use-qstash-in-your-handler).




* Redis is a trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Upstash is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Upstash.

[PreviousTurso](https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/)[NextXata](https://developers.cloudflare.com/workers/databases/third-party-integrations/xata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/databases/third-party-integrations/upstash.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
