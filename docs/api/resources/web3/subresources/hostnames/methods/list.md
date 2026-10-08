---
url: https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/list/
title: List Web3 Hostnames | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:15.486698+00:00
---

# List Web3 Hostnames | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/web3/subresources/hostnames/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[Web3](https://developers.cloudflare.com/api/resources/web3)

[Hostnames](https://developers.cloudflare.com/api/resources/web3/subresources/hostnames)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List Web3 Hostnames

GET/zones/{zone_id}/web3/hostnames

List Web3 Hostnames

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

`Web3 Hostnames Write``Web3 Hostnames Read`

##### Path ParametersExpand Collapse 

zone_id: string

Specify the identifier of the hostname.

maxLength32

##### ReturnsExpand Collapse 

errors: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of [ResponseInfo](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20response_info%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

result: array of [Hostname](https://developers.cloudflare.com/api/resources/web3#\(resource\)%20web3.hostnames%20%3E%20\(model\)%20hostname%20%3E%20\(schema\)) { id, created_on, description, 5 more } 

id: optional string

Specify the identifier of the hostname.

maxLength32

created_on: optional string

formatdate-time

description: optional string

Specify an optional description of the hostname.

maxLength500

dnslink: optional string

Specify the DNSLink value used if the target is ipfs.

modified_on: optional string

formatdate-time

name: optional string

Specify the hostname that points to the target gateway via CNAME.

maxLength255

status: optional "active" or "pending" or "deleting" or "error"

Specifies the status of the hostname’s activation.

One of the following:

"active"

"pending"

"deleting"

"error"

target: optional "ethereum" or "ipfs" or "ipfs_universal_path"

Specify the target gateway of the hostname.

One of the following:

"ethereum"

"ipfs"

"ipfs_universal_path"

success: true

Specifies whether the API call was successful.

result_info: optional object { count, page, per_page, total_count } 

count: optional number

Specifies the total number of results for the requested service.

page: optional number

Specifies the current page within paginated list of results.

per_page: optional number

Specifies the number of results per page of results.

total_count: optional number

Specifies the total results available without any search parameters.

### List Web3 Hostnames

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/web3/hostnames \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "created_on": "2014-01-01T05:20:00.12345Z",
          "description": "This is my IPFS gateway.",
          "dnslink": "/ipns/onboarding.ipfs.cloudflare.com",
          "modified_on": "2014-01-01T05:20:00.12345Z",
          "name": "gateway.example.com",
          "status": "active",
          "target": "ipfs"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "result": [
        {
          "id": "023e105f4ecef8ad9ca31a8372d0c353",
          "created_on": "2014-01-01T05:20:00.12345Z",
          "description": "This is my IPFS gateway.",
          "dnslink": "/ipns/onboarding.ipfs.cloudflare.com",
          "modified_on": "2014-01-01T05:20:00.12345Z",
          "name": "gateway.example.com",
          "status": "active",
          "target": "ipfs"
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000
      }
    }
