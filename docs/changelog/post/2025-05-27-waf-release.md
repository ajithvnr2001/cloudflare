---
url: https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/
title: WAF Release - 2025-05-27 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:12.800559+00:00
---

# WAF Release - 2025-05-27 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 27, 2025

## WAF Release - 2025-05-27

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-27-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.

**Key Findings**

  * Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.
  * GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.
  * Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.
  * F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.
  * AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.
  * NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.
  * SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.
  * Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.
  * Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.



**Impact**

These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.

GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...d127592a| 100746| Vercel - Information Disclosure| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...95442495| 100754| AJ-Report - Remote Code Execution - CVE:CVE-2024-15077| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...dfee7ae4| 100756| NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...1c52f6d0| 100757| Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...95442495| 100759| SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...5366ccc1| 100760| Craft CMS - Remote Code Execution - CVE:CVE-2025-32432| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...eb40686b| 100761| GitHub Action - Remote Code Execution - CVE:CVE-2025-30066| Log| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...60fc041c| 100762| Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...ebafdfe6| 100763| F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644| Log| Disabled| This is a New Detection
