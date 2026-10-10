---
url: https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/
title: Workers for Platforms - Instant dispatch for newly created User Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.682982+00:00
---

# Workers for Platforms - Instant dispatch for newly created User Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-20-synchronous-uploads/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 20, 2025

## Workers for Platforms - Instant dispatch for newly created User Workers

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers for Platforms ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/) is an architecture wherein a centralized [dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker) processes incoming requests and routes them to isolated sub-Workers, called [User Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers).

![Workers for Platforms Requests](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1366,height=711,format=webp/_astro/wfp-request.CZmZLaYf.png)

Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.

**With this update, first-time uploads of User Workers are now deployed synchronously**. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.
