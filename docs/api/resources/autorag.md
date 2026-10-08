---
url: https://developers.cloudflare.com/api/resources/autorag/
title: AutoRAG | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:04.144943+00:00
---

# AutoRAG | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/autorag/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# AutoRAG

##### [AI Search](https://developers.cloudflare.com/api/resources/autorag/methods/ai_search)

Deprecated

POST/accounts/{account_id}/autorag/rags/{id}/ai-search

##### [Search](https://developers.cloudflare.com/api/resources/autorag/methods/search)

Deprecated

POST/accounts/{account_id}/autorag/rags/{id}/search

##### [Sync](https://developers.cloudflare.com/api/resources/autorag/methods/sync)

Deprecated

PATCH/accounts/{account_id}/autorag/rags/{id}/sync

##### [Files](https://developers.cloudflare.com/api/resources/autorag/methods/files)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/files

##### ModelsExpand Collapse 

AutoRAGAISearchResponse object { response, search_query, data, 3 more } 

response: string

search_query: string

data: optional array of object { score, attributes, content, 2 more } 

score: number

attributes: optional unknown

content: optional array of object { text, type } 

text: optional string

type: optional string

file_id: optional string

filename: optional string

has_more: optional boolean

next_page: optional string

object: optional string

AutoRAGSearchResponse object { search_query, data, has_more, 2 more } 

search_query: string

data: optional array of object { score, attributes, content, 2 more } 

score: number

attributes: optional unknown

content: optional array of object { text, type } 

text: optional string

type: optional string

file_id: optional string

filename: optional string

has_more: optional boolean

next_page: optional string

object: optional string

AutoRAGSyncResponse object { job_id } 

job_id: string

AutoRAGFilesResponse = array of object { error, key } 

error: string

key: string

#### AutoRAGJobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/list)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/get)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/logs)

Deprecated

GET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}/logs

##### ModelsExpand Collapse 

JobListResponse object { id, source, end_reason, 3 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobGetResponse object { id, source, end_reason, 3 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobLogsResponse = array of object { id, created_at, message, message_type } 

id: number

created_at: number

message: string

message_type: number

[ Previous

* * *

Versions ](https://developers.cloudflare.com/api/resources/workflows/subresources/versions)[ Next

* * *

Jobs ](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs)
