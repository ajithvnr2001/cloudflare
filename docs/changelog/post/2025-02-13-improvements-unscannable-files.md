---
url: https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/
title: Block files that are password-protected, compressed, or otherwise unscannable. \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:04.079445+00:00
---

# Block files that are password-protected, compressed, or otherwise unscannable. · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 3, 2025

## Block files that are password-protected, compressed, or otherwise unscannable.

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-13-improvements-unscannable-files/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.

These unscannable files are now matched with the [Download and Upload File Types traffic selectors](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types) for HTTP policies:

  * Password-protected Microsoft Office document
  * Password-protected PDF
  * Password-protected ZIP archive
  * Unscannable ZIP archive



To get started inspecting and modifying behavior based on these and other rules, refer to [HTTP filtering](https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/http/).
