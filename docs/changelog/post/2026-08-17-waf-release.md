---
url: https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/
title: WAF Release - 2026-08-17 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.855061+00:00
---

# WAF Release - 2026-08-17 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 17, 2026

## WAF Release - 2026-08-17

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release updates WordPress remote code execution rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify CVE-2026-65640.

**Key Findings**

  * CVE-2026-65640: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.



**Impact**

The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...3590a4ad| N/A| Wordpress - Remote Code Execution - CVE:CVE-2026-65640| Block| N/A| Rule metadata description refined. Detection unchanged.  
Cloudflare Free Ruleset| ...cfe1a93c| N/A| Wordpress - Remote Code Execution - CVE:CVE-2026-65640| Block| N/A| Rule metadata description refined. Detection unchanged.
