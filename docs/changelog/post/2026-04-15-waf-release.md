---
url: https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/
title: WAF Release - 2026-04-15 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.369988+00:00
---

# WAF Release - 2026-04-15 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-15-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 15, 2026

## WAF Release - 2026-04-15

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces a new detection for a critical Remote Code Execution (RCE) vulnerability in Mesop (CVE-2026-33057), alongside protections for high-impact vulnerabilities in Cisco Secure Firewall Management Center (CVE-2026-20079) and FortiClient EMS (CVE-2026-21643). Additionally, this release includes an update to our existing React Server DoS coverage to address recently identified resource exhaustion vectors (CVE-2026-23869).

**Key Findings**

  * Cisco Secure FMC (CVE-2026-20079): A vulnerability in the web-based management interface of Cisco Secure Firewall Management Center (FMC) that allows an unauthenticated, remote attacker to execute arbitrary commands or bypass security filters.

  * FortiClient EMS (CVE-2026-21643): A critical vulnerability in the FortiClient EMS permitting unauthorized access or administrative configuration manipulation via crafted HTTP requests.

  * Mesop (CVE-2026-33057): A vulnerability in the Mesop Python-based UI framework where unauthenticated attackers can execute arbitrary code by sending specially crafted, Base64-encoded payloads in the request body.




**Impact**

Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, gain administrative control over network management infrastructure, or trigger server-side resource exhaustion. Administrators are strongly encouraged to apply official vendor updates.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...aef9415b| N/A| Cisco Secure FMC - RCE via upgradeReadinessCall - CVE:CVE-2026-20079| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...ee7be621| N/A| FortiClient EMS - Pre-Auth SQL Injection - CVE:CVE-2026-21643| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...c953a72b| N/A| Mesop - Remote Code Execution - Base64 Payload - CVE:CVE-2026-33057| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...50c08f6f| N/A| React Server - DOS - CVE:CVE-2026-23864 - 1 - Beta| Log| Block| This rule has been merged into the original rule "React Server - DOS - CVE:CVE-2026-23864 - 1" (ID: ...61680354)  
Cloudflare Managed Ruleset| ...ebd81645| N/A| XSS, HTML Injection - Link Tag - URI (beta)| N/A| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...0af34bba| N/A| XSS, HTML Injection - Embed Tag - URI (beta)| N/A| Disabled| This is a new detection.
