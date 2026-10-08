---
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/analytics-sql/
title: Analytics SQL binding \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:41.720206+00:00
---

# Analytics SQL binding · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/bindings/analytics-sql/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Bindings (env)](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
  5. /Analytics SQL binding



# Analytics SQL binding

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/bindings/analytics-sql/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the bindingUse the bindingquery() Request ResultErrors

Use the Analytics SQL binding to query analytics datasets from a Worker.

## Configure the binding

Add an Analytics SQL binding to your Worker's Wrangler configuration. The `analytics` key requires Wrangler 4.145.0 or later.
    
    
    {
    	"analytics": {
    		"binding": "ANALYTICS_SQL"
    	}
    }
    
    
    [analytics]
    binding = "ANALYTICS_SQL"

The `binding` value determines the property used to access the binding on your Worker's `env` object.

## Use the binding
    
    
    export default {
    	async fetch(_request, env) {
    		const start = new Date(Date.now() - 60 * 60 * 1000).toISOString();
    		const result = await env.ANALYTICS_SQL.query({
    			query:
    				"SELECT COUNT(*) AS requests FROM events.httpRequests WHERE timestamp >= $start",
    			params: { start },
    		});
    
    		return Response.json(result);
    	},
    };
    
    
    interface Env {
    	ANALYTICS_SQL: AnalyticsSQLBinding;
    }
    
    type CountRow = {
    	requests: number;
    };
    
    export default {
    	async fetch(_request, env): Promise<Response> {
    		const start = new Date(Date.now() - 60 * 60 * 1000).toISOString();
    		const result = await env.ANALYTICS_SQL.query<CountRow>({
    			query: "SELECT COUNT(*) AS requests FROM events.httpRequests WHERE timestamp >= $start",
    			params: { start },
    		});
    
    		return Response.json(result);
    	},
    } satisfies ExportedHandler<Env>;

For available datasets and supported SQL syntax, refer to the [Analytics SQL documentation](https://developers.cloudflare.com/analytics/sql-api/).

## `query()`

The `query()` method executes one SQL `SELECT` statement:
    
    
    query<T extends Record<string, unknown> = Record<string, unknown>>(
    	request: AnalyticsSQLQuery,
    ): Promise<AnalyticsSQLResult<T>>;

The optional type parameter defines the shape of each result row.

### Request

The `AnalyticsSQLQuery` object has the following properties:

Property | Type | Required | Description  
---|---|---|---  
`query` | `string` | Yes | SQL statement to execute. Use `$1` for positional parameters or `$name` for named parameters.  
`params` | array or object | No | Values for the placeholders in `query`.  
  
An `AnalyticsSQLParameter` can be a `string`, `number`, `boolean`, or `null`.

The binding derives account scope from the Worker. It does not accept `scope` or `time_range` request properties.

### Result

The `AnalyticsSQLResult<T>` object has the following properties:

Property | Type | Description  
---|---|---  
`data` | `T[]` | Query result rows keyed by selected column names.  
`rows` | `number` | Number of rows in `data`.  
`statistics` | `AnalyticsSQLStatistics` | Execution statistics for the query.  
  
The `statistics` object contains `elapsed_ms`, `rows_read`, and `bytes_read`. For details about these values, refer to [Query the SQL API](https://developers.cloudflare.com/analytics/sql-api/query-api/#response-formats).

## Errors

The method rejects its promise when a query fails. The thrown error has a boolean `retryable` property. Retry with bounded exponential backoff only when this property is `true`.

The binding does not retry queries automatically. For query and service errors, refer to [SQL API errors](https://developers.cloudflare.com/analytics/sql-api/errors/).

[PreviousAnalytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/)[NextAssets ↗︎](https://developers.cloudflare.com/workers/static-assets/binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/bindings/analytics-sql.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
