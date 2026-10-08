---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/
title: Struct functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:26.955273+00:00
---

# Struct functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /Struct functions



# Struct functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewstruct

 _Basin Pipelines scalar function implementations are based on[Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference._

## `struct`

Returns an Arrow struct using the specified input expressions. Fields in the returned struct use the `cN` naming convention. For example: `c0`, `c1`, `c2`, etc.
    
    
    struct(expression1[, ..., expression_n])

For example, this query converts two columns `a` and `b` to a single column with a struct type of fields `c0` and `c1`:
    
    
    select * from t;
    +---+---+
    | a | b |
    +---+---+
    | 1 | 2 |
    | 3 | 4 |
    +---+---+
    
    select struct(a, b) from t;
    +-----------------+
    | struct(t.a,t.b) |
    +-----------------+
    | {c0: 1, c1: 2}  |
    | {c0: 3, c1: 4}  |
    +-----------------+

#### Arguments

  * **expression_n** : Expression to include in the output struct. Can be a constant, column, or function, and any combination of arithmetic or string operators.



[PreviousArray functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/array/)[NextHashing functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/hashing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/struct.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
