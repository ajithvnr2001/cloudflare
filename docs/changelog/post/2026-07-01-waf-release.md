---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/
title: WAF Release - 2026-07-01 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:00.853644+00:00
---

# WAF Release - 2026-07-01 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## WAF Release - 2026-07-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-01-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.

**Key Findings**

  * CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...d84c92c9| N/A| Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...c12cf9c8| N/A| Anomaly:Header:User-Agent - Fake Bing or MSN Bot| Enabled| Disabled| We are changing the action for this rule from BLOCK to Disabled
