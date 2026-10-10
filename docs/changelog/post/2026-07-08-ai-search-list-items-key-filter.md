---
url: https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/
title: Filter AI Search list items by exact object key \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.255470+00:00
---

# Filter AI Search list items by exact object key · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-08-ai-search-list-items-key-filter/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 8, 2026

## Filter AI Search list items by exact object key

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [AI Search](https://developers.cloudflare.com/ai-search/), you can upload files to an instance, or connect a [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/) such as an R2 bucket, to make your content searchable with natural language. Each file becomes an **item** identified by an object **key** (its filename or path). The [list items endpoint](https://developers.cloudflare.com/ai-search/api/items/rest-api/) returns the items in an instance.

That endpoint now accepts a `key` query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing `item_id` filter for when you know the key but not the ID.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/instances/<INSTANCE_NAME>/items?key=docs/readme.md" \
      -H "Authorization: Bearer <API_TOKEN>"

Keys are unique per data source, so combine `key` with `source` (for example, `source=builtin`) to disambiguate when the same key exists across multiple sources.

For more information, refer to [managing items](https://developers.cloudflare.com/ai-search/api/items/rest-api/).
