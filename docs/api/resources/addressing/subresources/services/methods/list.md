---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/services/methods/list/
title: List Services | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:31.279788+00:00
---

# List Services | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/services/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Services](https://developers.cloudflare.com/api/resources/addressing/subresources/services)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Services

GET/accounts/{account_id}/addressing/services

Bring-Your-Own IP (BYOIP) prefixes onboarded to Cloudflare must be bound to a service running on the Cloudflare network to enable a Cloudflare product on the IP addresses. This endpoint can be used as a reference of available services on the Cloudflare network, and their service IDs.

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

`IP Prefixes: Write``IP Prefixes: Read`

##### Path ParametersExpand Collapse 

account_id: string

Identifier of a Cloudflare account.

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

result: optional array of object { id, name } 

id: optional string

Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint.

maxLength32

name: optional string

Name of a service running on the Cloudflare network

### List Services

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/services \
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
          "id": "2db684ee7ca04e159946fd05b99e1bcd",
          "name": "Magic Transit"
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
          "id": "2db684ee7ca04e159946fd05b99e1bcd",
          "name": "Magic Transit"
        }
      ]
    }
