---
url: https://developers.cloudflare.com/api/resources/workflows/methods/list/
title: List all Workflows | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:17.000368+00:00
---

# List all Workflows | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/workflows/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Workflows](https://developers.cloudflare.com/api/resources/workflows)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List all Workflows

GET/accounts/{account_id}/workflows

Lists all workflows configured for the account.

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

`Workers Tail Read``Workers Scripts Write``Workers Scripts Read`

##### Path ParametersExpand Collapse 

account_id: string

##### Query ParametersExpand Collapse 

page: optional number

minimum1

per_page: optional number

maximum100

minimum1

search: optional string

Allows filtering workflows` name.

maxLength64

minLength1

##### ReturnsExpand Collapse 

errors: array of object { code, message } 

code: number

message: string

messages: array of object { code, message } 

code: number

message: string

result: array of object { id, class_name, created_on, 7 more } 

id: string

formatuuid

class_name: string

created_on: string

formatdate-time

instances: map[number]

modified_on: string

formatdate-time

name: string

maxLength64

minLength1

script_name: string

triggered_on: string

formatdate-time

schedules: optional array of object { cron, next_instance } 

cron: string

next_instance: string

script_deleted: optional boolean

Whether the bound Worker was deleted, leaving this Workflow inactive.

success: true

result_info: optional object { count, per_page, total_count, 3 more } 

count: number

per_page: number

total_count: number

cursor: optional string

page: optional number

total_pages: optional number

### List all Workflows

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workflows \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [],
      "messages": [
        {
          "code": 0,
          "message": "message"
        }
      ],
      "result": [
        {
          "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          "class_name": "class_name",
          "created_on": "2019-12-27T18:11:19.117Z",
          "instances": {
            "foo": 0
          },
          "modified_on": "2019-12-27T18:11:19.117Z",
          "name": "x",
          "script_name": "script_name",
          "triggered_on": "2019-12-27T18:11:19.117Z",
          "schedules": [
            {
              "cron": "cron",
              "next_instance": "next_instance"
            }
          ],
          "script_deleted": true
        }
      ],
      "success": true,
      "result_info": {
        "count": 0,
        "per_page": 0,
        "total_count": 0,
        "cursor": "cursor",
        "page": 0,
        "total_pages": 0
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [],
      "messages": [
        {
          "code": 0,
          "message": "message"
        }
      ],
      "result": [
        {
          "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          "class_name": "class_name",
          "created_on": "2019-12-27T18:11:19.117Z",
          "instances": {
            "foo": 0
          },
          "modified_on": "2019-12-27T18:11:19.117Z",
          "name": "x",
          "script_name": "script_name",
          "triggered_on": "2019-12-27T18:11:19.117Z",
          "schedules": [
            {
              "cron": "cron",
              "next_instance": "next_instance"
            }
          ],
          "script_deleted": true
        }
      ],
      "success": true,
      "result_info": {
        "count": 0,
        "per_page": 0,
        "total_count": 0,
        "cursor": "cursor",
        "page": 0,
        "total_pages": 0
      }
    }
