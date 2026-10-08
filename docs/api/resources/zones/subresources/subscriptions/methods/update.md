---
url: https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/update/
title: Update Zone Subscription | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:05.834194+00:00
---

# Update Zone Subscription | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/update/

[API Reference](https://developers.cloudflare.com/api)

[Zones](https://developers.cloudflare.com/api/resources/zones)

[Subscriptions](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update Zone Subscription

PUT/zones/{zone_id}/subscription

Updates zone subscriptions, either plan or add-ons.

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

`Billing Write`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier

maxLength32

##### Body ParametersJSONExpand Collapse 

frequency: optional "weekly" or "monthly" or "quarterly" or "yearly"

How often the subscription is renewed automatically.

One of the following:

"weekly"

"monthly"

"quarterly"

"yearly"

rate_plan: optional [RatePlan](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20rate_plan%20%3E%20\(schema\)) { id, currency, externally_managed, 4 more } 

The rate plan applied to the subscription.

id: optional "free" or "lite" or "pro" or 7 more

The ID of the rate plan.

One of the following:

"free"

"lite"

"pro"

"pro_plus"

"business"

"enterprise"

"partners_free"

"partners_pro"

"partners_business"

"partners_enterprise"

currency: optional string

The currency applied to the rate plan subscription.

externally_managed: optional boolean

Whether this rate plan is managed externally from Cloudflare.

is_contract: optional boolean

Whether a rate plan is enterprise-based (or newly adopted term contract).

public_name: optional string

The full name of the rate plan.

scope: optional string

The scope that this rate plan applies to.

sets: optional array of string

The list of sets this rate plan applies to. Returns array of strings.

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

result: object { id, currency, current_period_end, 5 more } 

id: optional string

Subscription identifier tag.

maxLength32

currency: optional string

The monetary unit in which pricing information is displayed.

current_period_end: optional string

The end of the current period and also when the next billing is due.

formatdate-time

current_period_start: optional string

When the current billing period started. May match initial_period_start if this is the first period.

formatdate-time

frequency: optional "weekly" or "monthly" or "quarterly" or 2 more

How often the subscription is renewed automatically.

One of the following:

"weekly"

"monthly"

"quarterly"

"yearly"

"not-applicable"

price: optional number

The price of the subscription that will be billed, in US dollars.

rate_plan: optional [RatePlan](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20rate_plan%20%3E%20\(schema\)) { id, currency, externally_managed, 4 more } 

The rate plan applied to the subscription.

id: optional "free" or "lite" or "pro" or 7 more

The ID of the rate plan.

One of the following:

"free"

"lite"

"pro"

"pro_plus"

"business"

"enterprise"

"partners_free"

"partners_pro"

"partners_business"

"partners_enterprise"

currency: optional string

The currency applied to the rate plan subscription.

externally_managed: optional boolean

Whether this rate plan is managed externally from Cloudflare.

is_contract: optional boolean

Whether a rate plan is enterprise-based (or newly adopted term contract).

public_name: optional string

The full name of the rate plan.

scope: optional string

The scope that this rate plan applies to.

sets: optional array of string

The list of sets this rate plan applies to. Returns array of strings.

state: optional "Trial" or "Provisioned" or "Paid" or 4 more

The state that the subscription is in.

One of the following:

"Trial"

"Provisioned"

"Paid"

"AwaitingPayment"

"Cancelled"

"Failed"

"Expired"

success: true

Whether the API call was successful

### Update Zone Subscription

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/subscription \
        -X PUT \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "frequency": "monthly"
            }'

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
      "result": {
        "id": "506e3185e9c882d175a2d0cb0093d9f2",
        "currency": "USD",
        "current_period_end": "2014-03-31T12:20:00Z",
        "current_period_start": "2014-05-11T12:20:00Z",
        "frequency": "monthly",
        "price": 20,
        "rate_plan": {
          "id": "free",
          "currency": "USD",
          "externally_managed": false,
          "is_contract": false,
          "public_name": "Business Plan",
          "scope": "zone",
          "sets": [
            "string"
          ]
        },
        "state": "Paid"
      },
      "success": true
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
      "result": {
        "id": "506e3185e9c882d175a2d0cb0093d9f2",
        "currency": "USD",
        "current_period_end": "2014-03-31T12:20:00Z",
        "current_period_start": "2014-05-11T12:20:00Z",
        "frequency": "monthly",
        "price": 20,
        "rate_plan": {
          "id": "free",
          "currency": "USD",
          "externally_managed": false,
          "is_contract": false,
          "public_name": "Business Plan",
          "scope": "zone",
          "sets": [
            "string"
          ]
        },
        "state": "Paid"
      },
      "success": true
    }
