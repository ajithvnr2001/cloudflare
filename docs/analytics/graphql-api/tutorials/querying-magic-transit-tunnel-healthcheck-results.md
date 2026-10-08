---
url: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/
title: Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.189933+00:00
---

# Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Tutorials
  5. /Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL



# Querying Magic Transit and Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Call

This example uses the GraphQL Analytics API to query Magic Transit or Cloudflare WAN tunnel health check results. These results are aggregated from individual health checks that Cloudflare servers perform against the tunnels you configured in your account. You can query up to one week of data for dates up to three months in the past.

The following API call requests tunnel health checks for a specific account over a one-day period for a specific Cloudflare data center and outputs the requested fields. Replace `<CLOUDFLARE_ACCOUNT_TAG>` and `<API_TOKEN>`1 with your API credentials, and adjust the `datetimeStart` and `datetimeEnd` variables as needed.

The API call returns tunnel health check results by Cloudflare data center. Cloudflare aggregates each data center's result from health checks conducted on individual servers. The `tunnelState` field represents the state of the tunnel. Magic Transit or Cloudflare WAN uses these states for routing. A `tunnelState` value of `0` represents a down tunnel, `0.5` represents a degraded tunnel, and `1` represents a healthy tunnel.

## API Call
    
    
    echo '{ "query":
      "query GetTunnelHealthCheckResults($accountTag: string, $datetimeStart: string, $datetimeEnd: string) {
        viewer {
          accounts(filter: {accountTag: $accountTag}) {
            magicTransitTunnelHealthChecksAdaptiveGroups(
              limit: 100,
              filter: {
                datetime_geq: $datetimeStart,
                datetime_lt:  $datetimeEnd,
              }
            ) {
              avg {
                tunnelState
              }
              dimensions {
                tunnelName
                edgeColoName
              }
            }
          }
        }
      }",
      "variables": {
        "accountTag": "<CLOUDFLARE_ACCOUNT_TAG>",
        "datetimeStart": "2022-08-04T00:00:00.000Z",
        "datetimeEnd": "2022-08-04T01:00:00.000Z"
      }
    }' | tr -d '\n' | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @-

The results are returned in JSON (as requested), so piping the output to `jq` formats them for easier parsing, as in the following example:
    
    
    ... | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @- | jq .
    
    ## Example response:
    #=> {
    #=>   "data": {
    #=>     "viewer": {
    #=>       "accounts": [
    #=>         {
    #=>           "conduitEdgeTunnelHealthChecks": [
    #=>             {
    #=>               {
    #=>                 "avg": {
    #=>                   "tunnelState": 1
    #=>                 },
    #=>                 "dimensions": {
    #=>                   "edgeColoName": "mel01",
    #=>                   "tunnelName": "tunnel_01",
    #=>                   "tunnelState": 0.5
    #=>                 }
    #=>               },
    #=>               {
    #=>                 "avg": {
    #=>                   "tunnelState": 0.5
    #=>                 },
    #=>                 "count": 310,
    #=>                 "dimensions": {
    #=>                   "edgeColoName": "mel01",
    #=>                   "tunnelName": "tunnel_02",
    #=>                   "tunnelState": 0.5
    #=>                 }
    #=>               }
    #=>           ]
    #=>         }
    #=>       ]
    #=>     }
    #=>   },
    #=>   "errors": null
    #=> }

## Footnotes

  1. For details, refer to [Configure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/). ↩




[PreviousQuerying Magic Transit and Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-bandwidth-analytics/)[NextQuerying Magic Transit endpoint health check results with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
