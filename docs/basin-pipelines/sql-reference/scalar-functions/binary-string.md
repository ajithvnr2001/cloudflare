---
url: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/binary-string/
title: Binary string functions \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.875632+00:00
---

# Binary string functions · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/binary-string/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /…

SQL reference

  4. /Scalar functions
  5. /Binary string functions



# Binary string functions

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/binary-string/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewencodedecode

 _Basin Pipelines scalar function implementations are based on[Apache DataFusion ↗︎](https://arrow.apache.org/datafusion/) (via [Arroyo ↗︎](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference._

## `encode`

Encode binary data into a textual representation.
    
    
    encode(expression, format)

**Arguments**

  * **expression** : Expression containing string or binary data

  * **format** : Supported formats are: `base64`, `hex`




**Related functions** : decode

## `decode`

Decode binary data from textual representation in string.
    
    
    decode(expression, format)

**Arguments**

  * **expression** : Expression containing encoded string data

  * **format** : Same arguments as encode




**Related functions** : encode

[PreviousString functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/string/)[NextRegex functions](https://developers.cloudflare.com/basin-pipelines/sql-reference/scalar-functions/regex/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sql-reference/scalar-functions/binary-string.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
