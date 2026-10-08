---
url: https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/
title: D1 automatically retries read-only queries \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.460879+00:00
---

# D1 automatically retries read-only queries · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 11, 2025

## D1 automatically retries read-only queries

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned [response metadata](https://developers.cloudflare.com/d1/worker-api/return-object/#d1result) property `total_attempts`.

At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: `SELECT`, `EXPLAIN`, `WITH`. Queries containing any [SQLite keyword ↗︎](https://sqlite.org/lang_keywords.html) that leads to database writes are not retried.

The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).

The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying [retries in their own code](https://developers.cloudflare.com/d1/best-practices/retry-queries/) for queries that are not read-only but are idempotent according to the business logic of the application.

![D1 automatically query retries success ratio](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=946,format=webp/_astro/d1-auto-retry-success-ratio.yPw8B0tB.png)

D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.

The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.
