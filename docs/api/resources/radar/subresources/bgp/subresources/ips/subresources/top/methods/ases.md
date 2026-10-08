---
url: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/
title: Get top ASes by announced IP space | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:59.805882+00:00
---

# Get top ASes by announced IP space | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[IPs](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips)

[Top](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/ips/subresources/top)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get top ASes by announced IP space

GET/radar/bgp/ips/top/ases

Returns the top-N autonomous systems by announced IP space at the nearest 8-hour RIB boundary at or before the requested date. The snapped boundary is returned as `anchor_ts`.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`User Details Write``User Details Read`

##### Query ParametersExpand Collapse 

country: optional string

Optional ISO 3166-1 alpha-2 country filter. Omit for global top-N.

maxLength2

minLength2

date: optional string

Filters results by the specified datetime (ISO 8601).

formatdate-time

format: optional "JSON" or "CSV"

Format in which results will be returned.

One of the following:

"JSON"

"CSV"

limit: optional number

Limits the number of objects returned in the response.

maximum50

minimum1

metric: optional "v4_24s" or "v6_48s"

Ranking metric: IPv4 /24 count or IPv6 /48 count.

One of the following:

"v4_24s"

"v6_48s"

##### ReturnsExpand Collapse 

result: object { anchorTs, asns, country, metric } 

anchorTs: string

formatdate-time

asns: array of object { asn, v4_24s, v6_48s } 

asn: number

v4_24s: number

v6_48s: number

country: string

metric: string

success: boolean

### Get top ASes by announced IP space

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/radar/bgp/ips/top/ases \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "anchorTs": "2026-04-18T16:00:00Z",
        "asns": [
          {
            "asn": 749,
            "v4_24s": 875649,
            "v6_48s": 0
          }
        ],
        "country": "US",
        "metric": "v4_24s"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "anchorTs": "2026-04-18T16:00:00Z",
        "asns": [
          {
            "asn": 749,
            "v4_24s": 875649,
            "v6_48s": 0
          }
        ],
        "country": "US",
        "metric": "v4_24s"
      },
      "success": true
    }
