---
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/
title: SQL Reference \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:10.422587+00:00
---

# SQL Reference · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)

  4. /SQL Reference
  5. /Type conversion functions



# Type conversion functions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewtoUInt8 toUInt32

## toUInt8 New

Usage:
    
    
    toUInt8(<expression>)

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer.

Behaviour for negative numbers is undefined.

## toUInt32

Usage:
    
    
    toUInt32(<expression>)

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 32 bit integer.

Behaviour for negative numbers is undefined.

[PreviousString functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/)[NextQuerying from Grafana](https://developers.cloudflare.com/analytics/analytics-engine/grafana/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/sql-reference/type-conversion-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
