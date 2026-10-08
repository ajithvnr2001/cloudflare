---
url: https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list/
title: List Tokens | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:28.856730+00:00
---

# List Tokens | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[User](https://developers.cloudflare.com/api/resources/user)

[Tokens](https://developers.cloudflare.com/api/resources/user/subresources/tokens)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Tokens

GET/user/tokens

List all access tokens you created. Results include active, disabled, and recently-expired tokens when include_expired is set to true.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

##### Accepted Permissions (at least one required)

`API Tokens Write``API Tokens Read`

##### Query ParametersExpand Collapse 

direction: optional "asc" or "desc"

Direction to order results.

One of the following:

"asc"

"desc"

include_expired: optional boolean

When true, includes recently-expired tokens in the response.

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Maximum number of results per page.

maximum50

minimum5

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

result: optional array of [Token](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20token%20%3E%20\(schema\)) { id, condition, creator_email_at_creation, 10 more } 

id: optional string

Token identifier tag.

maxLength32

condition: optional object { request_ip } 

request_ip: optional object { in, not_in } 

Client IP restrictions.

in: optional array of [TokenConditionCIDRList](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20token_condition_cidr_list%20%3E%20\(schema\))

List of IPv4/IPv6 CIDR addresses.

not_in: optional array of [TokenConditionCIDRList](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20token_condition_cidr_list%20%3E%20\(schema\))

List of IPv4/IPv6 CIDR addresses.

creator_email_at_creation: optional string

The email address of the user who created the token at the time of creation. Only present for Account Owned API Tokens when a creator email was available.

maxLength90

expires_on: optional string

The expiration time on or after which the JWT MUST NOT be accepted for processing.

formatdate-time

issued_on: optional string

The time on which the token was created.

formatdate-time

last_used_on: optional string

Last time the token was used.

formatdate-time

modified_on: optional string

Last time the token was modified.

formatdate-time

name: optional string

Token name.

maxLength120

not_before: optional string

The time before which the token MUST NOT be accepted for processing.

formatdate-time

policies: optional array of [TokenPolicy](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20token_policy%20%3E%20\(schema\)) { id, effect, permission_groups, resources } 

List of access policies assigned to the token.

id: string

Policy identifier.

effect: "allow" or "deny"

Allow or deny operations against the resources.

One of the following:

"allow"

"deny"

permission_groups: array of object { id, meta, name } 

A set of permission groups that are specified to the policy.

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

resources: map[string] or map[map[string]]

A list of resource names that the policy applies to.

One of the following:

IAMResourcesTypeObjectString = map[string]

Map of simple string resource permissions

IAMResourcesTypeObjectNested = map[map[string]]

Map of nested resource permissions

provisioner_id: optional string

The identifier of the service that provisioned the token. For an OAuth-provisioned token, this is the OAuth client identifier. Present when `provisioner_type` is present and null when the identifier is unavailable.

provisioner_type: optional string

The type of service that provisioned the token. Only present for provisioned Account Owned API Tokens.

status: optional "active" or "disabled" or "expired"

Status of the token.

One of the following:

"active"

"disabled"

"expired"

result_info: optional object { count, page, per_page, total_count } 

count: optional number

Total number of results for the requested service

page: optional number

Current page within paginated list of results

per_page: optional number

Number of results per page of results

total_count: optional number

Total results available without any search parameters

### List Tokens

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
    
    
    curl https://api.cloudflare.com/client/v4/user/tokens \
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
      "success": true,
      "result": [
        {
          "id": "ed17574386854bf78a67040be0a770b0",
          "condition": {
            "request_ip": {
              "in": [
                "123.123.123.0/24",
                "2606:4700::/32"
              ],
              "not_in": [
                "123.123.123.100/24",
                "2606:4700:4700::/48"
              ]
            }
          },
          "creator_email_at_creation": "user@example.com",
          "expires_on": "2020-01-01T00:00:00Z",
          "issued_on": "2018-07-01T05:20:00Z",
          "last_used_on": "2020-01-02T12:34:00Z",
          "modified_on": "2018-07-02T05:20:00Z",
          "name": "readonly token",
          "not_before": "2018-07-01T05:20:00Z",
          "policies": [
            {
              "id": "f267e341f3dd4697bd3b9f71dd96247f",
              "effect": "allow",
              "permission_groups": [
                {
                  "id": "c8fed203ed3043cba015a93ad1616f1f",
                  "meta": {
                    "category": "category",
                    "deprecated": "deprecated",
                    "description": "description",
                    "editable": "editable",
                    "eol_at": "2019-12-27T18:11:19.117Z",
                    "label": "load_balancer_admin",
                    "scopes": "com.cloudflare.api.account",
                    "visibility": "visibility"
                  },
                  "name": "Zone Read"
                },
                {
                  "id": "82e64a83756745bbbb1c9c2701bf816b",
                  "meta": {
                    "category": "category",
                    "deprecated": "deprecated",
                    "description": "description",
                    "editable": "editable",
                    "eol_at": "2019-12-27T18:11:19.117Z",
                    "label": "fbm_user",
                    "scopes": "com.cloudflare.api.account",
                    "visibility": "visibility"
                  },
                  "name": "Magic Network Monitoring"
                }
              ],
              "resources": {
                "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*"
              }
            }
          ],
          "provisioner_id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
          "provisioner_type": "com.cloudflare.api.oauthtoken",
          "status": "active"
        }
      ],
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
      "success": true,
      "result": [
        {
          "id": "ed17574386854bf78a67040be0a770b0",
          "condition": {
            "request_ip": {
              "in": [
                "123.123.123.0/24",
                "2606:4700::/32"
              ],
              "not_in": [
                "123.123.123.100/24",
                "2606:4700:4700::/48"
              ]
            }
          },
          "creator_email_at_creation": "user@example.com",
          "expires_on": "2020-01-01T00:00:00Z",
          "issued_on": "2018-07-01T05:20:00Z",
          "last_used_on": "2020-01-02T12:34:00Z",
          "modified_on": "2018-07-02T05:20:00Z",
          "name": "readonly token",
          "not_before": "2018-07-01T05:20:00Z",
          "policies": [
            {
              "id": "f267e341f3dd4697bd3b9f71dd96247f",
              "effect": "allow",
              "permission_groups": [
                {
                  "id": "c8fed203ed3043cba015a93ad1616f1f",
                  "meta": {
                    "category": "category",
                    "deprecated": "deprecated",
                    "description": "description",
                    "editable": "editable",
                    "eol_at": "2019-12-27T18:11:19.117Z",
                    "label": "load_balancer_admin",
                    "scopes": "com.cloudflare.api.account",
                    "visibility": "visibility"
                  },
                  "name": "Zone Read"
                },
                {
                  "id": "82e64a83756745bbbb1c9c2701bf816b",
                  "meta": {
                    "category": "category",
                    "deprecated": "deprecated",
                    "description": "description",
                    "editable": "editable",
                    "eol_at": "2019-12-27T18:11:19.117Z",
                    "label": "fbm_user",
                    "scopes": "com.cloudflare.api.account",
                    "visibility": "visibility"
                  },
                  "name": "Magic Network Monitoring"
                }
              ],
              "resources": {
                "com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43": "*"
              }
            }
          ],
          "provisioner_id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
          "provisioner_type": "com.cloudflare.api.oauthtoken",
          "status": "active"
        }
      ],
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }
