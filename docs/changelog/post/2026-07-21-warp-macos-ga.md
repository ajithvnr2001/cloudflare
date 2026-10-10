---
url: https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/
title: Cloudflare One Client for macOS (version 2026.6.880.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.546888+00:00
---

# Cloudflare One Client for macOS (version 2026.6.880.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2026

## Cloudflare One Client for macOS (version 2026.6.880.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.
