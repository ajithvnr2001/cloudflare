---
url: https://developers.cloudflare.com/browser-run/cdp/session-management/
title: Session management (HTTP) \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:35.292151+00:00
---

# Session management (HTTP) · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/cdp/session-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /[Chrome DevTools Protocol (CDP)](https://developers.cloudflare.com/browser-run/cdp/)
  4. /Session management (HTTP)



# Session management (HTTP)

Last updated Sep 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/cdp/session-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStep 1: Acquire a browser sessionStep 2: Create a tab with a specific URLStep 3: List all targetsStep 4: Open the DevTools UIStep 5: Clean upTroubleshooting

Use the HTTP API to manage browser sessions and tabs without using WebSocket connections. This is useful for session lifecycle operations like creating sessions, listing tabs, and cleaning up resources.

Before you begin, [create a custom API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Browser Rendering - Edit` permission.

The [API reference](https://developers.cloudflare.com/api/resources/browser_rendering/) documents all session management endpoints under `/devtools`.

When your code runs in a Worker, you can use the typed [Browser binding API](https://developers.cloudflare.com/browser-run/reference/browser-binding-api/) instead of constructing HTTP requests. The binding exposes `acquire()`, `connectSession()`, `launch()`, and a nested `devtools` target for session and target management.

## Step 1: Acquire a browser session

Create a new browser session using the `POST /devtools/browser` endpoint. The session will remain active for the specified keep-alive time (in this example, 10 minutes).
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-run/devtools/browser?keep_alive=600000" \
    	--request POST \
    	--header "Authorization: Bearer {api_token}"
    
    
    {
    	"sessionId": "1909cef7-23e8-4394-bc31-27404bf4348f",
    	"webSocketDebuggerUrl": "wss://api.cloudflare.com/client/v4/accounts/{account_id}/browser-run/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f"
    }

Save the `sessionId` from the response. You will use it in subsequent requests.

## Step 2: Create a tab with a specific URL

Open a new tab in your browser session and navigate to a specific URL using the `PUT /devtools/browser/{session_id}/json/new` endpoint.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-run/devtools/browser/SESSION_ID/json/new?url=https%3A%2F%2Fexample.com" \
    	--request PUT \
    	--header "Authorization: Bearer {api_token}"
    
    
    {
    	"id": "8E598E996530FB09E46A22B8B7754F7F",
    	"type": "page",
    	"url": "https://example.com",
    	"title": "Example Domain",
    	"description": "",
    	"devtoolsFrontendUrl": "https://live.browser.run/ui/view?wss=live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...",
    	"webSocketDebuggerUrl": "wss://live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=..."
    }

## Step 3: List all targets

List all targets (tabs) in your session to verify the tab was created and get the `devtoolsFrontendUrl`.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-run/devtools/browser/SESSION_ID/json/list" \
    	--request GET \
    	--header "Authorization: Bearer {api_token}"
    
    
    [
    	{
    		"id": "8E598E996530FB09E46A22B8B7754F7F",
    		"type": "page",
    		"url": "https://example.com",
    		"title": "Example Domain",
    		"description": "",
    		"devtoolsFrontendUrl": "https://live.browser.run/ui/view?wss=live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=...",
    		"webSocketDebuggerUrl": "wss://live.browser.run/api/devtools/browser/1909cef7-23e8-4394-bc31-27404bf4348f/page/8E598E996530FB09E46A22B8B7754F7F?jwt=..."
    	}
    ]

## Step 4: Open the DevTools UI

Copy the `devtoolsFrontendUrl` from the response and open it in Chrome. This URL provides direct access to the Chrome DevTools UI connected to your remote browser session.

URL validity

The `devtoolsFrontendUrl` is valid for five minutes from when it was generated. If you do not open the URL within this timeframe, it will expire and you will need to list the targets again to get a fresh URL. Once the DevTools connection is established, it remains active as long as the browser session is alive.

Once opened, the DevTools UI will load and you can:

  * Inspect the DOM and CSS
  * Debug JavaScript with breakpoints
  * Monitor network requests
  * View console messages
  * Execute JavaScript in the console
  * Navigate to different URLs



## Step 5: Clean up

When you are done, close the browser session to release resources.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/browser-run/devtools/browser/SESSION_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer {api_token}"
    
    
    {
    	"status": "closing"
    }

## Troubleshooting

If you have questions or encounter an error, see the [Browser Run FAQ and troubleshooting guide](https://developers.cloudflare.com/browser-run/faq/).

[PreviousOverview](https://developers.cloudflare.com/browser-run/cdp/)[NextUsing with Puppeteer (CDP)](https://developers.cloudflare.com/browser-run/cdp/puppeteer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/cdp/session-management.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
