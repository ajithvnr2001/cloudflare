---
url: https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/
title: Turso \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:18.040815+00:00
---

# Turso · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

Databases

  4. /[3rd Party Integrations](https://developers.cloudflare.com/workers/databases/third-party-integrations/)
  5. /Turso



# Turso

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up an integration with Turso

[Turso ↗︎](https://turso.tech/) is an edge-hosted, distributed database based on [libSQL ↗︎](https://libsql.org/), an open-source fork of SQLite. Turso was designed to minimize query latency for applications where queries comes from anywhere in the world.

## Set up an integration with Turso

To set up an integration with Turso:

  1. You need to install Turso CLI to create and populate a database. Use one of the following two commands in your terminal to install the Turso CLI:
         
         # On macOS and linux with homebrew
         brew install tursodatabase/tap/turso
         
         # Manual scripted installation
         curl -sSfL https://get.tur.so/install.sh | bash

Next, run the following command to make sure the Turso CLI is installed:
         
         turso --version

  2. Before you create your first Turso database, you have to authenticate with your GitHub account by running:
         
         turso auth login
         
         Waiting for authentication...
         ✔  Success! Logged in as <YOUR_GITHUB_USERNAME>

After you have authenticated, you can create a database using the command `turso db create <DATABASE_NAME>`. Turso will create a database and automatically choose a location closest to you.
         
         turso db create my-db
         
         # Example:
         Creating database my-db in Amsterdam, Netherlands (ams)
         
         # Once succeeded:
         Created database my-db in Amsterdam, Netherlands (ams) in 13 seconds.

With the first database created, you can now connect to it directly and execute SQL queries against it.
         
         turso db shell my-db

  3. Copy the following SQL query into the shell you just opened:
         
         CREATE TABLE elements (
           id INTEGER NOT NULL,
           elementName TEXT NOT NULL,
           atomicNumber INTEGER NOT NULL,
           symbol TEXT NOT NULL
         );
         
         INSERT INTO elements (id, elementName, atomicNumber, symbol)
         VALUES (1, 'Hydrogen', 1, 'H'),
           (2, 'Helium', 2, 'He'),
           (3, 'Lithium', 3, 'Li'),
           (4, 'Beryllium', 4, 'Be'),
           (5, 'Boron', 5, 'B'),
           (6, 'Carbon', 6, 'C'),
           (7, 'Nitrogen', 7, 'N'),
           (8, 'Oxygen', 8, 'O'),
           (9, 'Fluorine', 9, 'F'),
           (10, 'Neon', 10, 'Ne');

  4. Configure the Turso database credentials in your Worker:

You need to add your Turso database URL and authentication token as secrets to your Worker. First, get your database URL and create an authentication token:
         
         # Get your database URL
         turso db show my-db --url
         
         # Create an authentication token
         turso db tokens create my-db

Then add these as secrets to your Worker using Wrangler:
         
         # Add the database URL as a secret
         npx wrangler secret put TURSO_URL
         # When prompted, paste your database URL
         
         # Add the authentication token as a secret  
         npx wrangler secret put TURSO_AUTH_TOKEN
         # When prompted, paste your authentication token

  5. In your Worker, install the Turso client library:

npmyarnpnpmbun
         
         npm i @libsql/client
         
         yarn add @libsql/client
         
         pnpm add @libsql/client
         
         bun add @libsql/client

  6. The following example shows how to make a query to your Turso database in a Worker. The credentials needed to connect to Turso have been added as [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) to your Worker.
         
         import { Client as LibsqlClient, createClient } from "@libsql/client/web";
         
         export interface Env {
         	TURSO_URL?: string;
         	TURSO_AUTH_TOKEN?: string;
         }
         
         export default {
         	async fetch(request, env, ctx): Promise<Response> {
         		const client = buildLibsqlClient(env);
         
         		try {
         			const res = await client.execute("SELECT * FROM elements");
         			return new Response(JSON.stringify(res), {
         				status: 200,
         				headers: { "Content-Type": "application/json" },
         			});
         		} catch (error) {
         			console.error("Error executing SQL query:", error);
         			return new Response(
         				JSON.stringify({ error: "Internal Server Error" }),
         				{
         					status: 500,
         				},
         			);
         		}
         	},
         } satisfies ExportedHandler<Env>;
         
         function buildLibsqlClient(env: Env): LibsqlClient {
         	const url = env.TURSO_URL?.trim();
         	if (url === undefined) {
         		throw new Error("TURSO_URL env var is not defined");
         	}
         
         	const authToken = env.TURSO_AUTH_TOKEN?.trim();
         	if (authToken == undefined) {
         		throw new Error("TURSO_AUTH_TOKEN env var is not defined");
         	}
         
         	return createClient({ url, authToken });
         }

     * The libSQL client library import `@libsql/client/web` must be imported exactly as shown when working with Cloudflare Workers. The non-web import will not work in the Workers environment.
     * The `Env` interface contains the [environment variable](https://developers.cloudflare.com/workers/configuration/environment-variables/) and [secret](https://developers.cloudflare.com/workers/configuration/secrets/) defined when you added the Turso integration in step 4.
     * The `Env` interface also caches the libSQL client object and router, which was created on the first request to the Worker.
     * The Worker uses `buildLibsqlClient` to query the `elements` database and returns the response as a JSON object.



With your environment configured and your code ready, you can now test your Worker locally before you deploy.

To learn more about Turso, refer to [Turso's official documentation ↗︎](https://docs.turso.tech).

[PreviousSupabase](https://developers.cloudflare.com/workers/databases/third-party-integrations/supabase/)[NextUpstash](https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/databases/third-party-integrations/turso.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
