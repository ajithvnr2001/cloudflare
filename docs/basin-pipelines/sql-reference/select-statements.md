---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/
title: SELECT statements \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.345047+00:00
---

# SELECT statements · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /SQL reference
  4. /SELECT statements



# SELECT statements

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWITH clauseSELECT clauseFROM clauseWHERE clauseUNNEST operatorMultiple statements

SELECT statements are used to transform data in Basin Pipelines. The general form is:
    
    
    [WITH with_query [, ...]]
    SELECT select_expr [, ...]
    FROM from_item
    [WHERE condition]

A pipeline runs one or more `INSERT INTO sink SELECT ... FROM stream` statements. To write to multiple sinks from the same pipeline, separate the statements with semicolons. See Multiple statements.

## WITH clause

The WITH clause allows you to define named subqueries that can be referenced in the main query. This can improve query readability by breaking down complex transformations.

Syntax:
    
    
    WITH query_name AS (subquery) [, ...]

Simple example:
    
    
    WITH filtered_events AS
        (SELECT user_id, event_type, amount
            FROM user_events WHERE amount > 50)
    SELECT user_id, amount * 1.1 as amount_with_tax
    FROM filtered_events
    WHERE event_type = 'purchase';

## SELECT clause

The SELECT clause is a comma-separated list of expressions, with optional aliases. Column names must be unique.
    
    
    SELECT select_expr [, ...]

Examples:
    
    
    -- Select specific columns
    SELECT user_id, event_type, amount FROM events
    
    -- Use expressions and aliases
    SELECT
        user_id,
        amount * 1.1 as amount_with_tax,
        UPPER(event_type) as event_type_upper
    FROM events
    
    -- Select all columns
    SELECT * FROM events

## FROM clause

The FROM clause specifies the data source for the query. It will be either a table name or subquery. The table name can be either a stream name or a table created in the WITH clause.
    
    
    FROM from_item

Tables can be given aliases:
    
    
    SELECT e.user_id, e.amount
    FROM user_events e
    WHERE e.event_type = 'purchase'

## WHERE clause

The WHERE clause filters data using boolean conditions. Predicates are applied to input rows.
    
    
    WHERE condition

Examples:
    
    
    -- Filter by field value
    SELECT * FROM events WHERE event_type = 'purchase'
    
    -- Multiple conditions
    SELECT * FROM events
    WHERE event_type = 'purchase' AND amount > 50
    
    -- String operations
    SELECT * FROM events
    WHERE user_id LIKE 'user_%'
    
    -- Null checks
    SELECT * FROM events
    WHERE description IS NOT NULL

## UNNEST operator

The UNNEST operator converts arrays into multiple rows. This is useful for processing list data types.

UNNEST restrictions:

  * May only appear in the SELECT clause
  * Only one array may be unnested per SELECT statement



Example:
    
    
    SELECT
        UNNEST([1, 2, 3]) as numbers
    FROM events;

This will produce:
    
    
    +---------+
    | numbers |
    +---------+
    |       1 |
    |       2 |
    |       3 |
    +---------+

## Multiple statements

A pipeline can contain multiple `INSERT` statements, separated by semicolons. Each statement reads from a stream and writes to a sink. Use multiple statements to route events from a single stream into several sinks based on their content.
    
    
    INSERT INTO purchases_sink
    SELECT user_id, product_id, amount FROM events
    WHERE event_type = 'purchase';
    
    INSERT INTO signups_sink
    SELECT user_id, created_at FROM events
    WHERE event_type = 'signup';

To provide multiple statements with the Wrangler CLI, pass a file with the `--sql-file` flag:

npmyarnpnpm
    
    
    npx wrangler basin pipelines create my-pipeline --sql-file pipeline.sql
    
    
    yarn wrangler basin pipelines create my-pipeline --sql-file pipeline.sql
    
    
    pnpm wrangler basin pipelines create my-pipeline --sql-file pipeline.sql

For a worked example, refer to [Fan out a stream to multiple Iceberg tables](https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/).

[PreviousSQL data types](https://developers.cloudflare.com/basin-pipelines/sql-reference/sql-data-types/)[NextMath functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/math/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/select-statements.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
