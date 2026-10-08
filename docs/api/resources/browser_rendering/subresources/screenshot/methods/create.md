---
url: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/screenshot/methods/create/
title: Get screenshot. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:59.010668+00:00
---

# Get screenshot. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/screenshot/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

[Screenshot](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/screenshot)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get screenshot.

POST/accounts/{account_id}/browser-rendering/screenshot

Takes a screenshot of a webpage from provided URL or HTML. Control page loading with `gotoOptions` and `waitFor*` options. Customize screenshots with `viewport`, `fullPage`, `clip` and others.

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

##### Query ParametersExpand Collapse 

browser: optional "kitesurf"

Rendering backend. Set to `kitesurf` to use Kitesurf (beta).

cacheTTL: optional number

Cache TTL default is 5s. Set to 0 to disable.

maximum86400

minimum0

##### Body ParametersJSONExpand Collapse 

body: object { url, actionTimeout, addScriptTag, 20 more }  or object { html, actionTimeout, addScriptTag, 20 more } 

One of the following:

object { url, actionTimeout, addScriptTag, 20 more } 

url: string

actionTimeout: optional number

The maximum duration allowed for the browser action to complete after the page has loaded (such as taking screenshots, extracting content, or generating PDFs). If this time limit is exceeded, the action stops and returns a timeout error.

maximum120000

addScriptTag: optional array of object { id, content, type, url } 

Adds a script element into the page with the desired URL or content.

id: optional string

content: optional string

type: optional string

url: optional string

formaturi

addStyleTag: optional array of object { content, url } 

Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a `<style type="text/css">` tag with the content.

content: optional string

url: optional string

formaturi

allowRequestPattern: optional array of string

Only allow requests that match the provided regex patterns, eg. ’/^.*.(css)’. Reject rules are applied first.

allowResourceTypes: optional array of "document" or "stylesheet" or "image" or 15 more

Only allow requests that match the provided resource types, eg. ‘image’ or ‘script’. Reject rules are applied first.

One of the following:

"document"

"stylesheet"

"image"

"media"

"font"

"script"

"texttrack"

"xhr"

"fetch"

"prefetch"

"eventsource"

"websocket"

"manifest"

"signedexchange"

"ping"

"cspviolationreport"

"preflight"

"other"

authenticate: optional object { password, username } 

Provide credentials for HTTP authentication.

password: string

minLength1

username: string

minLength1

bestAttempt: optional boolean

Attempt to proceed when ‘awaited’ events fail or timeout.

cookies: optional array of object { name, value, domain, 11 more } 

Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

name: string

Cookie name.

value: string

domain: optional string

expires: optional number

httpOnly: optional boolean

partitionKey: optional string

path: optional string

priority: optional "Low" or "Medium" or "High"

One of the following:

"Low"

"Medium"

"High"

sameParty: optional boolean

sameSite: optional "Strict" or "Lax" or "None"

One of the following:

"Strict"

"Lax"

"None"

secure: optional boolean

sourcePort: optional number

sourceScheme: optional "Unset" or "NonSecure" or "Secure"

One of the following:

"Unset"

"NonSecure"

"Secure"

url: optional string

emulateMediaType: optional string

gotoOptions: optional object { referer, referrerPolicy, timeout, waitUntil } 

Check [options](https://pptr.dev/api/puppeteer.gotooptions).

referer: optional string

referrerPolicy: optional string

timeout: optional number

maximum60000

waitUntil: optional "load" or "domcontentloaded" or "networkidle0" or "networkidle2" or array of "load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load"

"domcontentloaded"

"networkidle0"

"networkidle2"

array of "load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load"

"domcontentloaded"

"networkidle0"

"networkidle2"

html: optional string

rejectRequestPattern: optional array of string

Block undesired requests that match the provided regex patterns, eg. ’/^.*.(css)’.

rejectResourceTypes: optional array of "document" or "stylesheet" or "image" or 15 more

Block undesired requests that match the provided resource types, eg. ‘image’ or ‘script’.

One of the following:

"document"

"stylesheet"

"image"

"media"

"font"

"script"

"texttrack"

"xhr"

"fetch"

"prefetch"

"eventsource"

"websocket"

"manifest"

"signedexchange"

"ping"

"cspviolationreport"

"preflight"

"other"

screenshotOptions: optional object { captureBeyondViewport, clip, encoding, 6 more } 

Check [options](https://pptr.dev/api/puppeteer.screenshotoptions).

captureBeyondViewport: optional boolean

clip: optional object { height, width, x, 2 more } 

height: number

width: number

x: number

y: number

scale: optional number

encoding: optional "binary" or "base64"

One of the following:

"binary"

"base64"

fromSurface: optional boolean

fullPage: optional boolean

omitBackground: optional boolean

optimizeForSpeed: optional boolean

quality: optional number

type: optional "png" or "jpeg" or "webp"

One of the following:

"png"

"jpeg"

"webp"

scrollPage: optional boolean

selector: optional string

setExtraHTTPHeaders: optional map[string]

setJavaScriptEnabled: optional boolean

userAgent: optional string

viewport: optional object { height, width, deviceScaleFactor, 3 more } 

Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

height: number

width: number

deviceScaleFactor: optional number

hasTouch: optional boolean

isLandscape: optional boolean

isMobile: optional boolean

waitForSelector: optional object { selector, hidden, timeout, visible } 

Wait for the selector to appear in page. Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).

selector: string

hidden: optional true

timeout: optional number

maximum120000

visible: optional true

waitForTimeout: optional number

Waits for a specified timeout before continuing.

maximum120000

object { html, actionTimeout, addScriptTag, 20 more } 

html: string

actionTimeout: optional number

The maximum duration allowed for the browser action to complete after the page has loaded (such as taking screenshots, extracting content, or generating PDFs). If this time limit is exceeded, the action stops and returns a timeout error.

maximum120000

addScriptTag: optional array of object { id, content, type, url } 

Adds a script element into the page with the desired URL or content.

id: optional string

content: optional string

type: optional string

url: optional string

formaturi

addStyleTag: optional array of object { content, url } 

Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a `<style type="text/css">` tag with the content.

content: optional string

url: optional string

formaturi

allowRequestPattern: optional array of string

Only allow requests that match the provided regex patterns, eg. ’/^.*.(css)’. Reject rules are applied first.

allowResourceTypes: optional array of "document" or "stylesheet" or "image" or 15 more

Only allow requests that match the provided resource types, eg. ‘image’ or ‘script’. Reject rules are applied first.

One of the following:

"document"

"stylesheet"

"image"

"media"

"font"

"script"

"texttrack"

"xhr"

"fetch"

"prefetch"

"eventsource"

"websocket"

"manifest"

"signedexchange"

"ping"

"cspviolationreport"

"preflight"

"other"

authenticate: optional object { password, username } 

Provide credentials for HTTP authentication.

password: string

minLength1

username: string

minLength1

bestAttempt: optional boolean

Attempt to proceed when ‘awaited’ events fail or timeout.

cookies: optional array of object { name, value, domain, 11 more } 

Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

name: string

Cookie name.

value: string

domain: optional string

expires: optional number

httpOnly: optional boolean

partitionKey: optional string

path: optional string

priority: optional "Low" or "Medium" or "High"

One of the following:

"Low"

"Medium"

"High"

sameParty: optional boolean

sameSite: optional "Strict" or "Lax" or "None"

One of the following:

"Strict"

"Lax"

"None"

secure: optional boolean

sourcePort: optional number

sourceScheme: optional "Unset" or "NonSecure" or "Secure"

One of the following:

"Unset"

"NonSecure"

"Secure"

url: optional string

emulateMediaType: optional string

gotoOptions: optional object { referer, referrerPolicy, timeout, waitUntil } 

Check [options](https://pptr.dev/api/puppeteer.gotooptions).

referer: optional string

referrerPolicy: optional string

timeout: optional number

maximum60000

waitUntil: optional "load" or "domcontentloaded" or "networkidle0" or "networkidle2" or array of "load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load"

"domcontentloaded"

"networkidle0"

"networkidle2"

array of "load" or "domcontentloaded" or "networkidle0" or "networkidle2"

One of the following:

"load"

"domcontentloaded"

"networkidle0"

"networkidle2"

rejectRequestPattern: optional array of string

Block undesired requests that match the provided regex patterns, eg. ’/^.*.(css)’.

rejectResourceTypes: optional array of "document" or "stylesheet" or "image" or 15 more

Block undesired requests that match the provided resource types, eg. ‘image’ or ‘script’.

One of the following:

"document"

"stylesheet"

"image"

"media"

"font"

"script"

"texttrack"

"xhr"

"fetch"

"prefetch"

"eventsource"

"websocket"

"manifest"

"signedexchange"

"ping"

"cspviolationreport"

"preflight"

"other"

screenshotOptions: optional object { captureBeyondViewport, clip, encoding, 6 more } 

Check [options](https://pptr.dev/api/puppeteer.screenshotoptions).

captureBeyondViewport: optional boolean

clip: optional object { height, width, x, 2 more } 

height: number

width: number

x: number

y: number

scale: optional number

encoding: optional "binary" or "base64"

One of the following:

"binary"

"base64"

fromSurface: optional boolean

fullPage: optional boolean

omitBackground: optional boolean

optimizeForSpeed: optional boolean

quality: optional number

type: optional "png" or "jpeg" or "webp"

One of the following:

"png"

"jpeg"

"webp"

scrollPage: optional boolean

selector: optional string

setExtraHTTPHeaders: optional map[string]

setJavaScriptEnabled: optional boolean

url: optional string

userAgent: optional string

viewport: optional object { height, width, deviceScaleFactor, 3 more } 

Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

height: number

width: number

deviceScaleFactor: optional number

hasTouch: optional boolean

isLandscape: optional boolean

isMobile: optional boolean

waitForSelector: optional object { selector, hidden, timeout, visible } 

Wait for the selector to appear in page. Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).

selector: string

hidden: optional true

timeout: optional number

maximum120000

visible: optional true

waitForTimeout: optional number

Waits for a specified timeout before continuing.

maximum120000

##### ReturnsExpand Collapse 

success: boolean

Response status.

errors: optional array of object { code, message } 

code: number

Error code.

message: string

Error message.

### Get screenshot.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/screenshot \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "url": "url"
            }'

200 example

429 example
    
    
    {
      "success": true,
      "errors": [
        {
          "code": 0,
          "message": "message"
        }
      ]
    }
    
    
    {
      "errors": [
        {
          "code": 2001,
          "message": "Rate limit exceeded"
        }
      ],
      "success": false
    }

##### Returns Examples

200 example

429 example
    
    
    {
      "success": true,
      "errors": [
        {
          "code": 0,
          "message": "message"
        }
      ]
    }
    
    
    {
      "errors": [
        {
          "code": 2001,
          "message": "Rate limit exceeded"
        }
      ],
      "success": false
    }
