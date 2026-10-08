---
url: https://developers.cloudflare.com/changelog/post/2026-04-14-email-obfuscation-defer/
title: Email obfuscation decode script is now non-render-blocking \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:46.570052+00:00
---

# Email obfuscation decode script is now non-render-blocking · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-14-email-obfuscation-defer/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 14, 2026

## Email obfuscation decode script is now non-render-blocking

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-email-obfuscation-defer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The decode script injected by [Email Address Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/) now loads with the `defer` attribute. This means the script no longer blocks page rendering. It downloads in parallel with HTML parsing and executes after the document is fully parsed, before the `DOMContentLoaded` event.

This improves page loading performance, contributing to better Core Web Vitals, for all zones with Email Address Obfuscation on. No action is required.

If you have custom JavaScript that depends on email addresses being decoded at a specific point during page load, note that the decode script now executes after HTML parsing completes rather than inline during parsing.
