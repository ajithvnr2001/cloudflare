---
url: https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/
title: GraphQL Analytics \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:24.334345+00:00
---

# GraphQL Analytics · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /Tutorials
  4. /GraphQL Analytics



# GraphQL Analytics

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/tutorials/graphql-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Obtain your Cloudflare Account IDExplore GraphQL schema with Network Flow example

Use the GraphQL Analytics API to retrieve Network Flow (formerly Magic Network Monitoring) flow data.

Before you begin, you must have an [API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/). For additional help getting started with GraphQL Analytics, refer to [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

### Obtain your Cloudflare Account ID

To query Network Flow data via GraphQL, you need your Cloudflare Account ID.

  1. Log in to the Cloudflare dashboard, and select your account.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)

  2. The URL in your browser's address bar should show `https://dash.cloudflare.com/` followed by a hex string. The hex string is your Cloudflare Account ID.



## Explore GraphQL schema with Network Flow example

Run a test query to retrieve bits and packets aggregated in five-minute intervals. Copy and paste the following code into GraphiQL.

For additional information about the Analytics schema, refer to [Explore the Analytics schema with GraphiQL](https://developers.cloudflare.com/analytics/graphql-api/getting-started/explore-graphql-schema/).
    
    
    query MagicNetworkMonitoring($accountTag: string!, $start: Time, $end: Time) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			mnmFlowDataAdaptiveGroups(
    				filter: { datetime_gt: $start, datetime_leq: $end }
    				limit: 10
    				orderBy: [datetimeFiveMinutes_DESC]
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
    }

Note

Cloudflare analytics are case sensitive for paths and URIs. Make sure that filters or queries use the correct case.

[PreviousEncrypt network flow data](https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/)[NextDDoS testing guide](https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/tutorials/graphql-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
