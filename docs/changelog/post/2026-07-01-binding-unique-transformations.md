---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/
title: Images binding is now billed per unique transformation \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.704085+00:00
---

# Images binding is now billed per unique transformation · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-binding-unique-transformations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Images binding is now billed per unique transformation

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Images binding](https://developers.cloudflare.com/images/optimization/binding/) is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.

Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.

Calls to [`.info()`](https://developers.cloudflare.com/images/optimization/binding/#infostream) are no longer billed.

For more information, refer to [Images pricing](https://developers.cloudflare.com/images/pricing/#images-transformed) and the [Images binding documentation](https://developers.cloudflare.com/images/optimization/binding/).
