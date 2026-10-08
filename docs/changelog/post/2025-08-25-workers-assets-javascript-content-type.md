---
url: https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/
title: Content type returned in Workers Assets for Javascript files is now `text/javascript` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:20.683797+00:00
---

# Content type returned in Workers Assets for Javascript files is now `text/javascript` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 25, 2025

## Content type returned in Workers Assets for Javascript files is now `text/javascript`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-25-workers-assets-javascript-content-type/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

JavaScript asset responses have been updated to use the `text/javascript` Content-Type header instead of `application/javascript`. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends `text/javascript` as the preferred type going forward.

This change improves:

  * Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.
  * Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.
  * Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.
  * Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.



Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.

Users will see this change on the next deployment of their assets.
