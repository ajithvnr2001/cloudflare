---
url: https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/list/
title: List Vectorize Indexes | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:13.775683+00:00
---

# List Vectorize Indexes | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Vectorize](https://developers.cloudflare.com/api/resources/vectorize)

[Indexes](https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Vectorize Indexes

GET/accounts/{account_id}/vectorize/v2/indexes

Returns a list of Vectorize Indexes

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

`Vectorize Write``Vectorize Read`

##### Path ParametersExpand Collapse 

account_id: string

Identifier

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

result: array of [CreateIndex](https://developers.cloudflare.com/api/resources/vectorize#\(resource\)%20vectorize.indexes%20%3E%20\(model\)%20create_index%20%3E%20\(schema\)) { config, created_on, description, 2 more } 

config: optional object { dimensions, metric, preset } 

dimensions: number

Specifies the number of dimensions for the index

maximum1536

minimum1

metric: "cosine" or "euclidean" or "dot-product"

Specifies the type of metric to use calculating distance.

One of the following:

"cosine"

"euclidean"

"dot-product"

preset: optional "@cf/baai/bge-small-en-v1.5" or "@cf/baai/bge-base-en-v1.5" or "@cf/baai/bge-large-en-v1.5" or 2 more

Specifies the preset to use for the index.

One of the following:

"@cf/baai/bge-small-en-v1.5"

"@cf/baai/bge-base-en-v1.5"

"@cf/baai/bge-large-en-v1.5"

"openai/text-embedding-ada-002"

"cohere/embed-multilingual-v2.0"

created_on: optional string

Specifies the timestamp the resource was created as an ISO8601 string.

formatdate-time

description: optional string

Specifies the description of the index.

modified_on: optional string

Specifies the timestamp the resource was modified as an ISO8601 string.

formatdate-time

name: optional string

success: true

Whether the API call was successful

### List Vectorize Indexes

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/vectorize/v2/indexes \
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
      "result": [
        {
          "config": {
            "dimensions": 768,
            "metric": "cosine",
            "preset": "@cf/baai/bge-small-en-v1.5"
          },
          "created_on": "2022-11-15T18:25:44.442097Z",
          "description": "This is my example index.",
          "modified_on": "2022-11-15T18:25:44.442097Z",
          "name": "example-index"
        }
      ],
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
      "result": [
        {
          "config": {
            "dimensions": 768,
            "metric": "cosine",
            "preset": "@cf/baai/bge-small-en-v1.5"
          },
          "created_on": "2022-11-15T18:25:44.442097Z",
          "description": "This is my example index.",
          "modified_on": "2022-11-15T18:25:44.442097Z",
          "name": "example-index"
        }
      ],
      "success": true
    }
