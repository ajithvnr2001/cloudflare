---
url: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol/
title: Get Chrome DevTools Protocol schema. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:35.137523+00:00
---

# Get Chrome DevTools Protocol schema. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol/

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

[Devtools](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools)

[Browser](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Get Chrome DevTools Protocol schema.

GET/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol

Returns the complete Chrome DevTools Protocol schema including all domains, commands, events, and types. This schema describes the entire CDP API surface.

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

`Browser Rendering Write``Browser Rendering Read`

##### Path ParametersExpand Collapse 

account_id: string

Account ID.

session_id: string

Browser session ID.

formatuuid

##### ReturnsExpand Collapse 

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

### Get Chrome DevTools Protocol schema.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-rendering/devtools/browser/$SESSION_ID/json/protocol \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "domains": [
        {
          "domain": "domain",
          "commands": [
            {
              "foo": {}
            }
          ],
          "dependencies": [
            "string"
          ],
          "events": [
            {
              "foo": {}
            }
          ],
          "experimental": true,
          "types": [
            {
              "foo": {}
            }
          ]
        }
      ],
      "version": {
        "major": "major",
        "minor": "minor"
      }
    }

##### Returns Examples

200 example
    
    
    {
      "domains": [
        {
          "domain": "domain",
          "commands": [
            {
              "foo": {}
            }
          ],
          "dependencies": [
            "string"
          ],
          "events": [
            {
              "foo": {}
            }
          ],
          "experimental": true,
          "types": [
            {
              "foo": {}
            }
          ]
        }
      ],
      "version": {
        "major": "major",
        "minor": "minor"
      }
    }
