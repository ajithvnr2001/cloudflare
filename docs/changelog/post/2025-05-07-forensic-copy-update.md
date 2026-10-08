---
url: https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/
title: Send forensic copies to storage without DLP profiles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.011520+00:00
---

# Send forensic copies to storage without DLP profiles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2025

## Send forensic copies to storage without DLP profiles

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-07-forensic-copy-update/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now [send DLP forensic copies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination) to third-party storage for any HTTP policy with an `Allow` or `Block` action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.

By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1324,height=636,format=webp/_astro/forensic-copies-for-all.fxeFrCY4.png)
