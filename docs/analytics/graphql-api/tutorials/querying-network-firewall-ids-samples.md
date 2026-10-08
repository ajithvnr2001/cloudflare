---
url: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples/
title: Querying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.309044+00:00
---

# Querying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Tutorials
  5. /Querying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL



# Querying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Call

In this example, we are going to use the GraphQL Analytics API to query for IDS samples over a specified time period.

The following API call will request IDS samples over a one hour period, and output the requested fields. Be sure to replace `<CLOUDFLARE_ACCOUNT_TAG>` and `<API_TOKEN>`1 with your account tag and API credentials, and adjust the `datetime_geg` and `datetime_leq` values to your liking.

## API Call
    
    
    echo '{ "query":
      "query IDSActivity {
        viewer {
          accounts(filter: { accountTag: $accountTag }) {
            magicIDPSNetworkAnalyticsAdaptiveGroups(
              filter: $filter
              limit: 10
            ) {
              sum {
                bits
                packets
              }
              dimensions {
                datetimeFiveMinutes
              }
            }
          }
        }
      }",
      "variables": {
        "accountTag": "<CLOUDFLARE_ACCOUNT_TAG>",
        "filter": {
          "datetime_geq": "2023-06-20T11:00:00.000Z",
          "datetime_leq": "2023-06-20T12:00:00.000Z",
          "verdict": "drop",
          "outcome": "pass"
        }
      }
    }' | tr -d '\n' | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @-

The returned values represent the total number of packets and bits that matched IDS rules during the five minute interval. The result will be in JSON (as requested), so piping the output to `jq` will make it easier to read, like in the following example:
    
    
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
    #=>           "magicIDPSNetworkAnalyticsAdaptiveGroups": [
    #=>             {
    #=>               sum: { bits:  327680, packets: 16384 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:00-00:00'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  360448, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:05-00:00'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  327680, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:05-00:00'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  360448, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:20-00:00'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  327680, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:20-00:00'
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




[PreviousQuerying Access login events with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-access-login-events/)[NextQuerying Cloudflare Network Firewall Samples with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
