---
url: https://developers.cloudflare.com/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/
title: R2 SQL now supports JOINs, subqueries, and multi-table queries \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.196081+00:00
---

# R2 SQL now supports JOINs, subqueries, and multi-table queries · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 15, 2026

## R2 SQL now supports JOINs, subqueries, and multi-table queries

[Basin SQL](https://developers.cloudflare.com/basin-sql/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.

R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.

#### New capabilities

  * **JOINs** — `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`, `CROSS JOIN`, and implicit joins (comma-separated `FROM` with conditions in `WHERE`)
  * **Subqueries** — `IN` / `NOT IN`, `EXISTS` / `NOT EXISTS`, scalar subqueries in `SELECT` / `WHERE` / `HAVING`, and derived tables (subqueries in `FROM`)
  * **Multi-table CTEs** — `WITH` clauses can reference different tables and include JOINs
  * **Self-joins** — join a table with itself using different aliases
  * **Multi-way joins** — join three or more tables in a single query



#### Examples

#### Two-table JOIN with aggregation
    
    
    SELECT z.domain, z.plan, COUNT(*) AS request_count
    FROM my_namespace.zones z
    INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id
    WHERE z.plan = 'enterprise'
    GROUP BY z.domain, z.plan
    ORDER BY request_count DESC
    LIMIT 20

#### `EXISTS` subquery
    
    
    SELECT z.domain, z.plan
    FROM my_namespace.zones z
    WHERE EXISTS (
        SELECT 1 FROM my_namespace.firewall_events f
        WHERE f.zone_id = z.zone_id AND f.action = 'block'
    )
    ORDER BY z.domain
    LIMIT 20

#### Multi-table CTE with JOIN
    
    
    WITH top_zones AS (
        SELECT zone_id, COUNT(*) AS req_count
        FROM my_namespace.http_requests
        GROUP BY zone_id
        ORDER BY req_count DESC
        LIMIT 50
    ),
    zone_threats AS (
        SELECT zone_id, COUNT(*) AS threat_count
        FROM my_namespace.firewall_events
        WHERE risk_score > 0.5
        GROUP BY zone_id
    )
    SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count
    FROM top_zones tz
    LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id
    ORDER BY tz.req_count DESC
    LIMIT 20

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance with joins, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).
