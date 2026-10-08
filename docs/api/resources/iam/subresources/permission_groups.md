---
url: https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/
title: Permission Groups | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:23.953384+00:00
---

# Permission Groups | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/

[API Reference](https://developers.cloudflare.com/api)

[IAM](https://developers.cloudflare.com/api/resources/iam)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Permission Groups

##### [List Account Permission Groups](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/methods/list)

GET/accounts/{account_id}/iam/permission_groups

##### [Permission Group Details](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/methods/get)

GET/accounts/{account_id}/iam/permission_groups/{permission_group_id}

##### ModelsExpand Collapse 

PermissionGroupListResponse object { id, meta, name } 

A named group of permissions that map to a group of operations against resources.

id: string

Identifier of the permission group.

meta: optional object { category, deprecated, description, 5 more } 

Attributes associated to the permission group.

category: optional string

A category used to group permission groups.

deprecated: optional string

Indicates whether the permission group is deprecated.

description: optional string

Additional information about the permission group.

editable: optional string

Indicates whether the permission group can be edited.

eol_at: optional string

The planned end-of-life date and time, when provided.

formatdate-time

label: optional string

A label identifying the permission group.

scopes: optional string

The scope associated with the permission group.

visibility: optional string

Indicates the permission group’s availability or visibility.

name: optional string

Name of the permission group.

PermissionGroupGetResponse object { id, meta, name } 

A named group of permissions that map to a group of operations against resources.

id: string

Identifier of the permission group.

meta: optional object { category, deprecated, description, 5 more } 

Attributes associated to the permission group.

category: optional string

A category used to group permission groups.

deprecated: optional string

Indicates whether the permission group is deprecated.

description: optional string

Additional information about the permission group.

editable: optional string

Indicates whether the permission group can be edited.

eol_at: optional string

The planned end-of-life date and time, when provided.

formatdate-time

label: optional string

A label identifying the permission group.

scopes: optional string

The scope associated with the permission group.

visibility: optional string

Indicates the permission group’s availability or visibility.

name: optional string

Name of the permission group.

[ Previous

* * *

IAM ](https://developers.cloudflare.com/api/resources/iam)[ Next

* * *

Resource Groups ](https://developers.cloudflare.com/api/resources/iam/subresources/resource_groups)
