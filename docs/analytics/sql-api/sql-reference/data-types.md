---
url: https://developers.cloudflare.com/analytics/sql-api/sql-reference/data-types/
title: Data types and literals \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.580768+00:00
---

# Data types and literals · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/sql-api/sql-reference/data-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[SQL API](https://developers.cloudflare.com/analytics/sql-api/)

  4. /[SQL language reference](https://developers.cloudflare.com/analytics/sql-api/sql-reference/)
  5. /Data types and literals



# Data types and literals

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/sql-api/sql-reference/data-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLiteralsTimestamp valuesArraysJSON fields

Dataset schemas can expose the following field types:

Type | Description  
---|---  
`String` | UTF-8 text.  
`UInt8`, `UInt16`, `UInt32`, `UInt64` | Unsigned integers.  
`Int64` | Signed integer.  
`Float64` | Double-precision floating-point number.  
`Date` | Calendar date.  
`DateTime` | Timestamp with second precision.  
`DateTime64(3)` | Timestamp with millisecond precision.  
`Array(type)` | List of values of one scalar type.  
`Json` | Object with dynamically typed values.  
  
## Literals

The SQL API supports integer, floating-point, string, and Boolean literals.
    
    
    SELECT
      42 AS integer_value,
      3.14 AS float_value,
      'example' AS string_value,
      TRUE AS boolean_value
    FROM events.httpRequests
    WHERE accountTag = '<ACCOUNT_TAG>'
      AND timestamp >= '2026-09-15T00:00:00Z'
    LIMIT 1

Escape a single quote inside a string according to standard SQL string literal syntax.

Standalone `NULL` literals are not supported. Expressions can still produce null values, and `IS NULL` and `IS NOT NULL` predicates are supported.

## Timestamp values

Use an ISO 8601 timestamp with a timezone:
    
    
    timestamp >= '2026-09-15T08:30:00Z'
    timestamp >= '2026-09-15T10:30:00+02:00'

The API normalizes timestamp values to UTC. A date without a time is interpreted as midnight UTC:
    
    
    timestamp >= '2026-09-15'

A date and time without a timezone is rejected. For example, do not use `'2026-09-15T08:30:00'`.

## Arrays

An array field can only be selected as a complete, top-level result field:
    
    
    SELECT botTags
    FROM logs.httpRequests
    WHERE zoneTag = '<ZONE_TAG>'
      AND timestamp >= '2026-09-15T00:00:00Z'
    LIMIT 10

Array filtering, grouping, sorting, aggregation, indexing, and unnesting are not supported.

## JSON fields

Some datasets expose unstructured fields as JSON objects. You can select the complete object or one exact top-level key:
    
    
    SELECT attributes, attributes['http.method'] AS method
    FROM logs.workersLogs
    WHERE accountTag = '<ACCOUNT_TAG>'
      AND timestamp >= NOW() - INTERVAL '1' HOUR
    LIMIT 10

Key lookup is exact. A key such as `http.method` is one top-level key, not a path through a nested object. A missing key returns JSON `null`.

Depending on the dataset backend, an exact-key lookup can also be compared with a string, number, or Boolean literal, grouped, or passed to `SUM` and `AVG`:
    
    
    SELECT attributes['http.method'] AS method, COUNT(*) AS events
    FROM logs.workersLogs
    WHERE accountTag = '<ACCOUNT_TAG>'
      AND timestamp >= NOW() - INTERVAL '1' HOUR
      AND attributes['http.method'] = 'GET'
    GROUP BY attributes['http.method']

JSON casts, nested traversal, ordering by JSON values, comparisons between two JSON values, and `COUNT` of a JSON key are not supported. Dynamic JSON lookups also cannot be wrapped in `LIKE`, `BETWEEN`, `IS NULL`, or `CASE` expressions.

[PreviousFunctions](https://developers.cloudflare.com/analytics/sql-api/sql-reference/functions/)[NextLimits](https://developers.cloudflare.com/analytics/sql-api/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/sql-api/sql-reference/data-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
