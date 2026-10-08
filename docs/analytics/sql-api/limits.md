---
url: https://developers.cloudflare.com/analytics/sql-api/limits/
title: Limits \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:16.933994+00:00
---

# Limits · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/sql-api/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[SQL API](https://developers.cloudflare.com/analytics/sql-api/)
  4. /Limits



# Limits

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/sql-api/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following limits apply to SQL API queries:

Limit | Value  
---|---  
SQL statements per request | 1  
SQL statement length | 10 KiB  
Parser nesting depth | 10  
Datasets per statement | 1  
Accounts per statement | 1  
Minimum time constraint | A lower timestamp bound is required.  
`ORDER BY` | Requires `LIMIT`, except for Workers Analytics Engine datasets.  
`LIMIT` and `OFFSET` | Non-negative integer literals. `OFFSET` normally requires `LIMIT`.  
  
The lower timestamp bound and tenancy scope can be supplied in SQL or through the JSON request fields.

Dataset-specific limits can restrict field availability, the number of selected fields, historical retention, query duration, and the maximum number of returned rows. These limits depend on the dataset, your plan, and the account or zone being queried. A dataset-specific maximum page size rejects an explicit `LIMIT` above the maximum. It does not add a limit to a query that omits one.

The API also applies request-rate, concurrency, queue, execution-time, and resource-consumption limits. Cloudflare can adjust these operational limits to protect service availability.

When a request exceeds a rate or resource limit, the API returns HTTP `429`, `507`, or `503`. Reduce the requested time range or returned row count before retrying. Honor the `Retry-After` response header when it is present.

[PreviousData types and literals](https://developers.cloudflare.com/analytics/sql-api/sql-reference/data-types/)[NextError responses](https://developers.cloudflare.com/analytics/sql-api/errors/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/sql-api/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
