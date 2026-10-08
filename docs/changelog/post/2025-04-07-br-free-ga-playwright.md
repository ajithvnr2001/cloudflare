---
url: https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/
title: Browser Rendering REST API is Generally Available, with new endpoints and a free tier \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:08.610759+00:00
---

# Browser Rendering REST API is Generally Available, with new endpoints and a free tier · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2025

## Browser Rendering REST API is Generally Available, with new endpoints and a free tier

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-br-free-ga-playwright/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We’re excited to announce Browser Rendering is now available on the [Workers Free plan ↗︎](https://www.cloudflare.com/plans/developer-platform/), making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.

The Browser Rendering **[REST API](https://developers.cloudflare.com/browser-run/quick-actions/) is now Generally Available**, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:

  * **Extract structured data** – Use `/json` to retrieve structured data from a webpage.
  * **Retrieve links** – Use `/links` to pull all links from a webpage.
  * **Convert to Markdown** – Use `/markdown` to convert webpage content into Markdown format.



For example, to fetch the Markdown representation of a webpage:

Markdown examplebash
    
    
    curl -X 'POST' 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/markdown' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <apiToken>' \
      -d '{
        "url": "https://example.com"
      }'

For the full list of endpoints, check out our [REST API documentation](https://developers.cloudflare.com/browser-run/quick-actions/). You can also interact with Browser Rendering via the [Cloudflare TypeScript SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript).

We also recently landed support for [Playwright](https://developers.cloudflare.com/browser-run/playwright/) in Browser Rendering for browser automation from Cloudflare [Workers](https://developers.cloudflare.com/workers/), in addition to [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), giving you more flexibility to test across different browser environments.

Visit the [Browser Rendering docs](https://developers.cloudflare.com/browser-run/) to learn more about how to use headless browsers in your applications.
