---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/
title: Fix redirect URL fragment encoding for single-page applications \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:00.684454+00:00
---

# Fix redirect URL fragment encoding for single-page applications · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Fix redirect URL fragment encoding for single-page applications

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Access now correctly preserves URL fragment characters (`/`, `?`, `=`, `&`, `;`) when redirecting users back to an application after login. Previously, these characters were encoded with `encodeURIComponent`, which mangled fragment-based routes used by single-page applications (SPAs).

For example, an SPA URL like `https://app.example.com/#/dashboard?tab=settings&view=advanced` would previously redirect to a broken URL after login. This is now handled correctly.

If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.
