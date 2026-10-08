---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/
title: Use Browser Run Quick Actions directly from Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:55.841426+00:00
---

# Use Browser Run Quick Actions directly from Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Use Browser Run Quick Actions directly from Workers

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now call [Browser Run Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) directly from a [Cloudflare Worker](https://developers.cloudflare.com/workers/) using the `quickAction()` method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.

With the `quickAction()` method you can:

  * [Capture screenshots](https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/) from URLs or HTML
  * [Generate PDFs](https://developers.cloudflare.com/browser-run/quick-actions/pdf-endpoint/) with custom styling, headers, and footers
  * [Extract HTML content](https://developers.cloudflare.com/browser-run/quick-actions/content-endpoint/) from fully rendered pages
  * [Convert pages to Markdown](https://developers.cloudflare.com/browser-run/quick-actions/markdown-endpoint/)
  * [Extract structured JSON](https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/) using AI
  * [Scrape elements](https://developers.cloudflare.com/browser-run/quick-actions/scrape-endpoint/) with CSS selectors
  * [Get all links](https://developers.cloudflare.com/browser-run/quick-actions/links-endpoint/) from a page
  * [Capture snapshots](https://developers.cloudflare.com/browser-run/quick-actions/snapshot/) (HTML + screenshot in one request)



To get started, add a browser binding to your Wrangler configuration:
    
    
    {
      "compatibility_date": "2026-03-24",
      "browser": {
        "binding": "BROWSER"
      }
    }
    
    
    compatibility_date = "2026-03-24"
    
    [browser]
    binding = "BROWSER"

Then call any Quick Action directly from your Worker. For example, to capture a screenshot:
    
    
    const screenshot = await env.BROWSER.quickAction("screenshot", {
    	url: "https://www.cloudflare.com/",
    });
    
    
    const screenshot = await env.BROWSER.quickAction("screenshot", {
      url: "https://www.cloudflare.com/",
    });

The `quickAction()` method requires a compatibility date of `2026-03-24` or later.

For setup instructions and the full list of available actions, refer to [Browser Run Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/).
