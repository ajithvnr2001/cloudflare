---
url: https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/
title: Website Source CSS content selectors for precise content extraction in AI Search \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.679809+00:00
---

# Website Source CSS content selectors for precise content extraction in AI Search · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2026

## Website Source CSS content selectors for precise content extraction in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-09-ai-search-content-selectors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) now supports [CSS content selectors](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/) for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.

Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.

Configure content selectors via the dashboard or API:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances" \
      -H "Authorization: Bearer {api_token}" \
      -H "Content-Type: application/json" \
      -d '{
        "id": "my-ai-search",
        "source": "https://example.com",
        "type": "web-crawler",
        "source_params": {
          "web_crawler": {
            "parse_options": {
              "content_selector": [
                {
                  "path": "**/blog/**",
                  "selector": "article .post-body"
                }
              ]
            }
          }
        }
      }'

Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.

For configuration details and examples, refer to the [content selectors documentation](https://developers.cloudflare.com/ai-search/configuration/data-source/website/content-selectors/).
