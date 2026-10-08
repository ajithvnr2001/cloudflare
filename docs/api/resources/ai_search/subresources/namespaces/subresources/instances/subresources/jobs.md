---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/
title: Jobs | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:48.689804+00:00
---

# Jobs | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/

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

# Jobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Create new job](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [Cancel an indexing job.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/update)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs

##### ModelsExpand Collapse 

JobListResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobCreateResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobGetResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobUpdateResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

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

Instances ](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)[ Next

* * *

Items ](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items)
