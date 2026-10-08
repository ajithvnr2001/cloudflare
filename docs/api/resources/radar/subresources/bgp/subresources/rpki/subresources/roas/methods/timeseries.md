---
url: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/
title: Get RPKI ROA deployment time series | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:27:02.021349+00:00
---

# Get RPKI ROA deployment time series | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[BGP](https://developers.cloudflare.com/api/resources/radar/subresources/bgp)

[RPKI](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki)

[Roas](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get RPKI ROA deployment time series

GET/radar/bgp/rpki/roas/timeseries

Retrieves RPKI ROA (Route Origin Authorization) validation ratios over time. Returns the selected metric as a time series. Supports filtering by ASN or location (country code) — multiple values of the same filter type produce one series per value. If no ASN or location is specified, returns the global aggregate.

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

asn: optional array of string

Filters results by Autonomous System Number. Specify one or more ASNs. Multiple values generate one series per ASN.

dateEnd: optional string

End of the date range (inclusive). Alternative to `dateRange`; provide together with `dateStart`.

formatdate-time

dateStart: optional string

Start of the date range (inclusive). Alternative to `dateRange`; provide together with `dateEnd`.

formatdate-time

format: optional "JSON" or "CSV"

Format in which results will be returned.

One of the following:

"JSON"

"CSV"

location: optional array of string

Filters results by location. Specify a comma-separated list of alpha-2 location codes.

metric: optional "validPfxsRatio" or "validPfxsV4Ratio" or "validPfxsV6Ratio" or 3 more

Which RPKI ROA validation metric to return. validPfxsRatio = ratio of RPKI-valid prefixes (IPv4+IPv6 combined). validPfxsV4Ratio / validPfxsV6Ratio = same, split by IP version. validIpsRatio = ratio of RPKI-valid address space (IPv4 /24s + IPv6 /48s). validIpsV4Ratio / validIpsV6Ratio = same, split by IP version.

One of the following:

"validPfxsRatio"

"validPfxsV4Ratio"

"validPfxsV6Ratio"

"validIpsRatio"

"validIpsV4Ratio"

"validIpsV6Ratio"

name: optional array of string

Array of names used to label the series in the response.

##### ReturnsExpand Collapse 

result: object { meta, serie_0 } 

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

success: boolean

### Get RPKI ROA deployment time series

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
    
    
    curl https://api.cloudflare.com/client/v4/radar/bgp/rpki/roas/timeseries \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "meta": {
          "dataTime": "2019-12-27T18:11:19.117Z",
          "queryTime": "2019-12-27T18:11:19.117Z"
        },
        "serie_0": {
          "timestamps": [
            "2019-12-27T18:11:19.117Z"
          ],
          "values": [
            "10"
          ]
        }
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "meta": {
          "dataTime": "2019-12-27T18:11:19.117Z",
          "queryTime": "2019-12-27T18:11:19.117Z"
        },
        "serie_0": {
          "timestamps": [
            "2019-12-27T18:11:19.117Z"
          ],
          "values": [
            "10"
          ]
        }
      },
      "success": true
    }
