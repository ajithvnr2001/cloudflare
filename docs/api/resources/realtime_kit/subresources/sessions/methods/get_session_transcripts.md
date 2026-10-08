---
url: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/
title: Fetch the complete transcript for a session | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:46.158142+00:00
---

# Fetch the complete transcript for a session | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/

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

# Fetch the complete transcript for a session

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript

Returns a URL to download the transcript for the session ID in CSV format.

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

##### Query ParametersExpand Collapse 

format: optional "SRT" or "VTT" or "JSON" or "CSV"

Transcript file format to fetch.

One of the following:

"SRT"

"VTT"

"JSON"

"CSV"

##### ReturnsExpand Collapse 

data: optional object { sessionId, transcript_download_url, transcript_download_url_expiry } 

sessionId: string

transcript_download_url: string

URL where the transcript can be downloaded

transcript_download_url_expiry: string

Time when the download URL will expire

success: optional boolean

### Fetch the complete transcript for a session

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "data": {
        "sessionId": "sessionId",
        "transcript_download_url": "transcript_download_url",
        "transcript_download_url_expiry": "transcript_download_url_expiry"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "data": {
        "sessionId": "sessionId",
        "transcript_download_url": "transcript_download_url",
        "transcript_download_url_expiry": "transcript_download_url_expiry"
      },
      "success": true
    }
