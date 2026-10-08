---
url: https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/
title: Workers Static Assets: Corrected handling of double slashes in redirect rule paths \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:19.725999+00:00
---

# Workers Static Assets: Corrected handling of double slashes in redirect rule paths · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 15, 2025

## Workers Static Assets: Corrected handling of double slashes in redirect rule paths

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-15-static-assets-redirect-url/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Static Assets](https://developers.cloudflare.com/workers/static-assets/): Fixed a bug in how [redirect rules ↗︎](https://developers.cloudflare.com/workers/static-assets/redirects/) defined in your Worker's `_redirects` file are processed.

If you're serving Static Assets with a `_redirects` file containing a rule like `/ja/* /:splat`, paths with double slashes were previously misinterpreted as external URLs. For example, visiting `/ja//example.com` would incorrectly redirect to `https://example.com` instead of `/example.com` on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: [Cloudflare Pages](https://developers.cloudflare.com/pages/) was not affected by this issue.
