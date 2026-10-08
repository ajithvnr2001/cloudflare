---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/
title: Leaked credentials detection now scans Authorization headers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:09.716861+00:00
---

# Leaked credentials detection now scans Authorization headers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## Leaked credentials detection now scans Authorization headers

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-20-leaked-credentials-authorization-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) now scans the `Authorization` request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default.

This new default scan location decodes the `Authorization: Basic <credentials>` header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations. Matches populate the existing [leaked credentials fields](https://developers.cloudflare.com/waf/detections/leaked-credentials/#leaked-credentials-fields), such as `cf.waf.credential_check.password_leaked`, and trigger the [`Exposed-Credential-Check` managed transform header](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header) if configured, so you can reuse existing [custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) without changes.

This change was applied automatically for zones with leaked credentials detection enabled. No configuration changes are required.

For more information, refer to [Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/).
