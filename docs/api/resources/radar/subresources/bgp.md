---
url: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/
title: BGP | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:57.388995+00:00
---

# BGP | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# BGP

##### [Get BGP time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/methods/timeseries)

GET/radar/bgp/timeseries

##### ModelsExpand Collapse 

BGPTimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, lastUpdated } 

aggInterval: "15m" or "1h" or "1d" or "1w"

One of the following:

"15m"

"1h"

"1d"

"1w"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

#### BGPLeaks

#### BGPLeaksEvents

##### [Get BGP route leak events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks/subresources/events/methods/list)

GET/radar/bgp/leaks/events

##### ModelsExpand Collapse 

EventListResponse object { asn_info, events } 

asn_info: array of object { asn, country_code, org_name } 

asn: number

country_code: string

org_name: string

events: array of object { id, countries, detected_ts, 10 more } 

id: number

countries: array of string

detected_ts: string

finished: boolean

leak_asn: number

leak_count: number

leak_seg: array of number

leak_type: number

max_ts: string

min_ts: string

origin_count: number

peer_count: number

prefix_count: number

#### BGPTop

##### [Get top prefixes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/methods/prefixes)

GET/radar/bgp/top/prefixes

##### ModelsExpand Collapse 

TopPrefixesResponse object { meta, top_0 } 

meta: object { dateRange } 

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

top_0: array of object { prefix, value } 

prefix: string

value: string

A numeric string.

#### BGPTopAses

##### [Get top ASes by BGP updates](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/get)

GET/radar/bgp/top/ases

##### [Get top ASes by prefix count](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/top/subresources/ases/methods/prefixes)

GET/radar/bgp/top/ases/prefixes

##### ModelsExpand Collapse 

AseGetResponse object { meta, top_0 } 

meta: object { dateRange } 

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

top_0: array of object { asn, ASName, value } 

asn: number

ASName: string

value: string

Percentage of updates by this AS out of the total updates by all autonomous systems.

AsePrefixesResponse object { asns, meta } 

asns: array of object { asn, country, name, pfxs_count } 

asn: number

country: string

name: string

pfxs_count: number

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

#### BGPHijacks

#### BGPHijacksEvents

##### [Get BGP hijack events](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/hijacks/subresources/events/methods/list)

GET/radar/bgp/hijacks/events

##### ModelsExpand Collapse 

EventListResponse object { asn_info, events, total_monitors } 

asn_info: array of object { asn, country_code, org_name } 

asn: number

country_code: string

org_name: string

events: array of object { id, confidence_score, duration, 15 more } 

id: number

confidence_score: number

duration: number

event_type: number

hijack_msgs_count: number

hijacker_asn: number

hijacker_country: string

is_stale: boolean

max_hijack_ts: string

max_msg_ts: string

min_hijack_ts: string

on_going_count: number

peer_asns: array of number

peer_ip_count: number

prefixes: array of string

tags: array of object { name, score } 

name: string

score: number

victim_asns: array of number

victim_countries: array of string

total_monitors: number

#### BGPRoutes

##### [Get Multi-Origin AS (MOAS) prefixes](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/moas)

GET/radar/bgp/routes/moas

##### [Get prefix-to-ASN mapping](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as)

GET/radar/bgp/routes/pfx2as

##### [Get BGP routing table stats ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/stats)

GET/radar/bgp/routes/stats

##### [List ASes from global routing tables](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/ases)

GET/radar/bgp/routes/ases

##### [Get real-time BGP routes for a prefix](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime)

GET/radar/bgp/routes/realtime

##### ModelsExpand Collapse 

RouteMoasResponse object { meta, moas } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

moas: array of object { origins, prefix } 

origins: array of object { origin, peer_count, rpki_validation } 

origin: number

peer_count: number

rpki_validation: string

prefix: string

RoutePfx2asResponse object { meta, prefix_origins } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

prefix_origins: array of object { origin, peer_count, prefix, rpki_validation } 

origin: number

peer_count: number

prefix: string

rpki_validation: string

RouteStatsResponse object { meta, stats } 

meta: object { data_time, query_time, total_peers } 

data_time: string

query_time: string

total_peers: number

stats: object { distinct_origins, distinct_origins_ipv4, distinct_origins_ipv6, 15 more } 

distinct_origins: number

distinct_origins_ipv4: number

distinct_origins_ipv6: number

distinct_prefixes: number

distinct_prefixes_ipv4: number

distinct_prefixes_ipv6: number

routes_invalid: number

routes_invalid_ipv4: number

routes_invalid_ipv6: number

routes_total: number

routes_total_ipv4: number

routes_total_ipv6: number

routes_unknown: number

routes_unknown_ipv4: number

routes_unknown_ipv6: number

routes_valid: number

routes_valid_ipv4: number

routes_valid_ipv6: number

RouteAsesResponse object { asns, meta } 

asns: array of object { asn, coneSize, country, 7 more } 

asn: number

coneSize: number

AS’s customer cone size.

country: string

Alpha-2 code for the AS’s registration country.

ipv4Count: number

Number of IPv4 addresses originated by the AS.

ipv6Count: string

Number of IPv6 addresses originated by the AS.

name: string

Name of the AS.

pfxsCount: number

Number of total IP prefixes originated by the AS.

rpkiInvalid: number

Number of RPKI invalid prefixes originated by the AS.

rpkiUnknown: number

Number of RPKI unknown prefixes originated by the AS.

rpkiValid: number

Number of RPKI valid prefixes originated by the AS.

meta: object { dataTime, queryTime, totalPeers } 

dataTime: string

The timestamp of when the data is generated.

queryTime: string

The timestamp of the query.

totalPeers: number

Total number of route collector peers used to generate this data.

RouteRealtimeResponse object { meta, routes } 

meta: object { asn_info, collectors, data_time, 2 more } 

asn_info: array of object { as_name, asn, country_code, 2 more } 

as_name: string

Name of the autonomous system.

asn: number

AS number.

country_code: string

Alpha-2 code for the AS’s registration country.

org_id: string

Organization ID.

org_name: string

Organization name.

collectors: array of object { collector, latest_realtime_ts, latest_rib_ts, 4 more } 

collector: string

Public route collector ID.

latest_realtime_ts: string

Latest real-time stream timestamp for this collector.

latest_rib_ts: string

Latest RIB dump MRT file timestamp for this collector.

latest_updates_ts: string

Latest BGP updates MRT file timestamp for this collector.

peers_count: number

Total number of collector peers used from this collector.

peers_v4_count: number

Total number of collector peers used from this collector for IPv4 prefixes.

peers_v6_count: number

Total number of collector peers used from this collector for IPv6 prefixes.

data_time: string

The most recent data timestamp for from the real-time sources.

prefix_origins: array of object { origin, prefix, rpki_validation, 3 more } 

origin: number

Origin ASN.

prefix: string

IP prefix of this query.

rpki_validation: string

Prefix-origin RPKI validation: valid, invalid, unknown.

total_peers: number

Total number of peers.

total_visible: number

Total number of peers seeing this prefix.

visibility: number

Ratio of peers seeing this prefix to total number of peers.

query_time: string

The timestamp of this query.

routes: array of object { as_path, collector, communities, 2 more } 

as_path: array of number

AS-level path for this route, from collector to origin.

collector: string

Public collector ID for this route.

communities: array of string

BGP community values.

prefix: string

IP prefix of this query.

timestamp: string

Latest timestamp of change for this route.

#### BGPRoutesUpstreams

##### [Get upstream composition time series for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries)

GET/radar/bgp/routes/upstreams/{asn}/timeseries

##### ModelsExpand Collapse 

UpstreamTimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, effectiveCollector, queryTime, stale } 

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

effectiveCollector: string

queryTime: string

Timestamp when the query was executed.

formatdate-time

stale: boolean

serie_0: object { timestamps } 

timestamps: array of string

#### BGPRoutesPaths

##### [Get tier-1 path segments for an AS](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list)

GET/radar/bgp/routes/paths/{asn}

##### ModelsExpand Collapse 

PathListResponse object { asnInfo, collectors, meta, paths } 

asnInfo: map[object { asn, country, name } ]

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

collectors: array of string

meta: object { dataTime, effectiveCollector, queryTime, stale } 

dataTime: string

Timestamp of the underlying RIB data.

formatdate-time

effectiveCollector: string

queryTime: string

Timestamp when the query was executed.

formatdate-time

stale: boolean

paths: array of object { collectors, pathsCount, peersCount, segment } 

collectors: array of string

pathsCount: number

peersCount: number

segment: array of number

#### BGPIPs

##### [Get announced IP address space time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/methods/timeseries)

GET/radar/bgp/ips/timeseries

##### ModelsExpand Collapse 

IPTimeseriesResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 4 more } 

Metadata for the results.

aggInterval: "FIFTEEN_MINUTES" or "ONE_HOUR" or "ONE_DAY" or 2 more

Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

One of the following:

"FIFTEEN_MINUTES"

"ONE_HOUR"

"ONE_DAY"

"ONE_WEEK"

"ONE_MONTH"

confidenceInfo: object { annotations, level } 

annotations: array of object { dataSource, description, endDate, 5 more } 

dataSource: "ALL" or "AI_BOTS" or "AI_GATEWAY" or 22 more

Data source for annotations.

One of the following:

"ALL"

"AI_BOTS"

"AI_GATEWAY"

"BGP"

"BOTS"

"CONNECTION_ANOMALY"

"CT"

"DNS"

"DNS_MAGNITUDE"

"DNS_AS112"

"DOS"

"EMAIL_ROUTING"

"EMAIL_SECURITY"

"FW"

"FW_PG"

"HTTP"

"HTTP_CONTROL"

"HTTP_CRAWLER_REFERER"

"HTTP_ORIGINS"

"IQI"

"LEAKED_CREDENTIALS"

"NET"

"ROBOTS_TXT"

"SPEED"

"WORKERS_AI"

description: string

endDate: string

formatdate-time

eventType: "GENERAL" or "OUTAGE" or "PARTIAL_PROJECTION" or 2 more

Event type for annotations.

One of the following:

"GENERAL"

"OUTAGE"

"PARTIAL_PROJECTION"

"PIPELINE"

"TRAFFIC_ANOMALY"

isInstantaneous: boolean

Whether event is a single point in time or a time range.

linkedUrl: string

formaturi

startDate: string

formatdate-time

tags: optional array of string

level: number

Provides an indication of how much confidence Cloudflare has in the data.

dateRange: array of object { endTime, startTime } 

endTime: string

Adjusted end of date range.

formatdate-time

startTime: string

Adjusted start of date range.

formatdate-time

lastUpdated: string

Timestamp of the last dataset update.

formatdate-time

normalization: "PERCENTAGE" or "MIN0_MAX" or "MIN_MAX" or 5 more

Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

One of the following:

"PERCENTAGE"

"MIN0_MAX"

"MIN_MAX"

"RAW_VALUES"

"PERCENTAGE_CHANGE"

"ROLLING_AVERAGE"

"OVERLAPPED_PERCENTAGE"

"RATIO"

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

delay: optional object { asn_data, country_data, healthy, nowTs } 

asn_data: object { delaySecs, delayStr, healthy, latest } 

delaySecs: number

delayStr: string

healthy: boolean

latest: object { entries_count, path, timestamp } 

entries_count: number

path: string

timestamp: number

country_data: object { delaySecs, delayStr, healthy, latest } 

delaySecs: number

delayStr: string

healthy: boolean

latest: object { count, timestamp } 

count: number

timestamp: number

healthy: boolean

nowTs: number

serie_0: object { ipv4, ipv6, timestamps } 

ipv4: array of string

ipv6: array of string

timestamps: array of string

#### BGPIPsTop

##### [Get top ASes by announced IP space](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases)

GET/radar/bgp/ips/top/ases

##### ModelsExpand Collapse 

TopAsesResponse object { anchorTs, asns, country, metric } 

anchorTs: string

formatdate-time

asns: array of object { asn, v4_24s, v6_48s } 

asn: number

v4_24s: number

v6_48s: number

country: string

metric: string

#### BGPRPKI

#### BGPRPKIASPA

##### [Get ASPA objects snapshot](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot)

GET/radar/bgp/rpki/aspa/snapshot

##### [Get ASPA changes over time](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes)

GET/radar/bgp/rpki/aspa/changes

##### [Get ASPA count time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries)

GET/radar/bgp/rpki/aspa/timeseries

##### ModelsExpand Collapse 

ASPASnapshotResponse object { asnInfo, aspaObjects, meta } 

asnInfo: object { "13335" } 

"13335": object { asn, country, name } 

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

aspaObjects: array of object { customerAsn, providers } 

customerAsn: number

The customer ASN publishing the ASPA object.

providers: array of number

meta: object { dataTime, queryTime, totalCount } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

totalCount: number

Total number of ASPA objects.

ASPAChangesResponse object { asnInfo, changes, meta } 

asnInfo: object { "13335" } 

"13335": object { asn, country, name } 

asn: number

ASN number.

country: string

Alpha-2 country code.

name: string

AS name.

changes: array of object { customersAdded, customersRemoved, date, 4 more } 

customersAdded: number

Number of new ASPA objects created.

customersRemoved: number

Number of ASPA objects deleted.

date: string

Date of the changes in ISO 8601 format.

formatdate-time

entries: array of object { customerAsn, providers, type } 

customerAsn: number

The customer ASN affected.

providers: array of number

type: "CustomerAdded" or "CustomerRemoved" or "ProvidersAdded" or "ProvidersRemoved"

One of the following:

"CustomerAdded"

"CustomerRemoved"

"ProvidersAdded"

"ProvidersRemoved"

providersAdded: number

Number of providers added to existing objects.

providersRemoved: number

Number of providers removed from existing objects.

totalCount: number

Running total of active ASPA objects after this day.

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

ASPATimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

#### BGPRPKIRoas

##### [Get RPKI ROA deployment time series](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries)

GET/radar/bgp/rpki/roas/timeseries

##### ModelsExpand Collapse 

RoaTimeseriesResponse object { meta, serie_0 } 

meta: object { dataTime, queryTime } 

dataTime: string

Timestamp of the underlying data.

formatdate-time

queryTime: string

Timestamp when the query was executed.

formatdate-time

serie_0: object { timestamps, values } 

timestamps: array of string

values: array of string

[ Previous

* * *

Outages ](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages)[ Next

* * *

Leaks ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/leaks)
