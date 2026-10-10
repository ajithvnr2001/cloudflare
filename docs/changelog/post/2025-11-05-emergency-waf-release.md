---
url: https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/
title: WAF Release - 2025-11-05 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.089017+00:00
---

# WAF Release - 2025-11-05 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-05-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2025

## WAF Release - 2025-11-05 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s emergency release introduces a new detection signature that enhances coverage for a critical vulnerability in the React Native Metro Development Server, tracked as CVE-2025-11953.

**Key Findings**

The Metro Development Server exposes an HTTP endpoint that is vulnerable to OS command injection (CWE-78). An unauthenticated network attacker can send a crafted request to this endpoint and execute arbitrary commands on the host running Metro. The vulnerability affects Metro/cli-server-api builds used by React Native Community CLI in pre-patch development releases.

**Impact**

Successful exploitation of CVE-2025-11953 may result in remote command execution on developer workstations or CI/build agents, leading to credential and secret exposure, source tampering, and potential lateral movement into internal networks. Administrators and developers are strongly advised to apply the vendor's patches and restrict Metro’s network exposure to reduce this risk.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c8e30c5b| N/A| React Native Metro - Command Injection - CVE:CVE-2025-11953| N/A| Block| This is a New Detection
