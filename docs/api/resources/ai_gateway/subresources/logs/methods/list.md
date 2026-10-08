---
url: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list/
title: List Gateway Logs | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:23.183592+00:00
---

# List Gateway Logs | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[AI Gateway](https://developers.cloudflare.com/api/resources/ai_gateway)

[Logs](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Gateway Logs

GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs

Lists request/response log entries for the AI gateway with filtering and pagination.

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

`AI Gateway Write``AI Gateway Read`

##### Path ParametersExpand Collapse 

account_id: string

gateway_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

##### Query ParametersExpand Collapse 

Deprecatedcached: optional boolean

Deprecateddirection: optional "asc" or "desc"

One of the following:

"asc"

"desc"

Deprecatedend_date: optional string

formatdate-time

Deprecatedfeedback: optional 0 or 1

One of the following:

0

1

filters: optional array of object { key, operator, value } 

key: "id" or "created_at" or "request_content_type" or 21 more

One of the following:

"id"

"created_at"

"request_content_type"

"response_content_type"

"request_type"

"success"

"cached"

"provider"

"model"

"model_type"

"cost"

"tokens"

"tokens_in"

"tokens_out"

"duration"

"feedback"

"event_id"

"metadata.key"

"metadata.value"

"authentication"

"wholesale"

"compatibilityMode"

"dlp_action"

"user_agent"

operator: "eq" or "neq" or "contains" or 2 more

One of the following:

"eq"

"neq"

"contains"

"lt"

"gt"

value: array of string or number or boolean

Filter values.

One of the following:

string

number

boolean

Deprecatedmax_cost: optional number

Deprecatedmax_duration: optional number

Deprecatedmax_tokens_in: optional number

Deprecatedmax_tokens_out: optional number

Deprecatedmax_total_tokens: optional number

meta_info: optional boolean

Deprecatedmin_cost: optional number

Deprecatedmin_duration: optional number

Deprecatedmin_tokens_in: optional number

Deprecatedmin_tokens_out: optional number

Deprecatedmin_total_tokens: optional number

Deprecatedmodel: optional string

Model filter.

Deprecatedmodel_type: optional string

order_by: optional "created_at" or "provider" or "model" or 3 more

One of the following:

"created_at"

"provider"

"model"

"model_type"

"success"

"cached"

order_by_direction: optional "asc" or "desc"

One of the following:

"asc"

"desc"

page: optional number

minimum1

per_page: optional number

maximum50

minimum1

Deprecatedprovider: optional string

Deprecatedrequest_content_type: optional string

Deprecatedresponse_content_type: optional string

search: optional string

Free-text search over log metadata.

Deprecatedstart_date: optional string

formatdate-time

Deprecatedsuccess: optional boolean

##### ReturnsExpand Collapse 

result: array of object { id, cached, created_at, 16 more } 

id: string

cached: boolean

created_at: string

formatdate-time

duration: number

model: string

path: string

provider: string

success: boolean

tokens_in: number

tokens_out: number

cost: optional number

custom_cost: optional boolean

metadata: optional string

model_type: optional string

request_content_type: optional string

request_type: optional string

response_content_type: optional string

status_code: optional number

step: optional number

result_info: object { count, max_cost, max_duration, 11 more } 

count: optional number

max_cost: optional number

max_duration: optional number

max_tokens_in: optional number

max_tokens_out: optional number

max_total_tokens: optional number

min_cost: optional number

min_duration: optional number

min_tokens_in: optional number

min_tokens_out: optional number

min_total_tokens: optional number

page: optional number

per_page: optional number

total_count: optional number

success: boolean

### List Gateway Logs

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-gateway/gateways/$GATEWAY_ID/logs \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": [
        {
          "id": "id",
          "cached": true,
          "created_at": "2019-12-27T18:11:19.117Z",
          "duration": 0,
          "model": "model",
          "path": "path",
          "provider": "provider",
          "success": true,
          "tokens_in": 0,
          "tokens_out": 0,
          "cost": 0,
          "custom_cost": true,
          "metadata": "metadata",
          "model_type": "model_type",
          "request_content_type": "request_content_type",
          "request_type": "request_type",
          "response_content_type": "response_content_type",
          "status_code": 0,
          "step": 0
        }
      ],
      "result_info": {
        "count": 0,
        "max_cost": 0,
        "max_duration": 0,
        "max_tokens_in": 0,
        "max_tokens_out": 0,
        "max_total_tokens": 0,
        "min_cost": 0,
        "min_duration": 0,
        "min_tokens_in": 0,
        "min_tokens_out": 0,
        "min_total_tokens": 0,
        "page": 0,
        "per_page": 0,
        "total_count": 0
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": [
        {
          "id": "id",
          "cached": true,
          "created_at": "2019-12-27T18:11:19.117Z",
          "duration": 0,
          "model": "model",
          "path": "path",
          "provider": "provider",
          "success": true,
          "tokens_in": 0,
          "tokens_out": 0,
          "cost": 0,
          "custom_cost": true,
          "metadata": "metadata",
          "model_type": "model_type",
          "request_content_type": "request_content_type",
          "request_type": "request_type",
          "response_content_type": "response_content_type",
          "status_code": 0,
          "step": 0
        }
      ],
      "result_info": {
        "count": 0,
        "max_cost": 0,
        "max_duration": 0,
        "max_tokens_in": 0,
        "max_tokens_out": 0,
        "max_total_tokens": 0,
        "min_cost": 0,
        "min_duration": 0,
        "min_tokens_in": 0,
        "min_tokens_out": 0,
        "min_total_tokens": 0,
        "page": 0,
        "per_page": 0,
        "total_count": 0
      },
      "success": true
    }
