---
url: https://developers.cloudflare.com/changelog/post/2025-08-11-waf-release/
title: WAF Release - 2025-08-11 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:19.004850+00:00
---

# WAF Release - 2025-08-11 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-11-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 11, 2025

## WAF Release - 2025-08-11

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-11-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's update focuses on a wide range of enterprise software, from network infrastructure and security platforms to content management systems and development frameworks. Flaws include unsafe deserialization, OS command injection, SSRF, authentication bypass, and arbitrary file upload — many of which allow unauthenticated remote code execution. Notable risks include Cisco Identity Services Engine and Ivanti EPMM, where successful exploitation could grant attackers full administrative control of core network infrastructure and popular web services such as WordPress, SharePoint, and Ingress-Nginx, where security bypasses and arbitrary file uploads could lead to complete site or server compromise.

**Key Findings**

  * Cisco Identity Services Engine (CVE-2025-20281): Insufficient input validation in a specific API of Cisco Identity Services Engine (ISE) and ISE-PIC allows an unauthenticated, remote attacker to execute arbitrary code with root privileges on an affected device.

  * Wazuh Server (CVE-2025-24016): An unsafe deserialization vulnerability in Wazuh Server (versions 4.4.0 to 4.9.0) allows for remote code execution and privilege escalation. By injecting unsanitized data, an attacker can trigger an exception to execute arbitrary code on the server.

  * CrushFTP (CVE-2025-54309): A flaw in AS2 validation within CrushFTP allows remote attackers to gain administrative access via HTTPS on systems not using the DMZ proxy feature. This flaw can lead to unauthorized file access and potential system compromise.

  * Kentico Xperience CMS (CVE-2025-2747, CVE-2025-2748): Vulnerabilities in Kentico Xperience CMS could enable cross-site scripting (XSS), allowing attackers to inject malicious scripts into web pages. Additionally, a flaw could allow unauthenticated attackers to bypass the Staging Sync Server's authentication, potentially leading to administrative control over the CMS.

  * Node.js (CVE-2025-27210): An incomplete fix for a previous vulnerability (CVE-2025-23084) in Node.js affects the `path.join()` API method on Windows systems. The vulnerability can be triggered using reserved Windows device names such as `CON`, `PRN`, or `AUX`.

  * WordPress:Plugin:Simple File List (CVE-2025-34085, CVE-2020-36847): This vulnerability in the Simple File List plugin for WordPress allows an unauthenticated remote attacker to upload arbitrary files to a vulnerable site. This can be exploited to achieve remote code execution on the server.  
(Note: CVE-2025-34085 has been rejected as a duplicate.)

  * GeoServer (CVE-2024-29198): A Server-Side Request Forgery (SSRF) vulnerability exists in GeoServer's Demo request endpoint, which can be exploited where the Proxy Base URL has not been configured.

  * Ivanti EPMM (CVE-2025-6771): An OS command injection vulnerability in Ivanti Endpoint Manager Mobile (EPMM) before versions 12.5.0.2, 12.4.0.3, and 12.3.0.3 allows a remote, authenticated attacker with high privileges to execute arbitrary code.

  * Microsoft SharePoint (CVE-2024-38018): This is a remote code execution vulnerability affecting Microsoft SharePoint Server.

  * Manager-IO (CVE-2025-54122): A critical unauthenticated full read Server-Side Request Forgery (SSRF) vulnerability is present in the proxy handler of both Manager Desktop and Server editions up to version 25.7.18.2519. This allows an unauthenticated attacker to bypass network isolation and access internal services.

  * Ingress-Nginx (CVE-2025-1974): A vulnerability in the Ingress-Nginx controller for Kubernetes allows an attacker to bypass access control rules. An unauthenticated attacker with access to the pod network can achieve arbitrary code execution in the context of the ingress-nginx controller.

  * PaperCut NG/MF (CVE-2023-2533): A Cross-Site Request Forgery (CSRF) vulnerability has been identified in PaperCut NG/MF. Under specific conditions, an attacker could exploit this to alter security settings or execute arbitrary code if they can deceive an administrator with an active login session into clicking a malicious link.

  * SonicWall SMA (CVE-2025-40598): This vulnerability could allow an unauthenticated attacker to bypass security controls. This allows a remote, unauthenticated attacker to potentially execute arbitrary JavaScript code.

  * WordPress (CVE-2025-5394): The "Alone – Charity Multipurpose Non-profit WordPress Theme" for WordPress is vulnerable to arbitrary file uploads. A missing capability check allows unauthenticated attackers to upload ZIP files containing webshells disguised as plugins, leading to remote code execution.




**Impact**

These vulnerabilities span a broad range of enterprise technologies, including network access control systems, monitoring platforms, web servers, CMS platforms, cloud services, and collaboration tools. Exploitation techniques range from remote code execution and command injection to authentication bypass, SQL injection, path traversal, and configuration weaknesses.

A critical flaw in perimeter devices like Ivanti EPMM or SonicWall SMA could allow an unauthenticated attacker to gain remote code execution, completely breaching the primary network defense. A separate vulnerability within Cisco's Identity Services Engine could then be exploited to bypass network segmentation, granting an attacker widespread internal access. Insecure deserialization issues in platforms like Wazuh Server and CrushFTP could then be used to run malicious payloads or steal sensitive files from administrative consoles. Weaknesses in web delivery controllers like Ingress-Nginx or popular content management systems such as WordPress, SharePoint, and Kentico Xperience create vectors to bypass security controls, exfiltrate confidential data, or fully compromise servers.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...51bc8df1| 100538| GeoServer - SSRF - CVE:CVE-2024-29198| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...c9e0b290| 100548| Ivanti EPMM - Remote Code Execution - CVE:CVE-2025-6771| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...ad93cda8| 100550| Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38018| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...1dca5738| 100562| Manager-IO - SSRF - CVE:CVE-2025-54122| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...2e9137e1| 100565| Cisco Identity Services Engine - Remote Code Execution - CVE:CVE-2025-20281| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...5d8102e1| 100567| Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1974| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...99105c43| 100569| PaperCut NG/MF - Remote Code Execution - CVE:CVE-2023-2533| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...2c81dc88| 100571| SonicWall SMA - XSS - CVE:CVE-2025-40598| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...926c96d4| 100573| WordPress - Dangerous File Upload - CVE:CVE-2025-5394| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...40ec2fda| 100806  
| Wazuh Server - Remote Code Execution - CVE:CVE-2025-24016 | Log | Block | This is a New Detection  
Cloudflare Managed Ruleset| ...2401fa3b| 100824 | CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 | Log | Block  
| This is a New Detection  
Cloudflare Managed Ruleset| ...74920ace| 100824A | CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 2 | Log | Block  
| This is a New Detection  
Cloudflare Managed Ruleset| ...c7e63549| 100825| AMI MegaRAC - Auth Bypass - CVE:CVE-2024-54085| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...b79037e6| 100826| Kentico Xperience CMS - Auth Bypass - CVE:CVE-2025-2747| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...caf261aa| 100827| Kentico Xperience CMS - XSS - CVE:CVE-2025-2748| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...6f1c2d12| 100828| Node.js - Directory Traversal - CVE:CVE-2025-27210| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0341fccc| 100829| WordPress:Plugin:Simple File List - Remote Code Execution - CVE:CVE-2025-34085| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...4cefeeda| 100829A| WordPress:Plugin:Simple File List - Remote Code Execution - CVE:CVE-2025-34085 - 2| Log| Disabled| This is a New Detection
