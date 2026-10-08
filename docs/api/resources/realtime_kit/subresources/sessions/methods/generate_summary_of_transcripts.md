---
url: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/
title: Generate summary of Transcripts for the session | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:47.899436+00:00
---

# Generate summary of Transcripts for the session | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/

[API Reference](https://developers.cloudflare.com/api)

[Realtime Kit](https://developers.cloudflare.com/api/resources/realtime_kit)

[Sessions](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Generate summary of Transcripts for the session

POST/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

Trigger Summary generation of Transcripts for the session ID.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

##### Accepted Permissions (at least one required)

`Realtime Admin``Realtime`

##### Path ParametersExpand Collapse 

account_id: string

The account identifier tag.

maxLength32

app_id: string

The app identifier tag.

session_id: string

formatuuid

##### ReturnsExpand Collapse 

data: optional object { session_id, status } 

session_id: optional string

formatuuid

status: optional string

success: optional boolean

### Generate summary of Transcripts for the session

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary \
        -X POST \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "data": {
        "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "status": "status"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "data": {
        "session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "status": "status"
      },
      "success": true
    }
