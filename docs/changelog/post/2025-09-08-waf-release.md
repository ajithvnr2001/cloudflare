---
url: https://developers.cloudflare.com/changelog/post/2025-09-08-waf-release/
title: WAF Release - 2025-09-08 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.106950+00:00
---

# WAF Release - 2025-09-08 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-08-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 8, 2025

## WAF Release - 2025-09-08

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-08-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week’s focus highlights newly disclosed vulnerabilities in web frameworks, enterprise applications, and widely deployed CMS plugins. The vulnerabilities include SSRF, authentication bypass, arbitrary file upload, and remote code execution (RCE), exposing organizations to high-impact risks such as unauthorized access, system compromise, and potential data exposure. In addition, security rule enhancements have been deployed to cover general command injection and server-side injection attacks, further strengthening protections.

**Key Findings**

  * Next.js (CVE-2025-57822): Improper handling of redirects in custom middleware can lead to server-side request forgery (SSRF) when user-supplied headers are forwarded. Attackers could exploit this to access internal services or cloud metadata endpoints. The issue has been resolved in versions 14.2.32 and 15.4.7. Developers using custom middleware should upgrade and verify proper redirect handling in `next()` calls.

  * ScriptCase (CVE-2025-47227, CVE-2025-47228): In the Production Environment extension in Netmake ScriptCase through 9.12.006 (23), two vulnerabilities allow attackers to reset admin accounts and execute system commands, potentially leading to full compromise of affected deployments.

  * Sar2HTML (CVE-2025-34030): In Sar2HTML version 3.2.2 and earlier, insufficient input sanitization of the plot parameter allows remote, unauthenticated attackers to execute arbitrary system commands. Exploitation could compromise the underlying server and its data.

  * Zhiyuan OA (CVE-2025-34040): An arbitrary file upload vulnerability exists in the Zhiyuan OA platform. Improper validation in the `wpsAssistServlet` interface allows unauthenticated attackers to upload crafted files via path traversal, which can be executed on the web server, leading to remote code execution.

  * WordPress:Plugin:InfiniteWP Client (CVE-2020-8772): A vulnerability in the InfiniteWP Client plugin allows attackers to perform restricted actions and gain administrative control of connected WordPress sites.




**Impact**

These vulnerabilities could allow attackers to gain unauthorized access, execute malicious code, or take full control of affected systems. The Next.js SSRF flaw may expose internal services or cloud metadata endpoints to attackers. Exploitations of ScriptCase and Sar2HTML could result in remote code execution, administrative takeover, and full server compromise. In Zhiyuan OA, the arbitrary file upload vulnerability allows attackers to execute malicious code on the web server, potentially exposing sensitive data and applications. The authentication bypass in WordPress InfiniteWP Client enables attackers to gain administrative access, risking data exposure and unauthorized control of connected sites.

Administrators are strongly advised to apply vendor patches immediately, remove unsupported software, and review authentication and access controls to mitigate these risks.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...963d7afc| 100007D| Command Injection - Common Attack Commands Args| Log| Block| This rule has been merged into the original rule "Command Injection - Common Attack Commands" (ID: ...28345b9b) for New WAF customers only.  
Cloudflare Managed Ruleset| ...8230a75b| 100617| Next.js - SSRF - CVE:CVE-2025-57822| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...a22dabf1| 100659_BETA| Common Payloads for Server-Side Template Injection - Beta| Log| Block| This rule is merged into the original rule "Common Payloads for Server-Side Template Injection" (ID: ...a28a42c4)  
Cloudflare Managed Ruleset| ...b416b7ca| 100824B| CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 3| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...5db1fa6b| 100848| ScriptCase - Auth Bypass - CVE:CVE-2025-47227| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...2c62d330| 100849| ScriptCase - Command Injection - CVE:CVE-2025-47228| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...ef971afd| 100872| WordPress:Plugin:InfiniteWP Client - Missing Authorization - CVE:CVE-2020-8772| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...bab19b0b| 100873| Sar2HTML - Command Injection - CVE:CVE-2025-34030| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...f24c0fbe| 100875| Zhiyuan OA - Remote Code Execution - CVE:CVE-2025-34040| Log| Block| This is a New Detection
