---
url: https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/clear/
title: Start Cache Reserve Clear | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:41.133773+00:00
---

# Start Cache Reserve Clear | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/cache/subresources/cache_reserve/methods/clear/

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

# Start Cache Reserve Clear

POST/zones/{zone_id}/cache/cache_reserve_clear

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

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

result: optional object { id, start_ts, state, 2 more } 

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

id: [CacheReserveClear](https://developers.cloudflare.com/api/resources/cache#\(resource\)%20cache.cache_reserve%20%3E%20\(model\)%20cache_reserve_clear%20%3E%20\(schema\))

ID of the zone setting.

start_ts: string

The time that the latest Cache Reserve Clear operation started.

formatdate-time

state: "In-progress" or "Completed"

The current state of the Cache Reserve Clear operation.

One of the following:

"In-progress"

"Completed"

end_ts: optional string

The time that the latest Cache Reserve Clear operation completed.

formatdate-time

modified_on: optional string

Last time this setting was modified.

formatdate-time

### Start Cache Reserve Clear

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve_clear \
        -X POST \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example

4XX example
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "id": "cache_reserve_clear",
        "start_ts": "2023-10-02T10:00:00.12345Z",
        "state": "In-progress"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1152,
          "message": "Turn off Cache Reserve sync to proceed with deletion."
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
        "id": "cache_reserve_clear",
        "start_ts": "2023-10-02T10:00:00.12345Z",
        "state": "In-progress"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1152,
          "message": "Turn off Cache Reserve sync to proceed with deletion."
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }
