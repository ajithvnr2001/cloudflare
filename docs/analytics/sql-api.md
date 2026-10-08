---
url: https://developers.cloudflare.com/analytics/sql-api/
title: SQL API \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:16.403206+00:00
---

# SQL API · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/sql-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /SQL API



# SQL API

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/sql-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewQuery scopeGet started

The SQL API lets you query Cloudflare analytics and observability datasets with SQL. Use the API to select fields, filter events, calculate aggregates, group results, and integrate analytics data with your applications.

The SQL API provides `GET` and `POST` query endpoints at:
    
    
    https://api.cloudflare.com/client/v4/analytics/sql

Send one `SELECT` statement in each request. Use `POST` to send raw SQL or a JSON request with parameters, request-level scope, and a time range. Use `GET` for URL-encoded queries. The API validates the statement against the available datasets and supported SQL language before it executes the query.

Use the [introspection endpoint](https://developers.cloudflare.com/analytics/sql-api/datasets/#discover-datasets) to discover dataset names, categories, descriptions, kinds, columns, and data types. You can also run queries with [`cf sql query`](https://developers.cloudflare.com/analytics/sql-api/get-started/#use-the-cloudflare-cli) and list datasets with `cf sql datasets`.

The SQL API supports a deliberately limited SQL dialect. It does not pass arbitrary SQL through to the underlying data store. For the complete language surface, refer to the [SQL language reference](https://developers.cloudflare.com/analytics/sql-api/sql-reference/).

## Query scope

Every query must include:

  * An account or zone scope, supplied in the SQL statement or request body, that identifies the data you are authorized to query.
  * A lower time bound that limits how far back the query reads.
  * One schema-qualified dataset, such as `events.httpRequests`.



Dataset and field availability depends on your Cloudflare plan and permissions. The API authorizes every account or zone named by a query.

## Get started

Refer to [Get started](https://developers.cloudflare.com/analytics/sql-api/get-started/) to create an API token and run your first query.

To query datasets from a Cloudflare Worker without managing an API token, use the [Workers binding](https://developers.cloudflare.com/analytics/sql-api/workers-binding/).

[PreviousLimits](https://developers.cloudflare.com/analytics/analytics-engine/limits/)[NextGet started](https://developers.cloudflare.com/analytics/sql-api/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/sql-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
