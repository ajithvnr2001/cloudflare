---
url: https://developers.cloudflare.com/changelog/post/2025-12-12-aggregation-support-and-more/
title: R2 SQL now supports aggregations and schema discovery \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:31.665579+00:00
---

# R2 SQL now supports aggregations and schema discovery · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-12-aggregation-support-and-more/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 12, 2025

## R2 SQL now supports aggregations and schema discovery

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-12-aggregation-support-and-more/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 SQL now supports aggregation functions, `GROUP BY`, `HAVING`, along with schema discovery commands to make it easy to explore your data catalog.

#### Aggregation Functions

You can now perform aggregations on Apache Iceberg tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) using standard SQL functions including `COUNT(*)`, `SUM()`, `AVG()`, `MIN()`, and `MAX()`. Combine these with `GROUP BY` to analyze data across dimensions, and use `HAVING` to filter aggregated results.
    
    
    -- Calculate average transaction amounts by department
    SELECT department, COUNT(*), AVG(total_amount)
    FROM my_namespace.sales_data
    WHERE region = 'North'
    GROUP BY department
    HAVING COUNT(*) > 50
    ORDER BY AVG(total_amount) DESC
    
    
    -- Find high-value departments
    SELECT department, SUM(total_amount)
    FROM my_namespace.sales_data
    GROUP BY department
    HAVING SUM(total_amount) > 50000

#### Schema Discovery

New metadata commands make it easy to explore your data catalog and understand table structures:

  * `SHOW DATABASES` or `SHOW NAMESPACES` \- List all available namespaces
  * `SHOW TABLES IN namespace_name` \- List tables within a namespace
  * `DESCRIBE namespace_name.table_name` \- View table schema and column types


    
    
    ❯ npx wrangler r2 sql query "{ACCOUNT_ID}_{BUCKET_NAME}" "DESCRIBE default.sales_data;"
    
     ⛅️ wrangler 4.54.0
    ─────────────────────────────────────────────
    
    ┌──────────────────┬────────────────┬──────────┬─────────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐
    │ column_name      │ type           │ required │ initial_default │ write_default │ doc                                                                                               │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_id          │ BIGINT         │ false    │                 │               │ Unique identifier for each sales transaction                                                      │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_timestamp   │ TIMESTAMPTZ    │ false    │                 │               │ Exact date and time when the sale occurred (used for partitioning)                                │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ department       │ TEXT           │ false    │                 │               │ Product department (8 categories: Electronics, Beauty, Home, Toys, Sports, Food, Clothing, Books) │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ category         │ TEXT           │ false    │                 │               │ Product category grouping (4 categories: Premium, Standard, Budget, Clearance)                    │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ region           │ TEXT           │ false    │                 │               │ Geographic sales region (5 regions: North, South, East, West, Central)                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ product_id       │ INT            │ false    │                 │               │ Unique identifier for the product sold                                                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ quantity         │ INT            │ false    │                 │               │ Number of units sold in this transaction (range: 1-50)                                            │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ unit_price       │ DECIMAL(10, 2) │ false    │                 │               │ Price per unit in dollars (range: $5.00-$500.00)                                                  │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ total_amount     │ DECIMAL(10, 2) │ false    │                 │               │ Total sale amount before tax (quantity × unit_price with discounts applied)                       │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ discount_percent │ INT            │ false    │                 │               │ Discount percentage applied to this sale (0-50%)                                                  │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ tax_amount       │ DECIMAL(10, 2) │ false    │                 │               │ Tax amount collected on this sale                                                                 │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ profit_margin    │ DECIMAL(10, 2) │ false    │                 │               │ Profit margin on this sale as a decimal percentage                                                │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ customer_id      │ INT            │ false    │                 │               │ Unique identifier for the customer who made the purchase                                          │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ is_online_sale   │ BOOLEAN        │ false    │                 │               │ Boolean flag indicating if sale was made online (true) or in-store (false)                        │
    ├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ sale_date        │ DATE           │ false    │                 │               │ Calendar date of the sale (extracted from sale_timestamp)                                         │
    └──────────────────┴────────────────┴──────────┴─────────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘
    Read 0 B across 0 files from R2
    On average, 0 B / s

To learn more about the new aggregation capabilities and schema discovery commands, check out the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). If you're new to R2 SQL, visit our [getting started guide](https://developers.cloudflare.com/basin-sql/get-started/) to begin querying your data.
