---
url: https://developers.cloudflare.com/changelog/post/2026-04-07-waf-release/
title: WAF Release - 2026-04-07 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:45.384255+00:00
---

# WAF Release - 2026-04-07 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-07-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 7, 2026

## WAF Release - 2026-04-07

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-07-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for a critical Remote Code Execution (RCE) vulnerability in MCP Server (CVE-2026-23744), alongside targeted protection for an authentication bypass vulnerability in SolarWinds products (CVE-2025-40552). Additionally, this release includes a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts leveraging "OnEvent" handlers within HTTP cookies.

**Key Findings**

  * MCP Server (CVE-2026-23744): A vulnerability in the Model Context Protocol (MCP) server implementation where malformed input payloads can trigger a memory corruption state, allowing for arbitrary code execution.

  * SolarWinds (CVE-2025-40552): A critical flaw in the authentication module allows unauthenticated attackers to bypass security filters and gain unauthorized access to the management console due to improper identity token validation.

  * XSS OnEvents Cookies: This generic rule identifies malicious event handlers (such as onload or onerror) embedded within HTTP cookie values.




**Impact**

Successful exploitation of the MCP Server and SolarWinds vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain administrative control, leading to a full system takeover. Additionally, the new generic XSS detection prevents attackers from leveraging browser event handlers in cookies to hijack user sessions or execute malicious scripts.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...0aa410af| N/A| Generic Rules - Command Execution - 5 - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...9131ec2f| N/A| Generic Rules - Command Execution - 5 - Header| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...551eb9e5| N/A| Generic Rules - Command Execution - 5 - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...d46229eb| N/A| MCP Server - Remote Code Execution - CVE:CVE-2026-23744| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a864b9c2| N/A| XSS - OnEvents - Cookies| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9712a863| N/A| SQLi - Evasion - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...40732d48| N/A| SQLi - Evasion - Headers| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...e68a99b5| N/A| SQLi - Evasion - URI| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...3e8143d2| N/A| SQLi - LIKE 3 - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...70e7fb97| N/A| SQLi - LIKE 3 - URI| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...4c538bd9| N/A| SQLi - UNION - 2 - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...61c439c9| N/A| SQLi - UNION - 2 - URI| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...cf33ea10| N/A| SolarWinds - Auth Bypass - CVE:CVE-2025-40552| Log| Block| This is a new detection.
