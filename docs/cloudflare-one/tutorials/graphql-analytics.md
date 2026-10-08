---
url: https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/
title: GraphQL Analytics \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:22.749516+00:00
---

# GraphQL Analytics · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Tutorials](https://developers.cloudflare.com/cloudflare-one/tutorials/)
  4. /Graphql Analytics



# GraphQL Analytics

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewObtain Cloudflare Account ID Obtain your Cloudflare Account ID Obtain the rule ID for a firewall ruleExplore GraphQL schema with Cloudflare Network Firewall query exampleExample queries for Cloudflare Network Firewall Obtain analytics for a specific rule Obtain IDS analytics

Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic. This contains both rules you configured in the Cloudflare Network Firewall dashboard, and the rules managed by Cloudflare as a part of [Cloudflare Network Firewall Managed rules](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/) and [Cloudflare Network Firewall IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/) features.

Before you begin, you must have an [API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/). For additional help getting started with GraphQL Analytics, refer to [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

## Obtain Cloudflare Account ID

To construct a Network Firewall GraphQL query for an object, you will need a Cloudflare Account ID

### Obtain your Cloudflare Account ID

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), and select your account.
  2. The URL in your browser's address bar should show `https://dash.cloudflare.com/` followed by a hex string. The hex string is your Cloudflare Account ID.



### Obtain the rule ID for a firewall rule

To construct queries to gather analytics for a particular rule, you need the rule ID for each firewall rule.

  1. In the Cloudflare dashboard, go to the **Cloudflare Network Firewall** page.

[ Go to **Firewall policies** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall)
  2. In the **Custom rules** tab, locate the rule you need the rule ID for from the list and select the three dots > **Edit**.

  3. Locate the **Rule ID** and select the copy button.

  4. Select **Cancel** to return to the **Cloudflare Network Firewall** page.




## Explore GraphQL schema with Cloudflare Network Firewall query example

In this section, you will run a test query to retrieve a five minute count of all configured Cloudflare Network Firewall rules within five minute intervals. You can copy and paste the code below into GraphiQL.

For additional information about the Analytics schema, refer to [Explore the Analytics schema with GraphiQL](https://developers.cloudflare.com/analytics/graphql-api/getting-started/explore-graphql-schema/).
    
    
    query MagicFirewallExample($accountTag: string!, $start: Time, $end: Time) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			magicFirewallSamplesAdaptiveGroups(
    				filter: { datetime_geq: $start, datetime_leq: $end }
    				limit: 2
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
    }

## Example queries for Cloudflare Network Firewall

### Obtain analytics for a specific rule

Use the example below to display the total number of packets and bits for the top ten suspected malicious traffic streams within the last hour. After receiving the results, you can sort by packet rates with a five minute average.

For each stream, display the:

  * Source and destination IP addresses
  * Ingress Cloudflare data centers that received it
  * Total traffic volume in bits and packets received within the hour
  * Actions taken by the firewall rule


    
    
    query MagicFirewallObtainRules(
    	$accountId: string!
    	$ruleId: string
    	$start: Time
    	$end: Time
    ) {
    	viewer {
    		accounts(filter: { accountTag: $accountId }) {
    			magicFirewallNetworkAnalyticsAdaptiveGroups(
    				filter: { ruleId: $ruleId, datetime_geq: $start, datetime_leq: $end }
    				limit: 10
    				orderBy: [avg_packetRateFiveMinutes_DESC]
    			) {
    				sum {
    					bits
    					packets
    				}
    				dimensions {
    					coloCity
    					ipDestinationAddress
    					ipSourceAddress
    					outcome
    				}
    			}
    		}
    	}
    }

### Obtain IDS analytics

Use the example below to display the total number of packets and bits for the top 10 traffic streams that Cloudflare Network Firewall IDS has detected in the last hour.

By setting `verdict` to `drop` and `outcome` as `pass`, we are filtering for traffic that was marked as a detection (i.e. verdict was drop) but was not dropped (for example, outcome was `pass`). This is because currently, Cloudflare Network Firewall IDS only detects malicious traffic but does not drop the traffic.

For each stream, display the:

  * Source and destination IP addresses.
  * Ingress Cloudflare data centers that received it.
  * Total traffic volume in bits and packets received within the hour.


    
    
    query MagicFirewallObtainIDS($accountTag: string!, $start: Time, $end: Time) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			magicIDPSNetworkAnalyticsAdaptiveGroups(
    				filter: {
    					datetime_geq: $start
    					datetime_leq: $end
    					verdict: drop
    					outcome: pass
    				}
    				limit: 10
    				orderBy: [avg_packetRateFiveMinutes_DESC]
    			) {
    				sum {
    					bits
    					packets
    				}
    				dimensions {
    					coloCity
    					ipDestinationAddress
    					ipSourceAddress
    				}
    			}
    		}
    	}
    }

Alternatively, to inspect all traffic that was analyzed, but grouped into malicious traffic and other traffic, the example below can be used. The response will contain two entries for each five minute timestamp. `verdict` will be set to `drop` for malicious traffic, and `verdict` will be set to `pass` for traffic that did not match any of the IDS rules.
    
    
    query MagicFirewallTraffic($accountTag: string!, $start: Time, $end: Time) {
    	viewer {
    		accounts(filter: { accountTag: $accountTag }) {
    			magicIDPSNetworkAnalyticsAdaptiveGroups(
    				filter: { datetime_geq: $start, datetime_leq: $end }
    				limit: 10
    				orderBy: [avg_packetRateFiveMinutes_DESC]
    			) {
    				sum {
    					bits
    					packets
    				}
    				dimensions {
    					coloCity
    					ipDestinationAddress
    					ipSourceAddress
    					verdict
    				}
    			}
    		}
    	}
    }

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/tutorials/graphql-analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
