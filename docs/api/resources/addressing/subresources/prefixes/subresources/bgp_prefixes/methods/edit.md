---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit/
title: Update BGP Prefix | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:34.498396+00:00
---

# Update BGP Prefix | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/methods/edit/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

[BGP Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update BGP Prefix

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}

Update the properties of a BGP Prefix, such as the on demand advertisement status (advertised or withdrawn).

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

`Magic Transit Write``IP Prefixes: Write``IP Prefixes: BGP On Demand Write`

##### Path ParametersExpand Collapse 

account_id: string

Identifier of a Cloudflare account.

maxLength32

prefix_id: string

Identifier of an IP Prefix.

maxLength32

bgp_prefix_id: string

Identifier of BGP Prefix.

maxLength32

##### Body ParametersJSONExpand Collapse 

asn_prepend_count: optional number

Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute

maximum3

minimum0

auto_advertise_withdraw: optional boolean

Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no matching BGP prefix in the Magic routing table. When true, Cloudflare will automatically withdraw the BGP prefix when there are no matching BGP routes, and will resume advertising when there is at least one matching BGP route.

on_demand: optional object { advertised } 

advertised: optional boolean

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

result: optional [BGPPrefix](https://developers.cloudflare.com/api/resources/addressing#\(resource\)%20addressing.prefixes.bgp_prefixes%20%3E%20\(model\)%20bgp_prefix%20%3E%20\(schema\)) { id, asn, asn_prepend_count, 6 more } 

id: optional string

Identifier of BGP Prefix.

maxLength32

asn: optional number

Autonomous System Number (ASN) the prefix will be advertised under.

asn_prepend_count: optional number

Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute

maximum3

minimum0

auto_advertise_withdraw: optional boolean

Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no matching BGP prefix in the Magic routing table. When true, Cloudflare will automatically withdraw the BGP prefix when there are no matching BGP routes, and will resume advertising when there is at least one matching BGP route.

bgp_signal_opts: optional object { enabled, modified_at } 

enabled: optional boolean

Whether control of advertisement of the prefix to the Internet is enabled to be performed via BGP signal

modified_at: optional string

Last time BGP signaling control was toggled. This field is null if BGP signaling has never been enabled.

formatdate-time

cidr: optional string

IP Prefix in Classless Inter-Domain Routing format.

created_at: optional string

formatdate-time

modified_at: optional string

formatdate-time

on_demand: optional object { advertised, advertised_modified_at, on_demand_enabled, on_demand_locked } 

advertised: optional boolean

Prefix advertisement status to the Internet. This field is only not ‘null’ if on demand is enabled.

advertised_modified_at: optional string

Last time the advertisement status was changed. This field is only not ‘null’ if on demand is enabled.

formatdate-time

on_demand_enabled: optional boolean

Whether advertisement of the prefix to the Internet may be dynamically enabled or disabled.

on_demand_locked: optional boolean

Whether the advertisement status of the prefix is locked, meaning it cannot be changed.

### Update BGP Prefix

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID/bgp/prefixes/$BGP_PREFIX_ID \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "asn_prepend_count": 2,
              "auto_advertise_withdraw": true
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
      "success": true,
      "result": {
        "id": "7009ba364c7a5760798ceb430e603b74",
        "asn": 13335,
        "asn_prepend_count": 2,
        "auto_advertise_withdraw": true,
        "bgp_signal_opts": {
          "enabled": false,
          "modified_at": "2014-01-01T05:20:00.12345Z"
        },
        "cidr": "192.0.2.0/24",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "modified_at": "2014-01-01T05:20:00.12345Z",
        "on_demand": {
          "advertised": true,
          "advertised_modified_at": "2014-01-01T05:20:00.12345Z",
          "on_demand_enabled": true,
          "on_demand_locked": false
        }
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
      "result": {
        "id": "7009ba364c7a5760798ceb430e603b74",
        "asn": 13335,
        "asn_prepend_count": 2,
        "auto_advertise_withdraw": true,
        "bgp_signal_opts": {
          "enabled": false,
          "modified_at": "2014-01-01T05:20:00.12345Z"
        },
        "cidr": "192.0.2.0/24",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "modified_at": "2014-01-01T05:20:00.12345Z",
        "on_demand": {
          "advertised": true,
          "advertised_modified_at": "2014-01-01T05:20:00.12345Z",
          "on_demand_enabled": true,
          "on_demand_locked": false
        }
      }
    }
