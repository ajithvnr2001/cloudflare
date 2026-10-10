---
url: https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/
title: WAF Release - 2026-08-11 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.173726+00:00
---

# WAF Release - 2026-08-11 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 11, 2026

## WAF Release - 2026-08-11

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.

**Key Findings**

  * A new detection provides protection against vBulletin CVE-2026-61511.
  * Two existing detections have been improved to strengthen coverage.



**Impact**

Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...94f3006b| N/A| vBulletin - Remote Code Execution - CVE:CVE-2026-61511| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...098b749e| N/A| Version Control - Information Disclosure - Beta| Log| Block| This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529)  
Cloudflare Managed Ruleset| ...d56225d8| N/A| vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta| Log| Block| This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: ...8fe9f1c7)
