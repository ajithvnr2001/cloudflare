---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/
title: Networks | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:10.377820+00:00
---

# Networks | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Networks

#### NetworksRoutes

##### [List tunnel routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list)

GET/accounts/{account_id}/teamnet/routes

##### [Get tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/get)

GET/accounts/{account_id}/teamnet/routes/{route_id}

##### [Create a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create)

POST/accounts/{account_id}/teamnet/routes

##### [Update a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit)

PATCH/accounts/{account_id}/teamnet/routes/{route_id}

##### [Delete a tunnel route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete)

DELETE/accounts/{account_id}/teamnet/routes/{route_id}

##### ModelsExpand Collapse 

NetworkRoute object { id, comment, created_at, 4 more } 

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

Route object { id, comment, created_at, 4 more } 

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

Teamnet object { id, comment, created_at, 7 more } 

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

#### NetworksRoutesIPs

##### [Get tunnel route by IP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/ips/methods/get)

GET/accounts/{account_id}/teamnet/routes/ip/{ip}

#### NetworksRoutesNetworks

##### [Create a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create)

Deprecated

POST/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

##### [Update a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit)

Deprecated

PATCH/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

##### [Delete a tunnel route (CIDR Endpoint)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete)

Deprecated

DELETE/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}

#### NetworksVirtual Networks

##### [List virtual networks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list)

GET/accounts/{account_id}/teamnet/virtual_networks

##### [Get a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/get)

GET/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

##### [Create a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/create)

POST/accounts/{account_id}/teamnet/virtual_networks

##### [Update a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/edit)

PATCH/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

##### [Delete a virtual network](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/delete)

DELETE/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}

##### ModelsExpand Collapse 

VirtualNetwork object { id, comment, created_at, 3 more } 

id: string

UUID of the virtual network.

formatuuid

comment: string

Optional remark describing the virtual network.

maxLength256

created_at: string

Timestamp of when the resource was created.

formatdate-time

is_default_network: boolean

If `true`, this virtual network is the default for the account.

name: string

A user-friendly name for the virtual network.

maxLength256

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

#### NetworksSubnets

##### [List Subnets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list)

GET/accounts/{account_id}/zerotrust/subnets

#### NetworksSubnetsWARP

##### [Create WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/create)

POST/accounts/{account_id}/zerotrust/subnets/warp

##### [Get WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/get)

GET/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

##### [Update WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/edit)

PATCH/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

##### [Delete WARP IP subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/warp/methods/delete)

DELETE/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}

##### ModelsExpand Collapse 

Subnet object { id, capacity, comment, 6 more } 

id: optional string

The UUID of the subnet.

formatuuid

capacity: optional object { total, used } 

IP capacity information for the subnet.

total: optional number

Total number of assignable IPs in the subnet.

used: optional number

Number of assigned IPs in the subnet.

comment: optional string

An optional description of the subnet.

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

is_default_network: optional boolean

If `true`, this is the default subnet for the account. There can only be one default subnet per account.

name: optional string

A user-friendly name for the subnet.

network: optional string

The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

subnet_type: optional "cloudflare_source" or "initial_resolved_ip" or "warp"

The type of subnet.

One of the following:

"cloudflare_source"

"initial_resolved_ip"

"warp"

WARPDeleteResponse object { id, capacity, comment, 6 more } 

id: optional string

The UUID of the subnet.

formatuuid

capacity: optional object { total, used } 

IP capacity information for the subnet.

total: optional number

Total number of assignable IPs in the subnet.

used: optional number

Number of assigned IPs in the subnet.

comment: optional string

An optional description of the subnet.

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

is_default_network: optional boolean

If `true`, this is the default subnet for the account. There can only be one default subnet per account.

name: optional string

A user-friendly name for the subnet.

network: optional string

The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

subnet_type: optional "cloudflare_source" or "initial_resolved_ip" or "warp"

The type of subnet.

One of the following:

"cloudflare_source"

"initial_resolved_ip"

"warp"

#### NetworksSubnetsCloudflare Source

##### [Update Cloudflare Source Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/cloudflare_source/methods/update)

PATCH/accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}

#### NetworksSubnetsInitial Resolved IP

##### [Get Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/get)

GET/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}

##### [Update Initial Resolved IP Subnet](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/subnets/subresources/initial_resolved_ip/methods/update)

PUT/accounts/{account_id}/zerotrust/subnets/initial_resolved_ip/{address_family}

#### NetworksHostname Routes

##### [List hostname routes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/list)

GET/accounts/{account_id}/zerotrust/routes/hostname

##### [Get hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/get)

GET/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

##### [Create hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/create)

POST/accounts/{account_id}/zerotrust/routes/hostname

##### [Update hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/edit)

PATCH/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

##### [Delete hostname route](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/hostname_routes/methods/delete)

DELETE/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}

##### ModelsExpand Collapse 

HostnameRoute object { id, comment, created_at, 5 more } 

id: optional string

The hostname route ID.

formatuuid

comment: optional string

An optional description of the hostname route.

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

hostname: optional string

The hostname of the route.

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

[ Previous

* * *

Pacfiles ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/pacfiles)[ Next

* * *

Routes ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/networks/subresources/routes)
