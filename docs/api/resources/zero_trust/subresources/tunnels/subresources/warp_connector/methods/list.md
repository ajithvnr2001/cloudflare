---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/
title: List Mesh nodes | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:18.607911+00:00
---

# List Mesh nodes | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels)

[WARP Connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Mesh nodes

GET/accounts/{account_id}/warp_connector

Lists and filters Mesh nodes in an account.

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

`Cloudflare One Connectors Write``Cloudflare One Connectors Read``Cloudflare One Connector: WARP Write``Cloudflare One Connector: WARP Read`

##### Path ParametersExpand Collapse 

account_id: string

Cloudflare account ID

maxLength32

##### Query ParametersExpand Collapse 

exclude_prefix: optional string

existed_at: optional string

If provided, include only resources that were created (and not deleted) before this time. URL encoded.

formaturl-encoded-date-time

include_prefix: optional string

is_deleted: optional boolean

If `true`, only include deleted tunnels. If `false`, exclude deleted tunnels. If empty, all tunnels will be included.

name: optional string

A user-friendly name for the tunnel.

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Number of results to display.

maximum1000

minimum1

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

uuid: optional string

UUID of the tunnel.

formatuuid

maxLength36

was_active_at: optional string

formatdate-time

was_inactive_at: optional string

formatdate-time

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

result: array of object { id, account_tag, connections, 8 more } 

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

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

### List Mesh nodes

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/warp_connector \
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
          "account_tag": "699d98642c564d2e855e9661899b7252",
          "connections": [
            {
              "id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
              "client_id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
              "client_version": "2022.7.1",
              "colo_name": "DFW",
              "is_pending_reconnect": false,
              "opened_at": "2021-01-25T18:22:34.317854Z",
              "origin_ip": "10.1.0.137",
              "uuid": "1bedc50d-42b3-473c-b108-ff3d10c0d925"
            }
          ],
          "conns_active_at": "2009-11-10T23:00:00Z",
          "conns_inactive_at": "2009-11-10T23:00:00Z",
          "created_at": "2021-01-25T18:22:34.317854Z",
          "deleted_at": "2009-11-10T23:00:00Z",
          "metadata": {},
          "name": "blog",
          "status": "healthy",
          "tun_type": "cfd_tunnel"
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
          "account_tag": "699d98642c564d2e855e9661899b7252",
          "connections": [
            {
              "id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
              "client_id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
              "client_version": "2022.7.1",
              "colo_name": "DFW",
              "is_pending_reconnect": false,
              "opened_at": "2021-01-25T18:22:34.317854Z",
              "origin_ip": "10.1.0.137",
              "uuid": "1bedc50d-42b3-473c-b108-ff3d10c0d925"
            }
          ],
          "conns_active_at": "2009-11-10T23:00:00Z",
          "conns_inactive_at": "2009-11-10T23:00:00Z",
          "created_at": "2021-01-25T18:22:34.317854Z",
          "deleted_at": "2009-11-10T23:00:00Z",
          "metadata": {},
          "name": "blog",
          "status": "healthy",
          "tun_type": "cfd_tunnel"
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
