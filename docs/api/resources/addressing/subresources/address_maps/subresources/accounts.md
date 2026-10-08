---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/
title: Accounts | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:19.372627+00:00
---

# Accounts | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/

[API Reference](https://developers.cloudflare.com/api)

[Addressing](https://developers.cloudflare.com/api/resources/addressing)

[Address Maps](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Accounts

##### [Add an account membership to an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/methods/update)

PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{member_account_id}

##### [Remove an account membership from an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts/methods/delete)

DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{member_account_id}

##### ModelsExpand Collapse 

AccountUpdateResponse object { errors, messages, success, result_info } 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

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

AccountDeleteResponse object { errors, messages, success, result_info } 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

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

[ Previous

* * *

Address Maps ](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps)[ Next

* * *

IPs ](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips)
