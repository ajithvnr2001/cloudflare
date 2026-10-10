---
url: https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/
title: Attack Signature Detection is now available in Early Access \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.527297+00:00
---

# Attack Signature Detection is now available in Early Access · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 7, 2026

## Attack Signature Detection is now available in Early Access

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Attack Signature Detection is now available in Early Access. It evaluates requests against Cloudflare attack signatures and records matches without applying a mitigation action, allowing you to investigate detected traffic before deciding how to respond.

In **Security Analytics** > **Attack Analysis** , you can review matching signature references, categories, confidence levels, and request outcomes. You can then use these fields in [Security Rules](https://developers.cloudflare.com/security/rules/) and combine them with request properties such as hostname, path, and HTTP method to apply scoped mitigation.

Attack Signature Detection uses the same signature definitions as [Cloudflare Managed Rules](https://developers.cloudflare.com/waf/managed-rules/), but it does not inherit your Managed Rules actions, overrides, or deployment configuration. Managed Rules remain the recommended baseline protection during Early Access.

Contact your Cloudflare account team to request access. For more information, refer to [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/).
