---
url: https://developers.cloudflare.com/api/resources/zones/subresources/plans/methods/list/
title: List Available Plans | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:07.332580+00:00
---

# List Available Plans | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zones/subresources/plans/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Zones](https://developers.cloudflare.com/api/resources/zones)

[Plans](https://developers.cloudflare.com/api/resources/zones/subresources/plans)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Available Plans

GET/zones/{zone_id}/available_plans

Lists available plans the zone can subscribe to.

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

`Billing Write``Billing Read`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier

maxLength32

##### ReturnsExpand Collapse 

errors: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

result: array of [AvailableRatePlan](https://developers.cloudflare.com/api/resources/zones#\(resource\)%20zones.plans%20%3E%20\(model\)%20available_rate_plan%20%3E%20\(schema\)) { id, can_subscribe, currency, 6 more } 

id: optional string

Identifier

maxLength32

can_subscribe: optional boolean

Indicates whether you can subscribe to this plan.

currency: optional string

The monetary unit in which pricing information is displayed.

externally_managed: optional boolean

Indicates whether this plan is managed externally.

frequency: optional "weekly" or "monthly" or "quarterly" or "yearly"

The frequency at which you will be billed for this plan.

One of the following:

"weekly"

"monthly"

"quarterly"

"yearly"

is_subscribed: optional boolean

Indicates whether you are currently subscribed to this plan.

legacy_id: optional string

The legacy identifier for this rate plan, if any.

name: optional string

The plan name.

maxLength80

price: optional number

The amount you will be billed for this plan.

success: true

Whether the API call was successful

result_info: optional object { count, page, per_page, total_count } 

count: optional number

Total number of results for the requested service

page: optional number

Current page within paginated list of results

per_page: optional number

Number of results per page of results

total_count: optional number

Total results available without any search parameters

### List Available Plans

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/available_plans \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "can_subscribe": true,
          "currency": "USD",
          "externally_managed": false,
          "frequency": "monthly",
          "is_subscribed": false,
          "legacy_id": "free",
          "name": "Free Plan",
          "price": 0
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "can_subscribe": true,
          "currency": "USD",
          "externally_managed": false,
          "frequency": "monthly",
          "is_subscribed": false,
          "legacy_id": "free",
          "name": "Free Plan",
          "price": 0
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }
