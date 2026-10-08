---
url: https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/
title: DuckDB \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.685423+00:00
---

# DuckDB · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Connect to Iceberg engines
  4. /DuckDB



# DuckDB

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesExample usage

Below is an example of using [DuckDB ↗︎](https://duckdb.org/) to connect to Basin Catalog. For more information on connecting to Basin Catalog with DuckDB, refer to [DuckDB documentation ↗︎](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs#r2-catalog).

## Prerequisites

  * Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket).
  * [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
  * Install [DuckDB ↗︎](https://duckdb.org/docs/installation/). 
    * Note: [DuckDB 1.4.0 ↗︎](https://github.com/duckdb/duckdb/releases/tag/v1.4.0) or greater is required to attach and write to [Iceberg REST Catalogs ↗︎](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs).
  * Note: DuckDB [does not currently support ↗︎](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs#limitations-for-update-and-delete) `DELETE` on partitioned tables.



## Example usage

In the [DuckDB CLI ↗︎](https://duckdb.org/docs/stable/clients/cli/overview.html) (Command Line Interface), run the following commands:
    
    
    -- Install the Iceberg DuckDB extension if needed, then load the extension.
    INSTALL iceberg;
    LOAD iceberg;
    
    -- Install and load httpfs extension for reading/writing files over HTTP(S).
    INSTALL httpfs;
    LOAD httpfs;
    
    -- Create a DuckDB secret to store Basin Catalog credentials.
    CREATE SECRET r2_secret (
        TYPE ICEBERG,
        TOKEN '<token>'
    );
    
    -- Attach Basin Catalog with the following ATTACH statement.
    ATTACH '<warehouse_name>' AS my_r2_catalog (
        TYPE ICEBERG,
        ENDPOINT '<catalog_uri>'
    );
    
    -- Create the default schema in the catalog and set it as the active schema.
    CREATE SCHEMA my_r2_catalog.default;
    USE my_r2_catalog.default;
    
    -- Create and populate a sample Iceberg table with data.
    CREATE TABLE my_iceberg_table AS SELECT a FROM range(4) t(a);
    
    -- Show all available tables.
    SHOW ALL TABLES;
    
    -- Query the Iceberg table you just created.
    SELECT * FROM my_r2_catalog.default.my_iceberg_table;

[PreviousTable maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/)[NextPyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/config-examples/duckdb.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
