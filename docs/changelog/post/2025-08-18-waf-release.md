---
url: https://developers.cloudflare.com/changelog/post/2025-08-18-waf-release/
title: WAF Release - 2025-08-18 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.863711+00:00
---

# WAF Release - 2025-08-18 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-18-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 18, 2025

## WAF Release - 2025-08-18

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**This week's update**

This week, a series of critical vulnerabilities were discovered impacting core enterprise and open-source infrastructure. These flaws present a range of risks, providing attackers with distinct pathways for remote code execution, methods to breach internal network boundaries, and opportunities for critical data exposure and operational disruption.

**Key Findings**

  * SonicWall SMA (CVE-2025-32819, CVE-2025-32820, CVE-2025-32821): A remote authenticated attacker with SSLVPN user privileges can bypass path traversal protections. These vulnerabilities enable a attacker to bypass security checks to read, modify, or delete arbitrary files. An attacker with administrative privileges can escalate this further, using a command injection flaw to upload malicious files, which could ultimately force the appliance to reboot to its factory default settings.

  * Ms-Swift Project (CVE-2025-50460): An unsafe deserialization vulnerability exists in the Ms-Swift project's handling of YAML configuration files. If an attacker can control the content of a configuration file passed to the application, they can embed a malicious payload that will execute arbitrary code and it can be executed during deserialization.

  * Apache Druid (CVE-2023-25194): This vulnerability in Apache Druid allows an attacker to cause the server to connect to a malicious LDAP server. By sending a specially crafted LDAP response, the attacker can trigger an unrestricted deserialization of untrusted data. If specific "gadgets" (classes that can be abused) are present in the server's classpath, this can be escalated to achieve Remote Code Execution (RCE).

  * Tenda AC8v4 (CVE-2025-51087, CVE-2025-51088): Vulnerabilities allow an authenticated attacker to trigger a stack-based buffer overflow. By sending malformed arguments in a request to specific endpoints, an attacker can crash the device or potentially achieve arbitrary code execution.

  * Open WebUI (CVE-2024-7959): This vulnerability allows a user to change the OpenAI URL endpoint to an arbitrary internal network address without proper validation. This flaw can be exploited to access internal services or cloud metadata endpoints, potentially leading to remote command execution if the attacker can retrieve instance secrets or access sensitive internal APIs.

  * BentoML (CVE-2025-54381): The vulnerability exists in the serialization/deserialization handlers for multipart form data and JSON requests, which automatically download files from user-provided URLs without proper validation of internal network addresses. This allows attackers to fetch from unintended internal services, including cloud metadata and localhost.

  * Adobe Experience Manager Forms (CVE-2025-54254): An Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could lead to arbitrary file system read in Adobe AEM (≤6.5.23).




**Impact**

These vulnerabilities affect core infrastructure, from network security appliances like SonicWall to data platforms such as Apache Druid and ML frameworks like BentoML. The code execution and deserialization flaws are particularly severe, offering deep system access that allows attackers to steal data, disrupt services, and establish a foothold for broader intrusions. Simultaneously, SSRF and XXE vulnerabilities undermine network boundaries, exposing sensitive internal data and creating pathways for lateral movement. Beyond data-centric threats, flaws in edge devices like the Tenda router introduce the tangible risk of operational disruption, highlighting a multi-faceted threat to the security and stability of key enterprise systems.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...418d9a3b| 100574| SonicWall SMA - Remote Code Execution - CVE:CVE-2025-32819, CVE:CVE-2025-32820, CVE:CVE-2025-32821| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...1e6fefdb| 100576| Ms-Swift Project - Remote Code Execution - CVE:CVE-2025-50460| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...08ac45b3| 100585| Apache Druid - Remote Code Execution - CVE:CVE-2023-25194| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...e4855472| 100834| Tenda AC8v4 - Auth Bypass - CVE:CVE-2025-51087, CVE:CVE-2025-51088| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...022ab542| 100835| Open WebUI - SSRF - CVE:CVE-2024-7959| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...6339f132| 100837| SQLi - OOB| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...b83d2625| 100841| BentoML - SSRF - CVE:CVE-2025-54381| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...739180d2| 100841A| BentoML - SSRF - CVE:CVE-2025-54381 - 2| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...6ab910c2| 100841B| BentoML - SSRF - CVE:CVE-2025-54381 - 3| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...2197ec51| 100845| Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...96f34ce3| 100845A| Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254 - 2| Log| Block| This is a New Detection
