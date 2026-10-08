---
url: https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/
title: Workers WebSocket message size limit increased from 1 MiB to 32 MiB \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.864544+00:00
---

# Workers WebSocket message size limit increased from 1 MiB to 32 MiB · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 31, 2025

## Workers WebSocket message size limit increased from 1 MiB to 32 MiB

[Workers](https://developers.cloudflare.com/workers/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers, including those using [Durable Objects](https://developers.cloudflare.com/durable-objects/) and [Browser Rendering](https://developers.cloudflare.com/browser-run/), may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.

This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.

For more information, please see the [Durable Objects startup limits](https://developers.cloudflare.com/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits).
