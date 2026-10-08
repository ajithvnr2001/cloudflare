---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/
title: Targets | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:49.884714+00:00
---

# Targets | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Access](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access)

[Infrastructure](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Targets

##### [List all targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/list)

GET/accounts/{account_id}/infrastructure/targets

##### [Get target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/get)

GET/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Create new target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/create)

POST/accounts/{account_id}/infrastructure/targets

##### [Update target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/update)

PUT/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Delete target](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/delete)

DELETE/accounts/{account_id}/infrastructure/targets/{target_id}

##### [Create new targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_update)

PUT/accounts/{account_id}/infrastructure/targets/batch

##### [Delete targets (Deprecated)](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_delete)

Deprecated

DELETE/accounts/{account_id}/infrastructure/targets/batch

##### [Delete targets](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/methods/bulk_delete_v2)

POST/accounts/{account_id}/infrastructure/targets/batch_delete

##### ModelsExpand Collapse 

TargetListResponse object { id, created_at, hostname, 3 more } 

id: string

Target identifier

formatuuid

maxLength36

created_at: string

Date and time at which the target was created

formatdate-time

hostname: string

A non-unique field that refers to a target

ip: object { ipv4, ipv6 } 

The IPv4/IPv6 address that identifies where to reach a target

ipv4: optional object { ip_addr, virtual_network_id } 

The target’s IPv4 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

ipv6: optional object { ip_addr, virtual_network_id } 

The target’s IPv6 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

modified_at: string

Date and time at which the target was modified

formatdate-time

tags: optional map[string]

Tags assigned to the target. Empty when no tags are assigned.

TargetGetResponse object { id, created_at, hostname, 3 more } 

id: string

Target identifier

formatuuid

maxLength36

created_at: string

Date and time at which the target was created

formatdate-time

hostname: string

A non-unique field that refers to a target

ip: object { ipv4, ipv6 } 

The IPv4/IPv6 address that identifies where to reach a target

ipv4: optional object { ip_addr, virtual_network_id } 

The target’s IPv4 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

ipv6: optional object { ip_addr, virtual_network_id } 

The target’s IPv6 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

modified_at: string

Date and time at which the target was modified

formatdate-time

tags: optional map[string]

Tags assigned to the target. Empty when no tags are assigned.

TargetCreateResponse object { id, created_at, hostname, 3 more } 

id: string

Target identifier

formatuuid

maxLength36

created_at: string

Date and time at which the target was created

formatdate-time

hostname: string

A non-unique field that refers to a target

ip: object { ipv4, ipv6 } 

The IPv4/IPv6 address that identifies where to reach a target

ipv4: optional object { ip_addr, virtual_network_id } 

The target’s IPv4 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

ipv6: optional object { ip_addr, virtual_network_id } 

The target’s IPv6 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

modified_at: string

Date and time at which the target was modified

formatdate-time

tags: optional map[string]

Tags assigned to the target. Empty when no tags are assigned.

TargetUpdateResponse object { id, created_at, hostname, 3 more } 

id: string

Target identifier

formatuuid

maxLength36

created_at: string

Date and time at which the target was created

formatdate-time

hostname: string

A non-unique field that refers to a target

ip: object { ipv4, ipv6 } 

The IPv4/IPv6 address that identifies where to reach a target

ipv4: optional object { ip_addr, virtual_network_id } 

The target’s IPv4 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

ipv6: optional object { ip_addr, virtual_network_id } 

The target’s IPv6 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

modified_at: string

Date and time at which the target was modified

formatdate-time

tags: optional map[string]

Tags assigned to the target. Empty when no tags are assigned.

TargetBulkUpdateResponse object { id, created_at, hostname, 3 more } 

id: string

Target identifier

formatuuid

maxLength36

created_at: string

Date and time at which the target was created

formatdate-time

hostname: string

A non-unique field that refers to a target

ip: object { ipv4, ipv6 } 

The IPv4/IPv6 address that identifies where to reach a target

ipv4: optional object { ip_addr, virtual_network_id } 

The target’s IPv4 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

ipv6: optional object { ip_addr, virtual_network_id } 

The target’s IPv6 address

ip_addr: optional string

IP address of the target

virtual_network_id: optional string

(optional) Private virtual network identifier for the target. If omitted, the default virtual network ID will be used.

formatuuid

modified_at: string

Date and time at which the target was modified

formatdate-time

tags: optional map[string]

Tags assigned to the target. Empty when no tags are assigned.

[ Previous

* * *

Infrastructure ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure)[ Next

* * *

Applications ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications)
