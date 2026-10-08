---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/
title: Create Service Binding | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:33.547671+00:00
---

# Create Service Binding | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

[Service Bindings](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Create Service Binding

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings

Creates a new Service Binding, routing traffic to IPs within the given CIDR to a service running on Cloudflare’s network. **NOTE:** The first Service Binding created for an IP Prefix must exactly match the IP Prefix’s CIDR. Subsequent Service Bindings may be created with a more-specific CIDR. Refer to the [Service Bindings Documentation](https://developers.cloudflare.com/byoip/service-bindings/) for compatibility details.

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

`IP Prefixes: Write`

##### Path ParametersExpand Collapse 

account_id: string

Identifier of a Cloudflare account.

maxLength32

prefix_id: string

Identifier of an IP Prefix.

maxLength32

##### Body ParametersJSONExpand Collapse 

cidr: string

IP Prefix in Classless Inter-Domain Routing format.

service_id: string

Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint.

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

result: optional [ServiceBinding](https://developers.cloudflare.com/api/resources/addressing#\(resource\)%20addressing.prefixes.service_bindings%20%3E%20\(model\)%20service_binding%20%3E%20\(schema\)) { id, cidr, provisioning, 2 more } 

id: optional string

Identifier of a Service Binding.

maxLength32

cidr: optional string

IP Prefix in Classless Inter-Domain Routing format.

provisioning: optional object { state } 

Status of a Service Binding’s deployment to the Cloudflare network

state: optional "provisioning" or "active" or "magic_transit_route_missing"

When a binding has been deployed to a majority of Cloudflare datacenters, the binding will become active and can be used with its associated service.

One of the following:

"provisioning"

"active"

"magic_transit_route_missing"

service_id: optional string

Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint.

maxLength32

service_name: optional string

Name of a service running on the Cloudflare network

### Create Service Binding

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID/bindings \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "cidr": "192.0.2.0/24",
              "service_id": "2db684ee7ca04e159946fd05b99e1bcd"
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
        "id": "0429b49b6a5155297b78e75a44b09e14",
        "cidr": "192.0.2.0/24",
        "provisioning": {
          "state": "provisioning"
        },
        "service_id": "2db684ee7ca04e159946fd05b99e1bcd",
        "service_name": "Magic Transit"
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
        "id": "0429b49b6a5155297b78e75a44b09e14",
        "cidr": "192.0.2.0/24",
        "provisioning": {
          "state": "provisioning"
        },
        "service_id": "2db684ee7ca04e159946fd05b99e1bcd",
        "service_name": "Magic Transit"
      }
    }
