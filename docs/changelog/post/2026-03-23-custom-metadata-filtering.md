---
url: https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/
title: Custom metadata filtering for AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:42.474236+00:00
---

# Custom metadata filtering for AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 23, 2026

## Custom metadata filtering for AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-custom-metadata-filtering/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.

#### Define a custom metadata schema

You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (`text`, `number`, or `boolean`):
    
    
    curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "id": "my-instance",
        "type": "r2",
        "source": "my-bucket",
        "custom_metadata": [
          { "field_name": "category", "data_type": "text" },
          { "field_name": "version", "data_type": "number" },
          { "field_name": "is_public", "data_type": "boolean" }
        ]
      }'

#### Add metadata to your documents

How you attach metadata depends on your data source:

  * **R2 bucket** : Set metadata using S3-compatible custom headers (`x-amz-meta-*`) when uploading objects. Refer to [R2 custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/#custom-metadata) for examples.
  * **Website** : Add `<meta>` tags to your HTML pages. Refer to [Website custom metadata](https://developers.cloudflare.com/ai-search/configuration/data-source/website/custom-metadata/) for details.



#### Filter search results

Use custom metadata fields in your search queries alongside built-in attributes like `folder` and `timestamp`:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer {API_TOKEN}" \
      -d '{
        "messages": [
          {
            "content": "How do I configure authentication?",
            "role": "user"
          }
        ],
        "ai_search_options": {
          "retrieval": {
            "filters": {
              "category": "documentation",
              "version": { "$gte": 2.0 }
            }
          }
        }
      }'

Learn more in the [metadata filtering documentation](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).
