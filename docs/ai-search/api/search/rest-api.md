---
url: https://developers.cloudflare.com/ai-search/api/search/rest-api/
title: REST API \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:38.753066+00:00
---

# REST API · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/search/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Search
  5. /REST API



# REST API

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/api/search/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationSearch and chat API paths Search Chat completions Image queriesCross-instance search and chat

Use the AI Search REST API to query your AI Search instances over HTTP.

## Authentication

All requests require an API token with **AI Search:Edit** and **AI Search:Run** permissions.

  1. In the Cloudflare dashboard, go to **My Profile** > **API Tokens**.

[ Go to **API Tokens** ↗ ](https://dash.cloudflare.com/profile/api-tokens)
  2. Select **Create Token**.

  3. Select **Create Custom Token**.

  4. Enter a **Token name** , for example `AI Search Manager`.

  5. Under **Permissions** , add two permissions:

     * **Account** > **AI Search:Edit**
     * **Account** > **AI Search:Run**
  6. Select **Continue to summary** , then select **Create Token**.

  7. Copy and save the token value. This is your `API_TOKEN`.




Include the token in the `Authorization` header for all requests:
    
    
    Authorization: Bearer <API_TOKEN>

## Search and chat

AI Search provides two APIs for querying an instance. Both use an OpenAI-compatible `messages` format.

  * **Search** returns relevant content chunks. Use this when you want to handle generation yourself or display results directly.
  * **Chat completions** retrieves content and generates a response in one call.



### API paths

Search and chat APIs are scoped to a [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/):

Path | Description  
---|---  
`/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}/` | Operates on a specific instance within a namespace  
  
Every account has a `default` namespace. Use `default` unless you created a custom namespace. For the full specification, refer to the [Namespace API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/).

### Search

Search a specific instance. The search endpoint also accepts a `query` string parameter. For the full specification, refer to the [Search API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/).
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/search" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {
            "content": "What is Cloudflare?",
            "role": "user"
          }
        ]
      }'

### Chat completions

Generate a response from a specific instance. For the full specification, refer to the [Chat completions API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/).
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/chat/completions" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {
            "content": "What is Cloudflare?",
            "role": "user"
          }
        ]
      }'

### Image queries

Set `messages[].content` to an array of content parts. Use an `image_url` part with an HTTPS URL or an inline `data:image/<subtype>;base64,...` URI.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/search" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [{
          "role": "user",
          "content": [{
            "type": "image_url",
            "image_url": { "url": "https://example.com/product.png" }
          }]
        }]
      }'

The response includes `query_kind` as `image`. Image-only responses omit `search_query`. Add a `text` part to create a multimodal query. Native image embedding requires `@cf/qwen/qwen3-vl-embedding-2b` or `google-ai-studio/gemini-embedding-2`. Text-only embedding models caption the image before embedding it.

#### Streaming

Set `stream` to `true` to receive responses as Server-Sent Events (SSE). The retrieved chunks are sent first as a `chunks` event, followed by the streamed response.
    
    
    event: chunks
    data: [{"id":"chunk-001","type":"text","score":0.85,"text":"...","item":{"key":"about-cloudflare.md","timestamp":1775925540000},"scoring_details":{"vector_score":0.85}}]
    
    data: {"id":"id-1776072781845","created":1776072781,"model":"@cf/meta/llama-3.3-70b-instruct-fp8-fast","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" document"}}]}
    
    data: {"id":"id-1776072781845","created":1776072781,"model":"@cf/meta/llama-3.3-70b-instruct-fp8-fast","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" you provided doesn"}}]}
    
    data: {"id":"id-1776072781845","created":1776072781,"model":"@cf/meta/llama-3.3-70b-instruct-fp8-fast","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"'t contain"}}]}
    
    data: {"id":"id-1776072781845","created":1776072781,"model":"@cf/meta/llama-3.3-70b-instruct-fp8-fast","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" information"}}]}
    
    data: [DONE]

## Cross-instance search and chat

The search and chat completions APIs are also available at the namespace level. These work the same as the instance endpoints, but you pass an `instance_ids` array to specify which instances to query. Each chunk in the response includes an `instance_id` field identifying which instance it came from. For the full specification, refer to the [Namespace API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/).
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/<NAMESPACE>/search" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {
            "role": "user",
            "content": "What is Cloudflare?"
          }
        ],
        "ai_search_options": {
          "instance_ids": ["product-docs", "customer-abc123"]
        }
      }'

[PreviousWorkers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)[NextMCP](https://developers.cloudflare.com/ai-search/api/search/mcp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/search/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
