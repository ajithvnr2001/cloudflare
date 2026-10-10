---
url: https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/
title: View the user agent of requests in AI Gateway logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.951194+00:00
---

# View the user agent of requests in AI Gateway logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-12-user-agent-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 12, 2026

## View the user agent of requests in AI Gateway logs

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from `openai-python` versus a custom application or a Cloudflare Worker.

The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.

For more information, refer to [Logging](https://developers.cloudflare.com/ai-gateway/observability/logging/).
