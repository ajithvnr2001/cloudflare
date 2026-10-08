---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/list/
title: List Prefix Delegations | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:28.199189+00:00
---

# List Prefix Delegations | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

[Delegations](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/delegations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Prefix Delegations

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations

List all delegations for a given account IP prefix.

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

Identifier of a Cloudflare account.

maxLength32

prefix_id: string

Identifier of an IP Prefix.

maxLength32

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

result: optional array of [Delegations](https://developers.cloudflare.com/api/resources/addressing#\(resource\)%20addressing.prefixes.delegations%20%3E%20\(model\)%20delegations%20%3E%20\(schema\)) { id, cidr, created_at, 3 more } 

id: optional string

Identifier of a Delegation.

maxLength32

cidr: optional string

IP Prefix in Classless Inter-Domain Routing format.

created_at: optional string

formatdate-time

delegated_account_id: optional string

Account identifier for the account to which prefix is being delegated.

maxLength32

modified_at: optional string

formatdate-time

parent_prefix_id: optional string

Identifier of an IP Prefix.

maxLength32

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

### List Prefix Delegations

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID/delegations \
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
          "id": "d933b1530bc56c9953cf8ce166da8004",
          "cidr": "192.0.2.0/24",
          "created_at": "2014-01-01T05:20:00.12345Z",
          "delegated_account_id": "b1946ac92492d2347c6235b4d2611184",
          "modified_at": "2014-01-01T05:20:00.12345Z",
          "parent_prefix_id": "2af39739cc4e3b5910c918468bb89828"
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
          "id": "d933b1530bc56c9953cf8ce166da8004",
          "cidr": "192.0.2.0/24",
          "created_at": "2014-01-01T05:20:00.12345Z",
          "delegated_account_id": "b1946ac92492d2347c6235b4d2611184",
          "modified_at": "2014-01-01T05:20:00.12345Z",
          "parent_prefix_id": "2af39739cc4e3b5910c918468bb89828"
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
