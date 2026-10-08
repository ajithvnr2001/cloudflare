---
url: https://developers.cloudflare.com/api/resources/browser_rendering/
title: Browser Rendering | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:34.994944+00:00
---

# Browser Rendering | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/browser_rendering/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Browser Rendering

#### Browser RenderingContent

##### [Get HTML content.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/content/methods/create)

POST/accounts/{account_id}/browser-rendering/content

##### ModelsExpand Collapse 

ContentCreateResponse = string

HTML content.

#### Browser RenderingPDF

##### [Get PDF.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/pdf/methods/create)

POST/accounts/{account_id}/browser-rendering/pdf

#### Browser RenderingScrape

##### [Scrape elements.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/scrape/methods/create)

POST/accounts/{account_id}/browser-rendering/scrape

##### ModelsExpand Collapse 

ScrapeCreateResponse = array of object { results, selector } 

results: object { attributes, height, html, 4 more } 

attributes: array of object { name, value } 

name: string

Attribute name.

value: string

Attribute value.

height: number

Element height.

html: string

HTML content.

left: number

Element left.

text: string

Text content.

top: number

Element top.

width: number

Element width.

selector: string

Selector.

#### Browser RenderingScreenshot

##### [Get screenshot.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/screenshot/methods/create)

POST/accounts/{account_id}/browser-rendering/screenshot

##### ModelsExpand Collapse 

ScreenshotCreateResponse object { success, errors } 

success: boolean

Response status.

errors: optional array of object { code, message } 

code: number

Error code.

message: string

Error message.

#### Browser RenderingSnapshot

##### [Get HTML content and screenshot.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/snapshot/methods/create)

POST/accounts/{account_id}/browser-rendering/snapshot

##### ModelsExpand Collapse 

SnapshotCreateResponse object { accessibilityTree, content, markdown, screenshot } 

accessibilityTree: optional object { role, autocomplete, checked, 23 more } 

Accessibility tree node

role: string

autocomplete: optional string

checked: optional boolean or "mixed"

One of the following:

boolean

"mixed"

children: optional array of unknown

description: optional string

disabled: optional boolean

expanded: optional boolean

focused: optional boolean

haspopup: optional string

invalid: optional string

keyshortcuts: optional string

level: optional number

modal: optional boolean

multiline: optional boolean

multiselectable: optional boolean

name: optional string

orientation: optional string

pressed: optional boolean or "mixed"

One of the following:

boolean

"mixed"

readonly: optional boolean

required: optional boolean

roledescription: optional string

selected: optional boolean

value: optional string or number

One of the following:

string

number

valuemax: optional number

valuemin: optional number

valuetext: optional string

content: optional string

HTML content.

markdown: optional string

Markdown content. Prefixed with YAML frontmatter (e.g. `title`) when the page provides that metadata.

screenshot: optional string

Base64 encoded image.

#### Browser RenderingJson

##### [Get json.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/json/methods/create)

POST/accounts/{account_id}/browser-rendering/json

##### ModelsExpand Collapse 

JsonCreateResponse = map[unknown]

#### Browser RenderingLinks

##### [Get Links.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/links/methods/create)

POST/accounts/{account_id}/browser-rendering/links

##### ModelsExpand Collapse 

LinkCreateResponse = array of string

#### Browser RenderingMarkdown

##### [Get markdown.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/markdown/methods/create)

POST/accounts/{account_id}/browser-rendering/markdown

##### ModelsExpand Collapse 

MarkdownCreateResponse = string

Markdown content. Prefixed with YAML frontmatter (e.g. `title`) when the page provides that metadata.

#### Browser RenderingAccessibility Tree

##### [Get accessibility tree page](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/accessibility_tree/methods/create)

POST/accounts/{account_id}/browser-rendering/accessibilityTree

##### ModelsExpand Collapse 

AccessibilityTreeCreateResponse object { accessibilityTree } 

accessibilityTree: object { role, autocomplete, checked, 23 more } 

Accessibility tree node

role: string

autocomplete: optional string

checked: optional boolean or "mixed"

One of the following:

boolean

"mixed"

children: optional array of unknown

description: optional string

disabled: optional boolean

expanded: optional boolean

focused: optional boolean

haspopup: optional string

invalid: optional string

keyshortcuts: optional string

level: optional number

modal: optional boolean

multiline: optional boolean

multiselectable: optional boolean

name: optional string

orientation: optional string

pressed: optional boolean or "mixed"

One of the following:

boolean

"mixed"

readonly: optional boolean

required: optional boolean

roledescription: optional string

selected: optional boolean

value: optional string or number

One of the following:

string

number

valuemax: optional number

valuemin: optional number

valuetext: optional string

#### Browser RenderingCrawl

##### [Crawl websites.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/create)

POST/accounts/{account_id}/browser-rendering/crawl

##### [Get crawl result.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/get)

GET/accounts/{account_id}/browser-rendering/crawl/{job_id}

##### [Cancel a crawl job.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/crawl/methods/delete)

DELETE/accounts/{account_id}/browser-rendering/crawl/{job_id}

##### ModelsExpand Collapse 

CrawlCreateResponse = string

Crawl job ID.

CrawlGetResponse object { id, browserSecondsUsed, finished, 5 more } 

id: string

Crawl job ID.

browserSecondsUsed: number

Total seconds spent in browser so far.

finished: number

Total number of URLs that have been crawled so far.

records: array of object { status, url, html, 3 more } 

List of crawl job records.

status: "queued" or "errored" or "completed" or 3 more

Current status of the crawled URL.

One of the following:

"queued"

"errored"

"completed"

"disallowed"

"skipped"

"cancelled"

url: string

Crawled URL.

html: optional string

HTML content of the crawled URL.

json: optional map[unknown]

JSON of the content of the crawled URL.

markdown: optional string

Markdown of the content of the crawled URL.

metadata: optional object { status, url, title } 

Absent for urls that never reached a fetch.

status: number

HTTP status code of the crawled page.

url: string

Final URL of the crawled page.

title: optional string

Title of the crawled page.

skipped: number

Total number of URLs that were skipped due to include/exclude/subdomain filters. Skipped URLs are included in records but are not counted toward total/finished.

status: string

Current crawl job status.

total: number

Total current number of URLs in the crawl job.

cursor: optional string

Cursor for pagination.

CrawlDeleteResponse object { job_id, message } 

job_id: string

The ID of the cancelled job.

message: string

Cancellation confirmation message.

#### Browser RenderingDevtools

#### Browser RenderingDevtoolsSession

##### [List sessions.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/list)

GET/accounts/{account_id}/browser-rendering/devtools/session

##### [Get session details.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/get)

GET/accounts/{account_id}/browser-rendering/devtools/session/{session_id}

##### ModelsExpand Collapse 

SessionListResponse = array of object { sessionId, closeReason, closeReasonText, 8 more } 

sessionId: string

Session ID.

formatuuid

closeReason: optional number

Reason code for session closure.

closeReasonText: optional string

Human-readable close reason.

connectionEndTime: optional number

Connection end time.

connectionId: optional string

Connection ID.

connectionStartTime: optional number

Connection start time.

devtoolsFrontendUrl: optional string

DevTools frontend URL.

endTime: optional number

Session end time.

lastUpdated: optional number

Last updated timestamp.

startTime: optional number

Session start time.

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

SessionGetResponse object { sessionId, closeReason, closeReasonText, 8 more } 

sessionId: string

Session ID.

formatuuid

closeReason: optional number

Reason code for session closure.

closeReasonText: optional string

Human-readable close reason.

connectionEndTime: optional number

Connection end time.

connectionId: optional string

Connection ID.

connectionStartTime: optional number

Connection start time.

devtoolsFrontendUrl: optional string

DevTools frontend URL.

endTime: optional number

Session end time.

lastUpdated: optional number

Last updated timestamp.

startTime: optional number

Session start time.

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

#### Browser RenderingDevtoolsBrowser

##### [Get a browser session ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/create)

POST/accounts/{account_id}/browser-rendering/devtools/browser

##### [Close browser session.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/delete)

DELETE/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}

##### [Get browser version metadata.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/version)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/version

##### [Get Chrome DevTools Protocol schema.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol

##### ModelsExpand Collapse 

BrowserCreateResponse object { sessionId, webSocketDebuggerUrl } 

sessionId: string

Browser session ID.

webSocketDebuggerUrl: optional string

WebSocket URL for the session.

BrowserDeleteResponse object { status } 

status: "closing" or "closed"

One of the following:

"closing"

"closed"

BrowserVersionResponse object { Browser, "Protocol-Version", "User-Agent", 3 more } 

Browser: string

Browser name and version.

"Protocol-Version": string

Chrome DevTools Protocol version.

"User-Agent": string

User agent string.

"V8-Version": string

V8 JavaScript engine version.

"WebKit-Version": string

WebKit version.

webSocketDebuggerUrl: string

WebSocket URL for debugging the browser.

BrowserProtocolResponse object { domains, version } 

domains: array of object { domain, commands, dependencies, 3 more } 

List of protocol domains.

domain: string

Domain name.

commands: optional array of map[unknown]

Available commands.

dependencies: optional array of string

Domain dependencies.

events: optional array of map[unknown]

Available events.

experimental: optional boolean

Whether this domain is experimental.

types: optional array of map[unknown]

Type definitions.

version: optional object { major, minor } 

Protocol version.

major: string

Major version.

minor: string

Minor version.

#### Browser RenderingDevtoolsBrowserLive View

##### [Mint live view URLs for a browser session](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create)

POST/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/live_view

##### ModelsExpand Collapse 

LiveViewCreateResponse object { id, devtoolsFrontendUrl, options, webSocketDebuggerUrl } 

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

#### Browser RenderingDevtoolsBrowserPage

#### Browser RenderingDevtoolsBrowserTargets

##### [Open a new browser tab.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/create)

PUT/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/new

##### [List targets.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/list)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list

##### [Get a target by ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/get)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list/{target_id}

##### [Activate a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/activate)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/activate/{target_id}

##### [Close a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/close)

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/close/{target_id}

##### ModelsExpand Collapse 

TargetCreateResponse object { id, type, url, 4 more } 

id: string

Target ID.

type: string

Target type (page, background_page, worker, etc.).

url: string

URL of the target.

description: optional string

Target description.

devtoolsFrontendUrl: optional string

DevTools frontend URL.

title: optional string

Title of the target.

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

TargetListResponse = array of object { id, type, url, 4 more } 

id: string

Target ID.

type: string

Target type (page, background_page, worker, etc.).

url: string

URL of the target.

description: optional string

Target description.

devtoolsFrontendUrl: optional string

DevTools frontend URL.

title: optional string

Title of the target.

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

TargetGetResponse object { id, type, url, 4 more } 

id: string

Target ID.

type: string

Target type (page, background_page, worker, etc.).

url: string

URL of the target.

description: optional string

Target description.

devtoolsFrontendUrl: optional string

DevTools frontend URL.

title: optional string

Title of the target.

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

TargetActivateResponse object { message } 

message: string

Target activated.

TargetCloseResponse object { message } 

message: string

Target is closing.

[ Previous

* * *

Scans ](https://developers.cloudflare.com/api/resources/url_scanner/subresources/scans)[ Next

* * *

Content ](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/content)
