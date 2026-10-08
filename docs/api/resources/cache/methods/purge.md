---
url: https://developers.cloudflare.com/api/resources/cache/methods/purge/
title: Purge Cached Content | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:47.434969+00:00
---

# Purge Cached Content | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/cache/methods/purge/

[API Reference](https://developers.cloudflare.com/api)

[Cache](https://developers.cloudflare.com/api/resources/cache)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Purge Cached Content

POST/zones/{zone_id}/purge_cache

Deletes cached content in every Cloudflare data center and cache tier, including Cache Reserve. The next request for purged content is a cache `MISS`: Cloudflare fetches the full response from your origin and caches it again. Cloudflare does not serve purged content from cache again, even if your origin is unavailable.

To keep content cached and have Cloudflare revalidate it with your origin instead, use `POST /zones/{zone_id}/invalidate_cache`.

### Choose what to purge

Send one of these fields in the request body:

  * `files`: specific URLs. If your cache key includes request headers, send each URL with the header values it was cached with.
  * `tags`: all content whose `Cache-Tag` response header contains one of the tags.
  * `hosts`: all content cached for the hostnames.
  * `prefixes`: all content whose URL starts with one of the prefixes.
  * `purge_everything`: all cached content in the zone.



### Check the result

A `200` response with `success: true` means Cloudflare accepted the request. It does not confirm that any content was cached or removed. To check, request a purged URL and confirm that the `CF-Cache-Status` response header is `MISS`.

### Availability and limits

Rate limits and the number of items you can send in one request depend on your plan. See [Purge cache: availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

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

`Cache Purge`

##### Path ParametersExpand Collapse 

zone_id: string

maxLength32

##### Body ParametersJSONExpand Collapse 

body: object { tags }  or object { hosts }  or object { prefixes }  or 3 more

One of the following:

CachePurgeFlexPurgeByTags object { tags } 

tags: optional array of string

Cache tags. Targets all content whose `Cache-Tag` response header contains at least one of these tags. See [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).

CachePurgeFlexPurgeByHostnames object { hosts } 

hosts: optional array of string

Hostnames, such as `www.example.com`. Targets all content cached for these hostnames. See [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).

CachePurgeFlexPurgeByPrefixes object { prefixes } 

prefixes: optional array of string

URL prefixes, each a hostname followed by a path, such as `www.example.com/blog/`. Targets all content whose URL starts with one of these prefixes. Do not include a scheme, query string, or fragment. See [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).

CachePurgeEverything object { purge_everything } 

purge_everything: optional boolean

Set to `true` to target all cached content in the zone, or in the environment for the environment endpoints. Must be the only field in the request. See [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).

CachePurgeSingleFile object { files } 

files: optional array of string

Full URLs, such as `https://www.example.com/css/styles.css`. Targets the content cached for each URL. If your cache key includes request headers, send objects with `url` and `headers` instead. See [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

CachePurgeSingleFileWithURLAndHeaders object { files } 

files: optional array of object { headers, url } 

URLs with the request headers your cache key uses. Use this form when your cache key includes request headers, or the visitor’s device type, country, or language: send the header values each URL was cached with, such as `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

When you send the `Origin` header, include the scheme and hostname. Include the port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

See [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).

headers: optional map[string]

Request headers and the values the content was cached with.

url: optional string

Full URL of the content.

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

success: boolean

Indicates the API call’s success or failure.

result: optional object { id } 

id: string

maxLength32

### Purge Cached Content

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "tags": [
                "product-1234",
                "homepage"
              ]
            }'

200 example

4XX example

4XX example
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "id": "023e105f4ecef8ad9ca31a8372d0c353"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1092,
          "message": "Request cannot contain \"purge_everything\" and any of \"files\", \"tags\", \"hosts\" or \"prefixes\""
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }
    
    
    {
      "errors": [
        {
          "code": 1134,
          "message": "Unable to purge, rate limit reached. Please wait and consider throttling your request speed"
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }

##### Returns Examples

200 example

4XX example

4XX example
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "id": "023e105f4ecef8ad9ca31a8372d0c353"
      },
      "success": true
    }
    
    
    {
      "errors": [
        {
          "code": 1092,
          "message": "Request cannot contain \"purge_everything\" and any of \"files\", \"tags\", \"hosts\" or \"prefixes\""
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }
    
    
    {
      "errors": [
        {
          "code": 1134,
          "message": "Unable to purge, rate limit reached. Please wait and consider throttling your request speed"
        }
      ],
      "messages": [],
      "result": null,
      "success": false
    }
