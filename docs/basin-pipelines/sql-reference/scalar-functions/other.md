---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/
title: Other functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:26.361751+00:00
---

# Other functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /Other functions



# Other functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewarrow_castarrow_typeof

 _Basin Pipelines scalar function implementations are based on[Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference._

## `arrow_cast`

Casts a value to a specific Arrow data type:
    
    
    arrow_cast(expression, datatype)

**Arguments**

  * **expression** : Expression to cast. Can be a constant, column, or function, and any combination of arithmetic or string operators.
  * **datatype** : [Arrow data type ↗︎](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) name to cast to, as a string. The format is the same as that returned by [`arrow_typeof`]



**Example**
    
    
    > select arrow_cast(-5, 'Int8') as a,
      arrow_cast('foo', 'Dictionary(Int32, Utf8)') as b,
      arrow_cast('bar', 'LargeUtf8') as c,
      arrow_cast('2023-01-02T12:53:02', 'Timestamp(Microsecond, Some("+08:00"))') as d
      ;
    +----+-----+-----+---------------------------+
    | a  | b   | c   | d                         |
    +----+-----+-----+---------------------------+
    | -5 | foo | bar | 2023-01-02T12:53:02+08:00 |
    +----+-----+-----+---------------------------+
    1 row in set. Query took 0.001 seconds.

## `arrow_typeof`

Returns the name of the underlying [Arrow data type ↗︎](https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html) of the expression:
    
    
    arrow_typeof(expression)

**Arguments**

  * **expression** : Expression to evaluate. Can be a constant, column, or function, and any combination of arithmetic or string operators.



**Example**
    
    
    > select arrow_typeof('foo'), arrow_typeof(1);
    +---------------------------+------------------------+
    | arrow_typeof(Utf8("foo")) | arrow_typeof(Int64(1)) |
    +---------------------------+------------------------+
    | Utf8                      | Int64                  |
    +---------------------------+------------------------+
    1 row in set. Query took 0.001 seconds.

[PreviousHashing functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/hashing/)[NextMetrics and analytics](https://developers.cloudflare.com/basin-pipelines/observability/metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/other.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
