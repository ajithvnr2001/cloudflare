---
url: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/
title: Querying Workers Metrics with GraphQL \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.371112+00:00
---

# Querying Workers Metrics with GraphQL · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Tutorials
  5. /Querying Workers Metrics with GraphQL



# Querying Workers Metrics with GraphQL

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-workers-metrics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Call

In this example, we are going to use the GraphQL Analytics API to query for Workers Metrics over a specified time period. We can query up to one month of data for dates up to three months ago.

The following API call will request a Worker script's metrics over a one day period, and output the requested fields. Be sure to replace `<CLOUDFLARE_ACCOUNT_TAG>` and `<API_TOKEN>`1 with your API credentials, and adjust the `datetimeStart`, `datetimeEnd`, and `scriptName` variables as needed.

## API Call
    
    
    echo '{ "query":
      "query GetWorkersAnalytics($accountTag: string, $datetimeStart: string, $datetimeEnd: string, $scriptName: string) {
        viewer {
          accounts(filter: {accountTag: $accountTag}) {
            workersInvocationsAdaptive(limit: 100, filter: {
              scriptName: $scriptName,
              datetime_geq: $datetimeStart,
              datetime_leq: $datetimeEnd
            }) {
              sum {
                subrequests
                requests
                errors
              }
              quantiles {
                cpuTimeP50
                cpuTimeP99
              }
              dimensions{
                datetime
                scriptName
                status
              }
            }
          }
        }
      }",
      "variables": {
        "accountTag": "<CLOUDFLARE_ACCOUNT_TAG>",
        "datetimeStart": "2022-08-04T00:00:00.000Z",
        "datetimeEnd": "2022-08-04T01:00:00.000Z",
        "scriptName": "worker-subrequest-test-client"
      }
    }' | tr -d '\n' | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @-

The results returned will be in JSON (as requested), so piping the output to `jq` will make them easier to read, like in the following example:
    
    
    ... | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @- | jq .
    
    #=> {
    #=>   "data": {
    #=>     "viewer": {
    #=>       "accounts": [
    #=>         {
    #=>           "workersInvocationsAdaptive": [
    #=>             {
    #=>               "dimensions": {
    #=>                 "datetime": "2020-05-04T18:10:35Z",
    #=>                 "scriptName": "worker-subrequest-test-client",
    #=>                 "status": "success"
    #=>               },
    #=>               "quantiles": {
    #=>                 "cpuTimeP50": 206,
    #=>                 "cpuTimeP99": 206
    #=>               },
    #=>               "sum": {
    #=>                 "errors": 0,
    #=>                 "requests": 1,
    #=>                 "subrequests": 0
    #=>               }
    #=>             },
    #=>             {
    #=>               "dimensions": {
    #=>                 "datetime": "2020-05-04T18:10:34Z",
    #=>                 "scriptName": "worker-subrequest-test-client",
    #=>                 "status": "success"
    #=>               },
    #=>               "quantiles": {
    #=>                 "cpuTimeP50": 291,
    #=>                 "cpuTimeP99": 291
    #=>               },
    #=>               "sum": {
    #=>                 "errors": 0,
    #=>                 "requests": 1,
    #=>                 "subrequests": 0
    #=>               }
    #=>             },
    #=>             {
    #=>               "dimensions": {
    #=>                 "datetime": "2020-05-04T18:10:49Z",
    #=>                 "scriptName": "worker-subrequest-test-client",
    #=>                 "status": "success"
    #=>               },
    #=>               "quantiles": {
    #=>                 "cpuTimeP50": 212.5,
    #=>                 "cpuTimeP99": 261.19
    #=>               },
    #=>               "sum": {
    #=>                 "errors": 0,
    #=>                 "requests": 4,
    #=>                 "subrequests": 0
    #=>               }
    #=>             }
    #=>           ]
    #=>         }
    #=>       ]
    #=>     }
    #=>   },
    #=>   "errors": null
    #=> }

## Footnotes

  1. Refer to [Configure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/) for more information on configuration and permissions. ↩




[PreviousQuerying Magic Transit endpoint health check results with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/)[NextOverview](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/tutorials/querying-workers-metrics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
