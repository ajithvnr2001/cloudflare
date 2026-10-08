---
url: https://developers.cloudflare.com/spectrum/reference/analytics/
title: Analytics \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:33.561401+00:00
---

# Analytics · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/reference/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /Reference
  4. /Analytics



# Analytics

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/spectrum/reference/analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional dimensionsOperators for filteringAnalytics request structureAnalytics query example

Cloudflare measures the following metrics for every connection.

Metric | Name | Example | Unit  
---|---|---|---  
count | Count of total events | `1000` | Count  
bytesIngress | Sum of ingress bytes | `1000` | Sum  
bytesEgress | Sum of egress bytes | `1000` | Sum  
durationAvg | Average connection duration | `1.0` | Time in milliseconds  
durationMedian | Median connection duration | `1.0` | Time in milliseconds  
duration90th | 90th percentile connection duration | `1.0` | Time in milliseconds  
duration99th | 99th percentile connection duration | `1.0` | Time in milliseconds  
  
## Additional dimensions

You can divide your analytics further by the following dimensions.

Dimension | Name | Example  
---|---|---  
event | Connection Event | `connect`, `progress`, `disconnect`, `originError`, `clientFiltered`  
appID | Application ID | `40d67c87c6cd4b889a4fd57805225e85`  
coloName | Colo Name | `SFO`  
ipVersion | IP version used by the client | `4`, `6`  
  
## Operators for filtering

Use the operators below to filter data.

Operator | Name | URL Encoded  
---|---|---  
`==` | Equals | `%3D%3D`  
`!=` | Does not equal | `!%3D`  
`>` | Greater Than | `%3E`  
`<` | Less Than | `%3C`  
`>=` | Greater than or equal to | `%3E%3D`  
`<=` | Less than or equal to | `%3C%3D`  
  
Combine filters using `OR` and `AND` boolean logic:

  * `AND` takes precedence over `OR` in all expressions.

  * The `OR` operator is defined using a comma `,` or the `OR` keyword surrounded by whitespace.

  * The `AND` operator is defined using a semicolon `;` or the `AND` keyword surrounded by whitespace.

Note

Note that the semicolon is a reserved character in URLs ([RFC 1738 ↗︎](https://www.rfc-editor.org/rfc/rfc1738)) and should be percent-encoded as `%3B`.




## Analytics request structure
    
    
    /api/v4/zones/{zone_id}/spectrum/analytics/events/summary?metrics=METRICS&dimensions=DIMENSIONS&filters=FILTERS&since=FROM_TS&sort=SORT&until=TO_TS&limit=LIMIT
    /api/v4/zones/{zone_id}/spectrum/analytics/events/bytime?metrics=METRICS&dimensions=DIMENSIONS&filters=FILTERS&since=FROM_TS&sort=SORT&until=TO_TS&limit=LIMIT

  * METRICS is one or more metrics (such as count) to compute
  * DIMENSIONS can be used to break down the data by given attributes
  * FILTERS used to filter rows by one or more dimensions (see Filters section below)
  * SORT is the sort order for the result set; sort fields must be included in METRICS or DIMENSIONS
  * TO_TS is the end of time interval to query, defaults to current time
  * FROM_TS is the start of time interval to query, defaults to TO_TS - 6 hours
  * STEP is used to select time series resolution when using endpoint:
  * auto or omitted - selects time step most appropriate to time interval 
    * year
    * quarter
    * month
    * week
    * day
    * hour



## Analytics query example

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Analytics Read`

Get analytics summarybash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/analytics/events/summary" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Refer to the [Spectrum API documentation](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/aggregates/subresources/currents/methods/get/) for more examples of API requests.

[PreviousEnable Proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/)[NextConfiguration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/reference/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
