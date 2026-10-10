---
url: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/
title: Origin Content Signals for Markdown for Agents \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.036031+00:00
---

# Origin Content Signals for Markdown for Agents · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 13, 2026

## Origin Content Signals for Markdown for Agents

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:

  * Markdown for Agents preserves security headers such as `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options`, `Set-Cookie`, and CORS headers (for example, `Access-Control-Allow-Origin`) on the converted response.
  * Caching headers (`Cache-Control`, `Expires`, `Age`) continue to pass through.



Your origin's [Content Signals ↗︎](https://contentsignals.org/) policy is now authoritative. If your origin sets a `content-signal` header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default `Content-Signal: ai-train=yes, search=yes, ai-input=yes`.

This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as `../page/` could resolve one path segment too high and return a `404`. Links are now resolved correctly per [RFC 3986 ↗︎](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3).

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) for more details.
