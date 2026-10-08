---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/sql-data-types/
title: SQL data types \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:27.068585+00:00
---

# SQL data types · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/sql-data-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /SQL reference
  4. /SQL data types



# SQL data types

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/sql-data-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrimitive typesComposite types List types Struct types

Basin Pipelines supports a set of primitive and composite data types for SQL transformations. These types can be used in stream schemas and SQL literals with automatic type inference.

## Primitive types

Pipelines | SQL Types | Example Literals  
---|---|---  
`bool` | `BOOLEAN` | `TRUE`, `FALSE`  
`int32` | `INT`, `INTEGER` | `0`, `1`, `-2`  
`int64` | `BIGINT` | `0`, `1`, `-2`  
`float32` | `FLOAT`, `REAL` | `0.0`, `-2.4`, `1E-3`  
`float64` | `DOUBLE` | `0.0`, `-2.4`, `1E-35`  
`string` | `VARCHAR`, `CHAR`, `TEXT`, `STRING` | `"hello"`, `"world"`  
`timestamp` | `TIMESTAMP` | `'2020-01-01'`, `'2023-05-17T22:16:00.648662+00:00'`  
`binary` | `BYTEA` | `X'A123'` (hex)  
`json` | `JSON` | `'{"event": "purchase", "amount": 29.99}'`  
  
## Composite types

In addition to primitive types, Basin Pipelines SQL supports composite types for more complex data structures.

### List types

Lists group together zero or more elements of the same type. In stream schemas, lists are declared using the `list` type with an `items` field specifying the element type. In SQL, lists correspond to arrays and are declared by suffixing another type with `[]`, for example `INT[]`.

List values can be indexed using 1-indexed subscript notation (`v[1]` is the first element of `v`).

Lists can be constructed via `[]` literals:
    
    
    SELECT [1, 2, 3] as numbers

Basin Pipelines provides array functions for manipulating list values, and lists may be unnested using the `UNNEST` operator.

### Struct types

Structs combine related fields into a single value. In stream schemas, structs are declared using the `struct` type with a `fields` array. In SQL, structs can be created using the `struct` function.

Example creating a struct in SQL:
    
    
    SELECT struct('user123', 'purchase', 29.99) as event_data FROM events

This creates a struct with fields `c0`, `c1`, `c2` containing the user ID, event type, and amount.

Struct fields can be accessed via `.` notation, for example `event_data.c0` for the user ID.

[PreviousManage pipelines](https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/)[NextSELECT statements](https://developers.cloudflare.com/basin-pipelines/sql-reference/select-statements/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/sql-data-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
