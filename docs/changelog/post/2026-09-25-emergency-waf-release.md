---
url: https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/
title: WAF Release - 2026-09-25 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.456816+00:00
---

# WAF Release - 2026-09-25 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 25, 2026

## WAF Release - 2026-09-25 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This update provides immediate defense against critical vulnerabilities affecting WordPress and JFrog Artifactory, including path traversal, local file inclusion (LFI), cross-site scripting (XSS), and authentication bypass exploits.

**Key Findings**

  * CVE-2026-87902: A high-severity Path Traversal and Local File Inclusion (LFI) vulnerability affecting WordPress. Unauthenticated attackers can exploit this flaw to read arbitrary files on the host server, potentially exposing sensitive configuration data or system files.

  * CVE-2026-42018 & CVE-2026-82329: Critical authentication bypass vulnerabilities affecting JFrog Artifactory. Successful exploitation allows unauthenticated attackers to bypass security controls and achieve unauthorized access to the Artifactory instance.




**Impact**

We strongly recommend that administrators apply the latest vendor patches for WordPress and JFrog Artifactory to fully secure origin servers.

Detailed Rule Changes

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...70a43f96| N/A| Wordpress - Path Traversal, Local File Inclusion - CVE:CVE-2026-87902| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...909a4db4| N/A| Wordpress - XSS - Comment| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...c797ef03| N/A| JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-42018| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a813ac74| N/A| JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-82329| N/A| Block| This is a new detection.
