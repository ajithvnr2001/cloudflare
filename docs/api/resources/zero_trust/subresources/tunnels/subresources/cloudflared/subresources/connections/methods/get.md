---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/
title: List Cloudflare Tunnel connections | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:21.223586+00:00
---

# List Cloudflare Tunnel connections | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels)

[Cloudflared](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared)

[Connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Cloudflare Tunnel connections

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections

Lists the connections for a Cloudflare Tunnel, including connector IDs, cloudflared versions, and Cloudflare locations.

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

`Cloudflare One Connectors Write``Cloudflare One Connectors Read``Cloudflare One Connector: cloudflared Write``Cloudflare One Connector: cloudflared Read``Cloudflare Tunnel Write``Cloudflare Tunnel Read`

##### Path ParametersExpand Collapse 

account_id: string

Cloudflare account ID

maxLength32

tunnel_id: string

UUID of the tunnel.

formatuuid

maxLength36

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

result: array of [Client](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.tunnels.cloudflared.connections%20%3E%20\(model\)%20client%20%3E%20\(schema\)) { id, arch, config_version, 4 more } 

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

arch: optional string

The cloudflared OS architecture used to establish this connection.

config_version: optional number

The version of the remote tunnel configuration. Used internally to sync cloudflared with the Zero Trust dashboard.

conns: optional array of object { id, client_id, client_version, 5 more } 

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

features: optional array of string

Features enabled for the Cloudflare Tunnel.

run_at: optional string

Timestamp of when the tunnel connection was started.

formatdate-time

version: optional string

The cloudflared version used to establish this connection.

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

### List Cloudflare Tunnel connections

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \
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
          "id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
          "arch": "linux_amd64",
          "config_version": 0,
          "conns": [
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
          "features": [
            "ha-origin"
          ],
          "run_at": "2009-11-10T23:00:00Z",
          "version": "2022.7.1"
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
          "id": "1bedc50d-42b3-473c-b108-ff3d10c0d925",
          "arch": "linux_amd64",
          "config_version": 0,
          "conns": [
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
          "features": [
            "ha-origin"
          ],
          "run_at": "2009-11-10T23:00:00Z",
          "version": "2022.7.1"
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
