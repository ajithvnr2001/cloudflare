---
url: https://developers.cloudflare.com/basin-sql/
title: Basin SQL \u00b7 Basin SQL docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.437520+00:00
---

# Basin SQL · Basin SQL docs

> Source: https://developers.cloudflare.com/basin-sql/

  1. [Home](https://developers.cloudflare.com/)
  2. /Basin SQL



# Basin SQL

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-sql/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Query Apache Iceberg tables managed by Basin Catalog using SQL.

Basin SQL is Cloudflare's serverless, distributed, analytics query engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [Basin Catalog](https://developers.cloudflare.com/basin-catalog/). Basin SQL is designed to efficiently query large amounts of data by automatically utilizing file pruning, Cloudflare's distributed compute, and R2 object storage.

Basin SQL is now Generally Available

Basin SQL, formerly known as R2 SQL, is now Generally Available. Existing R2 SQL APIs continue to work and will be deprecated in the future.

To report bugs or give feedback, go to the [**#basin-sql Discord channel** ↗︎](https://discord.cloudflare.com/). If you are having issues with Wrangler, report issues in the [**Wrangler GitHub repository** ↗︎](https://github.com/cloudflare/workers-sdk/issues/new/choose).

npmyarnpnpm
    
    
    npx wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT * FROM default.transactions LIMIT 10"
    
    
    yarn wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT * FROM default.transactions LIMIT 10"
    
    
    pnpm wrangler basin sql query "YOUR_WAREHOUSE_NAME" "SELECT * FROM default.transactions LIMIT 10"

Create an end-to-end data pipeline by following [this step by step guide](https://developers.cloudflare.com/basin-sql/get-started/), which shows you how to stream events into an Apache Iceberg table and query it with Basin SQL.

[NextGetting started](https://developers.cloudflare.com/basin-sql/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-sql/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
