---
url: https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/
title: Workers Analytics Engine adds supports for new SQL functions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:24.319777+00:00
---

# Workers Analytics Engine adds supports for new SQL functions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2025

## Workers Analytics Engine adds supports for new SQL functions

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now perform more powerful queries directly in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/) with a major expansion of our SQL function library.

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.

Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:

[**New aggregate functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/)

  * `argMin()` \- Returns the value associated with the minimum in a group
  * `argMax()` \- Returns the value associated with the maximum in a group
  * `topK()` \- Returns an array of the most frequent values in a group
  * `topKWeighted()` \- Returns an array of the most frequent values in a group using weights
  * `first_value()` \- Returns the first value in an ordered set of values within a partition
  * `last_value()` \- Returns the last value in an ordered set of values within a partition



[**New bit functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/)

  * `bitAnd()` \- Returns the bitwise AND of two expressions
  * `bitCount()` \- Returns the number of bits set to one in the binary representation of a number
  * `bitHammingDistance()` \- Returns the number of bits that differ between two numbers
  * `bitNot()` \- Returns a number with all bits flipped
  * `bitOr()` \- Returns the inclusive bitwise OR of two expressions
  * `bitRotateLeft()` \- Rotates all bits in a number left by specified positions
  * `bitRotateRight()` \- Rotates all bits in a number right by specified positions
  * `bitShiftLeft()` \- Shifts all bits in a number left by specified positions
  * `bitShiftRight()` \- Shifts all bits in a number right by specified positions
  * `bitTest()` \- Returns the value of a specific bit in a number
  * `bitXor()` \- Returns the bitwise exclusive-or of two expressions



[**New mathematical functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/)

  * `abs()` \- Returns the absolute value of a number
  * `log()` \- Computes the natural logarithm of a number
  * `round()` \- Rounds a number to a specified number of decimal places
  * `ceil()` \- Rounds a number up to the nearest integer
  * `floor()` \- Rounds a number down to the nearest integer
  * `pow()` \- Returns a number raised to the power of another number



[**New string functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/)

  * `lowerUTF8()` \- Converts a string to lowercase using UTF-8 encoding
  * `upperUTF8()` \- Converts a string to uppercase using UTF-8 encoding



[**New encoding functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/)

  * `hex()` \- Converts a number to its hexadecimal representation
  * `bin()` \- Converts a string to its binary representation



[**New type conversion functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/)

  * `toUInt8()` \- Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer



#### Ready to get started?

Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](https://developers.cloudflare.com/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/).
