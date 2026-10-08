---
url: https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/
title: Manage pipelines \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:24.802027+00:00
---

# Manage pipelines · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /[Pipelines](https://developers.cloudflare.com/basin-pipelines/pipelines/)
  4. /Manage pipelines



# Manage pipelines

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a pipeline Dashboard Wrangler CLI SQL transformationsView pipeline configuration Dashboard Wrangler CLIDelete a pipeline Dashboard Wrangler CLILimitations

Learn how to:

  * Create pipelines with SQL transformations
  * View pipeline configuration and SQL
  * Delete pipelines when no longer needed



## Create a pipeline

Pipelines execute SQL statements that define how data flows from streams to sinks.

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

[ Go to **Pipelines** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/overview)
  2. Select **Create Pipeline** to launch the pipeline creation wizard.

  3. Follow the wizard to configure your stream, sink, and SQL transformation.




### Wrangler CLI

To create a pipeline, run the `basin pipelines create` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines create my-pipeline --sql "INSERT INTO my_sink SELECT * FROM my_stream"
    
    
    yarn wrangler basin pipelines create my-pipeline --sql "INSERT INTO my_sink SELECT * FROM my_stream"
    
    
    pnpm wrangler basin pipelines create my-pipeline --sql "INSERT INTO my_sink SELECT * FROM my_stream"

You can also provide SQL from a file:

npmyarnpnpm
    
    
    npx wrangler basin pipelines create my-pipeline --sql-file pipeline.sql
    
    
    yarn wrangler basin pipelines create my-pipeline --sql-file pipeline.sql
    
    
    pnpm wrangler basin pipelines create my-pipeline --sql-file pipeline.sql

Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the `basin pipelines setup` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

### SQL transformations

Pipelines support SQL statements for data transformation. For complete syntax, supported functions, and data types, see the [SQL reference](https://developers.cloudflare.com/basin-pipelines/sql-reference/).

Common patterns include:

#### Basic data flow

Transfer all data from stream to sink:
    
    
    INSERT INTO my_sink SELECT * FROM my_stream

#### Filtering events

Filter events based on conditions:
    
    
    INSERT INTO my_sink
    SELECT * FROM my_stream
    WHERE event_type = 'purchase' AND amount > 100

#### Selecting specific fields

Choose only the fields you need:
    
    
    INSERT INTO my_sink
    SELECT user_id, event_type, timestamp, amount
    FROM my_stream

#### Transforming data

Apply transformations to fields:
    
    
    INSERT INTO my_sink
    SELECT
      user_id,
      UPPER(event_type) as event_type,
      timestamp,
      amount * 1.1 as amount_with_tax
    FROM my_stream

#### Route one stream to multiple tables

A single pipeline can run multiple `INSERT` statements, separated by semicolons. Each statement reads from the same stream and writes to a different sink, so you can route ("fan out") events from one stream into several tables based on their content.

This avoids running a separate pipeline for each destination. Each statement filters the stream with its own `WHERE` clause and projects only the columns relevant to that table. This can also be a used as a cost optimization as you will be [billed](https://developers.cloudflare.com/basin-pipelines/platform/pricing/) once for the transformations, not per statement.
    
    
    INSERT INTO purchases_sink
    SELECT user_id, product_id, amount FROM my_stream
    WHERE event_type = 'purchase';
    
    INSERT INTO page_views_sink
    SELECT user_id, product_id FROM my_stream
    WHERE event_type = 'view_product';

For a complete example that fans a live event stream out into five tables, refer to [Fan out a stream to multiple Iceberg tables](https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/).

## View pipeline configuration

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

  2. Select a pipeline to view its SQL transformation, connected streams/sinks, and associated metrics.




### Wrangler CLI

To view a specific pipeline, run the `basin pipelines get` command with either the pipeline ID or pipeline name:

npmyarnpnpm
    
    
    npx wrangler basin pipelines get <PIPELINE_NAME_OR_ID>
    
    
    yarn wrangler basin pipelines get <PIPELINE_NAME_OR_ID>
    
    
    pnpm wrangler basin pipelines get <PIPELINE_NAME_OR_ID>

To list all pipelines in your account, run the `basin pipelines list` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines list
    
    
    yarn wrangler basin pipelines list
    
    
    pnpm wrangler basin pipelines list

## Delete a pipeline

Deleting a pipeline stops data flow from the connected stream to sink.

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

  2. Select the pipeline you want to delete. 3. In the **Settings** tab, and select **Delete**.




### Wrangler CLI

To delete a pipeline, run the `basin pipelines delete` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines delete <PIPELINE_ID>
    
    
    yarn wrangler basin pipelines delete <PIPELINE_ID>
    
    
    pnpm wrangler basin pipelines delete <PIPELINE_ID>

Caution

Deleting a pipeline immediately stops data flow between the stream and sink.

## Limitations

Pipeline SQL cannot be modified after creation. To change the SQL transformation, you must delete and recreate the pipeline.

[PreviousOverview](https://developers.cloudflare.com/basin-pipelines/pipelines/)[NextSQL data types](https://developers.cloudflare.com/basin-pipelines/sql-reference/sql-data-types/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/pipelines/manage-pipelines.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
