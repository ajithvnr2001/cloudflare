---
url: https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/get/
title: Get Tiered Caching setting | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:56.244140+00:00
---

# Get Tiered Caching setting | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching/methods/get/

[API Reference](https://developers.cloudflare.com/api)

[Argo](https://developers.cloudflare.com/api/resources/argo)

[Tiered Caching](https://developers.cloudflare.com/api/resources/argo/subresources/tiered_caching)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get Tiered Caching setting

GET/zones/{zone_id}/argo/tiered_caching

Tiered Cache works by dividing Cloudflare’s data centers into a hierarchy of lower-tiers and upper-tiers. If content is not cached in lower-tier data centers (generally the ones closest to a visitor), the lower-tier must ask an upper-tier to see if it has the content. If the upper-tier does not have the content, only the upper-tier can ask the origin for content. This practice improves bandwidth efficiency by limiting the number of data centers that can ask the origin for content, which reduces origin load and makes websites more cost-effective to operate. Additionally, Tiered Cache concentrates connections to origin servers so they come from a small number of data centers rather than the full set of network locations. This results in fewer open connections using server resources.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

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

success: true

Whether the API call was successful.

result: optional object { id, editable, value, modified_on } 

id: "tiered_caching"

The identifier of the caching setting.

editable: boolean

Whether the setting is editable.

value: "on" or "off"

Value of the Tiered Cache zone setting.

One of the following:

"on"

"off"

modified_on: optional string

Last time this setting was modified.

formatdate-time

### Get Tiered Caching setting

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/argo/tiered_caching \
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
      "result": {
        "id": "tiered_caching",
        "editable": true,
        "value": "on",
        "modified_on": "2014-01-01T05:20:00.12345Z"
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
        "id": "tiered_caching",
        "editable": true,
        "value": "on",
        "modified_on": "2014-01-01T05:20:00.12345Z"
      }
    }
