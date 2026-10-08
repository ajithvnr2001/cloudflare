---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs/
title: Item Logs. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:08.986911+00:00
---

# Item Logs. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces)

[Instances](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)

[Items](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Item Logs.

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs

Lists processing logs for a specific item in an AI Search instance.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Path ParametersExpand Collapse 

account_id: string

name: string

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

item_id: string

##### Query ParametersExpand Collapse 

cursor: optional string

maxLength512

limit: optional number

maximum100

minimum1

##### ReturnsExpand Collapse 

result: array of object { action, chunkCount, errorType, 4 more } 

action: string

chunkCount: number

errorType: string

fileKey: string

message: string

processingTimeMs: number

timestamp: string

formatdate-time

result_info: object { count, cursor, per_page, truncated } 

count: number

cursor: string

per_page: number

truncated: boolean

success: boolean

### Item Logs.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/items/$ITEM_ID/logs \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": [
        {
          "action": "action",
          "chunkCount": 0,
          "errorType": "errorType",
          "fileKey": "fileKey",
          "message": "message",
          "processingTimeMs": 0,
          "timestamp": "2019-12-27T18:11:19.117Z"
        }
      ],
      "result_info": {
        "count": 0,
        "cursor": "cursor",
        "per_page": 0,
        "truncated": true
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": [
        {
          "action": "action",
          "chunkCount": 0,
          "errorType": "errorType",
          "fileKey": "fileKey",
          "message": "message",
          "processingTimeMs": 0,
          "timestamp": "2019-12-27T18:11:19.117Z"
        }
      ],
      "result_info": {
        "count": 0,
        "cursor": "cursor",
        "per_page": 0,
        "truncated": true
      },
      "success": true
    }
