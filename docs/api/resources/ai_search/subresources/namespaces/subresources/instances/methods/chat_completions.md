---
url: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/
title: Chat Completions | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:23:05.547366+00:00
---

# Chat Completions | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/

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

# Chat Completions

POST/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/chat/completions

Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.

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

id: string

AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

maxLength64

minLength1

##### Body ParametersJSONExpand Collapse 

messages: array of object { content, role } 

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

ai_search_options: optional object { cache, custom_metadata, query_rewrite, 2 more } 

cache: optional object { cache_threshold, enabled } 

cache_threshold: optional "super_strict_match" or "close_enough" or "flexible_friend" or "anything_goes"

One of the following:

"super_strict_match"

"close_enough"

"flexible_friend"

"anything_goes"

enabled: optional boolean

custom_metadata: optional map[string or number or boolean]

Metadata added to AI Gateway logs for requests triggered by this operation. Accepts up to 2 string, number, or boolean entries. Keys ‘ai-search’, ‘task’, ‘origin’, and keys beginning with ‘cf.’ are reserved.

One of the following:

string

number

boolean

query_rewrite: optional object { enabled, model, rewrite_prompt } 

enabled: optional boolean

model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

rewrite_prompt: optional string

reranking: optional object { enabled, match_threshold, model } 

enabled: optional boolean

match_threshold: optional number

maximum1

minimum0

model: optional string

retrieval: optional object { boost_by, context_expansion, filters, 6 more } 

boost_by: optional array of object { field, direction } 

Metadata fields to boost search results by. Overrides the instance-level boost_by config. Direction defaults to ‘asc’ for numeric/datetime fields, ‘exists’ for text/boolean fields. Fields must match ‘timestamp’ or a defined custom_metadata field.

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

context_expansion: optional number

maximum3

minimum0

filters: optional map[unknown]

fusion_method: optional "max" or "rrf"

One of the following:

"max"

"rrf"

keyword_match_mode: optional "and" or "or"

Controls which documents are candidates for BM25 scoring. ‘and’ restricts candidates to documents containing all query terms; ‘or’ includes any document containing at least one term, ranked by BM25 relevance. When omitted, falls back to the instance-level retrieval_options.keyword_match_mode, then to ‘and’.

One of the following:

"and"

"or"

match_threshold: optional number

maximum1

minimum0

max_num_results: optional number

maximum50

minimum1

retrieval_type: optional "vector" or "keyword" or "hybrid"

One of the following:

"vector"

"keyword"

"hybrid"

return_on_failure: optional boolean

model: optional string

A Workers AI model ID or an AI Gateway model ID compatible with the OpenAI Chat Completions API. An empty string uses the configured or default model.

stream: optional boolean

##### ReturnsExpand Collapse 

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

### Chat Completions

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/$NAME/instances/$ID/chat/completions \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "messages": [
                {
                  "content": "string",
                  "role": "system"
                }
              ]
            }'

200 example
    
    
    {
      "choices": [
        {
          "message": {
            "content": "string",
            "role": "system"
          },
          "index": 0
        }
      ],
      "chunks": [
        {
          "id": "id",
          "score": 0,
          "text": "text",
          "type": "type",
          "item": {
            "key": "key",
            "metadata": {
              "foo": "bar"
            },
            "timestamp": 0
          },
          "scoring_details": {
            "fusion_method": "rrf",
            "keyword_rank": 0,
            "keyword_score": 0,
            "reranking_score": 0,
            "vector_rank": 0,
            "vector_score": 0
          }
        }
      ],
      "id": "id",
      "model": "model",
      "object": "object"
    }

##### Returns Examples

200 example
    
    
    {
      "choices": [
        {
          "message": {
            "content": "string",
            "role": "system"
          },
          "index": 0
        }
      ],
      "chunks": [
        {
          "id": "id",
          "score": 0,
          "text": "text",
          "type": "type",
          "item": {
            "key": "key",
            "metadata": {
              "foo": "bar"
            },
            "timestamp": 0
          },
          "scoring_details": {
            "fusion_method": "rrf",
            "keyword_rank": 0,
            "keyword_score": 0,
            "reranking_score": 0,
            "vector_rank": 0,
            "vector_score": 0
          }
        }
      ],
      "id": "id",
      "model": "model",
      "object": "object"
    }
