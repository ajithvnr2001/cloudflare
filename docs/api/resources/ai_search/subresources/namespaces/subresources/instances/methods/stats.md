---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats/
title: Get instance statistics. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:46.872882+00:00
---

# Get instance statistics. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces)

[Instances](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get instance statistics.

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/stats

Retrieve usage and indexing statistics for an AI Search instance.

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

account_id: string

name: string

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

##### ReturnsExpand Collapse 

result: object { completed, degraded, engine, 8 more } 

completed: optional number

degraded: optional boolean

True when status counts are unavailable (e.g. legacy stats query exceeded D1 statement-size limit). Counts are omitted in this case.

engine: optional object { r2, vectorize } 

Engine-specific metadata. Present only for managed (v3) instances.

r2: optional object { metadataSizeBytes, objectCount, payloadSizeBytes } 

R2 bucket storage usage in bytes.

metadataSizeBytes: number

objectCount: number

payloadSizeBytes: number

vectorize: optional object { dimensions, vectorsCount } 

Vectorize index metadata (dimensions, vector count).

dimensions: number

vectorsCount: number

error: optional number

file_embed_errors: optional map[unknown]

index_source_errors: optional map[unknown]

last_activity: optional string

formatdate-time

outdated: optional number

queued: optional number

running: optional number

skipped: optional number

success: boolean

### Get instance statistics.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/stats \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "completed": 0,
        "degraded": true,
        "engine": {
          "r2": {
            "metadataSizeBytes": 0,
            "objectCount": 0,
            "payloadSizeBytes": 0
          },
          "vectorize": {
            "dimensions": 0,
            "vectorsCount": 0
          }
        },
        "error": 0,
        "file_embed_errors": {
          "foo": "bar"
        },
        "index_source_errors": {
          "foo": "bar"
        },
        "last_activity": "2019-12-27T18:11:19.117Z",
        "outdated": 0,
        "queued": 0,
        "running": 0,
        "skipped": 0
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "completed": 0,
        "degraded": true,
        "engine": {
          "r2": {
            "metadataSizeBytes": 0,
            "objectCount": 0,
            "payloadSizeBytes": 0
          },
          "vectorize": {
            "dimensions": 0,
            "vectorsCount": 0
          }
        },
        "error": 0,
        "file_embed_errors": {
          "foo": "bar"
        },
        "index_source_errors": {
          "foo": "bar"
        },
        "last_activity": "2019-12-27T18:11:19.117Z",
        "outdated": 0,
        "queued": 0,
        "running": 0,
        "skipped": 0
      },
      "success": true
    }
