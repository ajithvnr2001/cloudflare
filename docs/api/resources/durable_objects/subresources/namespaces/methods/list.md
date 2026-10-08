---
url: https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces/methods/list/
title: List Durable Object Namespaces | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:37.717665+00:00
---

# List Durable Object Namespaces | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Durable Objects](https://developers.cloudflare.com/api/resources/durable_objects)

[Namespaces](https://developers.cloudflare.com/api/resources/durable_objects/subresources/namespaces)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Durable Object Namespaces

GET/accounts/{account_id}/workers/durable_objects/namespaces

Returns the Durable Object namespaces owned by an account.

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

`Workers Scripts Write``Workers Scripts Read`

##### Path ParametersExpand Collapse 

account_id: string

Identifier.

maxLength32

##### Query ParametersExpand Collapse 

page: optional number

Current page.

minimum1

per_page: optional number

Items per-page.

maximum1000

minimum1

##### ReturnsExpand Collapse 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

success: true

Whether the API call was successful.

result: optional array of [Namespace](https://developers.cloudflare.com/api/resources/durable_objects#\(resource\)%20durable_objects.namespaces%20%3E%20\(model\)%20namespace%20%3E%20\(schema\)) { id, class, name, 2 more } 

id: optional string

class: optional string

name: optional string

script: optional string

use_sqlite: optional boolean

result_info: optional object { count, page, per_page, 2 more } 

count: optional number

Total number of results for the requested service.

page: optional number

Current page within paginated list of results.

per_page: optional number

Number of results per page of results.

total_count: optional number

Total results available without any search parameters.

total_pages: optional number

The number of total pages in the entire result set.

### List Durable Object Namespaces

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/durable_objects/namespaces \
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
      "success": true,
      "result": [
        {
          "id": "id",
          "class": "class",
          "name": "name",
          "script": "script",
          "use_sqlite": true
        }
      ],
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
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
      "success": true,
      "result": [
        {
          "id": "id",
          "class": "class",
          "name": "name",
          "script": "script",
          "use_sqlite": true
        }
      ],
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
      }
    }
