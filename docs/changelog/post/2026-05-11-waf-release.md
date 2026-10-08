---
url: https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/
title: WAF Release - 2026-05-11 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.514133+00:00
---

# WAF Release - 2026-05-11 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 11, 2026

## WAF Release - 2026-05-11

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.



**Continuous Rule Improvements**

We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...68b3c389| N/A| Remote Code Execution - Java Deserialization - Body - Beta| Block| Disabled| This is a new detection. This rule is merged into the original rule "Remote Code Execution - Java Deserialization" (ID: ...744305c4).
