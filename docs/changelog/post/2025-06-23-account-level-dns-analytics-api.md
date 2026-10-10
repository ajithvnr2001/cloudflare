---
url: https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/
title: Account-level DNS analytics now available via GraphQL Analytics API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.502037+00:00
---

# Account-level DNS analytics now available via GraphQL Analytics API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-23-account-level-dns-analytics-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 19, 2025

## Account-level DNS analytics now available via GraphQL Analytics API

[DNS](https://developers.cloudflare.com/dns/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Authoritative DNS analytics are now available on the **account level** via the [Cloudflare GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

This allows users to query DNS analytics across multiple zones in their account, by using the `accounts` filter.

Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an `NXDOMAIN` response over a given time frame. Please replace `a30f822fcd7c401984bf85d8f2a5111c` with your actual account ID.

GraphQL example for account-level DNS analyticsgraphql
    
    
    query GetLatestNXDOMAINResponses {
    	viewer {
    		accounts(filter: { accountTag: "a30f822fcd7c401984bf85d8f2a5111c" }) {
    			dnsAnalyticsAdaptive(
    				filter: {
    					date_geq: "2025-06-16"
    					date_leq: "2025-06-18"
    					responseCode: "NXDOMAIN"
    				}
    				limit: 10000
    				orderBy: [datetime_DESC]
    			) {
    				zoneTag
    				queryName
    				responseCode
    				queryType
    				datetime
    			}
    		}
    	}
    }

To learn more and get started, refer to the [DNS Analytics documentation](https://developers.cloudflare.com/dns/additional-options/analytics/#analytics).
