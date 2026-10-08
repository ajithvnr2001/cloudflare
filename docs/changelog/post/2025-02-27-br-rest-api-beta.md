---
url: https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/
title: New REST API is in open beta! \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:04.761200+00:00
---

# New REST API is in open beta! · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 27, 2025

## New REST API is in open beta!

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-27-br-rest-api-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've released a new REST API for [Browser Rendering](https://developers.cloudflare.com/browser-run/) in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.

With the **REST API** you can:

  * **Capture screenshots** – Use `/screenshot` to take a screenshot of a webpage from provided URL or HTML.
  * **Generate PDFs** – Use `/pdf` to convert web pages into PDFs.
  * **Extract HTML content** – Use `/content` to retrieve the full HTML from a page. **Snapshot (HTML + Screenshot)** – Use `/snapshot` to capture both the page's HTML and a screenshot in one request
  * **Scrape Web Elements** – Use `/scrape` to extract specific elements from a page.



For example, to capture a screenshot:

Screenshot examplebash
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/screenshot' \
      -H 'Authorization: Bearer <apiToken>' \
      -H 'Content-Type: application/json' \
      -d '{
        "html": "Hello World!",
        "screenshotOptions": {
          "type": "webp",
          "omitBackground": true
        }
      }' \
      --output "screenshot.webp"

Learn more in our [documentation](https://developers.cloudflare.com/browser-run/quick-actions/).
