---
url: https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/
title: Worker startup time limit increased to 1 second \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:25.928019+00:00
---

# Worker startup time limit increased to 1 second · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 10, 2025

## Worker startup time limit increased to 1 second

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-10-increased-startup-time/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.

This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.

For more information, see the documentation on [Workers startup limits](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).
