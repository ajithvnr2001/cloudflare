---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql/
title: mysql \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:30.353451+00:00
---

# mysql · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to MySQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/)

  4. /Libraries and Drivers
  5. /mysql



# mysql

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [mysql ↗︎](https://github.com/mysqljs/mysql) package is a MySQL driver for Node.js. This example demonstrates how to use it with Cloudflare Workers and Hyperdrive.

Install the [mysql ↗︎](https://github.com/mysqljs/mysql) driver:

npmyarnpnpmbun
    
    
    npm i mysql
    
    
    yarn add mysql
    
    
    pnpm add mysql
    
    
    bun add mysql

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

Create a new connection and pass the Hyperdrive parameters:
    
    
    import { createConnection } from "mysql";
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const result = await new Promise<any>((resolve) => {
    			// Create a connection using the mysql driver with the Hyperdrive credentials (only accessible from your Worker).
    			const connection = createConnection({
    				host: env.HYPERDRIVE.host,
    				user: env.HYPERDRIVE.user,
    				password: env.HYPERDRIVE.password,
    				database: env.HYPERDRIVE.database,
    				port: env.HYPERDRIVE.port,
    			});
    
    			connection.connect((error: { message: string }) => {
    				if (error) {
    					throw new Error(error.message);
    				}
    
    				// Sample query
    				connection.query("SHOW tables;", [], (error, rows, fields) => {
    					resolve({ fields, rows });
    				});
    			});
    		});
    
    		// Return result  as JSON
    		return new Response(JSON.stringify(result), {
    			headers: {
    				"Content-Type": "application/json",
    			},
    		});
    	},
    } satisfies ExportedHandler<Env>;

[Previousmysql2](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/)[NextDrizzle ORM](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/drizzle-orm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
