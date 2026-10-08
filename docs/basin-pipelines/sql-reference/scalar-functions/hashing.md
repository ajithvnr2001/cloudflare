---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/hashing/
title: Hashing functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:26.025408+00:00
---

# Hashing functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/hashing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /Hashing functions



# Hashing functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/hashing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewdigestmd5sha224sha256sha384sha512

 _Basin Pipelines scalar function implementations are based on[Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference._

## `digest`

Computes the binary hash of an expression using the specified algorithm.
    
    
    digest(expression, algorithm)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.
  * **algorithm** : String expression specifying algorithm to use. Must be one of: 
    * md5
    * sha224
    * sha256
    * sha384
    * sha512
    * blake2s
    * blake2b
    * blake3



## `md5`

Computes an MD5 128-bit checksum for a string expression.
    
    
    md5(expression)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.



## `sha224`

Computes the SHA-224 hash of a binary string.
    
    
    sha224(expression)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.



## `sha256`

Computes the SHA-256 hash of a binary string.
    
    
    sha256(expression)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.



## `sha384`

Computes the SHA-384 hash of a binary string.
    
    
    sha384(expression)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.



## `sha512`

Computes the SHA-512 hash of a binary string.
    
    
    sha512(expression)

**Arguments**

  * **expression** : String expression to operate on. Can be a constant, column, or function, and any combination of string operators.



[PreviousStruct functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/struct/)[NextOther functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/other/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/hashing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
