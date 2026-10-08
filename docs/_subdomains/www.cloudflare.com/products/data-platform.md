---
url: https://www.cloudflare.com/products/data-platform/
title: Cloudflare Basin - Ingest, Catalog & Query Analytics Data
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.815457+00:00
---

# Cloudflare Basin - Ingest, Catalog & Query Analytics Data

> Source: https://www.cloudflare.com/products/data-platform/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  Ingest, Catalog & Query 

###  Build analytics-ready data warehouses and lakehouses on R2. Stream events via Basin Pipelines, catalog tables with Apache Iceberg, and query with Basin SQL or any compatible engine—all without egress fees. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/basin/)

**Zero egress fees**

Query your data from any cloud, data platform, or region without incurring transfer costs. R2 never charges for egress.

**Always fast**

Automatic table maintenance, such as compaction and snapshot expiration, keeps your data performant without the need for scheduling manual maintenance tasks.

**Serverless ingestion**

Stream and process events via HTTP endpoints or Workers bindings. No Apache Kafka, no Apache Flink, no infrastructure management.

**SQL at the edge**

Query Iceberg tables directly with Basin SQL or the wrangler CLI. Distributed compute, automatic file pruning.

**No infrastructure**

No servers to provision, no clusters to manage. Just define a schema, stream data, and query.

**Open table format**

Apache Iceberg tables means your data is accessible by your favorite query engines—Apache Spark, Snowflake, Trino, DuckDB, and more—via R2 Data Catalog's standard Iceberg REST API.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Basin`

####  A complete, serverless data platform built on R2 

Pipelines ingests and transforms your data, R2 stores it as Iceberg tables, and Basin SQL or your preferred query engine analyzes it. No infrastructure to manage, no egress fees to worry about. 

[ See more  ](https://developers.cloudflare.com/basin/)

Log analytics at scale 

Ingest server logs, application events, and telemetry data. Query with SQL to debug issues, track performance, and build operational dashboards.

Business intelligence pipelines 

Stream clickstream data, user events, and transactions. Connect your BI tools directly to Iceberg tables for real-time reporting.

ETL without the infrastructure 

Transform data with SQL at ingestion time. Filter, enrich, and validate before writing to storage—no separate ETL service required.

Multi-cloud analytics 

Store data once in R2, query from anywhere. Run Spark jobs in AWS, Snowflake queries from your data warehouse, or DuckDB locally—all hitting the same tables.

### From streaming events to SQL queries in minutes.

Define a schema, stream data via Pipelines, and query with R2 SQL or connect your favorite Iceberg-compatible engine.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  terminal  analytics.py 

01  02  03  04  05  06  07  08  09  10  11  12  13 
    
    
    export default {  async fetch(request, env, ctx): Promise<Response> {    // Stream events to Basin Pipelines    await env.ANALYTICS.send([      {        user_id: 'user_12345',        event_type: 'purchase',        product_id: 'widget-001',        amount: 29.99,      },    ]);
        return new Response('Event ingested');  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10 
    
    
    # Query your Iceberg tables directlynpx wrangler r2 sql query "my-warehouse" "SELECT    user_id,    event_type,    SUM(amount)FROM default.eventsWHERE event_type = 'purchase'GROUP BY user_id, event_typeLIMIT 10"

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15 
    
    
    from pyspark.sql import SparkSession
    # Connect to Basin Catalogspark = SparkSession.builder \  .appName("R2Analytics") \  .config("spark.sql.catalog.r2", "org.apache.iceberg.spark.SparkCatalog") \  .config("spark.sql.catalog.r2.type", "rest") \  .config("spark.sql.catalog.r2.uri", CATALOG_URI) \  .config("spark.sql.catalog.r2.warehouse", WAREHOUSE) \  .config("spark.sql.catalog.r2.token", TOKEN) \  .getOrCreate()
    # Query your data—same tables, any enginedf = spark.sql("SELECT * FROM r2.default.events")df.show()

Stream data via Pipelines 

Send events to [Pipelines](https://developers.cloudflare.com/pipelines/) via HTTP endpoints or Workers bindings. Data is automatically written to Iceberg tables in R2.

Query Iceberg tables directly 

Use [R2 SQL](https://developers.cloudflare.com/r2-sql/) to query your data with standard SQL. Distributed compute and automatic file pruning for fast analytics.

Use any Iceberg-compatible engine 

Connect Spark, Snowflake, Trino, DuckDB, or any engine that supports Iceberg. R2 Data Catalog exposes a [standard REST API](https://developers.cloudflare.com/r2/data-catalog/config-examples/).

Anomaly 

#### "

####  We moved our entire company's data pipeline to Basin Pipelines, Catalog, and SQL, replacing a complex AWS S3 and Athena setup with a cleaner, serverless architecture that reliably handles all of our event data. " 

Dax Raad  Co-Founder 

######  Deploy in seconds 

Get started with a single command.

npmpnpmyarn

$ █

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Basin runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

[ Compute ](https://www.cloudflare.com/products/#compute)

[ Browser Run  Automated browsers  ](https://www.cloudflare.com/products/browser-run/)

[ Containers  Any language, anywhere  ](https://www.cloudflare.com/products/containers/)

[ Durable Objects  Stateful compute  ](https://www.cloudflare.com/products/durable-objects/)

[ Sandboxes  Secure code execution  ](https://www.cloudflare.com/products/sandboxes/)

[ Workers  Global serverless functions  ](https://www.cloudflare.com/products/workers/)

[ Workers for Platforms  Programmable Platform Solutions  ](https://www.cloudflare.com/products/workers-for-platforms/)

[ Workflows  Process orchestration  ](https://www.cloudflare.com/products/workflows/)

[ Storage ](https://www.cloudflare.com/products/#storage)

[ Artifacts  Git-native versioned storage  ](https://www.cloudflare.com/products/artifacts/)

[ D1  Serverless SQL  ](https://www.cloudflare.com/products/d1/)

[ Basin  Ingest, catalog & query data  ](https://www.cloudflare.com/products/data-platform/)

[ Hyperdrive  Global databases  ](https://www.cloudflare.com/products/hyperdrive/)

[ K2  Publish and subscribe to durable, ordered event streams  ](https://www.cloudflare.com/products/k2/)

[ Queues  Message processing  ](https://www.cloudflare.com/products/queues/)

[ R2  Egress-free storage  ](https://www.cloudflare.com/products/r2/)

[ KV  Ultra-fast key-value storage  ](https://www.cloudflare.com/products/kv/)

[ AI ](https://www.cloudflare.com/products/#ai)

[ Agents  Build stateful AI agents  ](https://www.cloudflare.com/products/agents/)

[ AI Gateway  AI observability  ](https://www.cloudflare.com/products/ai-gateway/)

[ AI Search  Instant retrieval  ](https://www.cloudflare.com/products/ai-search/)

[ Vectorize  Vector database  ](https://www.cloudflare.com/products/vectorize/)

[ Workers AI  Edge AI models  ](https://www.cloudflare.com/products/workers-ai/)

[ SASE / Zero Trust ](https://www.cloudflare.com/products/#sase)

[ SASE  Cloudflare SASE platform  ](https://www.cloudflare.com/sase/)

[ Access  Zero trust access to private resources  ](https://www.cloudflare.com/products/access/)

[ CASB  SaaS and cloud posture  ](https://www.cloudflare.com/products/casb/)

[ Data Loss Prevention  Protect sensitive data  ](https://www.cloudflare.com/products/dlp/)

[ Gateway  Web filtering  ](https://www.cloudflare.com/products/gateway/)

[ Browser Isolation  Secure web browsing  ](https://www.cloudflare.com/products/browser-isolation/)

[ WAN  Cloud-delivered networking  ](https://www.cloudflare.com/products/wan/)

[ Email Security  Phishing protection  ](https://www.cloudflare.com/products/email-security/)

[ Security ](https://www.cloudflare.com/products/#security)

[ DDoS Protection  Mitigation Solutions  ](https://www.cloudflare.com/products/ddos/)

[ Rate Limiting  Abuse prevention  ](https://www.cloudflare.com/products/rate-limiting/)

[ SSL  Secure Your Site with SSL  ](https://www.cloudflare.com/products/ssl/)

[ Turnstile  A CAPTCHA Replacement Solution  ](https://www.cloudflare.com/products/turnstile/)

[ WAF  Web Application Firewall  ](https://www.cloudflare.com/products/waf/)

[ Magic Transit  DDoS Protection for Networks  ](https://www.cloudflare.com/products/magic-transit/)

[ Client-Side Security  Prevent browser supply chain attacks  ](https://www.cloudflare.com/products/client-side-security/)

[ Bot Management  Block bad bots  ](https://www.cloudflare.com/products/bot-management/)

[ Network & Content Delivery ](https://www.cloudflare.com/products/#network)

[ CDN  Faster delivery & caching  ](https://www.cloudflare.com/products/cdn/)

[ DNS  Fast DNS  ](https://www.cloudflare.com/products/dns/)

[ Load Balancing  Zero downtime  ](https://www.cloudflare.com/products/load-balancing/)

[ TURN / SFU  Real-time infra  ](https://www.cloudflare.com/products/turn-sfu/)

[ Analytics  Web Performance & Security  ](https://www.cloudflare.com/products/analytics/)

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up)[ View docs  ](https://developers.cloudflare.com/)

No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 
