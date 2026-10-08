---
url: https://developers.cloudflare.com/analytics/sql-api/get-started/
title: Get started \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:16.635296+00:00
---

# Get started · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/sql-api/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[SQL API](https://developers.cloudflare.com/analytics/sql-api/)
  4. /Get started



# Get started

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/sql-api/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesRun a queryUse the Cloudflare CLI

## Prerequisites

To run an account-scoped query, you need an account identifier and an API token with **Account Analytics Read** permission for that account. A query containing `zoneTag` requires either **Zone Analytics Read** permission for every named zone or **Account Analytics Read** permission for their owning account.

SQL API datasets represent different Cloudflare products. Some datasets and fields require additional API token permissions for the products whose data they expose. Include the permissions required by every dataset and field you plan to query.

Cloudflare recommends API tokens because you can restrict each token to specific resources. Refer to [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) for instructions.

## Run a query

Send a `POST` request to the SQL API endpoint. Pass the SQL statement and its parameters as JSON.

The following query returns the five most common HTTP response statuses for one account after a specified start time. Replace `<START_TIME>` with a recent ISO 8601 timestamp within the dataset's retention period.
    
    
    curl "https://api.cloudflare.com/client/v4/analytics/sql" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "SELECT edgeResponseStatus AS status, COUNT(*) AS requests FROM events.httpRequests WHERE accountTag = $account AND timestamp >= $start GROUP BY edgeResponseStatus ORDER BY requests DESC LIMIT 5",
        "params": {
          "account": "<ACCOUNT_TAG>",
          "start": "<START_TIME>"
        }
      }'

A successful response has the following structure:
    
    
    {
    	"data": [
    		{
    			"status": 200,
    			"requests": 125430
    		},
    		{
    			"status": 404,
    			"requests": 8240
    		},
    		{
    			"status": 301,
    			"requests": 5175
    		},
    		{
    			"status": 304,
    			"requests": 3960
    		},
    		{
    			"status": 500,
    			"requests": 82
    		}
    	],
    	"rows": 5,
    	"statistics": {
    		"elapsed_ms": 42,
    		"rows_read": 250000,
    		"bytes_read": 18000000
    	}
    }

The `data` array contains one object for each result row. The object keys match selected field names or aliases. The `rows` value is the number of returned rows. The `statistics` object describes the work performed by the data store.

This response shape applies to the default output from ClickHouse-backed datasets. Log Explorer and explicit output formats have different response shapes. Refer to [Response formats](https://developers.cloudflare.com/analytics/sql-api/query-api/#response-formats).

## Use the Cloudflare CLI

The Cloudflare CLI provides `cf sql query`. Pass the SQL statement as a positional argument, then provide exactly one scope flag and a lower time bound:
    
    
    cf sql query \
      'SELECT edgeResponseStatus AS status, COUNT(*) AS requests FROM events.httpRequests GROUP BY edgeResponseStatus ORDER BY requests DESC LIMIT 5' \
      --scope-account "<ACCOUNT_TAG>" \
      --time-since "<START_TIME>"

Use `--scope-zone` instead of `--scope-account` for zone scope. You can optionally add `--time-until`. Both time bounds are inclusive. Do not include tenancy or timestamp predicates in SQL when you supply the corresponding CLI flags.

For request options and parameter binding, refer to [Query the API](https://developers.cloudflare.com/analytics/sql-api/query-api/).

[PreviousOverview](https://developers.cloudflare.com/analytics/sql-api/)[NextDatasets](https://developers.cloudflare.com/analytics/sql-api/datasets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/sql-api/get-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
