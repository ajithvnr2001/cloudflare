---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/
title: Service Bindings | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:29.451052+00:00
---

# Service Bindings | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Service Bindings

##### [List Service Bindings](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings

##### [Get Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get)

GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}

##### [Create Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create)

POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings

##### [Delete Service Binding](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/delete)

DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}

##### ModelsExpand Collapse 

ServiceBinding object { id, cidr, provisioning, 2 more } 

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

ServiceBindingDeleteResponse object { errors, messages, success } 

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

[ Previous

* * *

Prefixes ](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)[ Next

* * *

BGP Prefixes ](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes)
