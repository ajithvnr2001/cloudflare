---
url: https://developers.cloudflare.com/api/resources/spectrum/
title: Spectrum | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:12.844237+00:00
---

# Spectrum | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/spectrum/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Spectrum

##### ModelsExpand Collapse 

DNS object { name, type } 

The name and type of DNS record for the Spectrum application.

name: optional string

The name of the DNS record associated with the application.

formathostname

type: optional "CNAME" or "ADDRESS"

The type of DNS record associated with the application.

One of the following:

"CNAME"

"ADDRESS"

EdgeIPs = object { connectivity, type }  or object { ips, type } 

The anycast edge IP configuration for the hostname of this application.

One of the following:

Dynamic object { connectivity, type } 

connectivity: optional "all" or "ipv4" or "ipv6"

The IP versions supported for inbound connections on Spectrum anycast IPs.

One of the following:

"all"

"ipv4"

"ipv6"

type: optional "dynamic"

The type of edge IP configuration specified. Dynamically allocated edge IPs use Spectrum anycast IPs in accordance with the connectivity you specify. Only valid with CNAME DNS names.

Static object { ips, type } 

ips: optional array of string

The array of customer owned IPs we broadcast via anycast for this hostname and application.

type: optional "static"

The type of edge IP configuration specified. Statically allocated edge IPs use customer IPs in accordance with the ips array you specify. Only valid with ADDRESS DNS names.

OriginDNS object { name, ttl, type } 

The name and type of DNS record for the Spectrum application.

name: optional string

The name of the DNS record associated with the origin.

formathostname

ttl: optional number

The TTL of our resolution of your DNS record in seconds.

minimum600

type: optional "" or "A" or "AAAA" or "SRV"

The type of DNS record associated with the origin. "" is used to specify a combination of A/AAAA records.

One of the following:

""

"A"

"AAAA"

"SRV"

OriginPort = number or string

The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the “protocol” field.

One of the following:

number

string

#### SpectrumAnalytics

#### SpectrumAnalyticsAggregates

#### SpectrumAnalyticsAggregatesCurrents

##### [Get current aggregated analytics](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/aggregates/subresources/currents/methods/get)

GET/zones/{zone_id}/spectrum/analytics/aggregate/current

##### ModelsExpand Collapse 

CurrentGetResponse = array of object { appID, bytesEgress, bytesIngress, 2 more } 

appID: string

Application identifier.

maxLength32

bytesEgress: number

Number of bytes sent.

bytesIngress: number

Number of bytes received.

connections: number

Number of connections.

durationAvg: number

Average duration of connections.

#### SpectrumAnalyticsEvents

##### ModelsExpand Collapse 

Dimension = "event" or "appID" or "coloName" or "ipVersion"

One of the following:

"event"

"appID"

"coloName"

"ipVersion"

#### SpectrumAnalyticsEventsBytimes

##### [Get analytics by time](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/events/subresources/bytimes/methods/get)

GET/zones/{zone_id}/spectrum/analytics/events/bytime

##### ModelsExpand Collapse 

BytimeGetResponse object { data, data_lag, max, 5 more } 

data: array of object { dimensions, metrics } 

List of columns returned by the analytics query.

dimensions: optional array of string

metrics: optional array of number or array of array of number

One of the following:

array of number

array of array of number

data_lag: number

Number of seconds between current time and last processed event, i.e. how many seconds of data could be missing.

minimum0

max: map[number]

Maximum result for each selected metrics across all data.

min: map[number]

Minimum result for each selected metrics across all data.

query: object { dimensions, filters, limit, 4 more } 

dimensions: optional array of [Dimension](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum.analytics.events%20%3E%20\(model\)%20dimension%20%3E%20\(schema\))

Can be used to break down the data by given attributes. Options are:

Dimension| Name| Example  
---|---|---  
event| Connection Event| connect, progress, disconnect, originError, clientFiltered  
appID| Application ID| 40d67c87c6cd4b889a4fd57805225e85  
coloName| Colo Name| SFO  
ipVersion| IP version used by the client| 4, 6.  
  
One of the following:

"event"

"appID"

"coloName"

"ipVersion"

filters: optional string

Used to filter rows by one or more dimensions. Filters can be combined using OR and AND boolean logic. AND takes precedence over OR in all the expressions. The OR operator is defined using a comma (,) or OR keyword surrounded by whitespace. The AND operator is defined using a semicolon (;) or AND keyword surrounded by whitespace. Note that the semicolon is a reserved character in URLs (rfc1738) and needs to be percent-encoded as %3B. Comparison options are:

Operator| Name| URL Encoded  
---|---|---  
==| Equals| %3D%3D  
!=| Does not equals| !%3D  
>| Greater Than| %3E  
<| Less Than| %3C  
>=| Greater than or equal to| %3E%3D  
<=| Less than or equal to| %3C%3D  
  
Use the above to construct filters.

limit: optional number

Limit number of returned metrics.

metrics: optional array of "count" or "bytesIngress" or "bytesEgress" or 4 more

One or more metrics to compute. Options are:

Metric| Name| Example| Unit  
---|---|---|---  
count| Count of total events| 1000| Count  
bytesIngress| Sum of ingress bytes| 1000| Sum  
bytesEgress| Sum of egress bytes| 1000| Sum  
durationAvg| Average connection duration| 1.0| Time in milliseconds  
durationMedian| Median connection duration| 1.0| Time in milliseconds  
duration90th| 90th percentile connection duration| 1.0| Time in milliseconds  
duration99th| 99th percentile connection duration| 1.0| Time in milliseconds.  
  
One of the following:

"count"

"bytesIngress"

"bytesEgress"

"durationAvg"

"durationMedian"

"duration90th"

"duration99th"

since: optional string

Start of time interval to query, defaults to `until` \- 6 hours. Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.

formatdate-time

sort: optional array of string

The sort order for the result set; sort fields must be included in `metrics` or `dimensions`.

until: optional string

End of time interval to query, defaults to current time. Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.

formatdate-time

rows: number

Total number of rows in the result.

minimum0

totals: map[number]

Total result for each selected metrics across all data.

time_intervals: optional array of array of string

List of time interval buckets: [start, end].

#### SpectrumAnalyticsEventsSummaries

##### [Get analytics summary](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics/subresources/events/subresources/summaries/methods/get)

GET/zones/{zone_id}/spectrum/analytics/events/summary

##### ModelsExpand Collapse 

SummaryGetResponse object { data, data_lag, max, 5 more } 

data: array of object { dimensions, metrics } 

List of columns returned by the analytics query.

dimensions: optional array of string

metrics: optional array of number or array of array of number

One of the following:

array of number

array of array of number

data_lag: number

Number of seconds between current time and last processed event, i.e. how many seconds of data could be missing.

minimum0

max: map[number]

Maximum result for each selected metrics across all data.

min: map[number]

Minimum result for each selected metrics across all data.

query: object { dimensions, filters, limit, 4 more } 

dimensions: optional array of [Dimension](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum.analytics.events%20%3E%20\(model\)%20dimension%20%3E%20\(schema\))

Can be used to break down the data by given attributes. Options are:

Dimension| Name| Example  
---|---|---  
event| Connection Event| connect, progress, disconnect, originError, clientFiltered  
appID| Application ID| 40d67c87c6cd4b889a4fd57805225e85  
coloName| Colo Name| SFO  
ipVersion| IP version used by the client| 4, 6.  
  
One of the following:

"event"

"appID"

"coloName"

"ipVersion"

filters: optional string

Used to filter rows by one or more dimensions. Filters can be combined using OR and AND boolean logic. AND takes precedence over OR in all the expressions. The OR operator is defined using a comma (,) or OR keyword surrounded by whitespace. The AND operator is defined using a semicolon (;) or AND keyword surrounded by whitespace. Note that the semicolon is a reserved character in URLs (rfc1738) and needs to be percent-encoded as %3B. Comparison options are:

Operator| Name| URL Encoded  
---|---|---  
==| Equals| %3D%3D  
!=| Does not equals| !%3D  
>| Greater Than| %3E  
<| Less Than| %3C  
>=| Greater than or equal to| %3E%3D  
<=| Less than or equal to| %3C%3D  
  
Use the above to construct filters.

limit: optional number

Limit number of returned metrics.

metrics: optional array of "count" or "bytesIngress" or "bytesEgress" or 4 more

One or more metrics to compute. Options are:

Metric| Name| Example| Unit  
---|---|---|---  
count| Count of total events| 1000| Count  
bytesIngress| Sum of ingress bytes| 1000| Sum  
bytesEgress| Sum of egress bytes| 1000| Sum  
durationAvg| Average connection duration| 1.0| Time in milliseconds  
durationMedian| Median connection duration| 1.0| Time in milliseconds  
duration90th| 90th percentile connection duration| 1.0| Time in milliseconds  
duration99th| 99th percentile connection duration| 1.0| Time in milliseconds.  
  
One of the following:

"count"

"bytesIngress"

"bytesEgress"

"durationAvg"

"durationMedian"

"duration90th"

"duration99th"

since: optional string

Start of time interval to query, defaults to `until` \- 6 hours. Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.

formatdate-time

sort: optional array of string

The sort order for the result set; sort fields must be included in `metrics` or `dimensions`.

until: optional string

End of time interval to query, defaults to current time. Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.

formatdate-time

rows: number

Total number of rows in the result.

minimum0

totals: map[number]

Total result for each selected metrics across all data.

time_intervals: optional array of array of string

List of time interval buckets: [start, end].

#### SpectrumApps

##### [List Spectrum applications](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/list)

GET/zones/{zone_id}/spectrum/apps

##### [Get Spectrum application configuration](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/get)

GET/zones/{zone_id}/spectrum/apps/{app_id}

##### [Create Spectrum application using a name for the origin](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/create)

POST/zones/{zone_id}/spectrum/apps

##### [Update Spectrum application configuration using a name for the origin](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/update)

PUT/zones/{zone_id}/spectrum/apps/{app_id}

##### [Delete Spectrum application](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/delete)

DELETE/zones/{zone_id}/spectrum/apps/{app_id}

##### ModelsExpand Collapse 

AppListResponse = object { id, created_on, dns, 13 more }  or object { id, created_on, dns, 3 more } 

One of the following:

SpectrumConfigAppConfig object { id, created_on, dns, 13 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

traffic_type: "direct" or "http" or "https" or "worker"

Determines how data travels from the edge to your origin. When set to “direct”, Spectrum will send traffic directly to your origin, and the application’s type is derived from the `protocol`. When set to “http” or “https”, Spectrum will apply Cloudflare’s HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. When set to “worker”, traffic is sent to the Worker specified by `origin_worker_id`.

One of the following:

"direct"

"http"

"https"

"worker"

argo_smart_routing: optional boolean

Enables Argo Smart Routing for this application. Notes: Only available for TCP or UDP applications with traffic_type set to “direct”.

edge_ips: optional [EdgeIPs](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20edge_ips%20%3E%20\(schema\))

The anycast edge IP configuration for the hostname of this application.

ip_firewall: optional boolean

Enables IP Access Rules for this application. Notes: Only available for TCP applications.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

origin_dns: optional [OriginDNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_dns%20%3E%20\(schema\)) { name, ttl, type } 

The name and type of DNS record for the Spectrum application.

origin_port: optional [OriginPort](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_port%20%3E%20\(schema\))

The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the “protocol” field.

maximum65535

minimum1

origin_worker_id: optional string

Optional Worker script tag (worker ID) to use as the application’s origin. Only supported for TCP applications with traffic_type “worker”; mutually exclusive with origin_direct, origin_dns, origin_port, proxy_protocol, and argo_smart_routing. tls may only be “off” or “flexible”.

proxy_protocol: optional "off" or "v1" or "v2" or "simple"

Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol.

One of the following:

"off"

"v1"

"v2"

"simple"

tls: optional "off" or "flexible" or "full" or "strict"

The type of TLS termination associated with the application.

One of the following:

"off"

"flexible"

"full"

"strict"

virtual_network_id: optional string

Optional UUID of a virtual network for routing origin traffic through tunnel virtual networks.

formatuuid

SpectrumConfigPaygoAppConfig object { id, created_on, dns, 3 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

AppGetResponse = object { id, created_on, dns, 13 more }  or object { id, created_on, dns, 3 more } 

One of the following:

SpectrumConfigAppConfig object { id, created_on, dns, 13 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

traffic_type: "direct" or "http" or "https" or "worker"

Determines how data travels from the edge to your origin. When set to “direct”, Spectrum will send traffic directly to your origin, and the application’s type is derived from the `protocol`. When set to “http” or “https”, Spectrum will apply Cloudflare’s HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. When set to “worker”, traffic is sent to the Worker specified by `origin_worker_id`.

One of the following:

"direct"

"http"

"https"

"worker"

argo_smart_routing: optional boolean

Enables Argo Smart Routing for this application. Notes: Only available for TCP or UDP applications with traffic_type set to “direct”.

edge_ips: optional [EdgeIPs](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20edge_ips%20%3E%20\(schema\))

The anycast edge IP configuration for the hostname of this application.

ip_firewall: optional boolean

Enables IP Access Rules for this application. Notes: Only available for TCP applications.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

origin_dns: optional [OriginDNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_dns%20%3E%20\(schema\)) { name, ttl, type } 

The name and type of DNS record for the Spectrum application.

origin_port: optional [OriginPort](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_port%20%3E%20\(schema\))

The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the “protocol” field.

maximum65535

minimum1

origin_worker_id: optional string

Optional Worker script tag (worker ID) to use as the application’s origin. Only supported for TCP applications with traffic_type “worker”; mutually exclusive with origin_direct, origin_dns, origin_port, proxy_protocol, and argo_smart_routing. tls may only be “off” or “flexible”.

proxy_protocol: optional "off" or "v1" or "v2" or "simple"

Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol.

One of the following:

"off"

"v1"

"v2"

"simple"

tls: optional "off" or "flexible" or "full" or "strict"

The type of TLS termination associated with the application.

One of the following:

"off"

"flexible"

"full"

"strict"

virtual_network_id: optional string

Optional UUID of a virtual network for routing origin traffic through tunnel virtual networks.

formatuuid

SpectrumConfigPaygoAppConfig object { id, created_on, dns, 3 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

AppCreateResponse = object { id, created_on, dns, 13 more }  or object { id, created_on, dns, 3 more } 

One of the following:

SpectrumConfigAppConfig object { id, created_on, dns, 13 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

traffic_type: "direct" or "http" or "https" or "worker"

Determines how data travels from the edge to your origin. When set to “direct”, Spectrum will send traffic directly to your origin, and the application’s type is derived from the `protocol`. When set to “http” or “https”, Spectrum will apply Cloudflare’s HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. When set to “worker”, traffic is sent to the Worker specified by `origin_worker_id`.

One of the following:

"direct"

"http"

"https"

"worker"

argo_smart_routing: optional boolean

Enables Argo Smart Routing for this application. Notes: Only available for TCP or UDP applications with traffic_type set to “direct”.

edge_ips: optional [EdgeIPs](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20edge_ips%20%3E%20\(schema\))

The anycast edge IP configuration for the hostname of this application.

ip_firewall: optional boolean

Enables IP Access Rules for this application. Notes: Only available for TCP applications.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

origin_dns: optional [OriginDNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_dns%20%3E%20\(schema\)) { name, ttl, type } 

The name and type of DNS record for the Spectrum application.

origin_port: optional [OriginPort](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_port%20%3E%20\(schema\))

The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the “protocol” field.

maximum65535

minimum1

origin_worker_id: optional string

Optional Worker script tag (worker ID) to use as the application’s origin. Only supported for TCP applications with traffic_type “worker”; mutually exclusive with origin_direct, origin_dns, origin_port, proxy_protocol, and argo_smart_routing. tls may only be “off” or “flexible”.

proxy_protocol: optional "off" or "v1" or "v2" or "simple"

Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol.

One of the following:

"off"

"v1"

"v2"

"simple"

tls: optional "off" or "flexible" or "full" or "strict"

The type of TLS termination associated with the application.

One of the following:

"off"

"flexible"

"full"

"strict"

virtual_network_id: optional string

Optional UUID of a virtual network for routing origin traffic through tunnel virtual networks.

formatuuid

SpectrumConfigPaygoAppConfig object { id, created_on, dns, 3 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

AppUpdateResponse = object { id, created_on, dns, 13 more }  or object { id, created_on, dns, 3 more } 

One of the following:

SpectrumConfigAppConfig object { id, created_on, dns, 13 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

traffic_type: "direct" or "http" or "https" or "worker"

Determines how data travels from the edge to your origin. When set to “direct”, Spectrum will send traffic directly to your origin, and the application’s type is derived from the `protocol`. When set to “http” or “https”, Spectrum will apply Cloudflare’s HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. When set to “worker”, traffic is sent to the Worker specified by `origin_worker_id`.

One of the following:

"direct"

"http"

"https"

"worker"

argo_smart_routing: optional boolean

Enables Argo Smart Routing for this application. Notes: Only available for TCP or UDP applications with traffic_type set to “direct”.

edge_ips: optional [EdgeIPs](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20edge_ips%20%3E%20\(schema\))

The anycast edge IP configuration for the hostname of this application.

ip_firewall: optional boolean

Enables IP Access Rules for this application. Notes: Only available for TCP applications.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

origin_dns: optional [OriginDNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_dns%20%3E%20\(schema\)) { name, ttl, type } 

The name and type of DNS record for the Spectrum application.

origin_port: optional [OriginPort](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20origin_port%20%3E%20\(schema\))

The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the “protocol” field.

maximum65535

minimum1

origin_worker_id: optional string

Optional Worker script tag (worker ID) to use as the application’s origin. Only supported for TCP applications with traffic_type “worker”; mutually exclusive with origin_direct, origin_dns, origin_port, proxy_protocol, and argo_smart_routing. tls may only be “off” or “flexible”.

proxy_protocol: optional "off" or "v1" or "v2" or "simple"

Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol.

One of the following:

"off"

"v1"

"v2"

"simple"

tls: optional "off" or "flexible" or "full" or "strict"

The type of TLS termination associated with the application.

One of the following:

"off"

"flexible"

"full"

"strict"

virtual_network_id: optional string

Optional UUID of a virtual network for routing origin traffic through tunnel virtual networks.

formatuuid

SpectrumConfigPaygoAppConfig object { id, created_on, dns, 3 more } 

id: string

App identifier.

maxLength32

created_on: string

When the Application was created.

formatdate-time

dns: [DNS](https://developers.cloudflare.com/api/resources/spectrum#\(resource\)%20spectrum%20%3E%20\(model\)%20dns%20%3E%20\(schema\)) { name, type } 

The name and type of DNS record for the Spectrum application.

modified_on: string

When the Application was last modified.

formatdate-time

protocol: string

The port configuration at Cloudflare’s edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`.

origin_direct: optional array of string

List of origin IP addresses. Array may contain multiple IP addresses for load balancing.

AppDeleteResponse object { id } 

id: string

Identifier.

maxLength32

#### SpectrumProtocols

##### [List Spectrum application protocols](https://developers.cloudflare.com/api/resources/spectrum/subresources/protocols/methods/list)

GET/zones/{zone_id}/spectrum/protocols

##### ModelsExpand Collapse 

ProtocolListResponse object { description, name, ports, transport } 

description: string

The full name of the application protocol.

name: string

The short name of the application protocol.

ports: array of number

The available listening ports for the given protocol.

transport: string

The transport layer protocol used by the application protocol

[ Previous

* * *

Cache Reserve Clear ](https://developers.cloudflare.com/api/resources/smart_shield/subresources/cache_reserve_clear)[ Next

* * *

Analytics ](https://developers.cloudflare.com/api/resources/spectrum/subresources/analytics)
