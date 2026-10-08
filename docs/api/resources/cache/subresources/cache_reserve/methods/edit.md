---
url: https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/edit/
title: Change Cache Reserve setting | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:42.007045+00:00
---

# Change Cache Reserve setting | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/edit/

[API Reference](https://developers.cloudflare.com/api)

[Cache](https://developers.cloudflare.com/api/resources/cache)

[Cache Reserve](https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Change Cache Reserve setting

PATCH/zones/{zone_id}/cache/cache_reserve

Increase cache lifetimes by automatically storing all cacheable files into Cloudflare’s persistent object storage buckets. Requires Cache Reserve subscription. Note: using Tiered Cache with Cache Reserve is highly recommended to reduce Reserve operations costs. See the [developer docs](https://developers.cloudflare.com/cache/about/cache-reserve) for more information.

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

`Zone Settings Write``Zone Write`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

##### Body ParametersJSONExpand Collapse 

value: "on" or "off"

Value of the Cache Reserve zone setting.

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

success: true

Whether the API call was successful.

result: optional object { id, editable, value, modified_on } 

id: [CacheReserve](https://developers.cloudflare.com/api/resources/cache#\(resource\)%20cache.cache_reserve%20%3E%20\(model\)%20cache_reserve%20%3E%20\(schema\))

The identifier of the caching setting.

editable: boolean

Whether the setting is editable.

value: "on" or "off"

Value of the Cache Reserve zone setting.

One of the following:

"on"

"off"

modified_on: optional string

Last time this setting was modified.

formatdate-time

### Change Cache Reserve setting

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve \
        -X PATCH \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "value": "on"
            }'

200 example

4XX example
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "editable": true,
        "id": "cache_reserve",
        "value": "on"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1153,
          "message": "Cache Reserve cannot be enabled because a deletion is already in progress."
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }

##### Returns Examples

200 example

4XX example
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "editable": true,
        "id": "cache_reserve",
        "value": "on"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1153,
          "message": "Cache Reserve cannot be enabled because a deletion is already in progress."
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }
