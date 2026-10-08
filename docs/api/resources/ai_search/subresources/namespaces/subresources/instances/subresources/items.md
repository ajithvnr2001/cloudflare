---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/
title: Items | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:54.559923+00:00
---

# Items | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/

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

# Items

##### [Items List.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Upload Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Create or Update Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/create_or_update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Get Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Sync Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Delete Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Download Item Content.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download

##### [Item Logs.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs

##### [List Item Chunks.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/chunks)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks

##### ModelsExpand Collapse 

ItemListResponse object { id, checksum, chunks_count, 10 more } 

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

ItemUploadResponse object { id, checksum, chunks_count, 11 more } 

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

warnings: optional array of object { code, expected_type, field }  or object { code, field } 

One of the following:

object { code, expected_type, field } 

code: "custom_metadata_value_not_indexed"

expected_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field: string

maxLength512

object { code, field } 

code: "custom_metadata_field_not_filterable"

field: string

maxLength512

ItemCreateOrUpdateResponse object { id, checksum, chunks_count, 10 more } 

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

ItemGetResponse object { id, checksum, chunks_count, 10 more } 

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

ItemSyncResponse object { id, checksum, chunks_count, 10 more } 

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

ItemDeleteResponse object { key } 

key: string

ItemLogsResponse = array of object { action, chunkCount, errorType, 4 more } 

action: string

chunkCount: number

errorType: string

fileKey: string

message: string

processingTimeMs: number

timestamp: string

formatdate-time

ItemChunksResponse = array of object { id, item, text, 2 more } 

id: string

item: object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

text: string

end_byte: optional number

start_byte: optional number

[ Previous

* * *

Jobs ](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs)[ Next

* * *

Instances ](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances)
