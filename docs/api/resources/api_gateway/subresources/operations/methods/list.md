---
url: https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/list/
title: List web and API operations | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:24:00.095766+00:00
---

# List web and API operations | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[API Gateway](https://developers.cloudflare.com/api/resources/api_gateway)

[Operations](https://developers.cloudflare.com/api/resources/api_gateway/subresources/operations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List web and API operations

GET/zones/{zone_id}/api_gateway/operations

Lists web and API operations tracked for the zone, including each operation’s method, path, and feature configuration.

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

`Account API Gateway``Account API Gateway Read``Domain API Gateway``Domain API Gateway Read`

##### Path ParametersExpand Collapse 

zone_id: string

Identifier.

maxLength32

##### Query ParametersExpand Collapse 

direction: optional "asc" or "desc"

Direction to order results.

One of the following:

"asc"

"desc"

endpoint: optional string

Filter results to only include endpoints containing this pattern.

feature: optional array of "thresholds" or "parameter_schemas" or "schema_info" or "confidence_intervals"

Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.

One of the following:

"thresholds"

"parameter_schemas"

"schema_info"

"confidence_intervals"

host: optional array of string

Filter results to only include the specified hosts.

method: optional array of string

Filter results to only include the specified HTTP methods.

order: optional "method" or "host" or "endpoint" or "thresholds.$key"

Field to order by. When requesting a feature, the feature keys are available for ordering as well, e.g., `thresholds.suggested_threshold`.

One of the following:

"method"

"host"

"endpoint"

"thresholds.$key"

page: optional number

Page number of paginated results.

minimum1

per_page: optional number

Maximum number of results per page.

maximum50

minimum5

##### ReturnsExpand Collapse 

errors: [Message](https://developers.cloudflare.com/api/resources/api_gateway#\(resource\)%20api_gateway.user_schemas%20%3E%20\(model\)%20message%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: [Message](https://developers.cloudflare.com/api/resources/api_gateway#\(resource\)%20api_gateway.user_schemas%20%3E%20\(model\)%20message%20%3E%20\(schema\)) { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

result: array of object { endpoint, host, last_updated, 3 more } 

endpoint: string

The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with {varN}, starting with {var1}, during insertion. This will further be Cloudflare-normalized upon insertion. See: <https://developers.cloudflare.com/rules/normalization/how-it-works/>.

formaturi-template

maxLength4096

host: string

RFC3986-compliant host.

formathostname

maxLength255

last_updated: string

formatdate-time

method: "GET" or "POST" or "HEAD" or 6 more

The HTTP method used to access the endpoint.

One of the following:

"GET"

"POST"

"HEAD"

"OPTIONS"

"PUT"

"DELETE"

"CONNECT"

"PATCH"

"TRACE"

operation_id: string

UUID.

maxLength36

minLength36

features: optional object { thresholds }  or object { parameter_schemas }  or object { api_routing }  or 2 more

One of the following:

APIShieldOperationFeatureThresholds object { thresholds } 

thresholds: optional object { auth_id_tokens, data_points, last_updated, 6 more } 

auth_id_tokens: optional number

The total number of auth-ids seen across this calculation.

data_points: optional number

The number of data points used for the threshold suggestion calculation.

last_updated: optional string

formatdate-time

p50: optional number

The p50 quantile of requests (in period_seconds).

p90: optional number

The p90 quantile of requests (in period_seconds).

p99: optional number

The p99 quantile of requests (in period_seconds).

period_seconds: optional number

The period over which this threshold is suggested.

requests: optional number

The estimated number of requests covered by these calculations.

suggested_threshold: optional number

The suggested threshold in requests done by the same auth_id or period_seconds.

APIShieldOperationFeatureParameterSchemas object { parameter_schemas } 

parameter_schemas: object { last_updated, parameter_schemas } 

last_updated: optional string

formatdate-time

parameter_schemas: optional object { parameters, responses } 

An operation schema object containing a response.

parameters: optional array of unknown

An array containing the learned parameter schemas.

responses: optional unknown

An empty response object. This field is required to yield a valid operation schema.

APIShieldOperationFeatureAPIRouting object { api_routing } 

api_routing: optional object { last_updated, route } 

API Routing settings on endpoint.

last_updated: optional string

formatdate-time

route: optional string

Target route.

APIShieldOperationFeatureConfidenceIntervals object { confidence_intervals } 

confidence_intervals: optional object { last_updated, suggested_threshold } 

last_updated: optional string

formatdate-time

suggested_threshold: optional object { confidence_intervals, mean } 

confidence_intervals: optional object { p90, p95, p99 } 

p90: optional object { lower, upper } 

Upper and lower bound for percentile estimate

lower: optional number

Lower bound for percentile estimate

upper: optional number

Upper bound for percentile estimate

p95: optional object { lower, upper } 

Upper and lower bound for percentile estimate

lower: optional number

Lower bound for percentile estimate

upper: optional number

Upper bound for percentile estimate

p99: optional object { lower, upper } 

Upper and lower bound for percentile estimate

lower: optional number

Lower bound for percentile estimate

upper: optional number

Upper bound for percentile estimate

mean: optional number

Suggested threshold.

APIShieldOperationFeatureSchemaInfo object { schema_info } 

schema_info: optional object { active_schema, mitigation_action } 

active_schema: optional object { id, created_at, name } 

Schema active on endpoint.

id: optional string

UUID.

maxLength36

minLength36

created_at: optional string

formatdate-time

name: optional string

Schema file name.

mitigation_action: optional "none" or "log" or "block"

Action taken on requests failing validation.

One of the following:

"none"

"log"

"block"

success: true

Whether the API call was successful.

result_info: optional object { count, page, per_page, 2 more } 

count: optional number

Total number of results for the requested service.

page: optional number

Current page within paginated list of results.

per_page: optional number

Number of results per page of results.

total_count: optional number

Total results available without any search parameters.

total_pages: optional number

The number of total pages in the entire result set.

### List web and API operations

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
    
    
    curl https://api.cloudflare.com/client/v4/zones/$ZONE_ID/api_gateway/operations \
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
          "endpoint": "/api/v1/users/{var1}",
          "host": "www.example.com",
          "last_updated": "2014-01-01T05:20:00.12345Z",
          "method": "GET",
          "operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
          "features": {
            "api_routing": {
              "last_updated": "2014-01-01T05:20:00.12345Z",
              "route": "https://api.example.com/api/service"
            }
          }
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
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
          "endpoint": "/api/v1/users/{var1}",
          "host": "www.example.com",
          "last_updated": "2014-01-01T05:20:00.12345Z",
          "method": "GET",
          "operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
          "features": {
            "api_routing": {
              "last_updated": "2014-01-01T05:20:00.12345Z",
              "route": "https://api.example.com/api/service"
            }
          }
        }
      ],
      "success": true,
      "result_info": {
        "count": 1,
        "page": 1,
        "per_page": 20,
        "total_count": 2000,
        "total_pages": 100
      }
    }
