---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/
title: Update Prefix Dynamic Advertisement Status | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:26.340305+00:00
---

# Update Prefix Dynamic Advertisement Status | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Prefixes](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes)

[Advertisement Status](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/advertisement_status)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update Prefix Dynamic Advertisement Status

Deprecated

PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status

Advertise or withdraw the BGP route for a prefix.

**Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing subnets of an IP prefix.

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

##### Body ParametersJSONExpand Collapse 

advertised: boolean

Advertisement status of the prefix. If `true`, the BGP route for the prefix is advertised to the Internet. If `false`, the BGP route is withdrawn.

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

result: optional object { advertised, advertised_modified_at } 

advertised: optional boolean

Advertisement status of the prefix. If `true`, the BGP route for the prefix is advertised to the Internet. If `false`, the BGP route is withdrawn.

advertised_modified_at: optional string

Last time the advertisement status was changed. This field is only not ‘null’ if on demand is enabled.

formatdate-time

### Update Prefix Dynamic Advertisement Status

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/addressing/prefixes/$PREFIX_ID/bgp/status \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "advertised": true
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
        "advertised": true,
        "advertised_modified_at": "2014-01-01T05:20:00.12345Z"
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
        "advertised": true,
        "advertised_modified_at": "2014-01-01T05:20:00.12345Z"
      }
    }
