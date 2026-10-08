---
url: https://developers.cloudflare.com/changelog/post/2026-07-21-waf-release/
title: WAF Release - 2026-07-21 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.233029+00:00
---

# WAF Release - 2026-07-21 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-21-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2026

## WAF Release - 2026-07-21

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-waf-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new rules for vulnerabilities in Adobe ColdFusion, Next.js, WordPress alongside updates to existing rules thereby providing enhanced generic protections against Server-Side Request Forgery (SSRF), Local File Inclusion (LFI), and Cross-Site Scripting (XSS).

**WAF and framework adapter mitigations for Next.js vulnerabilities**

Multiple [security vulnerabilities ↗︎](https://nextjs.org/blog/july-2026-security-release) were disclosed and patched by the Next.js team through July 2026 security release. These include denial of service, middleware and proxy bypass, server-side request forgery, information disclosure, and cache poisoning across a range of severities.

Several of the disclosed vulnerabilities are not possible to block at WAF layer,we strongly recommend updating your application and its dependencies immediately. Patched versions are available through v16.2.11 (Active LTS) and v15.5.21 (Maintenance LTS) to address these issues.

Advisory| CVE| Severity| Issue| WAF Coverage  
---|---|---|---|---  
[Denial of Service in App Router using Server Actions](https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj)| CVE-2026-64641| High| Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service.| WAF rule Next.js - DoS - CVE-2026-64641 (...90dcdb0a) has been deployed to provide coverage.  
[Middleware / Proxy bypass in App Router applications using Turbopack and single locale](https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24)| CVE-2026-64642| High| Next.js applications using App Router built with Turbopack and a single entry in config.i18n.locales are vulnerable to a middleware/proxy bypass. Accordingly, any authentication or security checks that a middleware/proxy may perform are bypassed.| This is a middleware bypass that unfortunately cannot be covered through Cloudflare WAF signature engine.  
[Server-Side Request Forgery in rewrites via attacker-controlled destination hostname](https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4)| CVE-2026-64645| High| A rewrites() or redirects() rule that builds its external destination hostname from request-controlled input can be pointed at an arbitrary hostname, regardless of the rule's hostname suffix. For rewrites, this behavior enables Server-Side Request Forgery (SSRF); for redirects, Open Redirect can be achieved.| Existing SSRF rules provide adequate coverage for this vulnerability, no tailored WAF rule was developed.  
[Server-Side Request Forgery in Server Actions on custom servers](https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x)| CVE-2026-64649| High| When a Server Action forwards or redirects a request, an attacker can cause the server to send that outbound request to a malicious host (Server-Side Request Forgery). This requires the attacker’s request to control Host-associated headers.| WAF rule Next.js - SSRF - CVE-2026-64649 (...930091a3) has been deployed to provide coverage.  
[Denial of Service in the Image Optimization API using SVGs](https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch)| CVE-2026-64644| Medium| When self-hosting Next.js with the default image loader, the Image Optimization API can optimize remotely hosted images if configured (not enabled by default). If those images contain malicious content, the images can cause CPU exhaustion in the /_next/image endpoint.| Malicious request is unfortunately indistinguishable from a legitimate image optimization request, so no WAF rule has been created to address this vulnerability.  
[Unbounded Server Action payload in Edge runtime](https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3)| CVE-2026-64646| Medium| A crafted request can lead to memory consumption on Server Actions in the Edge runtime. Next.js applications which use App Router and have at least one Server Action are affected.| Unfortunately there is no one size fits all rule that can be deployed through WAF in lieu of custom bodySizeLimit configurations, so no WAF rule has been created to address this vulnerability.  
[Unauthenticated disclosure of internal Server Function endpoints](https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp)| CVE-2026-64643| Medium| In Next.js applications using App Router, Server Actions (use server) or use cache endpoint IDs can be globally disclosed. An attacker can use this for reconnaissance and as part of a broader attack chain.| WAF rule Next.js - Information Disclosure - CVE-2026-64643 (...72952826) has been deployed to provide coverage.  
[Cache confusion of response bodies for requests with bodies](https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742)| CVE-2026-64648| Medium| A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies for fetch calls of the shape fetch(new Request(init), aDifferentInit)| This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.  
[Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences](https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q)| CVE-2026-64647| Medium| A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies when receiving request bodies which contain invalid UTF-8 characters.| This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.  
  
**Key Findings**

  * CVE-2026-48276: A path traversal vulnerability in Adobe ColdFusion file upload mechanisms allows unauthenticated attackers to write or upload files to arbitrary locations outside designated directories on the origin server.

  * CVE-2026-48282: A path traversal vulnerability in Adobe ColdFusion enables unauthenticated attackers to manipulate directory sequences and access restricted system files on the host filesystem.

  * CVE-2026-60137: An unauthenticated SQL injection vulnerability affecting WordPress. Threat actors exploit unsanitized input parameters to execute arbitrary SQL queries, leading to unauthorized database access, record manipulation, or data exfiltration.

  * CVE-2026-63030: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...215e7d31| N/A| SSRF - Restricted Protocol| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a935ee5d| N/A| SSRF - Obfuscated Host| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1b0230ac| N/A| LFI - Path Traversal| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...61349c8b| N/A| Adobe ColdFusion - File Upload Path Traversal - CVE:CVE-2026-48276| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9cb61eac| N/A| Adobe ColdFusion - Path Traversal - CVE:CVE-2026-48282| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...4ac5e21f| N/A| XSS — JS Bracket Concat Obfuscation - Body| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...f31f5559| N/A| XSS — JS Bracket Concat Obfuscation - Headers| Log| Disabled| This is a new detection.  
Cloudflare Managed Ruleset| ...987984fd| N/A| XSS — JS Bracket Concat Obfuscation - URI| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...ed933fcc| N/A| Wordpress - SQL Injection - CVE:CVE-2026-60137| N/A| Block| This was labeled as Generic Rules - SQLi.  
Cloudflare Managed Ruleset| ...550664b6| N/A| Wordpress - Remote Code Execution - CVE:CVE-2026-63030| N/A| Block| This was labeled as Generic Rules - Unauthenticated RCE.  
Cloudflare Free Ruleset| ...33697a1a| N/A| Wordpress - SQL Injection - CVE:CVE-2026-60137| N/A| Block| This was labeled as Generic Rules - SQLi.  
Cloudflare Free Ruleset| ...b5ec246a| N/A| Wordpress - Remote Code Execution - CVE:CVE-2026-63030| N/A| Block| This was labeled as Generic Rules - Unauthenticated RCE.  
Cloudflare Managed Ruleset| ...72952826| N/A| Next.js - Information Disclosure - CVE-2026-64643| N/A| Block| This was labeled as Generic Rules - Information Disclosure.  
Cloudflare Managed Ruleset| ...930091a3| N/A| Next.js - SSRF - CVE-2026-64649| N/A| Block| This was labeled as Generic Rules - Auth Bypass - 2.  
Cloudflare Managed Ruleset| ...63167195| N/A| Next.js - Remote Code Execution - Cache Components| N/A| Block| This was labeled as Generic Rules - RCE.  
Cloudflare Managed Ruleset| ...90dcdb0a| N/A| Next.js - DoS - CVE-2026-64641| N/A| Block| This was labeled as Generic Rules - DoS.  
Cloudflare Managed Ruleset| ...2049a60c| N/A| Generic Rules - Command Execution - Body - Beta| Disabled|  \- | This detection has been removed.  
Cloudflare Managed Ruleset| ...836855a4| N/A| Generic Rules - Command Execution - Header - Beta| Disabled|  \- | This detection has been removed.  
Cloudflare Managed Ruleset| ...6d060a0d| N/A| Generic Rules - Command Execution - URI - Beta| Disabled|  \- | This detection has been removed.
