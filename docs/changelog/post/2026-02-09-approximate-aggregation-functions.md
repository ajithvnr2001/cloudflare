---
url: https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/
title: R2 SQL now supports approximate aggregation functions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.193339+00:00
---

# R2 SQL now supports approximate aggregation functions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 9, 2026

## R2 SQL now supports approximate aggregation functions

[Basin SQL](https://developers.cloudflare.com/basin-sql/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.

#### New functions

  * `APPROX_PERCENTILE_CONT(column, percentile)` — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.
  * `APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)` — Weighted percentile calculation where each row contributes proportionally to its weight column value.
  * `APPROX_MEDIAN(column)` — Returns the approximate median. Equivalent to `APPROX_PERCENTILE_CONT(column, 0.5)`.
  * `APPROX_DISTINCT(column)` — Returns the approximate number of distinct values. Works on any column type.
  * `APPROX_TOP_K(column, k)` — Returns the `k` most frequent values with their counts as a JSON array.



All functions support `WHERE` filters. All except `APPROX_TOP_K` support `GROUP BY`.

#### Examples
    
    
    -- Percentile analysis on revenue data
    SELECT approx_percentile_cont(total_amount, 0.25),
           approx_percentile_cont(total_amount, 0.5),
           approx_percentile_cont(total_amount, 0.75)
    FROM my_namespace.sales_data
    
    
    -- Median per department
    SELECT department, approx_median(total_amount)
    FROM my_namespace.sales_data
    GROUP BY department
    
    
    -- Approximate distinct customers by region
    SELECT region, approx_distinct(customer_id)
    FROM my_namespace.sales_data
    GROUP BY region
    
    
    -- Top 5 most frequent departments
    SELECT approx_top_k(department, 5)
    FROM my_namespace.sales_data
    
    
    -- Combine approximate and standard aggregations
    SELECT COUNT(*),
           AVG(total_amount),
           approx_percentile_cont(total_amount, 0.5),
           approx_distinct(customer_id)
    FROM my_namespace.sales_data
    WHERE region = 'North'

For the full syntax and additional examples, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/).
