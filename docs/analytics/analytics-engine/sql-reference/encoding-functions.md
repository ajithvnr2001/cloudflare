---
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/
title: SQL Reference \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:10.241099+00:00
---

# SQL Reference · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)

  4. /SQL Reference
  5. /Encoding functions



# Encoding functions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewbin hex 

## bin New

Usage:
    
    
    bin(<expression>)

`bin` returns a string containing the binary representation of its argument.

Examples:
    
    
    -- get the binary representation of 1
    bin(1)
    -- get the binary representation of a string`
    bin('abc')

## hex New

Usage:
    
    
    hex(<expression>)

`hex` returns a string containing the hexadecimal representation of its argument.

Examples:
    
    
    -- get the hexadecimal representation of 1
    hex(1)
    -- get the hexadecimal representation of a string`
    hex('abc')

[PreviousDate and Time functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/)[NextMathematical functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/sql-reference/encoding-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
