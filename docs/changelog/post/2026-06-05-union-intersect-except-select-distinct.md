---
url: https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/
title: R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:56.957051+00:00
---

# R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 8, 2026

## R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports set operations (`UNION`, `INTERSECT`, `EXCEPT`) and `SELECT DISTINCT`, expanding the range of analytical queries you can run directly on [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### Set operations

Combine the results of multiple `SELECT` statements:

  * **`UNION`** — returns all rows from both queries, removing duplicates
  * **`UNION ALL`** — returns all rows from both queries, including duplicates
  * **`INTERSECT`** — returns only rows that appear in both queries
  * **`EXCEPT`** — returns rows from the first query that do not appear in the second


    
    
    -- Find zones that had either firewall blocks OR high-risk requests
    SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
    UNION
    SELECT zone_id FROM my_namespace.http_requests WHERE risk_score > 0.8
    
    
    -- Find zones with both firewall blocks AND high traffic
    SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
    INTERSECT
    SELECT zone_id FROM my_namespace.http_requests
    GROUP BY zone_id
    HAVING COUNT(*) > 10000
    
    
    -- Find enterprise zones that have not been compacted
    SELECT zone_id FROM my_namespace.zones WHERE plan = 'enterprise'
    EXCEPT
    SELECT zone_id FROM my_namespace.compaction_history

#### Select distinct

Eliminate duplicate rows from query results:
    
    
    SELECT DISTINCT region, department
    FROM my_namespace.sales_data
    WHERE total_amount > 1000
    ORDER BY region, department
    LIMIT 100

For large datasets where approximate results are acceptable, `approx_distinct()` remains a faster alternative for counting unique values.

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).
