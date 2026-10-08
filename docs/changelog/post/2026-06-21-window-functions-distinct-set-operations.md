---
url: https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/
title: R2 SQL now supports window functions, DISTINCT, and set operations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.253628+00:00
---

# R2 SQL now supports window functions, DISTINCT, and set operations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 22, 2026

## R2 SQL now supports window functions, DISTINCT, and set operations

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 SQL now supports window functions, `SELECT DISTINCT`, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### New capabilities

  * **Window functions** — `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PERCENT_RANK`, `CUME_DIST`, `NTILE`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE`, and aggregates with an `OVER (...)` clause, including `PARTITION BY` and explicit frames
  * **QUALIFY** — filter rows based on a window function result
  * **DISTINCT** — `SELECT DISTINCT`, `DISTINCT ON (...)`, and the `DISTINCT` modifier on aggregates such as `COUNT(DISTINCT ...)`
  * **Set operations** — `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`
  * **Grouping extensions** — `GROUPING SETS`, `ROLLUP`, and `CUBE`
  * **Exact aggregates** — `MEDIAN`, `PERCENTILE_CONT`, `ARRAY_AGG`, and `STRING_AGG`



#### Examples

#### Rank rows with a window function
    
    
    SELECT customer_id, region,
           ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region
    FROM my_namespace.sales_data

#### Filter with QUALIFY
    
    
    SELECT customer_id, region, total_amount
    FROM my_namespace.sales_data
    QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) <= 3

#### Combine tables with a set operation
    
    
    SELECT customer_id FROM my_namespace.sales_data
    EXCEPT
    SELECT customer_id FROM my_namespace.archived_sales

The named `WINDOW` clause is not supported — inline the `OVER (...)` specification at each call site. For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For supported features and performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).
