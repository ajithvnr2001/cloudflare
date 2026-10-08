---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create/
title: Create new job | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:50.317991+00:00
---

# Create new job | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces)

[Instances](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)

[Jobs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Create new job

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

Creates a new indexing job for an AI Search instance.

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

##### Body ParametersJSONExpand Collapse 

description: optional string

maxLength255

##### ReturnsExpand Collapse 

result: object { id, source, description, 4 more } 

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

success: boolean

### Create new job

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/jobs \
        -X POST \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": {
        "id": "id",
        "source": "user",
        "description": "description",
        "end_reason": "end_reason",
        "ended_at": "ended_at",
        "last_seen_at": "last_seen_at",
        "started_at": "started_at"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "id": "id",
        "source": "user",
        "description": "description",
        "end_reason": "end_reason",
        "ended_at": "ended_at",
        "last_seen_at": "last_seen_at",
        "started_at": "started_at"
      },
      "success": true
    }
