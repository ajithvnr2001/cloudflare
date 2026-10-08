---
url: https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/
title: WAF Release - 2026-05-15 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:53.918370+00:00
---

# WAF Release - 2026-05-15 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 15, 2026

## WAF Release - 2026-05-15 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-15-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's `is_args` stale-state bug (CVE-2026-42945).

**Key Findings**

CVE-2026-42945: nginx Heap Buffer Overflow via Stale `is_args` in Rewrite Module

Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in `ngx_http_script_copy_capture_code()` causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.

We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid `rewrite` directives with `?` in the replacement string followed by `set` or `if` referencing capture groups.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...7e52be73| N/A| nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9df0ee6c| N/A| nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945| N/A| Block| This is a new detection.
