---
url: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/json/methods/create/
title: Get json. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:41.429896+00:00
---

# Get json. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/json/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

[Json](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/json)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get json.

POST/accounts/{account_id}/browser-rendering/json

Gets json from a webpage from a provided URL or HTML. Pass `prompt` or `schema` in the body. Control page loading with `gotoOptions` and `waitFor*` options.

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

custom_ai: optional array of object { model, authorization } 

Optional list of custom AI models to use for the request. The models will be tried in the order provided, and in case a model returns an error, the next one will be used as fallback.

model: string

AI model to use for the request. Must be formed as `<provider>/<model_name>`, e.g. `workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast`.

authorization: optional string

Authorization token for the AI model: `Bearer <token>`. Not needed for workers-ai models.

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

prompt: optional string

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

response_format: optional object { type, json_schema } 

type: string

json_schema: optional map[unknown]

Schema for the response format. More information here: <https://developers.cloudflare.com/workers-ai/json-mode/>

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

custom_ai: optional array of object { model, authorization } 

Optional list of custom AI models to use for the request. The models will be tried in the order provided, and in case a model returns an error, the next one will be used as fallback.

model: string

AI model to use for the request. Must be formed as `<provider>/<model_name>`, e.g. `workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast`.

authorization: optional string

Authorization token for the AI model: `Bearer <token>`. Not needed for workers-ai models.

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

prompt: optional string

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

response_format: optional object { type, json_schema } 

type: string

json_schema: optional map[unknown]

Schema for the response format. More information here: <https://developers.cloudflare.com/workers-ai/json-mode/>

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

meta: object { finalUrl, headers, redirectChain, 2 more } 

finalUrl: optional string

URL that served the response, after any redirects the browser followed.

headers: optional map[string]

Origin response headers, lowercased. Repeated headers are joined with a newline. Credential and transport-only headers that do not survive rendering are omitted.

redirectChain: optional array of object { headers, status, url } 

HTTP redirects followed to reach `finalUrl`, oldest first. Omitted for direct navigation and for client-side redirects such as meta refresh. An empty array means redirects occurred but their intermediate responses could not be read.

headers: map[string]

Redirect response headers, including `location`.

status: number

HTTP status of the redirect.

url: string

URL that returned the redirect.

status: optional number

HTTP status returned by the origin.

title: optional string

Page title.

result: map[unknown]

success: boolean

Response status.

errors: optional array of object { code, message } 

code: number

Error code.

message: string

Error message.

### Get json.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/json \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "url": "url"
            }'

200 example

429 example
    
    
    {
      "meta": {
        "finalUrl": "finalUrl",
        "headers": {
          "foo": "string"
        },
        "redirectChain": [
          {
            "headers": {
              "foo": "string"
            },
            "status": 0,
            "url": "url"
          }
        ],
        "status": 0,
        "title": "title"
      },
      "result": {
        "foo": {}
      },
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
      "meta": {
        "finalUrl": "finalUrl",
        "headers": {
          "foo": "string"
        },
        "redirectChain": [
          {
            "headers": {
              "foo": "string"
            },
            "status": 0,
            "url": "url"
          }
        ],
        "status": 0,
        "title": "title"
      },
      "result": {
        "foo": {}
      },
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
