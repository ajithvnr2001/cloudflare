---
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/
title: SQL Reference \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:10.295380+00:00
---

# SQL Reference · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)

  4. /SQL Reference
  5. /Mathematical functions



# Mathematical functions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewintDivlog pow round floor ceil 

## intDiv

Usage:
    
    
    intDiv(a, b)

Divide `a` by `b`, rounding the answer down to the nearest whole number.

## log New

Usage:
    
    
    log(<expression>)

`log` returns the natural logarithm of a provided number. `ln` is also available as an alias.

Examples:
    
    
    -- get the natural logarithm of the double1 column
    log(double1)

## pow New

Usage:
    
    
    pow(<expression>, <expression>)

`pow` returns the first argument raised to the power of the second argument.

Examples:
    
    
    -- get the square of the double1 column
    pow(double1, 2)

## round New

Usage:
    
    
    round(<expression>[, n])

`round` returns a number rounded to the nearest whole number, or to a given number of decimal points specified by the second argument.

Examples:
    
    
    -- round 5.5 to 6
    round(5.5)
    -- round 3.14 to 3.1
    round(3.14, 1)

## floor New

Usage:
    
    
    floor(<expression>[, n])

`floor` returns a number rounded down to a whole number, or rounded down to a given number of decimal points specified by the second argument.

Examples:
    
    
    -- round down 5.5 to 5
    floor(5.5)
    -- round down 3.14 to 3.1
    floor(3.14, 1)

## ceil New

Usage:
    
    
    ceil(<expression>[, n])

`ceil` returns a number rounded up to a whole number, or rounded up to a given number of decimal points specified by the second argument.

Examples:
    
    
    -- round up 5.5 to 6
    ceil(5.5)
    -- round up 3.14 to 3.2
    ceil(3.14, 1)

[PreviousEncoding functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/)[NextString functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/sql-reference/mathematical-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
