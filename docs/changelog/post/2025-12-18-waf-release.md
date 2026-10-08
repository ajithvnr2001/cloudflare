---
url: https://developers.cloudflare.com/changelog/post/2025-12-18-waf-release/
title: WAF Release - 2025-12-18 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:32.510854+00:00
---

# WAF Release - 2025-12-18 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-12-18-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 18, 2025

## WAF Release - 2025-12-18

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release focuses on improvements to existing detections to enhance coverage.

**Key Findings**

  * Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...be5ec20c| N/A| Atlassian Confluence - Code Injection - CVE:CVE-2021-26084 - Beta| Log| Block| This rule is merged into the original rule "Atlassian Confluence - Code Injection - CVE:CVE-2021-26084" (ID: ...69e0b97a)  
Cloudflare Managed Ruleset| ...0d9206e3| N/A | PostgreSQL - SQLi - Copy - Beta | Log | Block  
| This rule is merged into the original rule "PostgreSQL - SQLi - COPY" (ID: ...e7265a4e)  
Cloudflare Managed Ruleset| ...0cd00ba7| N/A | Generic Rules - Command Execution - Body | Log | Disabled  
| This is a new detection.  
Cloudflare Managed Ruleset| ...cd679ad4| N/A| Generic Rules - Command Execution - Header| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...fd181fb3| N/A| Generic Rules - Command Execution - URI| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...7a95bc3a| N/A| SQLi - Tautology - URI - Beta| Log| Block| This rule is merged into the original rule "SQLi - Tautology - URI" (ID: ...b3de2e0a)  
Cloudflare Managed Ruleset| ...432ac90d| N/A| SQLi - WaitFor Function - Beta| Log| Block| This rule is merged into the original rule "SQLi - WaitFor Function" (ID: ...d5faba59)  
Cloudflare Managed Ruleset| ...596c741e| N/A| SQLi - AND/OR Digit Operator Digit 2 - Beta| Log| Block| This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit" (ID: ...88d80772)  
Cloudflare Managed Ruleset| ...03b2f3fe| N/A| SQLi - Equation 2 - Beta| Log| Block| This rule is merged into the original rule "SQLi - Equation" (ID: ...a72a6b3a)
