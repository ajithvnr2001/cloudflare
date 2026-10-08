---
url: https://developers.cloudflare.com/basin-catalog/observability/metrics/
title: Metrics and analytics \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:23.671277+00:00
---

# Metrics and analytics · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/observability/metrics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Observability
  4. /Metrics and analytics



# Metrics and analytics

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/observability/metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDashboard metricsGraphQL datasets Data operations metrics Table maintenance metricsQuery via the GraphQL API Measure data operations over a time period Measure request latency percentiles Query table maintenance job metrics Filter by operation or table Query across all warehouses

Basin Catalog exposes metrics that allow you to monitor Iceberg REST API requests and table maintenance jobs (compaction and snapshot expiration) across your warehouses.

Legacy product names

GraphQL dataset names such as `r2CatalogDataOperationsAdaptiveGroups` still use identifiers from R2 Data Catalog. These names will be updated in the coming weeks. Until then, use the dataset names shown in this guide.

The metrics displayed in the Cloudflare dashboard are queried from Cloudflare's [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). You can access the metrics programmatically via GraphQL or any HTTP client.

## Dashboard metrics

The **Metrics** tab on each catalog's detail page displays five charts that summarize catalog activity over a configurable time range:

Chart | Description  
---|---  
**Bytes Compacted** | Total bytes written by compaction jobs  
**Files Compacted** | Number of input files processed and output files created by compaction  
**Catalog Requests** | Total Iceberg REST API requests (for example, `load-table`, `list-namespaces`, `commit-table`)  
**Storage Size** | Current bucket storage size  
**Snapshots Expired** | Number of snapshots removed by snapshot expiration jobs  
  
The overview page also shows **Catalog Requests** and **Bucket Size** columns in the catalogs table, giving you a quick summary across all your catalogs.

## GraphQL datasets

### Data operations metrics

Basin Catalog exports the below metrics within the `r2CatalogDataOperationsAdaptiveGroups` dataset. These metrics track Iceberg REST API requests made to your catalog, such as loading tables, listing namespaces, and committing updates.

Metric | GraphQL Field Name | Aggregation | Description  
---|---|---|---  
Request count | `count` | count | Total number of Iceberg REST API requests  
Request body bytes | `requestBodyBytes` | sum | Total bytes sent in request bodies  
Request duration | `requestDurationMs` | sum, avg, quantiles | Request duration in milliseconds  
  
The `r2CatalogDataOperationsAdaptiveGroups` dataset provides the following dimensions for filtering and grouping queries:

  * `warehouseName` \- The name of the Basin Catalog warehouse
  * `operation` \- The Iceberg REST API operation name (for example, `load-table`, `list-namespaces`, `commit-table`)
  * `namespaceName` \- The Iceberg namespace targeted by the request, if applicable
  * `tableName` \- The Iceberg table targeted by the request, if applicable
  * `httpStatus` \- HTTP response status code
  * `datetime` \- Request timestamp
  * `date` \- Request timestamp, truncated to the start of a day
  * `datetimeHour` \- Request timestamp, truncated to the start of an hour
  * `datetimeMinute` \- Request timestamp, truncated to the start of a minute
  * `datetimeFiveMinutes` \- Request timestamp, truncated to the start of five minutes
  * `datetimeFifteenMinutes` \- Request timestamp, truncated to the start of fifteen minutes



### Table maintenance metrics

Basin Catalog exports the below metrics within the `r2CatalogTableMaintenanceAdaptiveGroups` dataset. These metrics track table maintenance jobs including [compaction and snapshot expiration](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Metric | GraphQL Field Name | Aggregation | Description  
---|---|---|---  
Job count | `count` | count | Total number of maintenance jobs executed  
Files processed | `filesProcessed` | sum | Total input files processed by maintenance jobs  
Files output | `filesOutput` | sum | Total output files created by maintenance jobs  
Input bytes | `inputBytes` | sum | Total bytes read or scanned by maintenance jobs  
Output bytes | `outputBytes` | sum | Total bytes written by maintenance jobs  
Job duration | `jobDurationMs` | sum, avg, quantiles | Job duration in milliseconds  
  
The `r2CatalogTableMaintenanceAdaptiveGroups` dataset provides the following dimensions for filtering and grouping queries:

  * `warehouseName` \- The name of the Basin Catalog warehouse
  * `jobType` \- The type of maintenance job (`compaction`, `snapshot-expiration`)
  * `namespaceName` \- The Iceberg namespace containing the table
  * `tableName` \- The Iceberg table that was maintained
  * `success` \- Whether the job succeeded (`1`) or failed (`0`)
  * `datetime` \- Job timestamp
  * `date` \- Job timestamp, truncated to the start of a day
  * `datetimeHour` \- Job timestamp, truncated to the start of an hour
  * `datetimeMinute` \- Job timestamp, truncated to the start of a minute
  * `datetimeFiveMinutes` \- Job timestamp, truncated to the start of five minutes
  * `datetimeFifteenMinutes` \- Job timestamp, truncated to the start of fifteen minutes



## Query via the GraphQL API

You can programmatically query analytics for your Basin Catalog warehouses via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/). This API queries the same datasets as the Cloudflare dashboard and supports GraphQL [introspection](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/).

Basin Catalog GraphQL datasets require an `accountTag` filter with your Cloudflare account ID.

### Measure data operations over a time period

This query returns the total number of Iceberg REST API requests and total request duration, grouped by operation, for a specific warehouse.
    
    
    query CatalogDataOperations(
    	$accountTag: String!
    	$warehouseName: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogDataOperationsAdaptiveGroups(
    				limit: 10000
    				filter: {
    					warehouseName: $warehouseName
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				count
    				dimensions {
    					operation
    				}
    				sum {
    					requestBodyBytes
    					requestDurationMs
    				}
    				avg {
    					requestDurationMs
    				}
    			}
    		}
    	}
    }

### Measure request latency percentiles

This query returns request duration percentiles for a specific warehouse, which is useful for understanding latency distribution.
    
    
    query CatalogLatencyPercentiles(
    	$accountTag: String!
    	$warehouseName: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogDataOperationsAdaptiveGroups(
    				limit: 10000
    				filter: {
    					warehouseName: $warehouseName
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				count
    				dimensions {
    					operation
    				}
    				quantiles {
    					requestDurationMsP50
    					requestDurationMsP90
    					requestDurationMsP99
    				}
    			}
    		}
    	}
    }

### Query table maintenance job metrics

This query returns a summary of compaction and snapshot expiration jobs for a specific warehouse, including files processed, bytes read and written, and success or failure status.
    
    
    query CatalogMaintenanceMetrics(
    	$accountTag: String!
    	$warehouseName: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogTableMaintenanceAdaptiveGroups(
    				limit: 10000
    				filter: {
    					warehouseName: $warehouseName
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				count
    				dimensions {
    					jobType
    					tableName
    					success
    				}
    				sum {
    					filesProcessed
    					filesOutput
    					inputBytes
    					outputBytes
    					jobDurationMs
    				}
    			}
    		}
    	}
    }

### Filter by operation or table

You can narrow results to a specific Iceberg operation or table. For example, to query only `load-table` operations for a specific table:
    
    
    query CatalogFilterByOperation(
    	$accountTag: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogDataOperationsAdaptiveGroups(
    				limit: 10000
    				filter: {
    					warehouseName: "my-warehouse"
    					operation: "load-table"
    					tableName: "my_table"
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				count
    				sum {
    					requestDurationMs
    				}
    			}
    		}
    	}
    }

To query only failed maintenance jobs:
    
    
    query CatalogFailedMaintenanceJobs(
    	$accountTag: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogTableMaintenanceAdaptiveGroups(
    				limit: 10000
    				filter: {
    					warehouseName: "my-warehouse"
    					success: 0
    					datetime_geq: $datetimeStart
    					datetime_leq: $datetimeEnd
    				}
    			) {
    				count
    				dimensions {
    					jobType
    					tableName
    				}
    			}
    		}
    	}
    }

### Query across all warehouses

To query metrics across all warehouses on an account, omit the `warehouseName` filter and include `warehouseName` in the dimensions:
    
    
    query CatalogAllWarehouses(
    	$accountTag: String!
    	$datetimeStart: Time!
    	$datetimeEnd: Time!
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			r2CatalogDataOperationsAdaptiveGroups(
    				limit: 10000
    				filter: { datetime_geq: $datetimeStart, datetime_leq: $datetimeEnd }
    			) {
    				count
    				dimensions {
    					warehouseName
    					operation
    				}
    				sum {
    					requestDurationMs
    				}
    			}
    		}
    	}
    }

[PreviousDeleting data](https://developers.cloudflare.com/basin-catalog/deleting-data/)[NextPricing](https://developers.cloudflare.com/basin-catalog/platform/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/observability/metrics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
