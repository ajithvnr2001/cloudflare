---
url: https://developers.cloudflare.com/basin-pipelines/getting-started/
title: Getting started \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:24.611290+00:00
---

# Getting started · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/getting-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Getting started



# Getting started

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/getting-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create an API token2\. Create your first pipeline3\. Send sample data4\. Validate data in your bucket5\. Query your data using Basin SQLLearn more

This guide will instruct you through:

  * Creating an [API token](https://developers.cloudflare.com/r2/api/tokens/) needed for pipelines to authenticate with your data catalog.
  * Creating your first pipeline with a simple ecommerce schema that writes to an [Apache Iceberg ↗︎](https://iceberg.apache.org/) table managed by Basin Catalog.
  * Sending sample ecommerce data via HTTP endpoint.
  * Validating data in your bucket and querying it with Basin SQL.



## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## 1\. Create an API token

Basin Pipelines must authenticate to Basin Catalog with an [R2 API token](https://developers.cloudflare.com/r2/api/tokens/) that has catalog and R2 permissions.

  1. In the Cloudflare dashboard, go to the **R2 object storage** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select **Manage API tokens**.

  3. Select **Create Account API token**.

  4. Give your API token a name.

  5. Under **Permissions** , select the **Admin Read & Write** permission.

  6. Select **Create Account API Token**.

  7. Note the **Token value**.




Note

This token also includes the Basin SQL Read permission, which allows you to query your data with Basin SQL.

## 2\. Create your first pipeline

First, create a schema file that defines your ecommerce data structure:

**Create`schema.json`:**
    
    
    {
    	"fields": [
    		{
    			"name": "user_id",
    			"type": "string",
    			"required": true
    		},
    		{
    			"name": "event_type",
    			"type": "string",
    			"required": true
    		},
    		{
    			"name": "product_id",
    			"type": "string",
    			"required": false
    		},
    		{
    			"name": "amount",
    			"type": "float64",
    			"required": false
    		}
    	]
    }

Use the interactive setup to create a pipeline that writes to Basin Catalog:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

Note

The setup command automatically creates the [R2 bucket](https://developers.cloudflare.com/r2/buckets/) and enables [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) if they do not already exist, so you do not need to create them beforehand.

Follow the prompts:

  1. **Pipeline name** : Enter `ecommerce`

  2. **Stream configuration** :

     * Enable HTTP endpoint: `yes`
     * Require authentication: `no` (for simplicity)
     * Configure custom CORS origins: `no`
     * Schema definition: `Load from file`
     * Schema file path: `schema.json` (or your file path)
  3. **Sink configuration** :

     * Destination type: `Data Catalog (Iceberg)`
     * Setup mode: `Simple (recommended defaults)`
     * R2 bucket name: `pipelines-tutorial` (created automatically if it does not exist)
     * Table name: `ecommerce`
     * Catalog API token: Enter your token from step 1
  4. **Review** : Confirm the summary and select `Create resources`

  5. **SQL transformation** : Choose `Simple ingestion (SELECT * FROM stream)`




Note

If you make a mistake during setup (such as an invalid name or incorrect credentials), you will be prompted to retry rather than needing to restart the entire setup process.

Advanced mode options

If you select **Advanced** instead of **Simple** during sink configuration, you can customize the following additional options:

  * **Format** : Output file format (for example, Parquet)
  * **Compression** : Compression algorithm (for example, zstd)
  * **Rolling policy** : File size threshold (minimum 5 MB) and time interval (minimum 10 seconds) for creating new files
  * **Credentials** : Choose between automatic credential generation or manually entering R2 credentials
  * **Namespace** : Data Catalog namespace (defaults to `default`)



After setup completes, the command outputs a configuration snippet for your Wrangler file, a Worker binding example with sample data, and a curl command for the HTTP endpoint. Note the HTTP endpoint URL and the `pipelines` configuration for use in the following steps.

You can also pre-set the pipeline name using the `--name` flag:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup --name ecommerce
    
    
    yarn wrangler basin pipelines setup --name ecommerce
    
    
    pnpm wrangler basin pipelines setup --name ecommerce

  1. In the Cloudflare dashboard, go to **R2 object storage**.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select **Create bucket** and enter the bucket name: `pipelines-tutorial`.

  3. Select **Create bucket**.

  4. Select the bucket, switch to the **Settings** tab, scroll down to **Basin Catalog** , and select **Enable**.

  5. Once enabled, note the **Catalog URI** and **Warehouse name**.

  6. Go to **Basin Pipelines** > **Pipelines**.

[ Go to **Pipelines** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/overview)
  7. Select **Create Pipeline**.

  8. **Connect to a Stream** :

     * Pipeline name: `ecommerce`
     * Enable HTTP endpoint for sending data: Enabled
     * HTTP authentication: Disabled (default)
     * Select **Next**
  9. **Define Input Schema** :

     * Select **JSON editor**
     * Copy in the schema: 
           
           {
           	"fields": [
           		{
           			"name": "user_id",
           			"type": "string",
           			"required": true
           		},
           		{
           			"name": "event_type",
           			"type": "string",
           			"required": true
           		},
           		{
           			"name": "product_id",
           			"type": "string",
           			"required": false
           		},
           		{
           			"name": "amount",
           			"type": "float64",
           			"required": false
           		}
           	]
           }

     * Select **Next**
  10. **Define Sink** :

     * Select your R2 bucket: `pipelines-tutorial`
     * Storage type: **Basin Catalog**
     * Namespace: `default`
     * Table name: `ecommerce`
     * **Advanced Settings** : Change **Maximum Time Interval** to `10 seconds`
     * Select **Next**
  11. **Credentials** :

     * Disable **Automatically create an Account API token for your sink**
     * Enter **Catalog Token** from step 1
     * Select **Next**
  12. **Pipeline Definition** :

     * Leave the default SQL query: 
           
           INSERT INTO ecommerce_sink SELECT * FROM ecommerce_stream;

     * Select **Create Pipeline**
  13. After pipeline creation, note the **Stream ID** for the next step.




## 3\. Send sample data

Send ecommerce events to your pipeline's HTTP endpoint:
    
    
    curl -X POST https://{stream-id}.ingest.cloudflare.com \
      -H "Content-Type: application/json" \
      -d '[
        {
          "user_id": "user_12345",
          "event_type": "purchase",
          "product_id": "widget-001",
          "amount": 29.99
        },
        {
          "user_id": "user_67890",
          "event_type": "view_product",
          "product_id": "widget-002"
        },
        {
          "user_id": "user_12345",
          "event_type": "add_to_cart",
          "product_id": "widget-003",
          "amount": 15.50
        }
      ]'

Replace `{stream-id}` with your actual stream endpoint from the pipeline setup.

## 4\. Validate data in your bucket

  1. In the Cloudflare dashboard, go to the **R2 object storage** page.

  2. Select your bucket: `pipelines-tutorial`.

  3. You should see Iceberg metadata files and data files created by your pipeline. If you are not seeing any files in your bucket, wait a couple of minutes and try again.

  4. The data is organized in the Apache Iceberg format with metadata tracking table versions.




## 5\. Query your data using Basin SQL

Set up your environment to use Basin SQL:
    
    
    export WRANGLER_BASIN_SQL_AUTH_TOKEN=YOUR_API_TOKEN

Or create a `.env` file with:
    
    
    WRANGLER_BASIN_SQL_AUTH_TOKEN=YOUR_API_TOKEN

Where `YOUR_API_TOKEN` is the token you created in step 1. For more information on setting environment variables, refer to [Wrangler system environment variables](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/).

Query your data:

npmyarnpnpm
    
    
    npx wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT user_id, event_type, product_id, amount FROM default.ecommerce WHERE event_type = 'purchase' LIMIT 10"
    
    
    yarn wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT user_id, event_type, product_id, amount FROM default.ecommerce WHERE event_type = 'purchase' LIMIT 10"
    
    
    pnpm wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT user_id, event_type, product_id, amount FROM default.ecommerce WHERE event_type = 'purchase' LIMIT 10"

Replace `YOUR_WAREHOUSE_NAME` with the warehouse name noted during pipeline setup. You can find it in the Cloudflare dashboard under **R2 object storage** > your bucket > **Settings** > **Basin Catalog**.

You can also query this table with any engine that supports Apache Iceberg. To learn more about connecting other engines to Basin Catalog, refer to [Connect to Iceberg engines](https://developers.cloudflare.com/basin-catalog/config-examples/).

## Learn more

### [Streams](https://developers.cloudflare.com/basin-pipelines/streams/)

Learn about configuring streams for data ingestion.

### [Pipelines](https://developers.cloudflare.com/basin-pipelines/pipelines/)

Understand SQL transformations and pipeline configuration.

### [Sinks](https://developers.cloudflare.com/basin-pipelines/sinks/)

Configure data destinations and output formats.

### [Examples](https://developers.cloudflare.com/basin-pipelines/examples/)

Browse end-to-end examples that show how to build with Basin Pipelines.

[PreviousOverview](https://developers.cloudflare.com/basin-pipelines/)[NextOverview](https://developers.cloudflare.com/basin-pipelines/streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/getting-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
