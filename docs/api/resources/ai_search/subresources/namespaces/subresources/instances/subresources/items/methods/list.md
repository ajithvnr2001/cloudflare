---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list/
title: Items List. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:57.007381+00:00
---

# Items List. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list/

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

# Items List.

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

Lists indexed items in an AI Search instance.

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

##### Query ParametersExpand Collapse 

item_id: optional string

Filter items by their unique ID. Returns at most one item.

maxLength64

key: optional string

Filter items by their exact key (object key / filename). Keys are unique per source, so combine with `source` to disambiguate across data sources.

maxLength1024

metadata_filter: optional string

JSON-encoded metadata filter using Vectorize filter syntax. Examples: {“folder”:“reports/”}, {“timestamp”:{“$gte”:1700000000000}}, {“folder”:{“$in”:[“docs/”,“reports/”]}}

maxLength2048

page: optional number

minimum1

per_page: optional number

maximum50

minimum0

search: optional string

maxLength256

sort_by: optional "status" or "modified_at"

Sort order for items. “status” (default) sorts by status priority then last_seen_at. “modified_at” sorts by file modification time (most recent first), falling back to created_at.

One of the following:

"status"

"modified_at"

source: optional string

Filter items by source_id. Use “builtin” for uploaded files, or a source identifier like “web-crawler:<https://example.com>”.

maxLength512

status: optional "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

##### ReturnsExpand Collapse 

result: array of object { id, checksum, chunks_count, 10 more } 

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

result_info: object { count, page, total_count, per_page } 

count: number

page: number

total_count: number

per_page: optional number

maximum50

minimum5

success: boolean

### Items List.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/items \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": [
        {
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
        }
      ],
      "result_info": {
        "count": 0,
        "page": 0,
        "total_count": 0,
        "per_page": 5
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": [
        {
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
        }
      ],
      "result_info": {
        "count": 0,
        "page": 0,
        "total_count": 0,
        "per_page": 5
      },
      "success": true
    }
