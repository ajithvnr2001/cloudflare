---
url: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/
title: Cloudflare Fonts error handling and security improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.602974+00:00
---

# Cloudflare Fonts error handling and security improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 18, 2026

## Cloudflare Fonts error handling and security improvements

[Speed](https://developers.cloudflare.com/speed/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Fonts now forwards `/cf-fonts` requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.
