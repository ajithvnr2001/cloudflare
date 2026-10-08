---
url: https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/
title: Settings node \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.420646+00:00
---

# Settings node · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)Features

  4. /[Discovery](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/)
  5. /Settings node



# Settings node

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFormatA sample query

Cloudflare GraphQL API exposes more than 70 datasets to its customers. These datasets represent different Cloudflare products with very different data shapes; thus, each has its configuration of [limits](https://developers.cloudflare.com/analytics/graphql-api/limits/).

Although we allow access to ALL plans for the essential datasets (like `httpRequestsAdaptiveGroups`, `firewallEventsAdaptive`, etc), users on larger plans benefit from an extended set of datasets and wider query limits.

In addition to [introspection](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/), users can use the Settings node that is available for both zones and accounts scopes.

## Format

`Settings` node has all datasets from `zones` and `accounts` as fields.

Using a settings node on accounts nodesgraphql
    
    
    {
      viewer {
        accounts(filter: { accountTag : $accountTag }) {
          settings {
            # any dataset(s) from accounts
          }
        }
        zones(filter: { zoneTag : $zoneTag }) {
          settings {
            # any dataset(s) from zones
          }
        }
      }
    }

Every subnode of `settings` node could consist of these fields:

  * `enabled` \- shows whether the node is available for a requester or not;
  * `availableFields` \- shows the list of fields available for a requester. If it is a nested field, the path will be returned, like `sum_requests`;
  * `maxPageSize` \- retrieves the maximum number of records that can be returned
  * `maxNumberOfFields` \- answers on how many fields could be used in a single query for that node;
  * `notOlderThan` \- returns a number of seconds on how far back in time a query can read;
  * `maxDuration` \- shows how wide the requested time range could be.



## A sample query

Get boundaries of firewallEventsAdaptive nodegraphql
    
    
    query SampleQuery($zoneTag: string) {
    	viewer {
    		zones(filter: { zoneTag: $zoneTag }) {
    			settings {
    				firewallEventsAdaptive {
    					enabled
    					maxDuration
    					maxNumberOfFields
    					maxPageSize
    					notOlderThan
    				}
    			}
    		}
    	}
    }

firewallEventsAdaptive limits for a given userjson
    
    
    {
    	"data": {
    		"viewer": {
    			"zones": [
    				{
    					"settings": {
    						"firewallEventsAdaptive": {
    							"enabled": true,
    							"maxDuration": 259200,
    							"maxNumberOfFields": 30,
    							"maxPageSize": 10000,
    							"notOlderThan": 2678400
    						}
    					}
    				}
    			]
    		}
    	},
    	"errors": null
    }

To get more details on how to execute queries, please refer to our how to get started [guides](https://developers.cloudflare.com/analytics/graphql-api/getting-started/).

[PreviousIntrospection](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/introspection/)[NextFiltering](https://developers.cloudflare.com/analytics/graphql-api/features/filtering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/features/discovery/settings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
