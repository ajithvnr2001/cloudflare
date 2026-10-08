---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/
title: Create an AI Search instance. | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:22:36.984689+00:00
---

# Create an AI Search instance. | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/

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

# Create an AI Search instance.

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances

Create a new AI Search instance with the given configuration. If type is omitted or null, a non-blank HTTP(S) source infers web-crawler and any other source infers r2; r2 sources must name an existing bucket. A missing or blank source without a type creates a managed upload-only instance.

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

##### Body ParametersJSONExpand Collapse 

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

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

chunk: optional boolean

chunk_overlap: optional number

maximum30

minimum0

chunk_size: optional number

minimum64

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

##### ReturnsExpand Collapse 

result: object { id, created_at, modified_at, 36 more } 

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

success: boolean

### Create an AI Search instance.

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
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "id": "my-ai-search"
            }'

200 example
    
    
    {
      "result": {
        "id": "my-ai-search",
        "created_at": "2019-12-27T18:11:19.117Z",
        "modified_at": "2019-12-27T18:11:19.117Z",
        "ai_gateway_id": "ai_gateway_id",
        "ai_search_model": "ai_search_model",
        "cache": true,
        "cache_threshold": "super_strict_match",
        "cache_ttl": 600,
        "chunk_overlap": 0,
        "chunk_size": 64,
        "created_by": "created_by",
        "custom_metadata": [
          {
            "data_type": "text",
            "field_name": "x"
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
        "max_num_results": 1,
        "metadata": {
          "created_from_aisearch_wizard": true,
          "created_from_emdash_plugin": {
            "type": "native",
            "version": "version"
          },
          "worker_domain": "worker_domain"
        },
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
            "search.example.com"
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
              "field": "timestamp",
              "direction": "desc"
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
            "/admin/**",
            "/private/**",
            "**\\temp\\**"
          ],
          "include_items": [
            "/blog/**",
            "/docs/**/*.html",
            "**\\blog\\**.html"
          ],
          "prefix": "prefix",
          "r2_jurisdiction": "r2_jurisdiction",
          "web_crawler": {
            "discover_options": {
              "depth": 5,
              "include_external_links": false,
              "include_subdomains": false,
              "limit": 10000,
              "max_age": 86400,
              "source": "all"
            },
            "parse_options": {
              "content_selector": [
                {
                  "path": "**/blog/**",
                  "selector": "article div.post-body"
                },
                {
                  "path": "**/docs/**",
                  "selector": "main"
                }
              ],
              "include_headers": {
                "cache-control": "no-cache, no-store"
              },
              "include_images": true,
              "specific_sitemaps": [
                "https://example.com/sitemap.xml",
                "https://example.com/blog-sitemap.xml"
              ],
              "use_browser_rendering": true
            },
            "parse_type": "sitemap"
          }
        },
        "status": "status",
        "sync_interval": 900,
        "token_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "type": "r2"
      },
      "success": true
    }

##### Returns Examples

200 example
    
    
    {
      "result": {
        "id": "my-ai-search",
        "created_at": "2019-12-27T18:11:19.117Z",
        "modified_at": "2019-12-27T18:11:19.117Z",
        "ai_gateway_id": "ai_gateway_id",
        "ai_search_model": "ai_search_model",
        "cache": true,
        "cache_threshold": "super_strict_match",
        "cache_ttl": 600,
        "chunk_overlap": 0,
        "chunk_size": 64,
        "created_by": "created_by",
        "custom_metadata": [
          {
            "data_type": "text",
            "field_name": "x"
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
        "max_num_results": 1,
        "metadata": {
          "created_from_aisearch_wizard": true,
          "created_from_emdash_plugin": {
            "type": "native",
            "version": "version"
          },
          "worker_domain": "worker_domain"
        },
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
            "search.example.com"
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
              "field": "timestamp",
              "direction": "desc"
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
            "/admin/**",
            "/private/**",
            "**\\temp\\**"
          ],
          "include_items": [
            "/blog/**",
            "/docs/**/*.html",
            "**\\blog\\**.html"
          ],
          "prefix": "prefix",
          "r2_jurisdiction": "r2_jurisdiction",
          "web_crawler": {
            "discover_options": {
              "depth": 5,
              "include_external_links": false,
              "include_subdomains": false,
              "limit": 10000,
              "max_age": 86400,
              "source": "all"
            },
            "parse_options": {
              "content_selector": [
                {
                  "path": "**/blog/**",
                  "selector": "article div.post-body"
                },
                {
                  "path": "**/docs/**",
                  "selector": "main"
                }
              ],
              "include_headers": {
                "cache-control": "no-cache, no-store"
              },
              "include_images": true,
              "specific_sitemaps": [
                "https://example.com/sitemap.xml",
                "https://example.com/blog-sitemap.xml"
              ],
              "use_browser_rendering": true
            },
            "parse_type": "sitemap"
          }
        },
        "status": "status",
        "sync_interval": 900,
        "token_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "type": "r2"
      },
      "success": true
    }
