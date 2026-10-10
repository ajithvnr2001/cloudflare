---
url: https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/
title: Test Data Loss Prevention profiles without sending traffic through Gateway \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.460340+00:00
---

# Test Data Loss Prevention profiles without sending traffic through Gateway · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-21-dlp-test-scan/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 21, 2026

## Test Data Loss Prevention profiles without sending traffic through Gateway

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Test scan** lets you check how [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.

![Test scan results showing matched profiles, detection entries, and match context](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=587,format=webp/_astro/dlp-test-scan.Dm6EgN6x.gif)

Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.

Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your [Zero Trust plan](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/).

For more details, refer to the [Test scan documentation](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/test-scan/).
