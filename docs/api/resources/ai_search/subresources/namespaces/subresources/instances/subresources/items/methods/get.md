---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get/
title: Get Item. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:58.151532+00:00
---

# Get Item. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces)

[Instances](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)

[Items](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get Item.

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

Retrieves a specific indexed item from an AI Search instance.

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

item_id: string

##### ReturnsExpand Collapse 

result: object { id, checksum, chunks_count, 10 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

success: boolean

### Get Item.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/items/$ITEM_ID \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "id": "id",
        "checksum": "checksum",
        "chunks_count": 0,
        "created_at": "2019-12-27T18:11:19.117Z",
        "file_size": 0,
        "key": "key",
        "last_seen_at": "2019-12-27T18:11:19.117Z",
        "metadata": {
          "foo": "string"
        },
        "namespace": "namespace",
        "next_action": "INDEX",
        "source_id": "source_id",
        "status": "queued",
        "error": "error"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "id": "id",
        "checksum": "checksum",
        "chunks_count": 0,
        "created_at": "2019-12-27T18:11:19.117Z",
        "file_size": 0,
        "key": "key",
        "last_seen_at": "2019-12-27T18:11:19.117Z",
        "metadata": {
          "foo": "string"
        },
        "namespace": "namespace",
        "next_action": "INDEX",
        "source_id": "source_id",
        "status": "queued",
        "error": "error"
      },
      "success": true
    }
