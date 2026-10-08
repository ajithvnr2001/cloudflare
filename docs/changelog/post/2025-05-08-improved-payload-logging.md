---
url: https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/
title: Improved Payload Logging for WAF Managed Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:11.617601+00:00
---

# Improved Payload Logging for WAF Managed Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 8, 2025

## Improved Payload Logging for WAF Managed Rules

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:

  * **Targeted logging** : Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.
  * **Visual highlighting** : Matched content is visually highlighted in the UI for faster identification.
  * **Enhanced context** : Logs now include surrounding context to make diagnostics more effective.

![Log entry showing payload logging details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=751,format=webp/_astro/2025-05-payload-logging-update.1M29LjNm.png)

Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can [get started](https://developers.cloudflare.com/waf/managed-rules/payload-logging/).

**Note:** The structure of the `encrypted_matched_data` field in Logpush has changed from `Map<Field, Value>` to `Map<Field, {Before: bytes, Content: Value, After: bytes}>`. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.
