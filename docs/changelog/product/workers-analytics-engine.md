---
url: https://developers.cloudflare.com/changelog/product/workers-analytics-engine/
title: Workers Analytics Engine Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:52.925445+00:00
---

# Workers Analytics Engine Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/workers-analytics-engine/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Jan 7, 2026

## [Workers Analytics Engine SQL now supports filtering using HAVING and LIKE](https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/)

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)[Workers](https://developers.cloudflare.com/workers/)

You can now use the `HAVING` clause and `LIKE` pattern matching operators in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/).

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.

#### Filtering using `HAVING`

The `HAVING` clause complements the `WHERE` clause by enabling you to filter groups based on aggregate values. While `WHERE` filters rows before aggregation, `HAVING` filters groups after aggregation is complete.

You can use `HAVING` to filter groups where the average exceeds a threshold:
    
    
    SELECT
        blob1 AS probe_name,
        avg(double1) AS average_temp
    FROM temperature_readings
    GROUP BY probe_name
    HAVING average_temp > 10

You can also filter groups based on aggregates such as the number of items in the group:
    
    
    SELECT
        blob1 AS probe_name,
        count() AS num_readings
    FROM temperature_readings
    GROUP BY probe_name
    HAVING num_readings > 100

#### Pattern matching using `LIKE`

The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:

  * `LIKE` \- case-sensitive pattern matching
  * `NOT LIKE` \- case-sensitive pattern exclusion
  * `ILIKE` \- case-insensitive pattern matching
  * `NOT ILIKE` \- case-insensitive pattern exclusion



Pattern matching supports two wildcard characters: `%` (matches zero or more characters) and `_` (matches exactly one character).

You can match strings starting with a prefix:
    
    
    SELECT *
    FROM logs
    WHERE blob1 LIKE 'error%'

You can also match file extensions (case-insensitive):
    
    
    SELECT *
    FROM requests
    WHERE blob2 ILIKE '%.jpg'

Another example is excluding strings containing specific text:
    
    
    SELECT *
    FROM events
    WHERE blob3 NOT ILIKE '%debug%'

#### Ready to get started?

Learn more about the [`HAVING` clause](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/statements/#having-clause) or [pattern matching operators](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators) in the Workers Analytics Engine SQL reference documentation.

Nov 12, 2025

## [More SQL aggregate, date and time functions available in Workers Analytics Engine](https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/)

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)[Workers](https://developers.cloudflare.com/workers/)

You can now perform more powerful queries directly in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/) with a major expansion of our SQL function library.

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.

Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:

[**New aggregate functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/)

  * `countIf()` \- count the number of rows which satisfy a provided condition
  * `sumIf()` \- calculate a sum from rows which satisfy a provided condition
  * `avgIf()` \- calculate an average from rows which satisfy a provided condition



[**New date and time functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/)

  * `toYear()`
  * `toMonth()`
  * `toDayOfMonth()`
  * `toDayOfWeek()`
  * `toHour()`
  * `toMinute()`
  * `toSecond()`
  * `toStartOfYear()`
  * `toStartOfMonth()`
  * `toStartOfWeek()`
  * `toStartOfDay()`
  * `toStartOfHour()`
  * `toStartOfFifteenMinutes()`
  * `toStartOfTenMinutes()`
  * `toStartOfFiveMinutes()`
  * `toStartOfMinute()`
  * `today()`
  * `toYYYYMM()`



#### Ready to get started?

Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](https://developers.cloudflare.com/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/).

Oct 2, 2025

## [Workers Analytics Engine adds supports for new SQL functions](https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/)

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)[Workers](https://developers.cloudflare.com/workers/)

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
