---
url: https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/
title: PyIceberg \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.809468+00:00
---

# PyIceberg · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Connect to Iceberg engines
  4. /PyIceberg



# PyIceberg

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesExample usage

Below is an example of using [PyIceberg ↗︎](https://py.iceberg.apache.org/) to connect to Basin Catalog.

## Prerequisites

  * Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket).
  * [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
  * Install the [PyIceberg ↗︎](https://py.iceberg.apache.org/#installation) and [PyArrow ↗︎](https://arrow.apache.org/docs/python/install.html) libraries.



## Example usage
    
    
    import pyarrow as pa
    from pyiceberg.catalog.rest import RestCatalog
    from pyiceberg.exceptions import NamespaceAlreadyExistsError
    
    # Define catalog connection details (replace variables)
    WAREHOUSE = "<WAREHOUSE>"
    TOKEN = "<TOKEN>"
    CATALOG_URI = "<CATALOG_URI>"
    
    # Connect to Basin Catalog
    catalog = RestCatalog(
        name="my_catalog",
        warehouse=WAREHOUSE,
        uri=CATALOG_URI,
        token=TOKEN,
    )
    
    # Create default namespace
    catalog.create_namespace("default")
    
    # Create simple PyArrow table
    df = pa.table({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
    })
    
    # Create an Iceberg table
    test_table = ("default", "my_table")
    table = catalog.create_table(
        test_table,
        schema=df.schema,
    )

[PreviousDuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/)[NextSnowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/config-examples/pyiceberg.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
