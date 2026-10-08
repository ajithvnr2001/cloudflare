---
url: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/
title: IPs | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:25:16.674914+00:00
---

# IPs | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/

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

# IPs

##### [Add an IP to an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/methods/update)

PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}

##### [Remove an IP from an Address Map](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/ips/methods/delete)

DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}

##### ModelsExpand Collapse 

IPUpdateResponse object { errors, messages, success, result_info } 

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

IPDeleteResponse object { errors, messages, success, result_info } 

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

Accounts ](https://developers.cloudflare.com/api/resources/addressing/subresources/address_maps/subresources/accounts)[ Next

* * *

LOA Documents ](https://developers.cloudflare.com/api/resources/addressing/subresources/loa_documents)
