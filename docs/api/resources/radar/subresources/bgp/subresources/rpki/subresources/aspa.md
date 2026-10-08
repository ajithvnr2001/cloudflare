---
url: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/
title: ASPA | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:28:09.041824+00:00
---

# ASPA | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[RPKI](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# ASPA

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

[ Previous

* * *

RPKI ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki)[ Next

* * *

Roas ](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas)
