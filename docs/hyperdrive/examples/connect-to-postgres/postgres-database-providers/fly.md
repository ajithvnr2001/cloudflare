---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/fly/
title: Fly \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:31.235296+00:00
---

# Fly · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/fly/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Database Providers
  5. /Fly



# Fly

Connect Hyperdrive to a Fly Postgres database instance.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/fly/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Allow Hyperdrive access2\. Create a database configuration3\. Use Hyperdrive from your WorkerNext steps

This example shows you how to connect Hyperdrive to a Fly Postgres database instance.

## 1\. Allow Hyperdrive access

You can connect Hyperdrive to any existing Fly database by:

  1. Allocating a public IP address to your Fly database instance
  2. Configuring an external service
  3. Deploying the configuration
  4. Obtain the connection string, which is used to connect the database to Hyperdrive.



  1. Run the following command to [allocate a public IP address ↗︎](https://fly.io/docs/postgres/connecting/connecting-external/#allocate-an-ip-address).
         
         fly ips allocate-v6 --app <pg-app-name>

Note

Cloudflare recommends using IPv6, but some Internet service providers may not support IPv6. In this case, [you can allocate an IPv4 address ↗︎](https://fly.io/docs/postgres/connecting/connecting-with-flyctl/).

  2. [Configure an external service ↗︎](https://fly.io/docs/postgres/connecting/connecting-external/#configure-an-external-service) by modifying the contents of your `fly.toml` file. Run the following command to download the `fly.toml` file.
         
         fly config save --app <pg-app-name>

Then, replace the `services` and `services.ports` section of the file with the following `toml` snippet:
         
         [[services]]
         	internal_port = 5432 # Postgres instance
         	protocol = "tcp"
         
         [[services.ports]]
         	handlers = ["pg_tls"]
         	port = 5432

  3. [Deploy the new configuration ↗︎](https://fly.io/docs/postgres/connecting/connecting-external/#deploy-with-the-new-configuration).

  4. [Obtain the connection string ↗︎](https://fly.io/docs/postgres/connecting/connecting-external/#adapting-the-connection-string), which is in the form of:
         
         postgres://{username}:{password}@{public-hostname}:{port}/{database}?options




## 2\. Create a database configuration

To configure Hyperdrive, you will need:

  * The IP address (or hostname) and port of your database.
  * The database username (for example, `hyperdrive-demo`) you configured in a previous step.
  * The password associated with that username.
  * The name of the database you want Hyperdrive to connect to. For example, `postgres`.



Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:
    
    
    postgres://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name

Most database providers will provide a connection string you can directly copy-and-paste directly into Hyperdrive.

To create a Hyperdrive configuration with the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Hyperdrive** page.

[ Go to **Hyperdrive** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive)
  2. Select **Create Configuration**.

  3. Fill out the form, including the connection string.

  4. Select **Create**.




To create a Hyperdrive configuration with the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/):

  1. Open your terminal and run the following command. Replace `<NAME_OF_HYPERDRIVE_CONFIG>` with a name for your Hyperdrive configuration and paste the connection string provided from your database host, or replace `user`, `password`, `HOSTNAME_OR_IP_ADDRESS`, `port`, and `database_name` placeholders with those specific to your database:
         
         npx wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string="postgres://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name"

  2. This command outputs a binding for the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
         
         {
         	"$schema": "./node_modules/wrangler/config-schema.json",
         	"name": "hyperdrive-example",
         	"main": "src/index.ts",
         	// Set this to today's date
         	"compatibility_date": "2026-10-08",
         	"compatibility_flags": [
         		"nodejs_compat"
         	],
         	// Pasted from the output of `wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string=[...]` above.
         	"hyperdrive": [
         		{
         			"binding": "HYPERDRIVE",
         			"id": "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"
         		}
         	]
         }
         
         "$schema" = "./node_modules/wrangler/config-schema.json"
         name = "hyperdrive-example"
         main = "src/index.ts"
         # Set this to today's date
         compatibility_date = "2026-10-08"
         compatibility_flags = [ "nodejs_compat" ]
         
         [[hyperdrive]]
         binding = "HYPERDRIVE"
         id = "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"




Note

Hyperdrive will attempt to connect to your database with the provided credentials to verify they are correct before creating a configuration. If you encounter an error when attempting to connect, refer to Hyperdrive's [troubleshooting documentation](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug possible causes.

## 3\. Use Hyperdrive from your Worker

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

## Next steps

  * Learn more about [How Hyperdrive Works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
  * Refer to the [troubleshooting guide](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug common issues.
  * Understand more about other [storage options](https://developers.cloudflare.com/workers/platform/storage-options/) available to Cloudflare Workers.



[PreviousOverview](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)[NextXata](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/xata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-database-providers/fly.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
