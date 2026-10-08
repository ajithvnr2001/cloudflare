---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/create/
title: Create a token | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:07.934463+00:00
---

# Create a token | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Tokens](https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Create a token

POST/accounts/{account_id}/ai-search/tokens

Create a stored Cloudflare credential for an AI Search instance to access its data source.

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

##### Body ParametersJSONExpand Collapse 

cf_api_id: string

cf_api_key: string

name: string

legacy: optional boolean

##### ReturnsExpand Collapse 

result: object { id, cf_api_id, created_at, 6 more } 

id: string

formatuuid

cf_api_id: string

created_at: string

formatdate-time

modified_at: string

formatdate-time

name: string

created_by: optional string

enabled: optional boolean

legacy: optional boolean

modified_by: optional string

success: true

### Create a token

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/tokens \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "cf_api_id": "a1b2c3d4e5f6",
              "cf_api_key": "abc123",
              "name": "my-token"
            }'

200 example
    
    
    {
      "result": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "cf_api_id": "cf_api_id",
        "created_at": "2019-12-27T18:11:19.117Z",
        "modified_at": "2019-12-27T18:11:19.117Z",
        "name": "name",
        "created_by": "created_by",
        "enabled": true,
        "legacy": true,
        "modified_by": "modified_by"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "cf_api_id": "cf_api_id",
        "created_at": "2019-12-27T18:11:19.117Z",
        "modified_at": "2019-12-27T18:11:19.117Z",
        "name": "name",
        "created_by": "created_by",
        "enabled": true,
        "legacy": true,
        "modified_by": "modified_by"
      },
      "success": true
    }
