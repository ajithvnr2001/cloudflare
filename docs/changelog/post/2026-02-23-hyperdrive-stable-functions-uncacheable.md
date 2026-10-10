---
url: https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/
title: Hyperdrive no longer caches queries using STABLE PostgreSQL functions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.376864+00:00
---

# Hyperdrive no longer caches queries using STABLE PostgreSQL functions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 23, 2026

## Hyperdrive no longer caches queries using STABLE PostgreSQL functions

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now treats queries containing PostgreSQL `STABLE` functions as uncacheable, in addition to `VOLATILE` functions.

Previously, only functions [that PostgreSQL categorizes ↗︎](https://www.postgresql.org/docs/current/xfunc-volatility.html) as `VOLATILE` (for example, `RANDOM()`, `LASTVAL()`) were detected as uncacheable. `STABLE` functions (for example, `NOW()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`) were incorrectly allowed to be cached.

Because `STABLE` functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.

If your queries use `STABLE` functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of `WHERE created_at > NOW()`, compute the timestamp in your Worker and pass it as `WHERE created_at > $1`.

Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like `NOW()` in SQL comments also cause the query to be marked as uncacheable.

For more information, refer to [Query caching](https://developers.cloudflare.com/hyperdrive/concepts/query-caching/) and [Troubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/).
