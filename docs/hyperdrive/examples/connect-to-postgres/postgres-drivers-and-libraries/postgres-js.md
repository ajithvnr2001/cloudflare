---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/
title: Postgres.js \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:32.510282+00:00
---

# Postgres.js · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Libraries and Drivers
  5. /Postgres.js



# Postgres.js

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Postgres.js ↗︎](https://github.com/porsager/postgres) is a modern, fully-featured PostgreSQL driver for Node.js. This example demonstrates how to use Postgres.js with Cloudflare Hyperdrive in a Workers application.

Recommended driver

[Node-postgres ↗︎](https://node-postgres.com/) (`pg`) is the recommended driver for connecting to your Postgres database from JavaScript or TypeScript Workers. It has the best compatibility with Hyperdrive's caching and is commonly available with popular ORM libraries. [Postgres.js ↗︎](https://github.com/porsager/postgres) is also supported.

Do not use `prepare: false` with Postgres.js

[`prepare: false` ↗︎](https://github.com/porsager/postgres?tab=readme-ov-file#prepared-statements) disables prepared statements. Postgres.js then sends additional protocol messages to discover parameter types before each query. Hyperdrive's [transaction pooling mode](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/#pooling-mode) does not reliably support this behavior. This can cause queries to hang or fail intermittently.

Install [Postgres.js ↗︎](https://github.com/porsager/postgres):

npmyarnpnpmbun
    
    
    npm i postgres@>3.4.5
    
    
    yarn add postgres@>3.4.5
    
    
    pnpm add postgres@>3.4.5
    
    
    bun add postgres@>3.4.5

Note

The minimum version of `postgres-js` required for Hyperdrive is `3.4.5`.

Add the required Node.js compatibility flags and Hyperdrive binding to your `wrangler.jsonc` file:
    
    
    {
    	// required for database drivers to function
    	"compatibility_flags": [
    		"nodejs_compat"
    	],
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"hyperdrive": [
    		{
    			"binding": "HYPERDRIVE",
    			"id": "<your-hyperdrive-id-here>"
    		}
    	]
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[hyperdrive]]
    binding = "HYPERDRIVE"
    id = "<your-hyperdrive-id-here>"

Create a Worker that connects to your PostgreSQL database via Hyperdrive:
    
    
    // filepath: src/index.ts
    import postgres from "postgres";
    
    export default {
    	async fetch(
    		request: Request,
    		env: Env,
    		ctx: ExecutionContext,
    	): Promise<Response> {
    		// Create a database client that connects to your database via Hyperdrive.
    		// Hyperdrive maintains the underlying database connection pool,
    		// so creating a new client on each request is fast and recommended.
    		const sql = postgres(env.HYPERDRIVE.connectionString, {
    			// Limit the connections for the Worker request to 5 due to Workers' limits on concurrent external connections
    			max: 5,
    			// If you are not using array types in your Postgres schema, disable `fetch_types` to avoid an additional round-trip (unnecessary latency)
    			fetch_types: false,
    
    			// This is set to true by default, but certain query generators such as Kysely or queries using sql.unsafe() will set this to false. Hyperdrive will not cache prepared statements when this option is set to false and will require additional round-trips.  
    			prepare: true,
    		});
    
    		try {
    			// A very simple test query
    			const result = await sql`select * from pg_tables`;
    
    			// Return result rows as JSON
    			return Response.json({ success: true, result: result });
    		} catch (e: any) {
    			console.error("Database error:", e.message);
    
    			return Response.error();
    		}
    	},
    } satisfies ExportedHandler<Env>;

[Previousnode-postgres (pg)](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/)[NextDrizzle ORM](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
