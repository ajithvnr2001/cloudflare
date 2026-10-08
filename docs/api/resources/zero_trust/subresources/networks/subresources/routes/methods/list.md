---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/
title: List tunnel routes | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:24.735362+00:00
---

# List tunnel routes | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/

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

# List tunnel routes

GET/accounts/{account_id}/teamnet/routes

Lists and filters private network routes in an account.

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

`Cloudflare One Networks Write``Cloudflare One Networks Read``Cloudflare Tunnel Write``Cloudflare Tunnel Read`

##### Path ParametersExpand Collapse 

account_id: string

Cloudflare account ID

maxLength32

##### Query ParametersExpand Collapse 

comment: optional string

Optional remark describing the route.

maxLength100

existed_at: optional string

If provided, include only resources that were created (and not deleted) before this time. URL encoded.

formaturl-encoded-date-time

is_deleted: optional boolean

If `true`, only include deleted routes. If `false`, exclude deleted routes. If empty, all routes will be included.

network_subset: optional string

If set, only list routes that are contained within this IP range.

network_superset: optional string

If set, only list routes that contain this IP range.

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Number of results to display.

maximum1000

minimum1

route_id: optional string

UUID of the route.

maxLength36

tun_types: optional array of "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The types of tunnels to filter by, separated by commas.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

tunnel_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

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

result: array of [Teamnet](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.networks.routes%20%3E%20\(model\)%20teamnet%20%3E%20\(schema\)) { id, comment, created_at, 7 more } 

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

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

tunnel_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

tunnel_name: optional string

A user-friendly name for a tunnel.

virtual_network_id: optional string

UUID of the virtual network.

formatuuid

virtual_network_name: optional string

A user-friendly name for the virtual network.

maxLength256

success: true

Whether the API call was successful

result_info: optional object { count, page, per_page, total_count } 

count: optional number

Total number of results for the requested service

page: optional number

Current page within paginated list of results

per_page: optional number

Number of results per page of results

total_count: optional number

Total results available without any search parameters

### List tunnel routes

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
      "result": [
        {
          "id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "comment": "Example comment for this route.",
          "created_at": "2021-01-25T18:22:34.317854Z",
          "deleted_at": "2009-11-10T23:00:00Z",
          "network": "172.16.0.0/16",
          "tun_type": "cfd_tunnel",
          "tunnel_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "tunnel_name": "blog",
          "virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "virtual_network_name": "us-east-1-vpc"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
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
      "result": [
        {
          "id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "comment": "Example comment for this route.",
          "created_at": "2021-01-25T18:22:34.317854Z",
          "deleted_at": "2009-11-10T23:00:00Z",
          "network": "172.16.0.0/16",
          "tun_type": "cfd_tunnel",
          "tunnel_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "tunnel_name": "blog",
          "virtual_network_id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
          "virtual_network_name": "us-east-1-vpc"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }
