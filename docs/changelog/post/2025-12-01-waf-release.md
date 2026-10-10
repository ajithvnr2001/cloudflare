---
url: https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/
title: WAF Release - 2025-12-01 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.256889+00:00
---

# WAF Release - 2025-12-01 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-01-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 1, 2025

## WAF Release - 2025-12-01

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s release introduces new detections for remote code execution attempts targeting Monsta FTP (CVE-2025-34299), alongside improvements to an existing XSS detection to enhance coverage.

**Key Findings**

  * CVE-2025-34299 is a critical remote code execution flaw in Monsta FTP, arising from improper handling of user-supplied parameters within the file-handling interface. Certain builds allow crafted requests to bypass sanitization and reach backend PHP functions that execute arbitrary commands. Attackers can send manipulated parameters through the web panel to trigger command execution within the application’s runtime environment.



**Impact**

If exploited, the vulnerability enables full remote command execution on the underlying server, allowing takeover of the hosting environment, unauthorized file access, and potential lateral movement. As the flaw can be triggered without authentication on exposed Monsta FTP instances, it represents a severe risk for publicly reachable deployments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...a4fcc8a8| N/A| Monsta FTP - Remote Code Execution - CVE:CVE-2025-34299| Log| Block| This is a new detection  
Cloudflare Managed Ruleset| ...b7492846| N/A| XSS - JS Context Escape - Beta| Log| Block| This rule is merged into the original rule "XSS - JS Context Escape" (ID: ...7a3769d3)
