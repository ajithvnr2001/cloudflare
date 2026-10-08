---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/
title: Get a Cloudflare Tunnel | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:19.392902+00:00
---

# Get a Cloudflare Tunnel | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels)

[Cloudflared](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get a Cloudflare Tunnel

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}

Fetches a single Cloudflare Tunnel.

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

result: [CloudflareTunnel](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20cloudflare_tunnel%20%3E%20\(schema\)) { id, account_tag, config_src, 10 more } 

A Cloudflare Tunnel that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

config_src: optional "local" or "cloudflare"

Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel on the Zero Trust dashboard.

One of the following:

"local"

"cloudflare"

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

Deprecatedremote_config: optional boolean

Use the config_src field instead.

If `true`, the tunnel can be configured remotely from the Zero Trust dashboard. If `false`, the tunnel must be configured locally on the origin machine.

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

### Get a Cloudflare Tunnel

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \
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
      "result": {
        "id": "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        "account_tag": "699d98642c564d2e855e9661899b7252",
        "config_src": "cloudflare",
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
        "remote_config": true,
        "status": "healthy",
        "tun_type": "cfd_tunnel"
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
        "account_tag": "699d98642c564d2e855e9661899b7252",
        "config_src": "cloudflare",
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
        "remote_config": true,
        "status": "healthy",
        "tun_type": "cfd_tunnel"
      },
      "success": true
    }
