---
url: https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/
title: WAF Release - 2026-08-07 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.383414+00:00
---

# WAF Release - 2026-08-07 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-07-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 7, 2026

## WAF Release - 2026-08-07

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release updates WordPress XSS rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify XSS2Shell (CVE-2026-64638). It also disables the Command Injection - Obfuscation rule.

**Key Findings**

  * CVE-2026-64638: A pre-authentication reflected cross-site scripting vulnerability affecting the WordPress login screen. Exploitation requires social engineering and explicit interaction by the target user. Under additional conditions, it may be escalated to remote code execution.



**Impact**

The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...9c6dff1c| N/A| Wordpress - XSS - CVE:CVE-2026-64638| Block| N/A| Rule metadata description refined. Detection unchanged.  
Cloudflare Free Ruleset| ...9ab5ed95| N/A| Wordpress - XSS - CVE:CVE-2026-64638| Block| N/A| Rule metadata description refined. Detection unchanged.  
Cloudflare Managed Ruleset| ...761e7a4c| N/A| Command Injection - Obfuscation| Block| Disabled| Detection logic has been deprecated
