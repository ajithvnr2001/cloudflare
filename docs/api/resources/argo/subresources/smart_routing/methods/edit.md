---
url: https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/edit/
title: Patch Argo Smart Routing setting | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:02.376707+00:00
---

# Patch Argo Smart Routing setting | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/methods/edit/

[API Reference](https://developers.cloudflare.com/api)

[Argo](https://developers.cloudflare.com/api/resources/argo)

[Smart Routing](https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Patch Argo Smart Routing setting

PATCH/zones/{zone_id}/argo/smart_routing

Configures the value of the Argo Smart Routing enablement setting.

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

`Zone Settings Write`

##### Path ParametersExpand Collapse 

zone_id: string

Specifies the zone associated with the API call.

maxLength32

##### Body ParametersJSONExpand Collapse 

value: "on" or "off"

Specifies the enablement value of Argo Smart Routing.

One of the following:

"on"

"off"

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

result: object { id, editable, value, modified_on } 

id: string

Specifies the identifier of the Argo Smart Routing setting.

editable: boolean

Specifies if the setting is editable.

value: "on" or "off"

Specifies the enablement value of Argo Smart Routing.

One of the following:

"on"

"off"

modified_on: optional string

Specifies the time when the setting was last modified.

formatdate-time

success: true

Describes a successful API response.

### Patch Argo Smart Routing setting

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/argo/smart_routing \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "value": "on"
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
      "result": {
        "id": "id",
        "editable": true,
        "value": "on",
        "modified_on": "2019-12-27T18:11:19.117Z"
      },
      "success": true
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
      "result": {
        "id": "id",
        "editable": true,
        "value": "on",
        "modified_on": "2019-12-27T18:11:19.117Z"
      },
      "success": true
    }
