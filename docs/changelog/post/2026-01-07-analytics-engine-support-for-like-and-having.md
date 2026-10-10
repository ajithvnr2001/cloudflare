---
url: https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/
title: Workers Analytics Engine SQL now supports filtering using HAVING and LIKE \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.418879+00:00
---

# Workers Analytics Engine SQL now supports filtering using HAVING and LIKE · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 7, 2026

## Workers Analytics Engine SQL now supports filtering using HAVING and LIKE

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use the `HAVING` clause and `LIKE` pattern matching operators in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/).

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.

#### Filtering using `HAVING`

The `HAVING` clause complements the `WHERE` clause by enabling you to filter groups based on aggregate values. While `WHERE` filters rows before aggregation, `HAVING` filters groups after aggregation is complete.

You can use `HAVING` to filter groups where the average exceeds a threshold:
    
    
    SELECT
        blob1 AS probe_name,
        avg(double1) AS average_temp
    FROM temperature_readings
    GROUP BY probe_name
    HAVING average_temp > 10

You can also filter groups based on aggregates such as the number of items in the group:
    
    
    SELECT
        blob1 AS probe_name,
        count() AS num_readings
    FROM temperature_readings
    GROUP BY probe_name
    HAVING num_readings > 100

#### Pattern matching using `LIKE`

The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:

  * `LIKE` \- case-sensitive pattern matching
  * `NOT LIKE` \- case-sensitive pattern exclusion
  * `ILIKE` \- case-insensitive pattern matching
  * `NOT ILIKE` \- case-insensitive pattern exclusion



Pattern matching supports two wildcard characters: `%` (matches zero or more characters) and `_` (matches exactly one character).

You can match strings starting with a prefix:
    
    
    SELECT *
    FROM logs
    WHERE blob1 LIKE 'error%'

You can also match file extensions (case-insensitive):
    
    
    SELECT *
    FROM requests
    WHERE blob2 ILIKE '%.jpg'

Another example is excluding strings containing specific text:
    
    
    SELECT *
    FROM events
    WHERE blob3 NOT ILIKE '%debug%'

#### Ready to get started?

Learn more about the [`HAVING` clause](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/statements/#having-clause) or [pattern matching operators](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators) in the Workers Analytics Engine SQL reference documentation.
