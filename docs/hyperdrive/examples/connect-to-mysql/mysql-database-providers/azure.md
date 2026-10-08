---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/azure/
title: Azure Database \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:30.302997+00:00
---

# Azure Database · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/azure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to MySQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/)

  4. /Database Providers
  5. /Azure Database



# Azure Database

Connect Hyperdrive to an Azure Database for MySQL instance.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/azure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Allow Hyperdrive access Azure Portal2\. Create a database configuration3\. Use Hyperdrive from your WorkerNext steps

This example shows you how to connect Hyperdrive to an Azure Database for MySQL instance.

## 1\. Allow Hyperdrive access

To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid credentials and network access.

Note

To allow Hyperdrive to connect to your database, you must allow Cloudflare IPs to be able to access your database. You can either allow-list all IP address ranges (0.0.0.0 - 255.255.255.255) or restrict your IP access control list to the [IP ranges used by Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/firewall-and-networking-configuration/).

Alternatively, you can connect to your databases over in your private network using [Cloudflare Tunnels](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/).

### Azure Portal

#### Public access networking

To connect to your Azure Database for MySQL instance using public Internet connectivity:

  1. In the [Azure Portal ↗︎](https://portal.azure.com/), select the instance you want Hyperdrive to connect to.
  2. Expand **Settings** > **Networking** > ensure **Public access** is enabled > in **Firewall rules** add `0.0.0.0` as **Start IP address** and `255.255.255.255` as **End IP address**.
  3. Select **Save** to persist your changes.
  4. Select **Overview** from the sidebar and note down the **Server name** of your instance.



With the username, password, server name, and database name (default: `mysql`), you can now create a Hyperdrive database configuration.

#### Private access networking

To connect to a private Azure Database for MySQL instance, refer to [Connect to a private database using Tunnel](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/).

## 2\. Create a database configuration

To configure Hyperdrive, you will need:

  * The IP address (or hostname) and port of your database.
  * The database username (for example, `hyperdrive-demo`) you configured in a previous step.
  * The password associated with that username.
  * The name of the database you want Hyperdrive to connect to. For example, `mysql`.



Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:
    
    
    mysql://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name

Most database providers will provide a connection string you can copy-and-paste directly into Hyperdrive.

To create a Hyperdrive configuration with the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/), open your terminal and run the following command.

  * Replace <NAME_OF_HYPERDRIVE_CONFIG> with a name for your Hyperdrive configuration and paste the connection string provided from your database host, or,
  * Replace `user`, `password`, `HOSTNAME_OR_IP_ADDRESS`, `port`, and `database_name` placeholders with those specific to your database:


    
    
    npx wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string="mysql://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name"

Note

Hyperdrive will attempt to connect to your database with the provided credentials to verify they are correct before creating a configuration. If you encounter an error when attempting to connect, refer to Hyperdrive's [troubleshooting documentation](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug possible causes.

This command outputs a binding for the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
    
    
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

## 3\. Use Hyperdrive from your Worker

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

## Next steps

  * Learn more about [How Hyperdrive Works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
  * Refer to the [troubleshooting guide](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug common issues.
  * Understand more about other [storage options](https://developers.cloudflare.com/workers/platform/storage-options/) available to Cloudflare Workers.



[PreviousPlanetScale](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/)[NextGoogle Cloud SQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-mysql/mysql-database-providers/azure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
