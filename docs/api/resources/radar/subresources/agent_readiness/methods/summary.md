---
url: https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary/
title: Get agent readiness summary | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:27:18.744985+00:00
---

# Get agent readiness summary | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness/methods/summary/

[API Reference](https://developers.cloudflare.com/api)

[Radar](https://developers.cloudflare.com/api/resources/radar)

[Agent Readiness](https://developers.cloudflare.com/api/resources/radar/subresources/agent_readiness)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get agent readiness summary

GET/radar/agent_readiness/summary/{dimension}

Returns a summary of AI agent readiness scores across scanned domains, grouped by the specified dimension. Data is sourced from weekly bulk scans. All values are raw domain counts.

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

##### Path ParametersExpand Collapse 

dimension: "CHECK"

Specifies the agent readiness data dimension by which to group the results.

##### Query ParametersExpand Collapse 

date: optional string

Filters results by the specified date.

formatdate

domainCategory: optional array of string

Filters results by domain category.

format: optional "JSON" or "CSV"

Format in which results will be returned.

One of the following:

"JSON"

"CSV"

name: optional array of string

Array of names used to label the series in the response.

##### ReturnsExpand Collapse 

result: object { meta, summary_0 } 

meta: object { date, domainCategories, lastUpdated, 4 more } 

date: string

Date of the returned scan (YYYY-MM-DD). May differ from the requested date if no scan exists for that exact date.

formatdate

domainCategories: array of object { name, value } 

Available domain sub-categories with their scan counts. Use as filter options for the domainCategory parameter.

name: string

Sub-category name.

value: number

Number of successfully scanned domains in this sub-category.

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

successfulDomains: number

Domains successfully scanned (excludes errors).

totalDomains: number

Total domains attempted in the scan.

units: array of object { name, value } 

Measurement units for the results.

name: string

value: string

summary_0: map[string]

success: boolean

### Get agent readiness summary

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
    
    
    curl https://api.cloudflare.com/client/v4/radar/agent_readiness/summary/$DIMENSION \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "meta": {
          "date": "2026-03-24",
          "domainCategories": [
            {
              "name": "News & Media",
              "value": 0
            }
          ],
          "lastUpdated": "2019-12-27T18:11:19.117Z",
          "normalization": "PERCENTAGE",
          "successfulDomains": 0,
          "totalDomains": 0,
          "units": [
            {
              "name": "*",
              "value": "requests"
            }
          ]
        },
        "summary_0": {
          "markdownNegotiation": "45000",
          "robotsTxt": "280000"
        }
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "meta": {
          "date": "2026-03-24",
          "domainCategories": [
            {
              "name": "News & Media",
              "value": 0
            }
          ],
          "lastUpdated": "2019-12-27T18:11:19.117Z",
          "normalization": "PERCENTAGE",
          "successfulDomains": 0,
          "totalDomains": 0,
          "units": [
            {
              "name": "*",
              "value": "requests"
            }
          ]
        },
        "summary_0": {
          "markdownNegotiation": "45000",
          "robotsTxt": "280000"
        }
      },
      "success": true
    }
