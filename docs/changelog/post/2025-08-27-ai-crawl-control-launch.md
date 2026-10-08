---
url: https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/
title: Enhanced crawler insights and custom 402 responses \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:20.864943+00:00
---

# Enhanced crawler insights and custom 402 responses · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 27, 2025

## Enhanced crawler insights and custom 402 responses

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.

**Enhanced Crawlers tab:**

  * View total allowed and blocked requests for each AI crawler
  * Trend charts show crawler activity over your selected time range per crawler

![Updated AI Crawl Control table showing request counts and trend charts](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1335,height=984,format=webp/_astro/ai-crawl-control-table.BDr0Qd-5.png)

**Custom block responses (paid plans):** You can now return HTTP 402 "Payment Required" responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.

For users on paid plans, when blocking AI crawlers you can configure:

  * **Response code:** Choose between 403 Forbidden or 402 Payment Required
  * **Response body:** Add a custom message with your licensing contact information

![AI Crawl Control block response configuration interface](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1327,height=419,format=webp/_astro/ai-crawl-control-block-response.L4duQj7-.png)

Example 402 response:
    
    
    HTTP 402 Payment Required
    Date: Mon, 24 Aug 2025 12:56:49 GMT
    Content-type: application/json
    Server: cloudflare
    Cf-Ray: 967e8da599d0c3fa-EWR
    Cf-Team: 2902f6db750000c3fa1e2ef400000001
    
    {
      "message": "Please contact the site owner for access."
    }
