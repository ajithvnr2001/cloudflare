---
url: https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/
title: WAF Release - 2025-10-13 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:26.081142+00:00
---

# WAF Release - 2025-10-13 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2025

## WAF Release - 2025-10-13

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-13-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.

**Key Findings**

New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.

**Impact**

  * CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson `ObjectMapper` abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c04bab5f| 100892| JinJava - SSTI - CVE:CVE-2025-59340| Log| Block| This is a New Detection
