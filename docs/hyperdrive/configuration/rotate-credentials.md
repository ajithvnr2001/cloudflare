---
url: https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/
title: Rotating database credentials \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:29.541093+00:00
---

# Rotating database credentials · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /Configuration
  4. /Rotating database credentials



# Rotating database credentials

Last updated Aug 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/hyperdrive/configuration/rotate-credentials/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse a new Hyperdrive configurationUpdate the existing Hyperdrive configuration

You can change the connection information and credentials of your Hyperdrive configuration in one of two ways:

  1. Create a new Hyperdrive configuration with the new connection information, and update your Worker to use the new Hyperdrive configuration.
  2. Update the existing Hyperdrive configuration with the new connection information and credentials.



## Use a new Hyperdrive configuration

Creating a new Hyperdrive configuration to update your database credentials allows you to keep your existing Hyperdrive configuration unchanged, gradually migrate your Worker to the new Hyperdrive configuration, and easily roll back to the previous configuration if needed.

To create a Hyperdrive configuration that connects to an existing PostgreSQL or MySQL database, use the [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) CLI or the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive).
    
    
    # wrangler v3.11 and above required
    npx wrangler hyperdrive create my-updated-hyperdrive --connection-string="<YOUR_CONNECTION_STRING>"

The command above will output the ID of your Hyperdrive. Set this ID in the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) for your Workers project:
    
    
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

To update your Worker to use the new Hyperdrive configuration, redeploy your Worker or use [gradual deployments](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/).

## Update the existing Hyperdrive configuration

You can update the configuration of an existing Hyperdrive configuration using the [wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/).
    
    
    # wrangler v3.11 and above required
    npx wrangler hyperdrive update <HYPERDRIVE_CONFIG_ID> --origin-host <YOUR_ORIGIN_HOST> --origin-password <YOUR_ORIGIN_PASSWORD> --origin-user <YOUR_ORIGIN_USERNAME> --database <YOUR_DATABASE> --origin-port <YOUR_ORIGIN_PORT>

Note

Updating the settings of an existing Hyperdrive configuration does not purge Hyperdrive's cache and does not tear down the existing database connection pool. New connections will be established using the new connection information. To drain the existing pool and force new connections immediately, [restart the connection pool](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/#restart-the-connection-pool).

[PreviousTune connection pooling](https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/)[NextTroubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/configuration/rotate-credentials.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
