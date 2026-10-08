---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/
title: New AI Search REST API endpoints for /search and /chat/completions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.159193+00:00
---

# New AI Search REST API endpoints for /search and /chat/completions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## New AI Search REST API endpoints for /search and /chat/completions

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-ai-search-new-rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now offers new [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/) endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar `messages` array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.

Endpoint | Path  
---|---  
Chat Completions | `POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions`  
Search | `POST /accounts/{account_id}/ai-search/instances/{name}/search`  
  
Here is an example request to the Chat Completions endpoint using the new `messages` array format:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful documentation assistant."
          },
          {
            "role": "user",
            "content": "How do I get started?"
          }
        ]
      }'

For more details, refer to the [AI Search REST API guide](https://developers.cloudflare.com/ai-search/api/search/rest-api/).

#### Migration from existing AutoRAG API (recommended)

If you are using the previous AutoRAG API endpoints (`/autorag/rags/`), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.

Refer to the [migration guide](https://developers.cloudflare.com/ai-search/api/migration/rest-api/) for step-by-step instructions.
