---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/
title: Namespaces | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:31.062350+00:00
---

# Namespaces | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/

[API Reference](https://developers.cloudflare.com/api)

[AI Search](https://developers.cloudflare.com/api/resources/ai_search)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Namespaces

##### [List namespaces](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/list)

GET/accounts/{account_id}/ai-search/namespaces

##### [Create a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/create)

POST/accounts/{account_id}/ai-search/namespaces

##### [Get a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/read)

GET/accounts/{account_id}/ai-search/namespaces/{name}

##### [Update a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}

##### [Delete a namespace](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}

##### [Multi-Instance Search](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/search)

POST/accounts/{account_id}/ai-search/namespaces/{name}/search

##### [Multi-Instance Chat Completions](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/methods/chat_completions)

POST/accounts/{account_id}/ai-search/namespaces/{name}/chat/completions

##### ModelsExpand Collapse 

NamespaceListResponse object { created_at, name, description, 2 more } 

created_at: string

formatdate-time

name: string

description: optional string

Optional description for the namespace. Max 256 characters.

maxLength256

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 6 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

instances_allowed: optional array of string

Instance IDs exposed through the namespace public endpoint. Empty means nothing is searchable. Every ID must be an existing instance in this namespace, and the list cannot exceed the account’s multi-instance search limit.

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

NamespaceCreateResponse object { created_at, name, description, 2 more } 

created_at: string

formatdate-time

name: string

description: optional string

Optional description for the namespace. Max 256 characters.

maxLength256

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 6 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

instances_allowed: optional array of string

Instance IDs exposed through the namespace public endpoint. Empty means nothing is searchable. Every ID must be an existing instance in this namespace, and the list cannot exceed the account’s multi-instance search limit.

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

NamespaceReadResponse object { created_at, name, description, 2 more } 

created_at: string

formatdate-time

name: string

description: optional string

Optional description for the namespace. Max 256 characters.

maxLength256

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 6 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

instances_allowed: optional array of string

Instance IDs exposed through the namespace public endpoint. Empty means nothing is searchable. Every ID must be an existing instance in this namespace, and the list cannot exceed the account’s multi-instance search limit.

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

NamespaceUpdateResponse object { created_at, name, description, 2 more } 

created_at: string

formatdate-time

name: string

description: optional string

Optional description for the namespace. Max 256 characters.

maxLength256

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 6 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

instances_allowed: optional array of string

Instance IDs exposed through the namespace public endpoint. Empty means nothing is searchable. Every ID must be an existing instance in this namespace, and the list cannot exceed the account’s multi-instance search limit.

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

NamespaceDeleteResponse = unknown

NamespaceSearchResponse object { chunks, query_kind, errors, search_query } 

chunks: array of object { id, instance_id, score, 4 more } 

id: string

instance_id: string

score: number

maximum1

minimum0

text: string

type: string

item: optional object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

scoring_details: optional object { fusion_method, keyword_rank, keyword_score, 3 more } 

fusion_method: optional "rrf" or "max"

One of the following:

"rrf"

"max"

keyword_rank: optional number

keyword_score: optional number

minimum0

reranking_score: optional number

maximum1

minimum0

vector_rank: optional number

vector_score: optional number

maximum1

minimum0

query_kind: "text" or "image" or "multimodal"

One of the following:

"text"

"image"

"multimodal"

errors: optional array of object { instance_id, message } 

instance_id: string

message: string

search_query: optional string

NamespaceChatCompletionsResponse object { choices, chunks, id, 3 more } 

choices: array of object { message, index } 

message: object { content, role } 

content: string or array of object { text, type }  or object { image_url, type }  or object { file, type }  or string

One of the following:

string

array of object { text, type }  or object { image_url, type }  or object { file, type } 

One of the following:

object { text, type } 

text: string

minLength1

type: "text"

object { image_url, type } 

image_url: object { url } 

url: string

maxLength20971520

minLength1

type: "image_url"

object { file, type } 

file: object { filename, file_data, file_id } 

filename: string

maxLength255

minLength1

file_data: optional string

maxLength13981144

minLength1

file_id: optional string

type: "file"

string

role: "system" or "developer" or "user" or 2 more

One of the following:

"system"

"developer"

"user"

"assistant"

"tool"

index: optional number

chunks: array of object { id, instance_id, score, 4 more } 

id: string

instance_id: string

score: number

maximum1

minimum0

text: string

type: string

item: optional object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

scoring_details: optional object { fusion_method, keyword_rank, keyword_score, 3 more } 

fusion_method: optional "rrf" or "max"

One of the following:

"rrf"

"max"

keyword_rank: optional number

keyword_score: optional number

minimum0

reranking_score: optional number

maximum1

minimum0

vector_rank: optional number

vector_score: optional number

maximum1

minimum0

id: optional string

errors: optional array of object { instance_id, message } 

instance_id: string

message: string

model: optional string

object: optional string

#### NamespacesInstances

##### [List AI Search instances.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances

##### [Create an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances

##### [Get an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/read)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Update an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Delete an AI Search instance.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}

##### [Get instance statistics.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/stats

##### [Search](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/search

##### [Chat Completions](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/chat/completions

##### ModelsExpand Collapse 

InstanceListResponse object { id, ai_gateway_id, ai_search_model, 42 more } 

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

InstanceCreateResponse object { id, created_at, modified_at, 36 more } 

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

created_at: string

formatdate-time

modified_at: string

formatdate-time

ai_gateway_id: optional string

ai_search_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

cache: optional boolean

cache_threshold: optional "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

cache_ttl: optional 600 or 1800 or 3600 or 7 more

Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).

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

chunk_overlap: optional number

maximum30

minimum0

chunk_size: optional number

minimum64

created_by: optional string

custom_metadata: optional array of object { data_type, field_name } 

data_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field_name: string

maxLength64

minLength1

embedding_model: optional string

enable: optional boolean

engine_version: optional number

fusion_method: optional "max" or "rrf"

One of the following:

"max"

"rrf"

Deprecatedhybrid_search_enabled: optional boolean

Deprecated — use index_method instead. Defaults to true for new instances; set false to create a vector-only instance.

index_method: optional object { keyword, vector } 

Controls which storage backends are used during indexing. Defaults to vector and keyword indexing for new instances.

keyword: boolean

Enable keyword (BM25) storage backend.

vector: boolean

Enable vector (embedding) storage backend.

indexing_options: optional object { keyword_tokenizer, use_ocr } 

keyword_tokenizer: optional "porter" or "trigram"

Tokenizer used for keyword search indexing. porter provides word-level tokenization with Porter stemming (good for natural language queries). trigram enables character-level substring matching (good for partial matches, code, identifiers). Changing this triggers a full re-index. Defaults to porter.

One of the following:

"porter"

"trigram"

use_ocr: optional boolean

Enables OCR ingestion for PDFs and images. Changing this triggers a full re-index. Defaults to false.

last_activity: optional string

formatdate-time

max_num_results: optional number

maximum50

minimum1

metadata: optional object { created_from_aisearch_wizard, created_from_emdash_plugin, worker_domain } 

created_from_aisearch_wizard: optional boolean

created_from_emdash_plugin: optional object { type, version } 

type: "native" or "rest"

One of the following:

"native"

"rest"

version: string

worker_domain: optional string

modified_by: optional string

namespace: optional string

paused: optional boolean

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 5 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

reranking: optional boolean

reranking_model: optional string

retrieval_options: optional object { boost_by, keyword_match_mode } 

boost_by: optional array of object { field, direction } 

Metadata fields to boost search results by. Each entry specifies a metadata field and an optional direction. Direction defaults to ‘asc’ for numeric/datetime fields and ‘exists’ for text/boolean fields. Fields must match ‘timestamp’ or a defined custom_metadata field.

field: string

Metadata field name to boost by. Use ‘timestamp’ for document freshness, or any custom_metadata field. Numeric and datetime fields support all four directions (asc, desc, exists, not_exists); text/boolean fields only support exists/not_exists.

maxLength64

minLength1

direction: optional "asc" or "desc" or "exists" or "not_exists"

Boost direction. ‘desc’ = higher values rank higher (e.g. newer timestamps). ‘asc’ = lower values rank higher. ‘exists’ = boost chunks that have the field. ‘not_exists’ = boost chunks that lack the field. Optional — defaults to ‘asc’ for numeric/datetime fields, ‘exists’ for text/boolean fields.

One of the following:

"asc"

"desc"

"exists"

"not_exists"

keyword_match_mode: optional "and" or "or"

Controls which documents are candidates for BM25 scoring. ‘and’ restricts candidates to documents containing all query terms; ‘or’ includes any document containing at least one term, ranked by BM25 relevance. When omitted on an update, the existing stored value is preserved; when never set, search falls back to ‘and’.

One of the following:

"and"

"or"

rewrite_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

rewrite_query: optional boolean

score_threshold: optional number

maximum1

minimum0

source: optional string

source_params: optional object { exclude_items, include_items, prefix, 2 more } 

exclude_items: optional array of string

List of path patterns to exclude. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /admin/** matches /admin/users and /admin/settings/advanced). Most accounts are limited to 10 rules; contact support to raise it.

include_items: optional array of string

List of path patterns to include. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most accounts are limited to 10 rules; contact support to raise it.

prefix: optional string

r2_jurisdiction: optional string

web_crawler: optional object { discover_options, parse_options, parse_type } 

discover_options: optional object { depth, include_external_links, include_subdomains, 3 more } 

Options for parse_type ‘discover’, where Browser Run discovers URLs by link following and sitemaps. Ignored for ‘sitemap’.

depth: optional number

Maximum link-follow depth from the seed URL.

maximum100000

minimum1

include_external_links: optional boolean

Follow links that point outside the source domain. Must stay `false` — discover crawls are restricted to the zone you own.

include_subdomains: optional boolean

Follow links to subdomains of the source host.

limit: optional number

Maximum number of pages to crawl (1-100000).

maximum100000

minimum1

max_age: optional number

Maximum content age in seconds to accept (0–604800).

maximum604800

minimum0

source: optional "all" or "sitemaps" or "links"

Where the crawler looks for URLs: ‘sitemaps’ reads sitemap XML only, ‘links’ follows page links only, ‘all’ does both.

One of the following:

"all"

"sitemaps"

"links"

parse_options: optional object { content_selector, include_headers, include_images, 2 more } 

content_selector: optional array of object { path, selector } 

List of path-to-selector mappings for extracting specific content from crawled pages. Each entry pairs a URL glob pattern with a CSS selector. The first matching path wins. Only the matched HTML fragment is stored and indexed. Omit the field to disable content selection — empty arrays are rejected.

path: string

Glob pattern to match against the page URL path. Uses standard glob syntax: * matches within a segment, ** crosses directories.

maxLength200

minLength1

selector: string

CSS selector to extract content from pages matching the path pattern. Must not contain disallowed characters (;, `, $, {, }, ). Must target a single element; if multiple elements match, the selector is ignored and the full page is used.

maxLength200

minLength1

include_headers: optional map[string]

Up to 5 custom HTTP headers sent with each crawl request. Names must be RFC-7230 token characters (no spaces, colons, or control characters); values must be HTAB + printable ASCII (no CR/LF).

include_images: optional boolean

specific_sitemaps: optional array of string

List of specific sitemap URLs to use for crawling. Only valid when parse_type is ‘sitemap’.

use_browser_rendering: optional boolean

parse_type: optional "sitemap" or "discover"

How URLs are discovered. ‘sitemap’ reads XML sitemaps; ‘discover’ follows links recursively and requires the source to be a Verified zone on this account.

One of the following:

"sitemap"

"discover"

status: optional string

sync_interval: optional 900 or 1800 or 3600 or 5 more

Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).

One of the following:

900

1800

3600

7200

14400

21600

43200

86400

token_id: optional string

formatuuid

type: optional "r2" or "web-crawler"

Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer web-crawler and existing R2 bucket names infer r2. A missing or blank source without a type uses managed upload-only storage.

One of the following:

"r2"

"web-crawler"

InstanceReadResponse object { id, created_at, modified_at, 36 more } 

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

created_at: string

formatdate-time

modified_at: string

formatdate-time

ai_gateway_id: optional string

ai_search_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

cache: optional boolean

cache_threshold: optional "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

cache_ttl: optional 600 or 1800 or 3600 or 7 more

Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).

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

chunk_overlap: optional number

maximum30

minimum0

chunk_size: optional number

minimum64

created_by: optional string

custom_metadata: optional array of object { data_type, field_name } 

data_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field_name: string

maxLength64

minLength1

embedding_model: optional string

enable: optional boolean

engine_version: optional number

fusion_method: optional "max" or "rrf"

One of the following:

"max"

"rrf"

Deprecatedhybrid_search_enabled: optional boolean

Deprecated — use index_method instead. Defaults to true for new instances; set false to create a vector-only instance.

index_method: optional object { keyword, vector } 

Controls which storage backends are used during indexing. Defaults to vector and keyword indexing for new instances.

keyword: boolean

Enable keyword (BM25) storage backend.

vector: boolean

Enable vector (embedding) storage backend.

indexing_options: optional object { keyword_tokenizer, use_ocr } 

keyword_tokenizer: optional "porter" or "trigram"

Tokenizer used for keyword search indexing. porter provides word-level tokenization with Porter stemming (good for natural language queries). trigram enables character-level substring matching (good for partial matches, code, identifiers). Changing this triggers a full re-index. Defaults to porter.

One of the following:

"porter"

"trigram"

use_ocr: optional boolean

Enables OCR ingestion for PDFs and images. Changing this triggers a full re-index. Defaults to false.

last_activity: optional string

formatdate-time

max_num_results: optional number

maximum50

minimum1

metadata: optional object { created_from_aisearch_wizard, created_from_emdash_plugin, worker_domain } 

created_from_aisearch_wizard: optional boolean

created_from_emdash_plugin: optional object { type, version } 

type: "native" or "rest"

One of the following:

"native"

"rest"

version: string

worker_domain: optional string

modified_by: optional string

namespace: optional string

paused: optional boolean

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 5 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

reranking: optional boolean

reranking_model: optional string

retrieval_options: optional object { boost_by, keyword_match_mode } 

boost_by: optional array of object { field, direction } 

Metadata fields to boost search results by. Each entry specifies a metadata field and an optional direction. Direction defaults to ‘asc’ for numeric/datetime fields and ‘exists’ for text/boolean fields. Fields must match ‘timestamp’ or a defined custom_metadata field.

field: string

Metadata field name to boost by. Use ‘timestamp’ for document freshness, or any custom_metadata field. Numeric and datetime fields support all four directions (asc, desc, exists, not_exists); text/boolean fields only support exists/not_exists.

maxLength64

minLength1

direction: optional "asc" or "desc" or "exists" or "not_exists"

Boost direction. ‘desc’ = higher values rank higher (e.g. newer timestamps). ‘asc’ = lower values rank higher. ‘exists’ = boost chunks that have the field. ‘not_exists’ = boost chunks that lack the field. Optional — defaults to ‘asc’ for numeric/datetime fields, ‘exists’ for text/boolean fields.

One of the following:

"asc"

"desc"

"exists"

"not_exists"

keyword_match_mode: optional "and" or "or"

Controls which documents are candidates for BM25 scoring. ‘and’ restricts candidates to documents containing all query terms; ‘or’ includes any document containing at least one term, ranked by BM25 relevance. When omitted on an update, the existing stored value is preserved; when never set, search falls back to ‘and’.

One of the following:

"and"

"or"

rewrite_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

rewrite_query: optional boolean

score_threshold: optional number

maximum1

minimum0

source: optional string

source_params: optional object { exclude_items, include_items, prefix, 2 more } 

exclude_items: optional array of string

List of path patterns to exclude. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /admin/** matches /admin/users and /admin/settings/advanced). Most accounts are limited to 10 rules; contact support to raise it.

include_items: optional array of string

List of path patterns to include. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most accounts are limited to 10 rules; contact support to raise it.

prefix: optional string

r2_jurisdiction: optional string

web_crawler: optional object { discover_options, parse_options, parse_type } 

discover_options: optional object { depth, include_external_links, include_subdomains, 3 more } 

Options for parse_type ‘discover’, where Browser Run discovers URLs by link following and sitemaps. Ignored for ‘sitemap’.

depth: optional number

Maximum link-follow depth from the seed URL.

maximum100000

minimum1

include_external_links: optional boolean

Follow links that point outside the source domain. Must stay `false` — discover crawls are restricted to the zone you own.

include_subdomains: optional boolean

Follow links to subdomains of the source host.

limit: optional number

Maximum number of pages to crawl (1-100000).

maximum100000

minimum1

max_age: optional number

Maximum content age in seconds to accept (0–604800).

maximum604800

minimum0

source: optional "all" or "sitemaps" or "links"

Where the crawler looks for URLs: ‘sitemaps’ reads sitemap XML only, ‘links’ follows page links only, ‘all’ does both.

One of the following:

"all"

"sitemaps"

"links"

parse_options: optional object { content_selector, include_headers, include_images, 2 more } 

content_selector: optional array of object { path, selector } 

List of path-to-selector mappings for extracting specific content from crawled pages. Each entry pairs a URL glob pattern with a CSS selector. The first matching path wins. Only the matched HTML fragment is stored and indexed. Omit the field to disable content selection — empty arrays are rejected.

path: string

Glob pattern to match against the page URL path. Uses standard glob syntax: * matches within a segment, ** crosses directories.

maxLength200

minLength1

selector: string

CSS selector to extract content from pages matching the path pattern. Must not contain disallowed characters (;, `, $, {, }, ). Must target a single element; if multiple elements match, the selector is ignored and the full page is used.

maxLength200

minLength1

include_headers: optional map[string]

Up to 5 custom HTTP headers sent with each crawl request. Names must be RFC-7230 token characters (no spaces, colons, or control characters); values must be HTAB + printable ASCII (no CR/LF).

include_images: optional boolean

specific_sitemaps: optional array of string

List of specific sitemap URLs to use for crawling. Only valid when parse_type is ‘sitemap’.

use_browser_rendering: optional boolean

parse_type: optional "sitemap" or "discover"

How URLs are discovered. ‘sitemap’ reads XML sitemaps; ‘discover’ follows links recursively and requires the source to be a Verified zone on this account.

One of the following:

"sitemap"

"discover"

status: optional string

sync_interval: optional 900 or 1800 or 3600 or 5 more

Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).

One of the following:

900

1800

3600

7200

14400

21600

43200

86400

token_id: optional string

formatuuid

type: optional "r2" or "web-crawler"

Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer web-crawler and existing R2 bucket names infer r2. A missing or blank source without a type uses managed upload-only storage.

One of the following:

"r2"

"web-crawler"

InstanceUpdateResponse object { id, created_at, modified_at, 36 more } 

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

created_at: string

formatdate-time

modified_at: string

formatdate-time

ai_gateway_id: optional string

ai_search_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

cache: optional boolean

cache_threshold: optional "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

cache_ttl: optional 600 or 1800 or 3600 or 7 more

Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).

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

chunk_overlap: optional number

maximum30

minimum0

chunk_size: optional number

minimum64

created_by: optional string

custom_metadata: optional array of object { data_type, field_name } 

data_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field_name: string

maxLength64

minLength1

embedding_model: optional string

enable: optional boolean

engine_version: optional number

fusion_method: optional "max" or "rrf"

One of the following:

"max"

"rrf"

Deprecatedhybrid_search_enabled: optional boolean

Deprecated — use index_method instead. Defaults to true for new instances; set false to create a vector-only instance.

index_method: optional object { keyword, vector } 

Controls which storage backends are used during indexing. Defaults to vector and keyword indexing for new instances.

keyword: boolean

Enable keyword (BM25) storage backend.

vector: boolean

Enable vector (embedding) storage backend.

indexing_options: optional object { keyword_tokenizer, use_ocr } 

keyword_tokenizer: optional "porter" or "trigram"

Tokenizer used for keyword search indexing. porter provides word-level tokenization with Porter stemming (good for natural language queries). trigram enables character-level substring matching (good for partial matches, code, identifiers). Changing this triggers a full re-index. Defaults to porter.

One of the following:

"porter"

"trigram"

use_ocr: optional boolean

Enables OCR ingestion for PDFs and images. Changing this triggers a full re-index. Defaults to false.

last_activity: optional string

formatdate-time

max_num_results: optional number

maximum50

minimum1

metadata: optional object { created_from_aisearch_wizard, created_from_emdash_plugin, worker_domain } 

created_from_aisearch_wizard: optional boolean

created_from_emdash_plugin: optional object { type, version } 

type: "native" or "rest"

One of the following:

"native"

"rest"

version: string

worker_domain: optional string

modified_by: optional string

namespace: optional string

paused: optional boolean

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 5 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

reranking: optional boolean

reranking_model: optional string

retrieval_options: optional object { boost_by, keyword_match_mode } 

boost_by: optional array of object { field, direction } 

Metadata fields to boost search results by. Each entry specifies a metadata field and an optional direction. Direction defaults to ‘asc’ for numeric/datetime fields and ‘exists’ for text/boolean fields. Fields must match ‘timestamp’ or a defined custom_metadata field.

field: string

Metadata field name to boost by. Use ‘timestamp’ for document freshness, or any custom_metadata field. Numeric and datetime fields support all four directions (asc, desc, exists, not_exists); text/boolean fields only support exists/not_exists.

maxLength64

minLength1

direction: optional "asc" or "desc" or "exists" or "not_exists"

Boost direction. ‘desc’ = higher values rank higher (e.g. newer timestamps). ‘asc’ = lower values rank higher. ‘exists’ = boost chunks that have the field. ‘not_exists’ = boost chunks that lack the field. Optional — defaults to ‘asc’ for numeric/datetime fields, ‘exists’ for text/boolean fields.

One of the following:

"asc"

"desc"

"exists"

"not_exists"

keyword_match_mode: optional "and" or "or"

Controls which documents are candidates for BM25 scoring. ‘and’ restricts candidates to documents containing all query terms; ‘or’ includes any document containing at least one term, ranked by BM25 relevance. When omitted on an update, the existing stored value is preserved; when never set, search falls back to ‘and’.

One of the following:

"and"

"or"

rewrite_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

rewrite_query: optional boolean

score_threshold: optional number

maximum1

minimum0

source: optional string

source_params: optional object { exclude_items, include_items, prefix, 2 more } 

exclude_items: optional array of string

List of path patterns to exclude. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /admin/** matches /admin/users and /admin/settings/advanced). Most accounts are limited to 10 rules; contact support to raise it.

include_items: optional array of string

List of path patterns to include. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most accounts are limited to 10 rules; contact support to raise it.

prefix: optional string

r2_jurisdiction: optional string

web_crawler: optional object { discover_options, parse_options, parse_type } 

discover_options: optional object { depth, include_external_links, include_subdomains, 3 more } 

Options for parse_type ‘discover’, where Browser Run discovers URLs by link following and sitemaps. Ignored for ‘sitemap’.

depth: optional number

Maximum link-follow depth from the seed URL.

maximum100000

minimum1

include_external_links: optional boolean

Follow links that point outside the source domain. Must stay `false` — discover crawls are restricted to the zone you own.

include_subdomains: optional boolean

Follow links to subdomains of the source host.

limit: optional number

Maximum number of pages to crawl (1-100000).

maximum100000

minimum1

max_age: optional number

Maximum content age in seconds to accept (0–604800).

maximum604800

minimum0

source: optional "all" or "sitemaps" or "links"

Where the crawler looks for URLs: ‘sitemaps’ reads sitemap XML only, ‘links’ follows page links only, ‘all’ does both.

One of the following:

"all"

"sitemaps"

"links"

parse_options: optional object { content_selector, include_headers, include_images, 2 more } 

content_selector: optional array of object { path, selector } 

List of path-to-selector mappings for extracting specific content from crawled pages. Each entry pairs a URL glob pattern with a CSS selector. The first matching path wins. Only the matched HTML fragment is stored and indexed. Omit the field to disable content selection — empty arrays are rejected.

path: string

Glob pattern to match against the page URL path. Uses standard glob syntax: * matches within a segment, ** crosses directories.

maxLength200

minLength1

selector: string

CSS selector to extract content from pages matching the path pattern. Must not contain disallowed characters (;, `, $, {, }, ). Must target a single element; if multiple elements match, the selector is ignored and the full page is used.

maxLength200

minLength1

include_headers: optional map[string]

Up to 5 custom HTTP headers sent with each crawl request. Names must be RFC-7230 token characters (no spaces, colons, or control characters); values must be HTAB + printable ASCII (no CR/LF).

include_images: optional boolean

specific_sitemaps: optional array of string

List of specific sitemap URLs to use for crawling. Only valid when parse_type is ‘sitemap’.

use_browser_rendering: optional boolean

parse_type: optional "sitemap" or "discover"

How URLs are discovered. ‘sitemap’ reads XML sitemaps; ‘discover’ follows links recursively and requires the source to be a Verified zone on this account.

One of the following:

"sitemap"

"discover"

status: optional string

sync_interval: optional 900 or 1800 or 3600 or 5 more

Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).

One of the following:

900

1800

3600

7200

14400

21600

43200

86400

token_id: optional string

formatuuid

type: optional "r2" or "web-crawler"

Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer web-crawler and existing R2 bucket names infer r2. A missing or blank source without a type uses managed upload-only storage.

One of the following:

"r2"

"web-crawler"

InstanceDeleteResponse object { id, created_at, modified_at, 36 more } 

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

created_at: string

formatdate-time

modified_at: string

formatdate-time

ai_gateway_id: optional string

ai_search_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

cache: optional boolean

cache_threshold: optional "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

cache_ttl: optional 600 or 1800 or 3600 or 7 more

Cache entry TTL in seconds. Allowed values: 600 (10min), 1800 (30min), 3600 (1h), 7200 (2h), 21600 (6h), 43200 (12h), 86400 (24h), 172800 (48h), 259200 (72h), 518400 (6d).

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

chunk_overlap: optional number

maximum30

minimum0

chunk_size: optional number

minimum64

created_by: optional string

custom_metadata: optional array of object { data_type, field_name } 

data_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field_name: string

maxLength64

minLength1

embedding_model: optional string

enable: optional boolean

engine_version: optional number

fusion_method: optional "max" or "rrf"

One of the following:

"max"

"rrf"

Deprecatedhybrid_search_enabled: optional boolean

Deprecated — use index_method instead. Defaults to true for new instances; set false to create a vector-only instance.

index_method: optional object { keyword, vector } 

Controls which storage backends are used during indexing. Defaults to vector and keyword indexing for new instances.

keyword: boolean

Enable keyword (BM25) storage backend.

vector: boolean

Enable vector (embedding) storage backend.

indexing_options: optional object { keyword_tokenizer, use_ocr } 

keyword_tokenizer: optional "porter" or "trigram"

Tokenizer used for keyword search indexing. porter provides word-level tokenization with Porter stemming (good for natural language queries). trigram enables character-level substring matching (good for partial matches, code, identifiers). Changing this triggers a full re-index. Defaults to porter.

One of the following:

"porter"

"trigram"

use_ocr: optional boolean

Enables OCR ingestion for PDFs and images. Changing this triggers a full re-index. Defaults to false.

last_activity: optional string

formatdate-time

max_num_results: optional number

maximum50

minimum1

metadata: optional object { created_from_aisearch_wizard, created_from_emdash_plugin, worker_domain } 

created_from_aisearch_wizard: optional boolean

created_from_emdash_plugin: optional object { type, version } 

type: "native" or "rest"

One of the following:

"native"

"rest"

version: string

worker_domain: optional string

modified_by: optional string

namespace: optional string

paused: optional boolean

public_endpoint_id: optional string

public_endpoint_params: optional object { authorized_hosts, chat_completions_endpoint, custom_domains, 5 more } 

authorized_hosts: optional array of string

chat_completions_endpoint: optional object { disabled } 

disabled: optional boolean

Disable chat completions endpoint for this public endpoint

custom_domains: optional array of string

Custom domain hostnames that alias this public endpoint. GET and create responses return the current set; on update (PUT) this field is only echoed back when supplied in the request body, otherwise it is null (omit it to leave domains unchanged).

default_domain_enabled: optional boolean

When false, the instance is reachable only via a registered custom domain and the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404. Requires at least one custom domain. Defaults to true. public_endpoint_params is replaced wholesale on update, so resend default_domain_enabled on every update to keep the default host off — omitting it resets to true.

enabled: optional boolean

mcp: optional object { description, disabled } 

description: optional string

disabled: optional boolean

Disable MCP endpoint for this public endpoint

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

Disable search endpoint for this public endpoint

reranking: optional boolean

reranking_model: optional string

retrieval_options: optional object { boost_by, keyword_match_mode } 

boost_by: optional array of object { field, direction } 

Metadata fields to boost search results by. Each entry specifies a metadata field and an optional direction. Direction defaults to ‘asc’ for numeric/datetime fields and ‘exists’ for text/boolean fields. Fields must match ‘timestamp’ or a defined custom_metadata field.

field: string

Metadata field name to boost by. Use ‘timestamp’ for document freshness, or any custom_metadata field. Numeric and datetime fields support all four directions (asc, desc, exists, not_exists); text/boolean fields only support exists/not_exists.

maxLength64

minLength1

direction: optional "asc" or "desc" or "exists" or "not_exists"

Boost direction. ‘desc’ = higher values rank higher (e.g. newer timestamps). ‘asc’ = lower values rank higher. ‘exists’ = boost chunks that have the field. ‘not_exists’ = boost chunks that lack the field. Optional — defaults to ‘asc’ for numeric/datetime fields, ‘exists’ for text/boolean fields.

One of the following:

"asc"

"desc"

"exists"

"not_exists"

keyword_match_mode: optional "and" or "or"

Controls which documents are candidates for BM25 scoring. ‘and’ restricts candidates to documents containing all query terms; ‘or’ includes any document containing at least one term, ranked by BM25 relevance. When omitted on an update, the existing stored value is preserved; when never set, search falls back to ‘and’.

One of the following:

"and"

"or"

rewrite_model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

rewrite_query: optional boolean

score_threshold: optional number

maximum1

minimum0

source: optional string

source_params: optional object { exclude_items, include_items, prefix, 2 more } 

exclude_items: optional array of string

List of path patterns to exclude. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /admin/** matches /admin/users and /admin/settings/advanced). Most accounts are limited to 10 rules; contact support to raise it.

include_items: optional array of string

List of path patterns to include. Uses micromatch glob syntax: * matches within a path segment, ** matches across path segments (e.g., /blog/** matches /blog/post and /blog/2024/post). Most accounts are limited to 10 rules; contact support to raise it.

prefix: optional string

r2_jurisdiction: optional string

web_crawler: optional object { discover_options, parse_options, parse_type } 

discover_options: optional object { depth, include_external_links, include_subdomains, 3 more } 

Options for parse_type ‘discover’, where Browser Run discovers URLs by link following and sitemaps. Ignored for ‘sitemap’.

depth: optional number

Maximum link-follow depth from the seed URL.

maximum100000

minimum1

include_external_links: optional boolean

Follow links that point outside the source domain. Must stay `false` — discover crawls are restricted to the zone you own.

include_subdomains: optional boolean

Follow links to subdomains of the source host.

limit: optional number

Maximum number of pages to crawl (1-100000).

maximum100000

minimum1

max_age: optional number

Maximum content age in seconds to accept (0–604800).

maximum604800

minimum0

source: optional "all" or "sitemaps" or "links"

Where the crawler looks for URLs: ‘sitemaps’ reads sitemap XML only, ‘links’ follows page links only, ‘all’ does both.

One of the following:

"all"

"sitemaps"

"links"

parse_options: optional object { content_selector, include_headers, include_images, 2 more } 

content_selector: optional array of object { path, selector } 

List of path-to-selector mappings for extracting specific content from crawled pages. Each entry pairs a URL glob pattern with a CSS selector. The first matching path wins. Only the matched HTML fragment is stored and indexed. Omit the field to disable content selection — empty arrays are rejected.

path: string

Glob pattern to match against the page URL path. Uses standard glob syntax: * matches within a segment, ** crosses directories.

maxLength200

minLength1

selector: string

CSS selector to extract content from pages matching the path pattern. Must not contain disallowed characters (;, `, $, {, }, ). Must target a single element; if multiple elements match, the selector is ignored and the full page is used.

maxLength200

minLength1

include_headers: optional map[string]

Up to 5 custom HTTP headers sent with each crawl request. Names must be RFC-7230 token characters (no spaces, colons, or control characters); values must be HTAB + printable ASCII (no CR/LF).

include_images: optional boolean

specific_sitemaps: optional array of string

List of specific sitemap URLs to use for crawling. Only valid when parse_type is ‘sitemap’.

use_browser_rendering: optional boolean

parse_type: optional "sitemap" or "discover"

How URLs are discovered. ‘sitemap’ reads XML sitemaps; ‘discover’ follows links recursively and requires the source to be a Verified zone on this account.

One of the following:

"sitemap"

"discover"

status: optional string

sync_interval: optional 900 or 1800 or 3600 or 5 more

Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).

One of the following:

900

1800

3600

7200

14400

21600

43200

86400

token_id: optional string

formatuuid

type: optional "r2" or "web-crawler"

Source type. When omitted or null with a non-blank source, HTTP(S) URLs infer web-crawler and existing R2 bucket names infer r2. A missing or blank source without a type uses managed upload-only storage.

One of the following:

"r2"

"web-crawler"

InstanceStatsResponse object { completed, degraded, engine, 8 more } 

completed: optional number

degraded: optional boolean

True when status counts are unavailable (e.g. legacy stats query exceeded D1 statement-size limit). Counts are omitted in this case.

engine: optional object { r2, vectorize } 

Engine-specific metadata. Present only for managed (v3) instances.

r2: optional object { metadataSizeBytes, objectCount, payloadSizeBytes } 

R2 bucket storage usage in bytes.

metadataSizeBytes: number

objectCount: number

payloadSizeBytes: number

vectorize: optional object { dimensions, vectorsCount } 

Vectorize index metadata (dimensions, vector count).

dimensions: number

vectorsCount: number

error: optional number

file_embed_errors: optional map[unknown]

index_source_errors: optional map[unknown]

last_activity: optional string

formatdate-time

outdated: optional number

queued: optional number

running: optional number

skipped: optional number

InstanceSearchResponse object { chunks, query_kind, search_query } 

chunks: array of object { id, score, text, 3 more } 

id: string

score: number

maximum1

minimum0

text: string

type: string

item: optional object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

scoring_details: optional object { fusion_method, keyword_rank, keyword_score, 3 more } 

fusion_method: optional "rrf" or "max"

One of the following:

"rrf"

"max"

keyword_rank: optional number

keyword_score: optional number

minimum0

reranking_score: optional number

maximum1

minimum0

vector_rank: optional number

vector_score: optional number

maximum1

minimum0

query_kind: "text" or "image" or "multimodal"

One of the following:

"text"

"image"

"multimodal"

search_query: optional string

InstanceChatCompletionsResponse object { choices, chunks, id, 2 more } 

choices: array of object { message, index } 

message: object { content, role } 

content: string or array of object { text, type }  or object { image_url, type }  or object { file, type }  or string

One of the following:

string

array of object { text, type }  or object { image_url, type }  or object { file, type } 

One of the following:

object { text, type } 

text: string

minLength1

type: "text"

object { image_url, type } 

image_url: object { url } 

url: string

maxLength20971520

minLength1

type: "image_url"

object { file, type } 

file: object { filename, file_data, file_id } 

filename: string

maxLength255

minLength1

file_data: optional string

maxLength13981144

minLength1

file_id: optional string

type: "file"

string

role: "system" or "developer" or "user" or 2 more

One of the following:

"system"

"developer"

"user"

"assistant"

"tool"

index: optional number

chunks: array of object { id, score, text, 3 more } 

id: string

score: number

maximum1

minimum0

text: string

type: string

item: optional object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

scoring_details: optional object { fusion_method, keyword_rank, keyword_score, 3 more } 

fusion_method: optional "rrf" or "max"

One of the following:

"rrf"

"max"

keyword_rank: optional number

keyword_score: optional number

minimum0

reranking_score: optional number

maximum1

minimum0

vector_rank: optional number

vector_score: optional number

maximum1

minimum0

id: optional string

model: optional string

object: optional string

#### NamespacesInstancesJobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Create new job](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [Cancel an indexing job.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/update)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs

##### ModelsExpand Collapse 

JobListResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobCreateResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobGetResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobUpdateResponse object { id, source, description, 4 more } 

id: string

source: "user" or "schedule"

One of the following:

"user"

"schedule"

description: optional string

end_reason: optional string

ended_at: optional string

last_seen_at: optional string

started_at: optional string

JobLogsResponse = array of object { id, created_at, message, message_type } 

id: number

created_at: number

message: string

message_type: number

#### NamespacesInstancesItems

##### [Items List.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Upload Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload)

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Create or Update Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/create_or_update)

PUT/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items

##### [Get Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Sync Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/sync)

PATCH/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Delete Item.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete)

DELETE/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}

##### [Download Item Content.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/download

##### [Item Logs.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/logs)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/logs

##### [List Item Chunks.](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/chunks)

GET/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/items/{item_id}/chunks

##### ModelsExpand Collapse 

ItemListResponse object { id, checksum, chunks_count, 10 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

ItemUploadResponse object { id, checksum, chunks_count, 11 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

warnings: optional array of object { code, expected_type, field }  or object { code, field } 

One of the following:

object { code, expected_type, field } 

code: "custom_metadata_value_not_indexed"

expected_type: "text" or "number" or "boolean" or "datetime"

One of the following:

"text"

"number"

"boolean"

"datetime"

field: string

maxLength512

object { code, field } 

code: "custom_metadata_field_not_filterable"

field: string

maxLength512

ItemCreateOrUpdateResponse object { id, checksum, chunks_count, 10 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

ItemGetResponse object { id, checksum, chunks_count, 10 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

ItemSyncResponse object { id, checksum, chunks_count, 10 more } 

id: string

checksum: string

chunks_count: number

created_at: string

formatdate-time

file_size: number

key: string

last_seen_at: string

formatdate-time

metadata: map[string or number or boolean]

Built-in, configured filterable, and retained source metadata for the item.

One of the following:

string

number

boolean

namespace: string

next_action: "INDEX" or "DELETE"

One of the following:

"INDEX"

"DELETE"

source_id: string

Identifies which data source this item belongs to. “builtin” for uploaded files, “{type}:{source}” for external sources, null for legacy items.

status: "queued" or "running" or "completed" or 3 more

One of the following:

"queued"

"running"

"completed"

"error"

"skipped"

"outdated"

error: optional string

ItemDeleteResponse object { key } 

key: string

ItemLogsResponse = array of object { action, chunkCount, errorType, 4 more } 

action: string

chunkCount: number

errorType: string

fileKey: string

message: string

processingTimeMs: number

timestamp: string

formatdate-time

ItemChunksResponse = array of object { id, item, text, 2 more } 

id: string

item: object { key, metadata, timestamp } 

key: string

metadata: optional map[unknown]

timestamp: optional number

text: string

end_byte: optional number

start_byte: optional number

[ Previous

* * *

AI Search ](https://developers.cloudflare.com/api/resources/ai_search)[ Next

* * *

Instances ](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances)
