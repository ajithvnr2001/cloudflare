---
url: https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/
title: Cloudflare Access Logging supports the Customer Metadata Boundary (CMB) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.239343+00:00
---

# Cloudflare Access Logging supports the Customer Metadata Boundary (CMB) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 14, 2025

## Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access logs now support the [Customer Metadata Boundary (CMB)](https://developers.cloudflare.com/data-localization/metadata-boundary/). If you have configured the CMB for your account, all Access logging will respect that configuration.

Note

For EU CMB customers, the logs will not be stored by Access and will appear as empty in the dashboard. EU CMB customers should utilize [Logpush](https://developers.cloudflare.com/logs/logpush/) to retain their Access logging, if desired.
