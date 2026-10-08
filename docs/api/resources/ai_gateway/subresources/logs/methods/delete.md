---
url: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/delete/
title: Delete Gateway Logs | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:27.306949+00:00
---

# Delete Gateway Logs | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/delete/

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

# Delete Gateway Logs

DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs

Deletes gateway log entries matching the specified criteria.

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

`AI Gateway Write`

##### Path ParametersExpand Collapse 

account_id: string

gateway_id: string

Unique identifier of the AI Gateway within the account.

maxLength64

minLength1

##### Query ParametersExpand Collapse 

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

limit: optional number

maximum10000

minimum1

order_by: optional "created_at" or "provider" or "model" or 8 more

One of the following:

"created_at"

"provider"

"model"

"model_type"

"success"

"cached"

"cost"

"tokens_in"

"tokens_out"

"duration"

"feedback"

order_by_direction: optional "asc" or "desc"

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse 

success: boolean

### Delete Gateway Logs

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
        -X DELETE \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "success": true
    }
