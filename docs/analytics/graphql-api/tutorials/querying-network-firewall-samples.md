---
url: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/
title: Querying Cloudflare Network Firewall Samples with GraphQL \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.607839+00:00
---

# Querying Cloudflare Network Firewall Samples with GraphQL · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Tutorials
  5. /Querying Cloudflare Network Firewall Samples with GraphQL



# Querying Cloudflare Network Firewall Samples with GraphQL

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAPI Call

In this example, we are going to use the GraphQL Analytics API to query for Cloudflare Network Firewall Samples over a specified time period.

The following API call will request Cloudflare Network Firewall Samples over a one hour period, and output the requested fields. Be sure to replace `<CLOUDFLARE_ACCOUNT_TAG>` and `<API_TOKEN>`1 with your zone tag and API credentials, and adjust the `datetime_geg` and `datetime_leq` values to your liking.

## API Call
    
    
    echo '{ "query":
      "query MFWActivity {
        viewer {
          accounts(filter: { accountTag: $accountTag }) {
            magicFirewallSamplesAdaptiveGroups(
              filter: $filter
              limit: 10
              orderBy: [datetimeFiveMinute_DESC]
            ) {
              sum {
                bits
                packets
              }
              dimensions {
                datetimeFiveMinute
                ruleId
              }
            }
          }
        }
      }",
      "variables": {
        "accountTag": "<CLOUDFLARE_ACCOUNT_TAG>",
        "filter": {
          "datetime_geq": "2022-07-24T11:00:00Z",
          "datetime_leq": "2022-07-24T11:10:00Z"
        }
      }
    }' | tr -d '\n' | curl --silent \
    https://api.cloudflare.com/client/v4/graphql \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --data @-

The returned values represent the total number of packets and bits received during the five minute interval for a particular rule. The result will be in JSON (as requested), so piping the output to `jq` will make it easier to read, like in the following example:
    
    
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
    #=>           "magicFirewallSamplesAdaptiveGroups": [
    #=>             {
    #=>               sum: { bits:  327680, packets: 16384 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:00-00:00',
    #=>                 ruleId: 'bdfa8f8f0ae142b4a70ef15f6160e532'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  360448, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:05-00:00',
    #=>                 ruleId: 'bdfa8f8f0ae142b4a70ef15f6160e532'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  327680, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:05-00:00',
    #=>                 ruleId: 'bdfa8f8f0ae142b4a70ef15f6160e532'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  360448, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:20-00:00',
    #=>                 ruleId: 'bdfa8f8f0ae142b4a70ef15f6160e532'
    #=>               }
    #=>             },
    #=>             {
    #=>               sum: { bits:  327680, packets: 8192 },
    #=>               dimensions: {
    #=>                 datetimeFiveMinute: '2021-05-12T22:20-00:00',
    #=>                 ruleId: 'bdfa8f8f0ae142b4a70ef15f6160e532'
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




[PreviousQuerying Cloudflare Network Firewall Intrusion Detection System (IDS) samples with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-ids-samples/)[NextQuerying Containers metrics with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-container-metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/tutorials/querying-network-firewall-samples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
