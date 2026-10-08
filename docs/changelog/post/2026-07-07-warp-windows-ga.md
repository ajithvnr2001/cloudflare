---
url: https://developers.cloudflare.com/changelog/post/2026-07-07-warp-windows-ga/
title: Cloudflare One Client for Windows (version 2026.6.850.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.758885+00:00
---

# Cloudflare One Client for Windows (version 2026.6.850.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-07-warp-windows-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 7, 2026

## Cloudflare One Client for Windows (version 2026.6.850.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-warp-windows-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.
