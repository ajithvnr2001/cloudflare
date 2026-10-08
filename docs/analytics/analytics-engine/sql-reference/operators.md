---
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/
title: Workers Analytics Engine SQL Reference \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:10.384139+00:00
---

# Workers Analytics Engine SQL Reference · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)

  4. /SQL Reference
  5. /Operators



# Operators

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArithmetic operatorsComparison operators Pattern matching operators Boolean operatorsUnary operators

The following operators are supported:

## Arithmetic operators

Operator | Description  
---|---  
`+` | addition  
`-` | subtraction  
`*` | multiplication  
`/` | division  
`%` | modulus  
  
## Comparison operators

Operator | Description  
---|---  
`=` | equals  
`<` | less than  
`>` | greater than  
`<=` | less than or equal to  
`>=` | greater than or equal to  
`<>` or `!=` | not equal  
`IN` | true if the preceding expression's value is in the list  
`column IN ('a', 'list', 'of', 'values')`  
`NOT IN` | true if the preceding expression's value is not in the list  
`column NOT IN ('a', 'list', 'of', 'values')`  
  
We also support the `BETWEEN` operator for checking a value is in an inclusive range: `a [NOT] BETWEEN b AND c`.

### Pattern matching operators New

Operator | Description  
---|---  
`LIKE` | true if the string matches the pattern (case-sensitive)  
`column LIKE 'pattern%'`  
`NOT LIKE` | true if the string does not match the pattern (case-sensitive)  
`column NOT LIKE 'pattern%'`  
`ILIKE` | true if the string matches the pattern (case-insensitive)  
`column ILIKE 'pattern%'`  
`NOT ILIKE` | true if the string does not match the pattern (case-insensitive)  
`column NOT ILIKE 'pattern%'`  
  
Pattern matching supports two wildcard characters:

  * `%` matches any sequence of zero or more characters
  * `_` matches any single character



Examples:
    
    
    -- Match strings starting with "error"
    WHERE blob1 LIKE 'error%'
    
    -- Match strings ending with ".jpg" (case-insensitive)
    WHERE blob2 ILIKE '%.jpg'
    
    -- Match strings containing "test" anywhere
    WHERE blob3 LIKE '%test%'
    
    -- Match exactly 5 characters starting with "log"
    WHERE blob4 LIKE 'log__'
    
    -- Exclude strings containing "debug" (case-insensitive)
    WHERE blob5 NOT ILIKE '%debug%'

## Boolean operators

Operator | Description  
---|---  
`AND` | boolean "AND" (true if both sides are true)  
`OR` | boolean "OR" (true if either side or both sides are true)  
`NOT` | boolean "NOT" (true if following expression is false and visa-versa)  
  
## Unary operators

Operator | Description  
---|---  
`-` | negation operator (for example, `-42`)  
  
[PreviousStatements](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/statements/)[NextLiterals](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/sql-reference/operators.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
