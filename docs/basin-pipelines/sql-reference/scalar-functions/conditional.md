---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/conditional/
title: Conditional functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.965310+00:00
---

# Conditional functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/conditional/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /Conditional functions



# Conditional functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/conditional/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewcoalescenullifnvlnvl2ifnull

 _Basin Pipelines scalar function implementations are based on[Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference._

## `coalesce`

Returns the first of its arguments that is not _null_. Returns _null_ if all arguments are _null_. This function is often used to substitute a default value for _null_ values.
    
    
    coalesce(expression1[, ..., expression_n])

**Arguments**

  * **expression1, expression_n** : Expression to use if previous expressions are _null_. Can be a constant, column, or function, and any combination of arithmetic operators. Pass as many expression arguments as necessary.



## `nullif`

Returns _null_ if _expression1_ equals _expression2_ ; otherwise it returns _expression1_. This can be used to perform the inverse operation of `coalesce`.
    
    
    nullif(expression1, expression2)

**Arguments**

  * **expression1** : Expression to compare and return if equal to expression2. Can be a constant, column, or function, and any combination of arithmetic operators.
  * **expression2** : Expression to compare to expression1. Can be a constant, column, or function, and any combination of arithmetic operators.



## `nvl`

Returns _expression2_ if _expression1_ is NULL; otherwise it returns _expression1_.
    
    
    nvl(expression1, expression2)

**Arguments**

  * **expression1** : return if expression1 not is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.
  * **expression2** : return if expression1 is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.



## `nvl2`

Returns _expression2_ if _expression1_ is not NULL; otherwise it returns _expression3_.
    
    
    nvl2(expression1, expression2, expression3)

**Arguments**

  * **expression1** : conditional expression. Can be a constant, column, or function, and any combination of arithmetic operators.
  * **expression2** : return if expression1 is not NULL. Can be a constant, column, or function, and any combination of arithmetic operators.
  * **expression3** : return if expression1 is NULL. Can be a constant, column, or function, and any combination of arithmetic operators.



## `ifnull`

_Alias ofnvl._

[PreviousMath functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/math/)[NextString functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/string/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/conditional.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
