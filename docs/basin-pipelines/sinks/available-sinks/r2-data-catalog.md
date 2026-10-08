---
url: https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/
title: Basin Catalog \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.452163+00:00
---

# Basin Catalog · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

[Sinks](https://developers.cloudflare.com/basin-pipelines/sinks/)

  4. /Available sinks
  5. /Basin Catalog



# Basin Catalog

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2-data-catalog/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFormat Compression options Row group sizeBatching and rolling policy Roll interval Roll sizeAuthentication

Basin Catalog sinks write processed data from pipelines as [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables to [Basin Catalog](https://developers.cloudflare.com/basin-catalog/). Iceberg tables provide ACID transactions, schema evolution, and time travel capabilities for analytics workloads.

To create a Basin Catalog sink, run the `basin pipelines sinks create` command and specify the sink type, target bucket, namespace, and table name:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks create my-sink --type basin-catalog --bucket my-bucket --namespace my_namespace --table my_table --catalog-token YOUR_CATALOG_TOKEN
    
    
    yarn wrangler basin pipelines sinks create my-sink --type basin-catalog --bucket my-bucket --namespace my_namespace --table my_table --catalog-token YOUR_CATALOG_TOKEN
    
    
    pnpm wrangler basin pipelines sinks create my-sink --type basin-catalog --bucket my-bucket --namespace my_namespace --table my_table --catalog-token YOUR_CATALOG_TOKEN

Use `basin-catalog` for new sinks. The legacy `r2-data-catalog` value also remains valid, and existing sink configurations do not need to change.

The sink will create the specified namespace and table if they do not exist. Sinks cannot be created for existing Iceberg tables.

## Format

Basin Catalog sinks only support Parquet format. JSON format is not supported for Iceberg tables.

### Compression options

Configure Parquet compression for optimal storage and query performance:
    
    
    --compression zstd

**Available compression options:**

  * `zstd` (default) - Best compression ratio
  * `snappy` \- Fastest compression
  * `gzip` \- Good compression, widely supported
  * `lz4` \- Fast compression with reasonable ratio
  * `uncompressed` \- No compression



### Row group size

[Row groups ↗︎](https://parquet.apache.org/docs/file-format/configurations/) are sets of rows in a Parquet file that are stored together, affecting memory usage and query performance. Configure the target row group size in MB:
    
    
    --target-row-group-size 256

## Batching and rolling policy

Control when data is written to Iceberg tables. Configure based on your needs:

  * **Lower values** : More frequent writes, smaller files, lower latency
  * **Higher values** : Less frequent writes, larger files, better query performance



### Roll interval

Set how often files are written (default: 300 seconds, minimum: 60 seconds):
    
    
    --roll-interval 60  # Write files every 60 seconds

The minimum interval for Basin Catalog sinks is 60 seconds to prevent compaction issues. Iceberg tables require periodic compaction to merge small files into larger ones for optimal query performance. Writing too often creates merge conflicts with the compaction process.

### Roll size

Set maximum file size in MB before creating a new file:
    
    
    --roll-size 100  # Create new file after 100MB

## Authentication

Basin Catalog sinks require an API token with [R2 Admin Read & Write permissions](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#create-api-token-in-the-dashboard). This permission grants the sink access to both Basin Catalog and R2 storage.
    
    
    --catalog-token YOUR_CATALOG_TOKEN

[PreviousR2](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2/)[NextOverview](https://developers.cloudflare.com/basin-pipelines/pipelines/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sinks/available-sinks/r2-data-catalog.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
