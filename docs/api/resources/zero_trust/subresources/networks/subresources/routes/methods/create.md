---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/
title: Create a tunnel route | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:13.191372+00:00
---

# Create a tunnel route | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks)

[Routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Create a tunnel route

POST/accounts/{account_id}/teamnet/routes

Routes a private network through a Cloudflare Tunnel.

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

`Cloudflare One Networks Write``Cloudflare Tunnel Write`

##### Path ParametersExpand Collapse 

account_id: string

Cloudflare account ID

maxLength32

##### Body ParametersJSONExpand Collapse 

network: string

The private IPv4 or IPv6 range connected by the route, in CIDR notation.

tunnel_id: string

UUID of the tunnel.

formatuuid

maxLength36

comment: optional string

Optional remark describing the route.

maxLength100

virtual_network_id: optional string

UUID of the virtual network.

formatuuid

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

result: [Route](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.networks.routes%20%3E%20\(model\)%20route%20%3E%20\(schema\)) { id, comment, created_at, 4 more } 

id: optional string

UUID of the route.

maxLength36

comment: optional string

Optional remark describing the route.

maxLength100

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

network: optional string

The private IPv4 or IPv6 range connected by the route, in CIDR notation.

tunnel_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

virtual_network_id: optional string

UUID of the virtual network.

formatuuid

success: true

Whether the API call was successful

### Create a tunnel route

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "network": "172.16.0.0/16",
              "tunnel_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
              "comment": "Example comment for this route.",
              "virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415"
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
        "id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        "comment": "Example comment for this route.",
        "created_at": "2021-01-25T18:22:34.317854Z",
        "deleted_at": "2009-11-10T23:00:00Z",
        "network": "172.16.0.0/16",
        "tunnel_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        "virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415"
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
        "id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        "comment": "Example comment for this route.",
        "created_at": "2021-01-25T18:22:34.317854Z",
        "deleted_at": "2009-11-10T23:00:00Z",
        "network": "172.16.0.0/16",
        "tunnel_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        "virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415"
      },
      "success": true
    }
