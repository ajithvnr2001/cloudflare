---
url: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/
title: Fetch summary of transcripts for a session | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:47.025344+00:00
---

# Fetch summary of transcripts for a session | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/

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

# Fetch summary of transcripts for a session

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

Returns a Summary URL to download the Summary of Transcripts for the session ID as plain text.

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

data: optional object { sessionId, summaryDownloadUrl, summaryDownloadUrlExpiry } 

sessionId: string

summaryDownloadUrl: string

URL where the summary of transcripts can be downloaded

summaryDownloadUrlExpiry: string

Time of Expiry before when you need to download the csv file.

success: optional boolean

### Fetch summary of transcripts for a session

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
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "data": {
        "sessionId": "sessionId",
        "summaryDownloadUrl": "summaryDownloadUrl",
        "summaryDownloadUrlExpiry": "summaryDownloadUrlExpiry"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "data": {
        "sessionId": "sessionId",
        "summaryDownloadUrl": "summaryDownloadUrl",
        "summaryDownloadUrlExpiry": "summaryDownloadUrlExpiry"
      },
      "success": true
    }
