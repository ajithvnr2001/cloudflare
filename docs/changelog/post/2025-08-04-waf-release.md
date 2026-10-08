---
url: https://developers.cloudflare.com/changelog/post/2025-08-04-waf-release/
title: WAF Release - 2025-08-04 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:18.015622+00:00
---

# WAF Release - 2025-08-04 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-04-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 4, 2025

## WAF Release - 2025-08-04

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-04-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's highlight focuses on a series of significant vulnerabilities identified across widely adopted web platforms, from enterprise-grade CMS to essential backend administration tools. The findings reveal multiple vectors for attack, including critical flaws that allow for full server compromise and others that enable targeted attacks against users.

**Key Findings**

  * Sitecore (CVE-2025-34509, CVE-2025-34510, CVE-2025-34511): A hardcoded credential allows remote attackers to access administrative APIs. Once authenticated, they can exploit an additional vulnerability to upload arbitrary files, leading to remote code execution.

  * Grafana (CVE-2025-4123): A cross-site scripting (XSS) vulnerability allows an attacker to redirect users to a malicious website, which can then execute arbitrary JavaScript in the victim's browser.

  * LaRecipe (CVE-2025-53833): Through Server-Side Template Injection, attackers can execute arbitrary commands on the server, potentially access sensitive environment variables, and escalate access depending on server configuration.

  * CentOS WebPanel (CVE-2025-48703): A command injection vulnerability could allow a remote attacker to execute arbitrary commands on the server.

  * WordPress (CVE-2023-5561): This vulnerability allows unauthenticated attackers to determine the email addresses of users who have published public posts on an affected website.

  * WordPress Plugin - WPBookit (CVE-2025-6058): A missing file type validation allows unauthenticated attackers to upload arbitrary files to the server, creating the potential for remote code execution.

  * WordPress Theme - Motors (CVE-2025-4322): Due to improper identity validation, an unauthenticated attacker can change the passwords of arbitrary users, including administrators, to gain access to their accounts.




**Impact**

These vulnerabilities pose a multi-layered threat to widely adopted web technologies, ranging from enterprise-grade platforms like Sitecore to everyday solutions such as WordPress, and backend tools like CentOS WebPanel. The most severe risks originate in remote code execution (RCE) flaws found in Sitecore, CentOS WebPanel, LaRecipe, and the WPBookit plugin. These allow attackers to bypass security controls and gain deep access to the server, enabling them to steal sensitive data, deface websites, install persistent malware, or use the compromised server as a launchpad for further attacks.

The privilege escalation vulnerability is the Motors theme, which allows for a complete administrative account takeover on WordPress sites. This effectively hands control of the application to an attacker, who can then manipulate content, exfiltrate user data, and alter site functionality without needing to breach the server itself.

The Grafana cross-site scripting (XSS) flaw can be used to hijack authenticated user sessions or steal credentials, turning a trusted user's browser into an attack vector.

Meanwhile, the information disclosure flaw in WordPress core provides attackers with valid user emails, fueling targeted phishing campaigns that aim to secure the same account access achievable through the other exploits.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...52f30a13| 100535A| Sitecore - Dangerous File Upload - CVE:CVE-2025-34510, CVE:CVE-2025-34511| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...5045a97f| 100535| Sitecore - Information Disclosure - CVE:CVE-2025-34509| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...579cd3e0| 100543| Grafana - Directory Traversal - CVE:CVE-2025-4123| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0cbd9abc| 100545| WordPress - Information Disclosure - CVE:CVE-2023-5561| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...8f634977| 100820| CentOS WebPanel - Remote Code Execution - CVE:CVE-2025-48703| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...82ae64c1| 100821| LaRecipe - SSTI - CVE:CVE-2025-53833| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...194f7b2d| 100822| WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058| Log| Block| This is a New Detection  
Cloudflare Managed Ruleset| ...0bf1b661| 100823| WordPress:Theme:Motors - Privilege Escalation - CVE:CVE-2025-4322| Log| Block| This is a New Detection
