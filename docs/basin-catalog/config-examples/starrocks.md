---
url: https://developers.cloudflare.com/basin-catalog/config-examples/starrocks/
title: StarRocks \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:23.183543+00:00
---

# StarRocks · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/config-examples/starrocks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Connect to Iceberg engines
  4. /StarRocks



# StarRocks

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/config-examples/starrocks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesExample usage

Below is an example of using [StarRocks ↗︎](https://docs.starrocks.io/docs/data_source/catalog/iceberg/iceberg_catalog/#rest) to connect, query, modify data from Basin Catalog (read-write).

## Prerequisites

  * Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket).
  * [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
  * A running [StarRocks ↗︎](https://www.starrocks.io/) frontend instance. You can use the [all-in-one ↗︎](https://docs.starrocks.io/docs/quick_start/shared-nothing/#launch-starrocks) docker setup.



## Example usage

In your running StarRocks instance, run these commands:
    
    
    -- Create an Iceberg catalog named `r2` and set it as the current catalog
    
    CREATE EXTERNAL CATALOG r2
    PROPERTIES
    (
        "type" = "iceberg",
        "iceberg.catalog.type" = "rest",
        "iceberg.catalog.uri" = "<r2_catalog_uri>",
        "iceberg.catalog.security" = "oauth2",
        "iceberg.catalog.oauth2.token" = "<r2_api_token>",
        "iceberg.catalog.warehouse" = "<r2_warehouse_name>"
    );
    
    SET CATALOG r2;
    
    -- Create a database and display all databases in newly connected catalog
    
    CREATE DATABASE testdb;
    
    SHOW DATABASES FROM r2;
    
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | testdb             |
    +--------------------+
    2 rows in set (0.66 sec)

[PreviousSpark (Scala)](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/)[NextTrino](https://developers.cloudflare.com/basin-catalog/config-examples/trino/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/config-examples/starrocks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
