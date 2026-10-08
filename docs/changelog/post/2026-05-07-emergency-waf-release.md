---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/
title: WAF Release - 2026-05-07 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.075521+00:00
---

# WAF Release - 2026-05-07 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## WAF Release - 2026-05-07 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-emergency-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release introduces a new rule to detect Next.js App Router middleware and proxy bypass attempts via segment-prefetch routes (CVE-2026-44575).

**Key Findings**

CVE-2026-44575: Next.js Middleware / Proxy Bypass in App Router Applications via Segment-Prefetch Routes

Successful exploitation allows unauthenticated attackers to bypass middleware or proxy-based authorization checks in affected Next.js App Router applications. This leads to unauthorized access to protected content, potential exposure of sensitive application data, and compromise of application security boundaries.

We strongly recommend upgrading to Next.js 15.5.16 or 16.2.5 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, enforce authorization in the underlying route or page logic instead of relying solely on middleware.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...e77e4a53| N/A| Next.js - Middleware Bypass via Invalid RSC Header - CVE:CVE-2026-44575| N/A| Disabled| This is a new detection.
