---
url: https://developers.cloudflare.com/basin-catalog/config-examples/spark-python/
title: Spark (PySpark) \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.983697+00:00
---

# Spark (PySpark) · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/config-examples/spark-python/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Connect to Iceberg engines
  4. /Spark (PySpark)



# Spark (PySpark)

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/config-examples/spark-python/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesExample usage

Below is an example of using [PySpark ↗︎](https://spark.apache.org/docs/latest/api/python/index.html) to connect to Basin Catalog.

## Prerequisites

  * Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket).
  * [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
  * Install the [PySpark ↗︎](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) library.



## Example usage
    
    
    from pyspark.sql import SparkSession
    
    # Define catalog connection details (replace variables)
    WAREHOUSE = "<WAREHOUSE>"
    TOKEN = "<TOKEN>"
    CATALOG_URI = "<CATALOG_URI>"
    
    # Build Spark session with Iceberg configurations
    spark = SparkSession.builder \
      .appName("R2DataCatalogExample") \
      .config('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1,org.apache.iceberg:iceberg-aws-bundle:1.6.1') \
      .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
      .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
      .config("spark.sql.catalog.my_catalog.type", "rest") \
      .config("spark.sql.catalog.my_catalog.uri", CATALOG_URI) \
      .config("spark.sql.catalog.my_catalog.warehouse", WAREHOUSE) \
      .config("spark.sql.catalog.my_catalog.token", TOKEN) \
      .config("spark.sql.catalog.my_catalog.header.X-Iceberg-Access-Delegation", "vended-credentials") \
      .config("spark.sql.catalog.my_catalog.s3.remote-signing-enabled", "false") \
      .config("spark.sql.defaultCatalog", "my_catalog") \
      .getOrCreate()
    spark.sql("USE my_catalog")
    
    # Create namespace if it does not exist
    spark.sql("CREATE NAMESPACE IF NOT EXISTS default")
    
    # Create a table in the namespace using Iceberg
    spark.sql("""
        CREATE TABLE IF NOT EXISTS default.my_table (
            id BIGINT,
            name STRING
        )
        USING iceberg
    """)
    
    # Create a simple DataFrame
    df = spark.createDataFrame(
        [(1, "Alice"), (2, "Bob"), (3, "Charlie")],
        ["id", "name"]
    )
    
    # Write the DataFrame to the Iceberg table
    df.write \
        .format("iceberg") \
        .mode("append") \
        .save("default.my_table")
    
    # Read the data back from the Iceberg table
    result_df = spark.read \
        .format("iceberg") \
        .load("default.my_table")
    
    result_df.show()

[PreviousSnowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/)[NextSpark (Scala)](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/config-examples/spark-python.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
