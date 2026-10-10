---
url: https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/
title: Enforce positive security with Application Profiles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.605233+00:00
---

# Enforce positive security with Application Profiles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 7, 2026

## Enforce positive security with Application Profiles

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Application Profiles add a positive-security layer to Cloudflare WAF. Instead of looking only for requests that resemble known attacks, Application Profiles learn what valid requests to your application look like and identify traffic that deviates from the expected structure.

The first available profile type, Schema Profiles, can learn path variables, query parameters, headers, cookies, JSON bodies, and form-encoded bodies. Profiles model field types and constraints such as numeric ranges, string lengths, and character classes. After a profile becomes available, an always-on detection classifies requests as conforming or non-conforming without blocking traffic.

Use **Profile Analysis** in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to review conformance trends and sampled violation details before enforcing a profile. When you are ready to mitigate traffic, use a [Custom Rule](https://developers.cloudflare.com/waf/custom-rules/) to scope enforcement by hostname, path, operation, or other security signals such as Attack Score.

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is also opening a closed beta to invited Enterprise customers without API Security. Contact your Cloudflare account team to express interest.

For more information, refer to [Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/).
