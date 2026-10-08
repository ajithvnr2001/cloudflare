---
url: https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/
title: Manage sinks \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.561192+00:00
---

# Manage sinks · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /[Sinks](https://developers.cloudflare.com/basin-pipelines/sinks/)
  4. /Manage sinks



# Manage sinks

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a sink Dashboard Wrangler CLIView sink configuration Dashboard Wrangler CLIDelete a sink Dashboard Wrangler CLILimitations

Learn how to:

  * Create and configure sinks for data storage
  * View sink configuration
  * Delete sinks when no longer needed



## Create a sink

Sinks are made available to pipelines as SQL tables using the sink name (for example, `INSERT INTO my_sink SELECT * FROM my_stream`).

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

[ Go to **Pipelines** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/overview)
  2. Select **Create Pipeline** to launch the pipeline creation wizard.

  3. Complete the wizard to create your sink along with the associated stream and pipeline.




### Wrangler CLI

To create a sink, run the `basin pipelines sinks create` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket
    
    
    yarn wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket
    
    
    pnpm wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket

For sink-specific configuration options, refer to [Available sinks](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/).

Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the `basin pipelines setup` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

## View sink configuration

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Sinks**.

  2. Select a sink to view its configuration.




### Wrangler CLI

To view a specific sink, run the `basin pipelines sinks get` command with either the sink ID or sink name:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks get <SINK_NAME_OR_ID>
    
    
    yarn wrangler basin pipelines sinks get <SINK_NAME_OR_ID>
    
    
    pnpm wrangler basin pipelines sinks get <SINK_NAME_OR_ID>

To list all sinks in your account, run the `basin pipelines sinks list` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks list
    
    
    yarn wrangler basin pipelines sinks list
    
    
    pnpm wrangler basin pipelines sinks list

## Delete a sink

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Sinks**.

  2. Select the sink you want to delete.

  3. In the **Settings** tab, go to **General** , and select **Delete**.




### Wrangler CLI

To delete a sink, run the `basin pipelines sinks delete` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks delete <SINK_ID>
    
    
    yarn wrangler basin pipelines sinks delete <SINK_ID>
    
    
    pnpm wrangler basin pipelines sinks delete <SINK_ID>

Caution

Deleting a sink stops all data writes to that destination.

## Limitations

  * Sinks cannot be modified after creation. To change sink configuration, you must delete and recreate the sink.
  * The Basin Catalog Sink does not currently support writing to R2 buckets into a different jurisdiction.



[PreviousOverview](https://developers.cloudflare.com/basin-pipelines/sinks/)[NextR2](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sinks/manage-sinks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
