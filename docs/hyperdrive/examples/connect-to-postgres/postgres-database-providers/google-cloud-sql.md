---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/
title: Google Cloud SQL \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:31.631104+00:00
---

# Google Cloud SQL · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Database Providers
  5. /Google Cloud SQL



# Google Cloud SQL

Connect Hyperdrive to a Google Cloud SQL for Postgres database instance.

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Allow Hyperdrive access Cloud Console gcloud CLI2\. Create a database configuration3\. Use Hyperdrive from your WorkerNext steps

This example shows you how to connect Hyperdrive to a Google Cloud SQL Postgres database instance.

## 1\. Allow Hyperdrive access

To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid user credentials and network access.

Note

To allow Hyperdrive to connect to your database, you must allow Cloudflare IPs to be able to access your database. You can either allow-list all IP address ranges (0.0.0.0 - 255.255.255.255) or restrict your IP access control list to the [IP ranges used by Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/firewall-and-networking-configuration/).

Alternatively, you can connect to your databases over in your private network using [Cloudflare Tunnels](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/).

### Cloud Console

When creating the instance or when editing an existing instance in the [Google Cloud Console ↗︎](https://console.cloud.google.com/sql/instances):

To allow Hyperdrive to reach your instance:

  1. In the [Cloud Console ↗︎](https://console.cloud.google.com/sql/instances), select the instance you want Hyperdrive to connect to.
  2. Expand **Connections** > **Networking** > ensure **Public IP** is enabled > **Add a Network** and input `0.0.0.0/0`.
  3. Select **Done** > **Save** to persist your changes.
  4. Select **Overview** from the sidebar and note down the **Public IP address** of your instance.



To create a user for Hyperdrive to connect as:

  1. Select **Users** in the sidebar.
  2. Select **Add User Account** > select **Built-in authentication**.
  3. Provide a name (for example, `hyperdrive-user`) > select **Generate** to generate a password.
  4. Copy this password to your clipboard before selecting **Add** to create the user.



With the username, password, public IP address and (optional) database name (default: `postgres`), you can now create a Hyperdrive database configuration.

### gcloud CLI

The [gcloud CLI ↗︎](https://cloud.google.com/sdk/docs/install) allows you to create a new user and enable Hyperdrive to connect to your database.

Use `gcloud sql` to create a new user (for example, `hyperdrive-user`) with a strong password:
    
    
    gcloud sql users create hyperdrive-user --instance=YOUR_INSTANCE_NAME --password=SUFFICIENTLY_LONG_PASSWORD

Run the following command to enable [Internet access ↗︎](https://cloud.google.com/sql/docs/postgres/configure-ip) to your database instance:
    
    
    # If you have any existing authorized networks, ensure you provide those as a comma separated list.
    # The gcloud CLI will replace any existing authorized networks with the list you provide here.
    gcloud sql instances patch YOUR_INSTANCE_NAME --authorized-networks="0.0.0.0/0"

Refer to [Google Cloud's documentation ↗︎](https://cloud.google.com/sql/docs/postgres/create-manage-users) for additional configuration options.

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



[PreviousPrisma Postgres](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/prisma-postgres/)[NextAWS RDS and Aurora](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
