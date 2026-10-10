---
url: https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/
title: WAF Release - 2026-03-02 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.058700+00:00
---

# WAF Release - 2026-03-02 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-02-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 2, 2026

## WAF Release - 2026-03-02

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week's release introduces new detections for vulnerabilities in SmarterTools SmarterMail (CVE-2025-52691 and CVE-2026-23760), alongside improvements to an existing Command Injection (nslookup) detection to enhance coverage.

**Key Findings**

  * CVE-2025-52691: SmarterTools SmarterMail mail server is vulnerable to Arbitrary File Upload, allowing an unauthenticated attacker to upload files to any location on the mail server, potentially enabling remote code execution.
  * CVE-2026-23760: SmarterTools SmarterMail versions prior to build 9511 contain an authentication bypass vulnerability in the password reset API permitting unaunthenticated to reset system administrator accounts failing to verify existing password or reset token.



**Impact**

Successful exploitation of these SmarterMail vulnerabilities could lead to full system compromise or unauthorized administrative access to mail servers. Administrators are strongly encouraged to apply vendor patches without delay.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...966ec6b1| N/A| SmarterMail - Arbitrary File Upload - CVE-2025-52691| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...ee964a8c| N/A| SmarterMail - Authentication Bypass - CVE-2026-23760| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...75b64d99| N/A| Command Injection - Nslookup - Beta| Log| Block| This rule is merged into the original rule "Command Injection - Nslookup" (ID: ...b090ba9a)
