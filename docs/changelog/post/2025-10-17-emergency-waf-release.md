---
url: https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/
title: New detections released for WAF managed rulesets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.622822+00:00
---

# New detections released for WAF managed rulesets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 17, 2025

## New detections released for WAF managed rulesets

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.

**Key Findings**

New detections added for multiple exploit categories:

SSRF (Server-Side Request Forgery) — new rules targeting both local and cloud metadata abuse patterns (Beta).

SQL Injection (SQLi) — rules for common patterns, sleep/time-based injections, and string/wait function exploitation across headers and URIs.

SSTI (Server-Side Template Injection) — arithmetic-based probe detections introduced across URI, header, and body fields.

Reverse Shell and XXE payloads — enhanced heuristics for command execution and XML external entity misuse.

Prototype Pollution — new Beta rule identifying common JSON payload structures used in object prototype poisoning.

PHP Wrapper Injection and HTTP Parameter Pollution detections — to catch path traversal and multi-parameter manipulation attempts.

Anomaly Header Checks — detecting CRLF injection attempts in header names.

**Impact**

These updates help detect multi-vector payloads that blend SSRF + RCE or SQLi + SSTI attacks, especially in cloud-hosted applications with exposed metadata endpoints or unsafe template rendering.

Prototype Pollution and HTTP parameter pollution rules address emerging JavaScript supply-chain exploitation patterns increasingly seen in real-world incidents.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...589f2a1d| N/A| Anomaly:Header - name - CR, LF| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...132fab7e| N/A| Generic Rules - Reverse Shell - Body| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...1a027008| N/A| Generic Rules - Reverse Shell - Header| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...958d0486| N/A| Generic Rules - Reverse Shell - URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...8e0cf7ad| N/A| Generic Rules - XXE - Body| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...bf8aab5e| N/A| Generic Rules - SQLi - Common Patterns - Header URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...2e466337| N/A| Generic Rules - SQLi - Sleep Function - Header URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...b686ab47| N/A| Generic Rules - SQLi - String Function - Header URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...b0633709| N/A| Generic Rules - SQLi - WaitFor Function - Header URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...01a076eb| N/A| SSRF - Local - Beta| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...743a63ec| N/A| SSRF - Local - 2 - Beta| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...c2e84e2d| N/A| SSRF - Cloud - Beta| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...ab8af26f| N/A| SSRF - Cloud - 2 - Beta| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...e6e8dc5b| N/A| SSTI - Arithmetic Probe - URI| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...2550d794| N/A| SSTI - Arithmetic Probe - Header| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...659d12a6| N/A| SSTI - Arithmetic Probe - Body| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...1a3e521e| N/A| PHP Wrapper Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...8f76bd74| N/A| PHP Wrapper Injection| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...091e296d| N/A| HTTP parameter pollution| N/A| Disabled| This is a New Detection  
Cloudflare Managed Ruleset| ...e34214ef| N/A| Prototype Pollution - Common Payloads - Beta| N/A| Disabled| This is a New Detection
