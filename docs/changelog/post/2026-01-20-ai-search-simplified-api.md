---
url: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-simplified-api/
title: Create AI Search instances programmatically via REST API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.941428+00:00
---

# Create AI Search instances programmatically via REST API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-20-ai-search-simplified-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 20, 2026

## Create AI Search instances programmatically via REST API

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create [AI Search](https://developers.cloudflare.com/ai-search/) instances programmatically using the [API](https://developers.cloudflare.com/ai-search/get-started/api/). For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.

If you have created an AI Search instance via the [dashboard](https://developers.cloudflare.com/ai-search/get-started/dashboard/) before, you already have a [service API token](https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/) registered and can start creating instances programmatically right away. If not, follow the [API guide](https://developers.cloudflare.com/ai-search/get-started/api/) to set up your first instance.

For example, you can now create separate search instances for each language on your website:
    
    
    for lang in en fr es de; do
      curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances" \
        -H "Authorization: Bearer $API_TOKEN" \
        -H "Content-Type: application/json" \
        --data '{
          "id": "docs-'"$lang"'",
          "type": "web-crawler",
          "source": "example.com",
          "source_params": {
            "path_include": ["**/'"$lang"'/**"]
          }
        }'
    done

Refer to the [REST API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/methods/create/) for additional configuration options.
