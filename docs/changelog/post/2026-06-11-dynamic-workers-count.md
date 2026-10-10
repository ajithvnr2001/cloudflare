---
url: https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/
title: Track Dynamic Workers usage from the dashboard and GraphQL API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.964631+00:00
---

# Track Dynamic Workers usage from the dashboard and GraphQL API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-11-dynamic-workers-count/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 11, 2026

## Track Dynamic Workers usage from the dashboard and GraphQL API

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

![Dynamic Workers usage on the Workers overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=1102,format=webp/_astro/dynamic-workers-count.BcGsgQ0m.png)

Customers can now view the number of [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) invoked during their billing period from the Workers overview page in the Cloudflare dashboard.

This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.

You can also query this count through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) by using `workersInvocationsByOwnerAndScriptGroups` and selecting `distinctDynamicWorkerCount`:
    
    
    query getDynamicWorkersCount(
    	$accountTag: string!
    	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {
    				uniq {
    					distinctDynamicWorkerCount
    				}
    			}
    		}
    	}
    }

Use variables to set the account and billing-period date range:
    
    
    {
    	"accountTag": "<ACCOUNT_ID>",
    	"filter": {
    		"date_geq": "2026-06-01",
    		"date_leq": "2026-06-30"
    	}
    }

For more information, refer to [Dynamic Workers pricing](https://developers.cloudflare.com/dynamic-workers/pricing/).
