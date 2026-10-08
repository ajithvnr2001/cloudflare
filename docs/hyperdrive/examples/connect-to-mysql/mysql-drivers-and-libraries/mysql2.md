---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/
title: mysql2 \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:30.419477+00:00
---

# mysql2 · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to MySQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/)

  4. /Libraries and Drivers
  5. /mysql2



# mysql2

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [mysql2 ↗︎](https://github.com/sidorares/node-mysql2) package is a modern MySQL driver for Node.js with better performance and built-in Promise support. This example demonstrates how to use it with Cloudflare Workers and Hyperdrive.

Install the [mysql2 ↗︎](https://github.com/sidorares/node-mysql2) driver:

npmyarnpnpmbun
    
    
    npm i mysql2@>3.13.0
    
    
    yarn add mysql2@>3.13.0
    
    
    pnpm add mysql2@>3.13.0
    
    
    bun add mysql2@>3.13.0

Note

`mysql2` v3.13.0 or later is required

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

Create a new `connection` instance and pass the Hyperdrive parameters:
    
    
    // mysql2 v3.13.0 or later is required
    import { createConnection } from "mysql2/promise";
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		// Create a new connection on each request. Hyperdrive maintains the underlying
    		// database connection pool, so creating a new connection is fast.
    		const connection = await createConnection({
    			host: env.HYPERDRIVE.host,
    			user: env.HYPERDRIVE.user,
    			password: env.HYPERDRIVE.password,
    			database: env.HYPERDRIVE.database,
    			port: env.HYPERDRIVE.port,
    
    			// Required to enable mysql2 compatibility for Workers
    			disableEval: true,
    		});
    
    		try {
    			// Sample query
    			const [results, fields] = await connection.query("SHOW tables;");
    
    			// Return result rows as JSON
    			return Response.json({ results, fields });
    		} catch (e) {
    			console.error(e);
    			return Response.json(
    				{ error: e instanceof Error ? e.message : e },
    				{ status: 500 },
    			);
    		}
    	},
    } satisfies ExportedHandler<Env>;

Note

The minimum version of `mysql2` required for Hyperdrive is `3.13.0`.

[PreviousAWS RDS and Aurora](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/aws-rds-aurora/)[Nextmysql](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
