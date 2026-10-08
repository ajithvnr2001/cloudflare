---
url: https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/list/
title: List Workers for Platforms Dispatch Namespaces | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:16.234790+00:00
---

# List Workers for Platforms Dispatch Namespaces | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Workers For Platforms](https://developers.cloudflare.com/api/resources/workers_for_platforms)

[Dispatch](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch)

[Namespaces](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Workers for Platforms Dispatch Namespaces

GET/accounts/{account_id}/workers/dispatch/namespaces

Fetch a list of Workers for Platforms dispatch namespaces.

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

Identifier.

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

result: optional array of object { created_by, created_on, modified_by, 5 more } 

created_by: optional string

Identifier.

maxLength32

created_on: optional string

When the script was created.

formatdate-time

modified_by: optional string

Identifier.

maxLength32

modified_on: optional string

When the script was last modified.

formatdate-time

namespace_id: optional string

API Resource UUID tag.

maxLength36

namespace_name: optional string

Name of the Workers for Platforms dispatch namespace.

script_count: optional number

The current number of scripts in this Dispatch Namespace.

trusted_workers: optional boolean

Whether the Workers in the namespace are executed in a “trusted” manner. When a Worker is trusted, it has access to the shared caches for the zone in the Cache API, and has access to the `request.cf` object on incoming Requests. When a Worker is untrusted, caches are not shared across the zone, and `request.cf` is undefined. By default, Workers in a namespace are “untrusted”.

### List Workers for Platforms Dispatch Namespaces

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces \
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
          "created_by": "023e105f4ecef8ad9ca31a8372d0c353",
          "created_on": "2017-01-01T00:00:00Z",
          "modified_by": "023e105f4ecef8ad9ca31a8372d0c353",
          "modified_on": "2017-01-01T00:00:00Z",
          "namespace_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
          "namespace_name": "my-dispatch-namespace",
          "script_count": 800,
          "trusted_workers": false
        }
      ]
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
          "created_by": "023e105f4ecef8ad9ca31a8372d0c353",
          "created_on": "2017-01-01T00:00:00Z",
          "modified_by": "023e105f4ecef8ad9ca31a8372d0c353",
          "modified_on": "2017-01-01T00:00:00Z",
          "namespace_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
          "namespace_name": "my-dispatch-namespace",
          "script_count": 800,
          "trusted_workers": false
        }
      ]
    }
