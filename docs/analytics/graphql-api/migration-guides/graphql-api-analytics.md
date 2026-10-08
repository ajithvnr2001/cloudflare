---
url: https://developers.cloudflare.com/analytics/graphql-api/migration-guides/graphql-api-analytics/
title: HTTP Requests by Colo Groups to HTTP Requests by Adaptive Groups \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.855072+00:00
---

# HTTP Requests by Colo Groups to HTTP Requests by Adaptive Groups · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/migration-guides/graphql-api-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /[Migration guides](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/)
  5. /HTTP Requests by Colo Groups to HTTP Requests by Adaptive Groups



# HTTP Requests by Colo Groups to HTTP Requests by Adaptive Groups

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/graphql-api-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewhttpRequestsAdaptiveGroups GraphQL API node

This guide shares considerations when migrating from the deprecated `httpRequests1mByColoGroups` and `httpRequests1dByColoGroups` GraphQL API nodes to the `httpRequestsAdaptiveGroups` GraphQL API node.

For example, if you wanted to see which five data centers had the most number of requests, the total number of those requests, and the total amount of data transfer, in the past you used the `httpRequests1mByColoGroups` GraphQL API node as in the following example:
    
    
    {
    	viewer {
    		zones(filter: { zoneTag: $zoneTag }) {
    			series: httpRequests1mByColoGroups(
    				limit: 5
    				orderBy: [sum_requests_DESC]
    				filter: { datetime_geq: $start, datetime_lt: $end }
    			) {
    				sum {
    					requests
    					bytes
    				}
    				dimensions {
    					coloCode
    				}
    			}
    		}
    	}
    }

Response
    
    
    {
    	"data": {
    		"viewer": {
    			"zones": [
    				{
    					"series": [
    						{
    							"dimensions": {
    								"coloCode": "LHR"
    							},
    							"sum": {
    								"bytes": 18260055,
    								"requests": 4404
    							}
    						},
    						{
    							"dimensions": {
    								"coloCode": "AMS"
    							},
    							"sum": {
    								"bytes": 17563009,
    								"requests": 4302
    							}
    						},
    						{
    							"dimensions": {
    								"coloCode": "CDG"
    							},
    							"sum": {
    								"bytes": 17200434,
    								"requests": 4032
    							}
    						},
    						{
    							"dimensions": {
    								"coloCode": "PTY"
    							},
    							"sum": {
    								"bytes": 10400209,
    								"requests": 2707
    							}
    						},
    						{
    							"dimensions": {
    								"coloCode": "JIB"
    							},
    							"sum": {
    								"bytes": 9040105,
    								"requests": 2601
    							}
    						}
    					]
    				}
    			]
    		}
    	},
    	"errors": null
    }

## `httpRequestsAdaptiveGroups` GraphQL API node

With the deprecation of the `httpRequests1mByColoGroups` and `httpRequests1dByColoGroups` GraphQL API nodes, use the `httpRequestsAdaptiveGroups` GraphQL API node to access the same data (`count`, `sum(edgeResponseBytes)`, and `visits`).

**Request**
    
    
    query MigrationSample($zoneTag: string, $start: Time, $end: Time) {
    	viewer {
    		zones(filter: { zoneTag: $zoneTag }) {
    			series: httpRequestsAdaptiveGroups(
    				limit: 5
    				orderBy: [count_DESC]
    				filter: {
    					datetime_geq: $start
    					datetime_lt: $end
    					requestSource: "eyeball"
    				}
    			) {
    				count
    				avg {
    					sampleInterval
    				}
    				sum {
    					visits
    					edgeResponseBytes
    				}
    				dimensions {
    					coloCode
    				}
    			}
    		}
    	}
    }

Response
    
    
    {
    	"data": {
    		"viewer": {
    			"zones": [
    				{
    					"series": [
    						{
    							"avg": {
    								"sampleInterval": 10
    							},
    							"count": 4350,
    							"dimensions": {
    								"coloCode": "LHR"
    							},
    							"sum": {
    								"edgeResponseBytes": 17860000,
    								"visits": 4120
    							}
    						},
    						{
    							"avg": {
    								"sampleInterval": 10
    							},
    							"count": 4210,
    							"dimensions": {
    								"coloCode": "AMS"
    							},
    							"sum": {
    								"edgeResponseBytes": 17110000,
    								"visits": 3910
    							}
    						},
    						{
    							"avg": {
    								"sampleInterval": 10
    							},
    							"count": 3890,
    							"dimensions": {
    								"coloCode": "CDG"
    							},
    							"sum": {
    								"edgeResponseBytes": 17050000,
    								"visits": 3700
    							}
    						},
    						{
    							"avg": {
    								"sampleInterval": 10
    							},
    							"count": 2550,
    							"dimensions": {
    								"coloCode": "PTY"
    							},
    							"sum": {
    								"edgeResponseBytes": 10286000,
    								"visits": 2130
    							}
    						},
    						{
    							"avg": {
    								"sampleInterval": 10
    							},
    							"count": 2410,
    							"dimensions": {
    								"coloCode": "JIB"
    							},
    							"sum": {
    								"edgeResponseBytes": 9029000,
    								"visits": 2080
    							}
    						}
    					]
    				}
    			]
    		}
    	},
    	"errors": null
    }

This query says:

  * Given the indicated `zones`, `limit`, and `time range`.
  * Fetch the total number of requests (as `count`), the total amount of data transfer (as `edgeResponseBytes` of `sum` object), and the total number of `visits` per data center.



A few points to note:

  * Adding the `requestSource` filter for `eyeball` returns request, data transfer, and visit data about only the end users of your website.
  * Instead of `requests`, the `httpRequestsAdaptiveGroups` node reports `count`, which indicates the number of requests per data center.
  * To measure data transfer, use `sum(edgeResponseBytes)`. Note that in the old API this was called `bandwidth` even though it actually measured data transfer.
  * `unique visitors per colocation` is not supported in `httpRequestsAdaptiveGroups`, but the `httpRequestsAdaptiveGroups` API does support `visits`. A visit is defined as a page view that originated from a different website or direct link. Cloudflare checks where the HTTP referer does not match the hostname. One visit can consist of multiple page views.



[PreviousOverview](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/)[NextZone Analytics to GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/zone-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/migration-guides/graphql-api-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
