---
url: https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/
title: WAF Release - 2025-11-24 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.445251+00:00
---

# WAF Release - 2025-11-24 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-24-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2025

## WAF Release - 2025-11-24

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.

**Key Findings**

This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the `CGIINFO` header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.

**Impact**

  * FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated `CGIINFO` header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...4e2e1a2e| N/A| FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446| Log| Block| This is a new detection  
Cloudflare Managed Ruleset| ...b6c44ed5| N/A| PHP Wrapper Injection - Body - Beta| Log| Disabled| This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:...1a3e521e)  
Cloudflare Managed Ruleset| ...900f4015| N/A| PHP Wrapper Injection - URI - Beta| Log| Disabled| This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:...8f76bd74)
