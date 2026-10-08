---
url: https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map/
title: NAv1 to NAv2 schema map \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:14.280718+00:00
---

# NAv1 to NAv2 schema map · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)[Migration guides](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/)

  4. /[Network Analytics v1 to Network Analytics v2](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/)
  5. /NAv1 to NAv2 schema map



# NAv1 to NAv2 schema map

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following table lists direct mappings between NAv1 and NAv2 fields, when available, and provides related fields when there is no direct mapping available.

ipFlows1mGroups| magicTransitNetworkAnalytics-AdaptiveGroups /  
spectrumNetworkAnalytics-AdaptiveGroups| dosdNetworkAnalytics-AdaptiveGroups| dosdAttackAnalytics-Groups| flowtrackdNetworkAnalytics-AdaptiveGroups| magicFirewallNetworkAnalytics-AdaptiveGroups  
---|---|---|---|---|---  
`date`|  _Related fields:_  
`datetime`  
`datetimeTenSeconds`|  _Related fields:_  
`datetime`  
`datetimeTenSeconds`| |  _Related fields:_  
`datetime`  
`datetimeTenSeconds`|  _Related fields:_  
`datetime`  
`datetimeTenSeconds`  
`datetimeMinute`| `datetimeMinute`| `datetimeMinute`| | `datetimeMinute`| `datetimeMinute`  
`datetimeFiveMinutes`| `datetimeFiveMinutes`| `datetimeFiveMinutes`| | `datetimeFiveMinutes`| `datetimeFiveMinutes`  
`datetimeFifteenMinutes`| `datetimeFifteenMinutes`| `datetimeFifteenMinutes`| | `datetimeFifteenMinutes`| `datetimeFifteenMinutes`  
`datetimeHour`| `datetimeHour`| `datetimeHour`| | `datetimeHour`| `datetimeHour`  
`attackId`*| | `attackId`*| `attackId`*| |   
`attackType`| | | `attackType`| |   
`attackMitigationType`| | | `mitigationType`| |   
`sourceIPCountry`| `sourceCountry`| `sourceCountry`| | `sourceCountry`| `sourceCountry`  
`sourceIPAsn`| `sourceAsn`| `sourceAsn`| | `sourceAsn`| `sourceAsn`  
`sourceIPASNDescription`|  _Related field:_  
`sourceGeohash`|  _Related field:_  
`sourceGeohash`| |  _Related field:_  
`sourceGeohash`|  _Related field:_  
`sourceGeohash`  
`coloCode`| `coloCode`| `coloCode`| | `coloCode`| `coloCode`  
`coloCity`| `coloCity`| `coloCity`| | `coloCity`| `coloCity`  
`coloCountry`| `coloCountry`| `coloCountry`| | `coloCountry`| `coloCountry`  
`coloRegion`|  _Related field:_  
`coloGeohash`|  _Related field:_  
`coloGeohash`| |  _Related field:_  
`coloGeohash`|  _Related field:_  
`coloGeohash`  
ipFlows1mGroups| magicTransitNetworkAnalytics-AdaptiveGroups /  
spectrumNetworkAnalytics-AdaptiveGroups| dosdNetworkAnalytics-AdaptiveGroups| dosdAttackAnalytics-Groups| flowtrackdNetworkAnalytics-AdaptiveGroups| magicFirewallNetworkAnalytics-AdaptiveGroups  
`ipVersion`| `ethertype`| `ethertype`| | `ethertype`| `ethertype`  
`bits`| `ipTotalLength`   
(`bits` divided by 8)| `ipTotalLength`   
(`bits` divided by 8)| `bits`| `ipTotalLength`   
(`bits` divided by 8)| `ipTotalLength`   
(`bits` divided by 8)  
`packets`|  _n/a_|  _n/a_| `packets`|  _n/a_|  _n/a_  
`ipProtocol`| `ipProtocol`| `ipProtocol`| `ipProtocol`| `ipProtocol`| `ipProtocol`  
`sourceIP`| `ipSourceAddress`| `ipSourceAddress`| `sourceIp`| `ipSourceAddress`| `ipSourceAddress`  
`destinationIP`| `ipDestinationAddress`| `ipDestinationAddress`| `destinationIp`| `ipDestinationAddress`| `ipDestinationAddress`  
`destinationIPv4Range24`| `ipDestinationSubnet`| `ipDestinationSubnet`| | `ipDestinationSubnet`| `ipDestinationSubnet`  
`destinationIPv4Range23`|  _n/a_|  _n/a_| |  _n/a_|  _n/a_  
`sourcePort`| `sourcePort`| `sourcePort`| `sourcePort`| `sourcePort`| `sourcePort`  
`destinationPort`| `destinationPort`| `destinationPort`| `destinationPort`| `destinationPort`| `destinationPort`  
`tcpFlags`| `tcpFlags`| `tcpFlags`| `tcpFlags`| `tcpFlags`| `tcpFlags`  
  
* The `attackId` field value may be different between NAv1 and NAv2 for the same attack.

[PreviousNAv2 node reference](https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/)[NextOverview](https://developers.cloudflare.com/analytics/analytics-engine/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
