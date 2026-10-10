---
url: https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/
title: Crawl endpoint now respects the Content Signals `use` directive \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.864724+00:00
---

# Crawl endpoint now respects the Content Signals `use` directive · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-31-crawl-content-use/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 31, 2026

## Crawl endpoint now respects the Content Signals `use` directive

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`/crawl`](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) endpoint now respects the `use` directive of the [Content Signals ↗︎](https://contentsignals.org/) standard, letting site owners express the maximum level at which their content may be used.

You can declare your intended level with the new `contentUse` parameter. Allowed values, from least to most permissive, are `reference` and `full`, and the default is `full`. If a target site's `robots.txt` sets a `use` level that is more restrictive than your declared `contentUse`, the crawl request is rejected with a `400` error.
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://example.com",
        "contentUse": "reference",
        "formats": ["markdown"]
      }'

For more information, refer to [Content Signals](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/#content-signals) in the `/crawl` endpoint documentation.
