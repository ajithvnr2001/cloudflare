---
url: https://developers.cloudflare.com/api/resources/api_gateway/subresources/schemas/methods/list/
title: Export web and API operations as OpenAPI schemas | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:58.559269+00:00
---

# Export web and API operations as OpenAPI schemas | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/api_gateway/subresources/schemas/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[API Gateway](https://developers.cloudflare.com/api/resources/api_gateway)

[Schemas](https://developers.cloudflare.com/api/resources/api_gateway/subresources/schemas)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Export web and API operations as OpenAPI schemas

GET/zones/{zone_id}/api_gateway/schemas

Returns tracked web and API operations and their feature configuration rendered as OpenAPI schemas.

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

`Account API Gateway``Account API Gateway Read``Domain API Gateway``Domain API Gateway Read`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

##### Query ParametersExpand Collapse 

feature: optional array of "thresholds" or "parameter_schemas" or "schema_info" or "confidence_intervals"

Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.

One of the following:

"thresholds"

"parameter_schemas"

"schema_info"

"confidence_intervals"

host: optional array of string

Receive schema only for the given host(s).

include_schema_kind: optional array of "learned"

Schema kinds to include in exported OpenAPI schemas.

##### ReturnsExpand Collapse 

errors: [Message](https://developers.cloudflare.com/api/resources/api_gateway#\(resource\)%20api_gateway.user_schemas%20%3E%20\(model\)%20message%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: [Message](https://developers.cloudflare.com/api/resources/api_gateway#\(resource\)%20api_gateway.user_schemas%20%3E%20\(model\)%20message%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

result: object { schemas, timestamp } 

schemas: optional array of unknown

timestamp: optional string

success: true

Whether the API call was successful.

### Export web and API operations as OpenAPI schemas

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/api_gateway/schemas \
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
      "result": {
        "schemas": [
          {
            "info": {
              "title": "OpenAPI JSON schema for www.example.com",
              "version": "1.0"
            },
            "openapi": "3.0.0",
            "paths": {
              "... Further paths ...": {},
              "/api/v1/users/{var1}": {
                "get": {
                  "parameters": [
                    {
                      "name": "var1",
                      "in": "path",
                      "required": true,
                      "schema": {
                        "type": "string"
                      }
                    }
                  ]
                }
              }
            },
            "servers": [
              {
                "url": "www.example.com"
              }
            ]
          }
        ],
        "timestamp": "timestamp"
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
        "schemas": [
          {
            "info": {
              "title": "OpenAPI JSON schema for www.example.com",
              "version": "1.0"
            },
            "openapi": "3.0.0",
            "paths": {
              "... Further paths ...": {},
              "/api/v1/users/{var1}": {
                "get": {
                  "parameters": [
                    {
                      "name": "var1",
                      "in": "path",
                      "required": true,
                      "schema": {
                        "type": "string"
                      }
                    }
                  ]
                }
              }
            },
            "servers": [
              {
                "url": "www.example.com"
              }
            ]
          }
        ],
        "timestamp": "timestamp"
      },
      "success": true
    }
