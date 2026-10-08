---
url: https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/
title: Post Quantum | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:27:53.376439+00:00
---

# Post Quantum | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Post Quantum

#### Post QuantumOrigin

##### [Get Origin Post-Quantum Data Summary](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/summary)

GET/radar/post_quantum/origin/summary/{dimension}

##### [Get Origin Post-Quantum Data Over Time](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin/methods/timeseries_groups)

GET/radar/post_quantum/origin/timeseries_groups/{dimension}

##### ModelsExpand Collapse 

OriginSummaryResponse object { meta, summary_0 } 

meta: object { confidenceInfo, dateRange, lastUpdated, 2 more } 

Metadata for the results.

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

summary_0: map[string]

OriginTimeseriesGroupsResponse object { meta, serie_0 } 

meta: object { aggInterval, confidenceInfo, dateRange, 3 more } 

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

serie_0: object { timestamps } 

timestamps: array of string

#### Post QuantumTLS

##### [Check Post-Quantum TLS support](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support)

GET/radar/post_quantum/tls/support

##### ModelsExpand Collapse 

TLSSupportResponse object { bugs, host, kex, 2 more } 

bugs: object { hrrFailure, splitClientHello, unknownKeyshare } 

hrrFailure: boolean

Server sends a HelloRetryRequest but fails to complete the handshake after the client sends the second ClientHello. Often caused by non-compliant TLS 1.3 implementations on shared hosting providers.

splitClientHello: boolean

Server rejects fragmented ClientHello caused by large PQ keyshare, but accepts classical (non-PQ) handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS ClientHello messages.

unknownKeyshare: boolean

Server cannot handle an unknown key exchange algorithm in the ClientHello keyshare extension. Compliant servers should respond with HelloRetryRequest for a supported algorithm.

host: string

The host that was tested

kex: number

TLS CurveID of the negotiated key exchange

kexName: string

Human-readable name of the key exchange algorithm

pq: boolean

Whether the negotiated key exchange uses Post-Quantum cryptography (specifically X25519MLKEM768)

[ Previous

* * *

Top ](https://developers.cloudflare.com/api/resources/radar/subresources/netflows/subresources/top)[ Next

* * *

Origin ](https://developers.cloudflare.com/api/resources/radar/subresources/post_quantum/subresources/origin)
