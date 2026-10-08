---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/
title: node-postgres (pg) \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:32.462390+00:00
---

# node-postgres (pg) · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Libraries and Drivers
  5. /node-postgres (pg)



# node-postgres (pg)

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[node-postgres ↗︎](https://node-postgres.com/) (pg) is a widely-used PostgreSQL driver for Node.js applications. This example demonstrates how to use node-postgres with Cloudflare Hyperdrive in a Workers application.

Recommended driver

[Node-postgres ↗︎](https://node-postgres.com/) (`pg`) is the recommended driver for connecting to your Postgres database from JavaScript or TypeScript Workers. It has the best compatibility with Hyperdrive's caching and is commonly available with popular ORM libraries. [Postgres.js ↗︎](https://github.com/porsager/postgres) is also supported.

Install the `node-postgres` driver:

npmyarnpnpmbun
    
    
    npm i pg@>8.16.3
    
    
    yarn add pg@>8.16.3
    
    
    pnpm add pg@>8.16.3
    
    
    bun add pg@>8.16.3

Note

The minimum version of `node-postgres` required for Hyperdrive is `8.16.3`.

If using TypeScript, install the types package:

npmyarnpnpmbun
    
    
    npm i -D @types/pg
    
    
    yarn add -D @types/pg
    
    
    pnpm add -D @types/pg
    
    
    bun add -d @types/pg

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

Create a new `Client` instance and pass the Hyperdrive `connectionString`:
    
    
    // filepath: src/index.ts
    import { Client } from "pg";
    
    export default {
    	async fetch(
    		request: Request,
    		env: Env,
    		ctx: ExecutionContext,
    	): Promise<Response> {
    		// Create a new client instance for each request. Hyperdrive maintains the
    		// underlying database connection pool, so creating a new client is fast.
    		const client = new Client({
    			connectionString: env.HYPERDRIVE.connectionString,
    		});
    
    		try {
    			// Connect to the database
    			await client.connect();
    
    			// Perform a simple query
    			const result = await client.query("SELECT * FROM pg_tables");
    
    			return Response.json({
    				success: true,
    				result: result.rows,
    			});
    		} catch (error: any) {
    			console.error("Database error:", error.message);
    
    			return new Response("Internal error occurred", { status: 500 });
    		}
    	},
    };

[PreviousAWS RDS and Aurora](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/)[NextPostgres.js](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
