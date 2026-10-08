---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/list/
title: List Address Maps | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:22.706555+00:00
---

# List Address Maps | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Address Maps](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Address Maps

GET/accounts/{account_id}/addressing/address_maps

List all address maps owned by the account.

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

`Address Maps Write``Address Maps Read`

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

result: optional array of [AddressMap](https://developers.cloudflare.com/api/resources/addressing#\(resource\)%20addressing.address_maps%20%3E%20\(model\)%20address_map%20%3E%20\(schema\)) { id, can_delete, can_modify_ips, 5 more } 

id: optional string

Identifier of an Address Map.

maxLength32

can_delete: optional boolean

If set to false, then the Address Map cannot be deleted via API. This is true for Cloudflare-managed maps.

can_modify_ips: optional boolean

If set to false, then the IPs on the Address Map cannot be modified via the API. This is true for Cloudflare-managed maps.

created_at: optional string

formatdate-time

default_sni: optional string

If you have legacy TLS clients which do not send the TLS server name indicator, then you can specify one default SNI on the map. If Cloudflare receives a TLS handshake from a client without an SNI, it will respond with the default SNI on those IPs. The default SNI can be any valid zone or subdomain owned by the account.

description: optional string

An optional description field which may be used to describe the types of IPs or zones on the map.

enabled: optional boolean

Whether the Address Map is enabled or not. Cloudflare’s DNS will not respond with IP addresses on an Address Map until the map is enabled.

modified_at: optional string

formatdate-time

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

### List Address Maps

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/address_maps \
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
          "id": "055817b111884e0227e1be16a0be6ee0",
          "can_delete": true,
          "can_modify_ips": true,
          "created_at": "2014-01-01T05:20:00.12345Z",
          "default_sni": "*.example.com",
          "description": "My Ecommerce zones",
          "enabled": true,
          "modified_at": "2014-01-01T05:20:00.12345Z"
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
          "id": "055817b111884e0227e1be16a0be6ee0",
          "can_delete": true,
          "can_modify_ips": true,
          "created_at": "2014-01-01T05:20:00.12345Z",
          "default_sni": "*.example.com",
          "description": "My Ecommerce zones",
          "enabled": true,
          "modified_at": "2014-01-01T05:20:00.12345Z"
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
