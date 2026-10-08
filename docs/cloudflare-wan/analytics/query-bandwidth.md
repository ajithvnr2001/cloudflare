---
url: https://developers.cloudflare.com/cloudflare-wan/analytics/query-bandwidth/
title: Querying Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL \u00b7 Cloudflare WAN docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:24.957132+00:00
---

# Querying Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL · Cloudflare WAN docs

> Source: https://developers.cloudflare.com/cloudflare-wan/analytics/query-bandwidth/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)
  3. /[Analytics](https://developers.cloudflare.com/cloudflare-wan/analytics/)
  4. /Querying Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL



# Querying Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-wan/analytics/query-bandwidth/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Call

This example uses the GraphQL Analytics API to query Cloudflare WAN ingress tunnel traffic over a specified time period.

The following API call requests Cloudflare WAN ingress tunnel traffic over a one-hour period and outputs the requested fields. Replace `<CLOUDFLARE_ACCOUNT_TAG>` with your account ID, `<EMAIL>`, `<API_KEY>`1 (legacy), or `<API_TOKEN>`2 (preferred) with your API credentials, and adjust the `datetime_geq` and `datetime_leq` values as needed.

The example queries for ingress traffic. To query for egress traffic, change the value in the `direction` filter.

## API Call
    
    
    PAYLOAD='{ "query":
      "query GetTunnelHealthCheckResults($accountTag: string, $datetimeStart: string, $datetimeEnd: string) {
          viewer {
            accounts(filter: {accountTag: $accountTag}) {
              magicTransitTunnelTrafficAdaptiveGroups(
                limit: 100,
                filter: {
                  datetime_geq: $datetimeStart,
                  datetime_lt:  $datetimeEnd,
                  direction: $direction
                }
              ) {
                avg {
                  bitRateFiveMinutes
                }
                dimensions {
                  tunnelName
                  datetimeFiveMinutes
                }
              }
            }
          }
      }",
        "variables": {
          "accountTag": "<CLOUDFLARE_ACCOUNT_TAG>",
          "direction": "ingress",
          "datetimeStart": "2022-05-04T11:00:00.000Z",
          "datetimeEnd": "2022-05-04T12:00:00.000Z"
        }
      }
    }'
    
    # curl with Legacy API Key
    curl https://api.cloudflare.com/client/v4/graphql \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data "$(echo $PAYLOAD)"
    
    # curl with API Token
    curl https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data "$(echo $PAYLOAD)"

The returned values represent the total bandwidth in bits per second during the five-minute interval for a particular tunnel. To use aggregations other than five minutes, use the same time window for both your metric and datetime. For example, to analyze hourly groups, use `bitRateHour` and `datetimeHour`.

The result is in JSON (as requested), so piping the output to `jq` formats it for easier parsing, as in the following example:
    
    
    curl https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data "$(echo $PAYLOAD)" | jq .
    
    ## Example response:
    #=> {
    #=>   "data": {
    #=>     "viewer": {
    #=>       "accounts": [
    #=>         {
    #=>           "magicTransitTunnelTrafficAdaptiveGroups": [
    #=>             {
    #=>               avg: { bitRateFiveMinutes:  327680 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:00-00:00',
    #=>                 tunnelName: 'tunnel_name'
    #=>               }
    #=>             },
    #=>             {
    #=>               avg: { bitRateFiveMinutes:  627213680 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:05-00:00',
    #=>                 tunnelName: 'another_tunnel'
    #=>              }
    #=>             }
    #=>           ]
    #=>         }
    #=>       ]
    #=>     }
    #=>   },
    #=>   "errors": null
    #=> }

## Footnotes

  1. For details, refer to [Authenticate with a Cloudflare API key](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-key-auth/). ↩

  2. For details, refer to [Configure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/). ↩




[PreviousPacket captures ↗︎](https://developers.cloudflare.com/cloudflare-network-firewall/packet-captures/)[NextQuerying Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL](https://developers.cloudflare.com/cloudflare-wan/analytics/query-tunnel-health/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-wan/analytics/query-bandwidth.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
