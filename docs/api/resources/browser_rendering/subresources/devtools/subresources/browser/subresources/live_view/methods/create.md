---
url: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create/
title: Mint live view URLs for a browser session | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:42.931132+00:00
---

# Mint live view URLs for a browser session | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

[Devtools](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools)

[Browser](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser)

[Live View](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Mint live view URLs for a browser session

POST/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/live_view

Generates time-limited URLs to view a remote browser session. Set `guardrails: { mode: 'readonly' }` to create a view-only link.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`Browser Rendering Write`

##### Path ParametersExpand Collapse 

account_id: string

Account ID.

session_id: string

Browser session ID

formatuuid

##### Body ParametersJSONExpand Collapse 

expiresInMs: optional number

How long the live view URLs remain valid, in milliseconds. Default: 5 minutes. Max: 60 minutes.

maximum3600000

minimum60000

guardrails: optional object { mode } 

Connection guardrails. Use `{ mode: 'readonly' }` to generate a view-only link.

mode: "readonly"

mode: optional "devtools" or "tab" or "full"

UI mode: ‘devtools’ (Chrome DevTools), ‘tab’ (single tab view), ‘full’ (multi-tab browser)

One of the following:

"devtools"

"tab"

"full"

targetId: optional string

Target ID (page) to connect to. If omitted, auto-resolves to the first active page.

##### ReturnsExpand Collapse 

id: string

Target ID

devtoolsFrontendUrl: string

URL to open the live view in a browser

formaturi

options: object { mode, guardrails } 

mode: "devtools" or "tab" or "full"

UI mode for the live view

One of the following:

"devtools"

"tab"

"full"

guardrails: optional object { mode } 

Connection guardrails applied to this link

mode: "readonly"

webSocketDebuggerUrl: string

WebSocket URL for CDP connection

formaturi

### Mint live view URLs for a browser session

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser/$SESSION_ID/live_view \
        -X POST \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "id": "id",
      "devtoolsFrontendUrl": "https://example.com",
      "options": {
        "mode": "devtools",
        "guardrails": {
          "mode": "readonly"
        }
      },
      "webSocketDebuggerUrl": "https://example.com"
    }

##### Returns Examples

200 example
    
    
    {
      "id": "id",
      "devtoolsFrontendUrl": "https://example.com",
      "options": {
        "mode": "devtools",
        "guardrails": {
          "mode": "readonly"
        }
      },
      "webSocketDebuggerUrl": "https://example.com"
    }
