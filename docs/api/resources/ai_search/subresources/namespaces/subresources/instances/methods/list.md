---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list/
title: List AI Search instances. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:38.816500+00:00
---

# List AI Search instances. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

[Namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces)

[Instances](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# List AI Search instances.

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances

List all AI Search instances in the account.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Path ParametersExpand Collapse 

account_id: string

name: string

##### Query ParametersExpand Collapse 

hostname: optional string

Filter by exact Search for Agents hostname (case-insensitive).

maxLength253

minLength1

order_by: optional "created_at"

Field to order results by.

order_by_direction: optional "asc" or "desc"

Order direction.

One of the following:

"asc"

"desc"

page: optional number

Page number (1-indexed).

minimum1

per_page: optional number

Number of results per page.

maximum100

minimum1

search: optional string

Filter instances whose id contains this string (case-insensitive).

maxLength64

##### ReturnsExpand Collapse 

result: array of object { id, ai_gateway_id, ai_search_model, 42 more } 

id: string

ai_gateway_id: string

ai_search_model: string

cache: boolean

cache_threshold: "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

cache_ttl: 600 or 1800 or 3600 or 7 more

One of the following:

600

1800

3600

7200

21600

43200

86400

172800

259200

518400

chunk: boolean

chunk_overlap: number

chunk_size: number

created_at: string

formatdate-time

created_by: string

custom_metadata: array of object { data_type, field_name } 

data_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field_name: string

embedding_model: string

enable: boolean

engine_version: number

fusion_method: "max" or "rrf"

One of the following:

"max"

"rrf"

hybrid_search_enabled: boolean

index_method: object { keyword, vector } 

keyword: boolean

vector: boolean

indexing_options: object { keyword_tokenizer, use_ocr } 

keyword_tokenizer: optional "porter" or "trigram"

One of the following:

"porter"

"trigram"

use_ocr: optional boolean

last_activity: string

formatdate-time

max_num_results: number

metadata: object { created_from_aisearch_wizard, created_from_emdash_plugin, worker_domain } 

created_from_aisearch_wizard: optional boolean

created_from_emdash_plugin: optional object { type, version } 

type: "native" or "rest"

One of the following:

"native"

"rest"

version: string

worker_domain: optional string

modified_at: string

formatdate-time

modified_by: string

namespace: string

paused: boolean

public_endpoint_id: string

public_endpoint_params: object { authorized_hosts, chat_completions_endpoint, custom_domains, 5 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

custom_domains: optional array of string

default_domain_enabled: optional boolean

enabled: optional boolean

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

rate_limit: optional object { period_ms, requests, technique } 

period_ms: optional number

maximum3600000

minimum60000

requests: optional number

minimum1

technique: optional "fixed" or "sliding"

One of the following:

"fixed"

"sliding"

search_endpoint: optional object { disabled } 

disabled: optional boolean

reranking: boolean

reranking_model: string

retrieval_options: object { boost_by, keyword_match_mode } 

boost_by: optional array of object { field, dataType, direction } 

field: string

maxLength64

minLength1

dataType: optional "number" or "datetime" or "text" or "boolean"

One of the following:

"number"

"datetime"

"text"

"boolean"

direction: optional "asc" or "desc" or "exists" or "not_exists"

One of the following:

"asc"

"desc"

"exists"

"not_exists"

keyword_match_mode: optional "and" or "or"

One of the following:

"and"

"or"

rewrite_model: string

rewrite_query: boolean

score_threshold: number

source: string

source_params: object { exclude_items, include_items, prefix, 2 more } 

exclude_items: optional array of string

include_items: optional array of string

prefix: optional string

r2_jurisdiction: optional string

web_crawler: optional object { discover_options, parse_options, parse_type } 

discover_options: optional object { depth, include_external_links, include_subdomains, 3 more } 

depth: optional number

maximum100000

minimum1

include_external_links: optional boolean

include_subdomains: optional boolean

limit: optional number

Maximum number of pages to crawl. New values are capped at 100000; instances configured before that cap may report a higher stored value, which the crawler clamps at run time.

maximum100000

minimum1

max_age: optional number

maximum604800

minimum0

source: optional "all" or "sitemaps" or "links"

One of the following:

"all"

"sitemaps"

"links"

parse_options: optional object { content_selector, include_headers, include_images, 2 more } 

content_selector: optional array of object { path, selector } 

path: string

maxLength200

minLength1

selector: string

maxLength200

minLength1

include_headers: optional map[string]

include_images: optional boolean

specific_sitemaps: optional array of string

use_browser_rendering: optional boolean

parse_type: optional "sitemap" or "discover"

One of the following:

"sitemap"

"discover"

status: string

summarization: boolean

summarization_model: string

sync_interval: 900 or 1800 or 3600 or 5 more

One of the following:

900

1800

3600

7200

14400

21600

43200

86400

system_prompt_ai_search: string

system_prompt_index_summarization: string

system_prompt_rewrite_query: string

token_id: string

type: "r2" or "web-crawler"

One of the following:

"r2"

"web-crawler"

result_info: object { count, page, per_page, total_count } 

count: number

page: number

per_page: number

total_count: number

success: true

### List AI Search instances.

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": [
        {
          "id": "id",
          "ai_gateway_id": "ai_gateway_id",
          "ai_search_model": "ai_search_model",
          "cache": true,
          "cache_threshold": "super_strict_match",
          "cache_ttl": 600,
          "chunk": true,
          "chunk_overlap": 0,
          "chunk_size": 0,
          "created_at": "2019-12-27T18:11:19.117Z",
          "created_by": "created_by",
          "custom_metadata": [
            {
              "data_type": "text",
              "field_name": "field_name"
            }
          ],
          "embedding_model": "embedding_model",
          "enable": true,
          "engine_version": 0,
          "fusion_method": "max",
          "hybrid_search_enabled": true,
          "index_method": {
            "keyword": true,
            "vector": true
          },
          "indexing_options": {
            "keyword_tokenizer": "porter",
            "use_ocr": true
          },
          "last_activity": "2019-12-27T18:11:19.117Z",
          "max_num_results": 0,
          "metadata": {
            "created_from_aisearch_wizard": true,
            "created_from_emdash_plugin": {
              "type": "native",
              "version": "version"
            },
            "worker_domain": "worker_domain"
          },
          "modified_at": "2019-12-27T18:11:19.117Z",
          "modified_by": "modified_by",
          "namespace": "namespace",
          "paused": true,
          "public_endpoint_id": "public_endpoint_id",
          "public_endpoint_params": {
            "authorized_hosts": [
              "string"
            ],
            "chat_completions_endpoint": {
              "disabled": true
            },
            "custom_domains": [
              "x"
            ],
            "default_domain_enabled": true,
            "enabled": true,
            "mcp": {
              "description": "description",
              "disabled": true
            },
            "rate_limit": {
              "period_ms": 60000,
              "requests": 1,
              "technique": "fixed"
            },
            "search_endpoint": {
              "disabled": true
            }
          },
          "reranking": true,
          "reranking_model": "reranking_model",
          "retrieval_options": {
            "boost_by": [
              {
                "field": "x",
                "dataType": "number",
                "direction": "asc"
              }
            ],
            "keyword_match_mode": "and"
          },
          "rewrite_model": "rewrite_model",
          "rewrite_query": true,
          "score_threshold": 0,
          "source": "source",
          "source_params": {
            "exclude_items": [
              "string"
            ],
            "include_items": [
              "string"
            ],
            "prefix": "prefix",
            "r2_jurisdiction": "r2_jurisdiction",
            "web_crawler": {
              "discover_options": {
                "depth": 1,
                "include_external_links": true,
                "include_subdomains": true,
                "limit": 1,
                "max_age": 0,
                "source": "all"
              },
              "parse_options": {
                "content_selector": [
                  {
                    "path": "x",
                    "selector": "x"
                  }
                ],
                "include_headers": {
                  "foo": "string"
                },
                "include_images": true,
                "specific_sitemaps": [
                  "https://example.com"
                ],
                "use_browser_rendering": true
              },
              "parse_type": "sitemap"
            }
          },
          "status": "status",
          "summarization": true,
          "summarization_model": "summarization_model",
          "sync_interval": 900,
          "system_prompt_ai_search": "system_prompt_ai_search",
          "system_prompt_index_summarization": "system_prompt_index_summarization",
          "system_prompt_rewrite_query": "system_prompt_rewrite_query",
          "token_id": "token_id",
          "type": "r2"
        }
      ],
      "result_info": {
        "count": 0,
        "page": 0,
        "per_page": 0,
        "total_count": 0
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": [
        {
          "id": "id",
          "ai_gateway_id": "ai_gateway_id",
          "ai_search_model": "ai_search_model",
          "cache": true,
          "cache_threshold": "super_strict_match",
          "cache_ttl": 600,
          "chunk": true,
          "chunk_overlap": 0,
          "chunk_size": 0,
          "created_at": "2019-12-27T18:11:19.117Z",
          "created_by": "created_by",
          "custom_metadata": [
            {
              "data_type": "text",
              "field_name": "field_name"
            }
          ],
          "embedding_model": "embedding_model",
          "enable": true,
          "engine_version": 0,
          "fusion_method": "max",
          "hybrid_search_enabled": true,
          "index_method": {
            "keyword": true,
            "vector": true
          },
          "indexing_options": {
            "keyword_tokenizer": "porter",
            "use_ocr": true
          },
          "last_activity": "2019-12-27T18:11:19.117Z",
          "max_num_results": 0,
          "metadata": {
            "created_from_aisearch_wizard": true,
            "created_from_emdash_plugin": {
              "type": "native",
              "version": "version"
            },
            "worker_domain": "worker_domain"
          },
          "modified_at": "2019-12-27T18:11:19.117Z",
          "modified_by": "modified_by",
          "namespace": "namespace",
          "paused": true,
          "public_endpoint_id": "public_endpoint_id",
          "public_endpoint_params": {
            "authorized_hosts": [
              "string"
            ],
            "chat_completions_endpoint": {
              "disabled": true
            },
            "custom_domains": [
              "x"
            ],
            "default_domain_enabled": true,
            "enabled": true,
            "mcp": {
              "description": "description",
              "disabled": true
            },
            "rate_limit": {
              "period_ms": 60000,
              "requests": 1,
              "technique": "fixed"
            },
            "search_endpoint": {
              "disabled": true
            }
          },
          "reranking": true,
          "reranking_model": "reranking_model",
          "retrieval_options": {
            "boost_by": [
              {
                "field": "x",
                "dataType": "number",
                "direction": "asc"
              }
            ],
            "keyword_match_mode": "and"
          },
          "rewrite_model": "rewrite_model",
          "rewrite_query": true,
          "score_threshold": 0,
          "source": "source",
          "source_params": {
            "exclude_items": [
              "string"
            ],
            "include_items": [
              "string"
            ],
            "prefix": "prefix",
            "r2_jurisdiction": "r2_jurisdiction",
            "web_crawler": {
              "discover_options": {
                "depth": 1,
                "include_external_links": true,
                "include_subdomains": true,
                "limit": 1,
                "max_age": 0,
                "source": "all"
              },
              "parse_options": {
                "content_selector": [
                  {
                    "path": "x",
                    "selector": "x"
                  }
                ],
                "include_headers": {
                  "foo": "string"
                },
                "include_images": true,
                "specific_sitemaps": [
                  "https://example.com"
                ],
                "use_browser_rendering": true
              },
              "parse_type": "sitemap"
            }
          },
          "status": "status",
          "summarization": true,
          "summarization_model": "summarization_model",
          "sync_interval": 900,
          "system_prompt_ai_search": "system_prompt_ai_search",
          "system_prompt_index_summarization": "system_prompt_index_summarization",
          "system_prompt_rewrite_query": "system_prompt_rewrite_query",
          "token_id": "token_id",
          "type": "r2"
        }
      ],
      "result_info": {
        "count": 0,
        "page": 0,
        "per_page": 0,
        "total_count": 0
      },
      "success": true
    }
