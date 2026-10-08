---
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/
title: SQL Reference \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:09.976144+00:00
---

# SQL Reference · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)

  4. /SQL Reference
  5. /Conditional functions



# Conditional functions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewif

## if

Usage:
    
    
    if(<condition>, <true_expression>, <false_expression>)

Returns `<true_expression>` if `<condition>` evaluates to true, else returns `<false_expression>`.

Example:
    
    
    if(temp > 20, 'It is warm', 'Bring a jumper')

[PreviousBit functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/)[NextDate and Time functions](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/analytics-engine/sql-reference/conditional-functions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
