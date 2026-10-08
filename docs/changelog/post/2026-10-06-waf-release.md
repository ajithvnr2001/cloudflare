---
url: https://developers.cloudflare.com/changelog/post/2026-10-06-waf-release/
title: WAF Release - 2026-10-06 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:19.482592+00:00
---

# WAF Release - 2026-10-06 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-06-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 6, 2026

## WAF Release - 2026-10-06

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-06-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces a new detection to mitigate a heap-based buffer overflow vulnerability in F5 BIG-IP, and enhances existing command injection protections by incorporating tested beta logic into the baseline rule.

**Key Findings**

  * CVE-2026-94127: A heap-based buffer overflow vulnerability in F5 BIG-IP. Attackers can exploit this flaw to execute arbitrary code on the affected system.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...a056caff| N/A| Command Injection - Generic 8 - uri - Beta| Log| Block| This rule is merged into the original rule "Command Injection - Generic 8 - uri" (ID: ...ee159e2e).  
Cloudflare Managed Ruleset| ...7206c737| N/A| F5 BIG-IP - UnAuth Heap-Overflow - CVE:CVE-2026-94127| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...549f7356| N/A| Next.js - Cache Poisoning - CVE:CVE-2026-94543| Block| Block| Rule metadata description refined. Detection unchanged.
