---
url: https://developers.cloudflare.com/basin-pipelines/streams/manage-streams/
title: Manage streams \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.218299+00:00
---

# Manage streams · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/streams/manage-streams/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /[Streams](https://developers.cloudflare.com/basin-pipelines/streams/)
  4. /Manage streams



# Manage streams

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/streams/manage-streams/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a stream Dashboard Wrangler CLI Schema configurationView stream configuration Dashboard Wrangler CLIUpdate HTTP ingest settings DashboardDelete a stream Dashboard Wrangler CLI

Learn how to:

  * Create and configure streams for data ingestion
  * View and update stream settings
  * Delete streams when no longer needed



## Create a stream

Streams are made available to pipelines as SQL tables using the stream name (for example, `SELECT * FROM my_stream`).

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

[ Go to **Pipelines** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/overview)
  2. Select **Create Pipeline** to launch the pipeline creation wizard.

  3. Complete the wizard to create your stream along with the associated sink and pipeline.




### Wrangler CLI

To create a stream, run the `basin pipelines streams create` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines streams create <STREAM_NAME>
    
    
    yarn wrangler basin pipelines streams create <STREAM_NAME>
    
    
    pnpm wrangler basin pipelines streams create <STREAM_NAME>

Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the `basin pipelines setup` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

### Schema configuration

Streams support two approaches for handling data:

  * **Structured streams** : Define a schema with specific fields and data types. Events are validated against the schema.
  * **Unstructured streams** : Accept any valid JSON without validation. These streams have a single `value` column containing the JSON data.



To create a structured stream, provide a schema file:

npmyarnpnpm
    
    
    npx wrangler basin pipelines streams create my-stream --schema-file schema.json
    
    
    yarn wrangler basin pipelines streams create my-stream --schema-file schema.json
    
    
    pnpm wrangler basin pipelines streams create my-stream --schema-file schema.json

Example schema file:
    
    
    {
    	"fields": [
    		{
    			"name": "user_id",
    			"type": "string",
    			"required": true
    		},
    		{
    			"name": "amount",
    			"type": "float64",
    			"required": false
    		},
    		{
    			"name": "tags",
    			"type": "list",
    			"required": false,
    			"items": {
    				"type": "string"
    			}
    		},
    		{
    			"name": "metadata",
    			"type": "struct",
    			"required": false,
    			"fields": [
    				{
    					"name": "source",
    					"type": "string",
    					"required": false
    				},
    				{
    					"name": "priority",
    					"type": "int32",
    					"required": false
    				}
    			]
    		}
    	]
    }

**Supported data types:**

  * `string` \- Text values
  * `int32`, `int64` \- Integer numbers
  * `float32`, `float64` \- Floating-point numbers
  * `bool` \- Boolean true/false
  * `timestamp` \- RFC 3339 timestamps, or numeric values parsed as Unix seconds, milliseconds, or microseconds (depending on unit)
  * `json` \- JSON objects
  * `binary` \- Binary data (base64-encoded)
  * `list` \- Arrays of values
  * `struct` \- Nested objects with defined fields



Note

Events that do not match the defined schema are accepted during ingestion but will be dropped during processing. To monitor dropped events and understand why they were dropped, query the [user error metrics](https://developers.cloudflare.com/basin-pipelines/observability/metrics/#user-error-metrics) via GraphQL. Schema modifications are not supported after stream creation.

## View stream configuration

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Streams**.

  2. Select a stream to view its associated configuration.




### Wrangler CLI

To view a specific stream, run the `basin pipelines streams get` command with either the stream ID or stream name:

npmyarnpnpm
    
    
    npx wrangler basin pipelines streams get <STREAM_NAME_OR_ID>
    
    
    yarn wrangler basin pipelines streams get <STREAM_NAME_OR_ID>
    
    
    pnpm wrangler basin pipelines streams get <STREAM_NAME_OR_ID>

To list all streams in your account, run the `basin pipelines streams list` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines streams list
    
    
    yarn wrangler basin pipelines streams list
    
    
    pnpm wrangler basin pipelines streams list

## Update HTTP ingest settings

You can update certain HTTP ingest settings after stream creation. Schema modifications are not supported once a stream is created.

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Streams**.

  2. Select the stream you want to update.

  3. In the **Settings** tab, go to **HTTP Ingest**.

  4. To turn on or turn off HTTP ingestion, select **Enable** or **Disable**.

  5. To update authentication and CORS settings, select **Edit** and modify.

  6. Save your changes.




Note

For details on configuring authentication tokens and making authenticated requests, refer to [Writing to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/).

## Delete a stream

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Streams**.

  2. Select the stream you want to delete.

  3. In the **Settings** tab, go to **General** , and select **Delete**.




### Wrangler CLI

To delete a stream, run the `basin pipelines streams delete` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines streams delete <STREAM_ID>
    
    
    yarn wrangler basin pipelines streams delete <STREAM_ID>
    
    
    pnpm wrangler basin pipelines streams delete <STREAM_ID>

Caution

Deleting a stream will permanently remove all buffered events that have not been processed and will delete any dependent pipelines. Ensure all data has been delivered to your sink before deletion.

[PreviousOverview](https://developers.cloudflare.com/basin-pipelines/streams/)[NextWriting to streams](https://developers.cloudflare.com/basin-pipelines/streams/writing-to-streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/streams/manage-streams.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
