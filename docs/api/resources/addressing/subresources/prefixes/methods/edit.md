---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/edit/
title: Update Prefix Description | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:32.426700+00:00
---

# Update Prefix Description | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/methods/edit/

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

# Update Prefix Description

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}

Modify the description for a prefix owned by the account.

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

`Magic Transit Write``IP Prefixes: Write`

##### Path ParametersExpand Collapse 

account_id: string

Identifier of a Cloudflare account.

maxLength32

prefix_id: string

Identifier of an IP Prefix.

maxLength32

##### Body ParametersJSONExpand Collapse 

description: string

Description of the prefix.

maxLength1000

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

result: optional [Prefix](https://developers.cloudflare.com/api/resources/addressing#\(resource\)%20addressing.prefixes%20%3E%20\(model\)%20prefix%20%3E%20\(schema\)) { id, account_id, advertised, 15 more } 

id: optional string

Identifier of an IP Prefix.

maxLength32

account_id: optional string

Identifier of a Cloudflare account.

maxLength32

Deprecatedadvertised: optional boolean

Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.

Prefix advertisement status to the Internet. This field is only not ‘null’ if on demand is enabled.

Deprecatedadvertised_modified_at: optional string

Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.

Last time the advertisement status was changed. This field is only not ‘null’ if on demand is enabled.

formatdate-time

approved: optional string

Approval state of the prefix (P = pending, V = active).

asn: optional number

Autonomous System Number (ASN) the prefix will be advertised under.

cidr: optional string

IP Prefix in Classless Inter-Domain Routing format.

created_at: optional string

formatdate-time

delegate_loa_creation: optional boolean

Whether Cloudflare is allowed to generate the LOA document on behalf of the prefix owner.

description: optional string

Description of the prefix.

maxLength1000

irr_validation_state: optional string

State of one kind of validation for an IP prefix.

loa_document_id: optional string

Identifier for the uploaded LOA document.

maxLength32

modified_at: optional string

formatdate-time

Deprecatedon_demand_enabled: optional boolean

Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.

Whether advertisement of the prefix to the Internet may be dynamically enabled or disabled.

Deprecatedon_demand_locked: optional boolean

Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.

Whether advertisement status of the prefix is locked, meaning it cannot be changed.

ownership_validation_state: optional string

State of one kind of validation for an IP prefix.

ownership_validation_token: optional string

Token provided to demonstrate ownership of the prefix.

rpki_validation_state: optional string

State of one kind of validation for an IP prefix.

### Update Prefix Description

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "description": "Internal test prefix"
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
        "id": "2af39739cc4e3b5910c918468bb89828",
        "account_id": "258def64c72dae45f3e4c8516e2111f2",
        "advertised": true,
        "advertised_modified_at": "2014-01-01T05:20:00.12345Z",
        "approved": "P",
        "asn": 13335,
        "cidr": "192.0.2.0/24",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "delegate_loa_creation": true,
        "description": "Internal test prefix",
        "irr_validation_state": "pending",
        "loa_document_id": "d933b1530bc56c9953cf8ce166da8004",
        "modified_at": "2014-01-01T05:20:00.12345Z",
        "on_demand_enabled": true,
        "on_demand_locked": false,
        "ownership_validation_state": "pending",
        "ownership_validation_token": "1234a5b6-1234-1abc-12a3-1234a5b6789c",
        "rpki_validation_state": "pending"
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
        "id": "2af39739cc4e3b5910c918468bb89828",
        "account_id": "258def64c72dae45f3e4c8516e2111f2",
        "advertised": true,
        "advertised_modified_at": "2014-01-01T05:20:00.12345Z",
        "approved": "P",
        "asn": 13335,
        "cidr": "192.0.2.0/24",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "delegate_loa_creation": true,
        "description": "Internal test prefix",
        "irr_validation_state": "pending",
        "loa_document_id": "d933b1530bc56c9953cf8ce166da8004",
        "modified_at": "2014-01-01T05:20:00.12345Z",
        "on_demand_enabled": true,
        "on_demand_locked": false,
        "ownership_validation_state": "pending",
        "ownership_validation_token": "1234a5b6-1234-1abc-12a3-1234a5b6789c",
        "rpki_validation_state": "pending"
      }
    }
