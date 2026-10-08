---
url: https://developers.cloudflare.com/analytics/sql-api/sql-reference/operators/
title: Operators \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.132904+00:00
---

# Operators · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/sql-api/sql-reference/operators/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[SQL API](https://developers.cloudflare.com/analytics/sql-api/)

  4. /[SQL language reference](https://developers.cloudflare.com/analytics/sql-api/sql-reference/)
  5. /Operators



# Operators

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/sql-api/sql-reference/operators/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArithmetic operatorsComparison operatorsLogical operatorsINBETWEENPattern matchingNull predicatesCASE

## Arithmetic operators

Operator | Description | Example  
---|---|---  
`+` | Addition | `requests + 1`  
`-` | Subtraction | `bytes - cachedBytes`  
`*` | Multiplication | `requests * 100`  
`/` | Division | `bytes / requests`  
`%` | Modulo | `edgeResponseStatus % 100`  
unary `-` | Negation | `-1`  
  
The field types in a dataset determine which arithmetic operations are valid.

## Comparison operators

Operator | Description  
---|---  
`=` | Equal to  
`!=` or `<>` | Not equal to  
`<` | Less than  
`<=` | Less than or equal to  
`>` | Greater than  
`>=` | Greater than or equal to  
  
## Logical operators

Operator | Description  
---|---  
`AND` | Both predicates are true.  
`OR` | At least one predicate is true.  
`NOT` | Negates a predicate.  
  
Parentheses control evaluation order:
    
    
    WHERE accountTag = '<ACCOUNT_TAG>'
      AND timestamp >= NOW() - INTERVAL '1' HOUR
      AND (edgeResponseStatus = 429 OR edgeResponseStatus >= 500)

Tenancy predicates are an exception. Keep `accountTag` and `zoneTag` predicates at the top level and join them with `AND`.

## IN

Use `IN` or `NOT IN` to compare a scalar expression with a non-empty list:
    
    
    edgeResponseStatus IN (403, 404, 429)

`NOT IN` is not supported for account or zone tenancy predicates.

## BETWEEN

Use `BETWEEN` to test an inclusive range. `NOT BETWEEN` negates the test:
    
    
    timestamp BETWEEN '2026-09-15T00:00:00Z' AND '2026-09-15T01:00:00Z'
    edgeResponseStatus BETWEEN 400 AND 499

## Pattern matching

Use `LIKE` and `NOT LIKE` for case-sensitive pattern matching. Use `ILIKE` and `NOT ILIKE` for case-insensitive matching. In a pattern, `%` matches any sequence of characters and `_` matches one character.
    
    
    clientRequestHttpHost ILIKE 'api.%'

`LIKE ... ESCAPE` is not supported.

## Null predicates

Use `IS NULL` or `IS NOT NULL` to test whether an expression is null:
    
    
    originResponseStatus IS NOT NULL

This does not make a standalone `NULL` literal valid in other expressions.

## CASE

The SQL API supports searched and simple `CASE` expressions:
    
    
    CASE
      WHEN edgeResponseStatus >= 500 THEN 'server error'
      WHEN edgeResponseStatus >= 400 THEN 'client error'
      ELSE 'other'
    END
    
    CASE edgeResponseStatus
      WHEN 200 THEN 'ok'
      ELSE 'other'
    END

[PreviousStatements and clauses](https://developers.cloudflare.com/analytics/sql-api/sql-reference/statements/)[NextFunctions](https://developers.cloudflare.com/analytics/sql-api/sql-reference/functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/sql-api/sql-reference/operators.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
