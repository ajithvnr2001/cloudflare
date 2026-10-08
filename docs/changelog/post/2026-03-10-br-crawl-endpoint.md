---
url: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
title: Crawl entire websites with a single API call using Browser Rendering \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:40.319194+00:00
---

# Crawl entire websites with a single API call using Browser Rendering · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 10, 2026

## Crawl entire websites with a single API call using Browser Rendering

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

 _Edit: this post has been edited to clarify crawling behavior with respect to site guidance._

You can now crawl an entire website with a single API call using [Browser Rendering](https://developers.cloudflare.com/browser-run/)'s new [`/crawl` endpoint](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/), available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a [verified bot (intermediary agent)](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) that respects robots.txt and [AI Crawl Control ↗︎](https://www.cloudflare.com/ai-crawl-control/) by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.

Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.
    
    
    # Initiate a crawl
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
        "url": "https://blog.cloudflare.com/"
      }'
    
    # Check results
    curl -X GET 'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}' \
      -H 'Authorization: Bearer <apiToken>'

Key features:

  * **Multiple output formats** \- Return crawled content as HTML, Markdown, and structured JSON (powered by [Workers AI](https://developers.cloudflare.com/workers-ai/))
  * **Crawl scope controls** \- Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths
  * **Automatic page discovery** \- Discovers URLs from sitemaps, page links, or both
  * **Incremental crawling** \- Use `modifiedSince` and `maxAge` to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls
  * **Static mode** \- Set `render: false` to fetch static HTML without spinning up a browser, for faster crawling of static sites
  * **Well-behaved bot** \- Honors `robots.txt` directives, including `crawl-delay`



Available on both the Workers Free and Paid plans.

**Note** : the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.

To get started, refer to the [crawl endpoint documentation](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/). If you are setting up your own site to be crawled, review the [robots.txt and sitemaps best practices](https://developers.cloudflare.com/browser-run/reference/robots-txt/).
