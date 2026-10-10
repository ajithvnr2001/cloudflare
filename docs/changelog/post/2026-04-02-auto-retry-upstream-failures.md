---
url: https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/
title: Automatically retry on upstream provider failures on AI Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.164907+00:00
---

# Automatically retry on upstream provider failures on AI Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-02-auto-retry-upstream-failures/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 2, 2026

## Automatically retry on upstream provider failures on AI Gateway

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.

You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.

![Retry Requests settings in the AI Gateway dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2344,height=502,format=webp/_astro/auto-retry-changelog.DoCXZnDy.png)

This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use [Dynamic Routing](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/).

For more information, refer to [Manage gateways](https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/#retry-requests).
