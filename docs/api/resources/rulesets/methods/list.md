---
url: https://developers.cloudflare.com/api/resources/rulesets/methods/list/
title: List account or zone rulesets | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:59.979791+00:00
---

# List account or zone rulesets | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/rulesets/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Rulesets](https://developers.cloudflare.com/api/resources/rulesets)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List account or zone rulesets

GET/{accounts_or_zones}/{account_or_zone_id}/rulesets

Fetches all rulesets.

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

`Mass URL Redirects Write``Mass URL Redirects Read``Magic Firewall Write``Magic Firewall Read``L4 DDoS Managed Ruleset Write``L4 DDoS Managed Ruleset Read``Transform Rules Write``Transform Rules Read``Select Configuration Write``Select Configuration Read``Account WAF Write``Account WAF Read``Account Rulesets Read``Account Rulesets Write``Logs Write``Logs Read`

##### Path ParametersExpand Collapse 

account_id: optional string

The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

zone_id: optional string

The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

##### Query ParametersExpand Collapse 

cursor: optional string

The cursor to use for the next page.

minLength1

per_page: optional number

The number of rulesets to return per page.

maximum50

minimum1

##### ReturnsExpand Collapse 

errors: array of object { message, code, source } 

A list of error messages.

message: string

A text description of this message.

minLength1

code: optional number

A unique code for this message.

source: optional object { pointer } 

The source of this message.

pointer: string

A JSON pointer to the field that is the source of the message.

minLength1

messages: array of object { message, code, source } 

A list of warning messages.

message: string

A text description of this message.

minLength1

code: optional number

A unique code for this message.

source: optional object { pointer } 

The source of this message.

pointer: string

A JSON pointer to the field that is the source of the message.

minLength1

result: array of object { id, kind, last_updated, 4 more } 

A list of rulesets. The returned information will not include the rules in each ruleset.

id: string

The unique ID of the ruleset.

kind: [Kind](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20kind%20%3E%20\(schema\))

The kind of the ruleset.

One of the following:

"managed"

"custom"

"root"

"zone"

last_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

name: string

The human-readable name of the ruleset.

minLength1

phase: [Phase](https://developers.cloudflare.com/api/resources/rulesets#\(resource\)%20rulesets%20%3E%20\(model\)%20phase%20%3E%20\(schema\))

The phase of the ruleset.

One of the following:

"ddos_l4"

"ddos_l7"

"http_config_settings"

"http_custom_errors"

"http_log_custom_fields"

"http_ratelimit"

"http_request_cache_settings"

"http_request_dynamic_redirect"

"http_request_firewall_custom"

"http_request_firewall_managed"

"http_request_late_transform"

"http_request_origin"

"http_request_redirect"

"http_request_sanitize"

"http_request_sbfm"

"http_request_transform"

"http_response_cache_settings"

"http_response_compression"

"http_response_firewall_managed"

"http_response_headers_transform"

"magic_transit"

"magic_transit_ids_managed"

"magic_transit_managed"

"magic_transit_ratelimit"

version: string

The version of the ruleset.

description: optional string

An informative description of the ruleset.

success: true

Whether the API call was successful.

result_info: optional object { cursors } 

Information to navigate the results.

cursors: optional object { after } 

The set of cursors.

after: string

The cursor to use for the next page.

minLength1

### List account or zone rulesets

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
    
    
    curl https://api.cloudflare.com/client/v4/$ACCOUNTS_OR_ZONES/$ACCOUNT_OR_ZONE_ID/rulesets \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "messages": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "result": [
        {
          "id": "2f2feab2026849078ba485f918791bdc",
          "kind": "root",
          "last_updated": "2000-01-01T00:00:00Z",
          "name": "My ruleset",
          "phase": "http_request_firewall_custom",
          "version": "1",
          "description": "A description for my ruleset."
        }
      ],
      "success": true,
      "result_info": {
        "cursors": {
          "after": "dGhpc2lzYW5leGFtcGxlCg"
        }
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "messages": [
        {
          "message": "something bad happened",
          "code": 10000,
          "source": {
            "pointer": "/rules/0/action"
          }
        }
      ],
      "result": [
        {
          "id": "2f2feab2026849078ba485f918791bdc",
          "kind": "root",
          "last_updated": "2000-01-01T00:00:00Z",
          "name": "My ruleset",
          "phase": "http_request_firewall_custom",
          "version": "1",
          "description": "A description for my ruleset."
        }
      ],
      "success": true,
      "result_info": {
        "cursors": {
          "after": "dGhpc2lzYW5leGFtcGxlCg"
        }
      }
    }
