---
url: https://developers.cloudflare.com/changelog/product-group/application-security/
title: Application security Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:25.207219+00:00
---

# Application security Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/application-security/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 9, 2026

## [Failed detections field available in Rules](https://developers.cloudflare.com/changelog/post/2026-10-09-failed-detections/)

[WAF](https://developers.cloudflare.com/waf/)[Rules](https://developers.cloudflare.com/rules/)

You can now use `cf.appsec.request.failed_detections` to control how your rules handle requests when a security detection reports a failure.

The field is an `Array<String>` of detection IDs that reports failures from content scanning, WAF attack score, attack signature detection, leaked credentials detection, and AI prompt detections for personally identifiable information (PII), prompt injection, custom topics, and unsafe topics.

The field does not alter the existing behavior of detections. Use it in rules to choose how to handle requests with reported failures.

When no failures are reported, the field returns `[]`. You can use it on all plans, but your plan must still include the detections and rule features you want to use.

Supported rules:

  * Custom rules at the zone and account levels
  * Rate limiting rules at the zone and account levels
  * Request Header Transform Rules at the zone level



Match any reported failure:
    
    
    len(cf.appsec.request.failed_detections) gt 0

Match a reported leaked credentials detection failure:
    
    
    any(cf.appsec.request.failed_detections[*] eq "waf_credential_check")

For more information, refer to the [Failed detections field reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.appsec.request.failed_detections/).

Oct 7, 2026

## [Updated unsafe topic detection for AI Security for Apps](https://developers.cloudflare.com/changelog/post/2026-10-07-ai-security-for-apps-unsafe-topic-detection/)

[WAF](https://developers.cloudflare.com/waf/)

AI Security for Apps now supports an updated set of categories for detecting unsafe topics in incoming prompts.

The values available in [`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) have changed. Existing WAF custom rules remain valid, but rules that reference a removed or renamed category will no longer match that category. Review any rules that use this field and update their expressions to use the currently supported values.

For category descriptions and configuration guidance, refer to [Unsafe topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/).

Oct 6, 2026

## [WAF Release - 2026-10-06](https://developers.cloudflare.com/changelog/post/2026-10-06-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces a new detection to mitigate a heap-based buffer overflow vulnerability in F5 BIG-IP, and enhances existing command injection protections by incorporating tested beta logic into the baseline rule.

**Key Findings**

  * CVE-2026-94127: A heap-based buffer overflow vulnerability in F5 BIG-IP. Attackers can exploit this flaw to execute arbitrary code on the affected system.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...a056caff| N/A| Command Injection - Generic 8 - uri - Beta| Log| Block| This rule is merged into the original rule "Command Injection - Generic 8 - uri" (ID: ...ee159e2e).  
Cloudflare Managed Ruleset| ...7206c737| N/A| F5 BIG-IP - UnAuth Heap-Overflow - CVE:CVE-2026-94127| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...549f7356| N/A| Next.js - Cache Poisoning - CVE:CVE-2026-94543| Block| Block| Rule metadata description refined. Detection unchanged.  
  
Oct 6, 2026

## [WAF Release - Scheduled changes for 2026-10-12](https://developers.cloudflare.com/changelog/post/scheduled-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

Announcement Date| Release Date| Release Behavior| Legacy Rule ID| Rule ID| Description| Comments  
---|---|---|---|---|---|---  
2026-10-06| 2026-10-12| Disable| N/A| ...02751ef3| Generic Rules - Template Injection - 2 - Beta| This rule will be merged into the original rule "Generic Rules - Template Injection - 2" (ID: ...d3ed0123).  
  
Oct 2, 2026

## [hash_in_range() is globally available for HTTP products](https://developers.cloudflare.com/changelog/post/2026-10-02-hash-in-range-ga/)

[Rules](https://developers.cloudflare.com/rules/)

`hash_in_range()` is globally available for HTTP products on all plans. It hashes fields into an integer within a specified range. Use this result to select a portion of requests.

Use `cf.random_seed` to select approximately 10% of requests at random:
    
    
    hash_in_range(0, 100, cf.random_seed) < 10

With Cloudflare for SaaS, use [custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/) to control rollout progression. Define `rollout_pct` as a custom key for each hostname. Set its value to an integer from 0 to 100. The expression selects approximately that percentage of requests:
    
    
    hash_in_range(0, 100, cf.random_seed) < coalesce(lookup_json_integer(cf.hostname.metadata, "rollout_pct"), 0)

If `rollout_pct` is missing, `coalesce()` supplies `0`. The rule then matches no requests.

For details, refer to the [`hash_in_range()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#hash_in_range).

Oct 2, 2026

## [Protect Quick Tunnels with email authentication](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)

You can now restrict who can access a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/). Use the new `--allowed-mail` flag in `cloudflared` to require visitors to authenticate with a one-time PIN sent to their email before they reach your local service.
    
    
    cloudflared tunnel --url http://localhost:8080 --allowed-mail alice@example.com

![Protected Quick Tunnel demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=854,format=webp/_astro/protected-quick-tunnels.DlA306r_.gif)

Previously, anyone with a `trycloudflare.com` URL could access the service behind it. Protected Quick Tunnels let you share a local development server, webhook receiver, or demo with specific people without creating a Cloudflare account or configuring a domain.

You can allow:

  * A single email address: `--allowed-mail alice@example.com`
  * Multiple email addresses, by repeating the flag or using a comma-separated list: `--allowed-mail 'alice@example.com,bob@example.com'`
  * Every address on a domain: `--allowed-mail '*@example.com'`



Visitors do not need a Cloudflare account. Access ends for everyone when you stop the `cloudflared` process.

To get started, [update `cloudflared`](https://developers.cloudflare.com/tunnel/downloads/) to the latest version and refer to [Restrict access by email](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/#restrict-access-by-email).

Oct 1, 2026

## [Handle missing values with coalesce()](https://developers.cloudflare.com/changelog/post/2026-10-01-coalesce-function/)

[Rules](https://developers.cloudflare.com/rules/)

The `coalesce()` function returns the first argument that is not nil. Use it to provide a fallback in rule expressions:
    
    
    http.request.uri.path eq coalesce(http.request.uri.args["expected_path"][0], "/")

For details, refer to the [`coalesce()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#coalesce).

Oct 1, 2026

## [Compare dynamic values in Rules expressions](https://developers.cloudflare.com/changelog/post/2026-10-01-dynamic-comparison-values/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules expressions now support dynamic values on both sides of equality and ordering comparisons. You can compare request fields or function results with one another.

For example, compare the current request path with its original value:
    
    
    http.request.uri.path ne raw.http.request.uri.path

For supported operators and examples, refer to [Compare dynamic values](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#compare-dynamic-values).

Oct 1, 2026

## [WAF Release - 2026-10-01 - Emergency](https://developers.cloudflare.com/changelog/post/2026-10-01-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This update provides immediate defense against a vulnerability affecting Citrix NetScaler ADC and Gateway appliances, deploying protection against improper input validation vectors.

**Key Findings**

  * CVE-2026-88771: An improper input validation vulnerability affecting Citrix NetScaler ADC and Gateway allows an unauthenticated attacker to execute arbitrary commands.



**Impact**

We strongly recommend that administrators apply the latest versions to fully secure origin servers. Additionally, customers should review configurations against applicable preconditions and follow standard incident response processes if signs of compromise are identified.

Detailed Rule Changes

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...827ab216| N/A| Citrix Netscaler ADC and Gateway - Improper input validation - CVE:CVE-2026-88771| N/A| Block| This is a new detection.  
  
Sep 30, 2026

## [WAF Release - 2026-09-30](https://developers.cloudflare.com/changelog/post/2026-09-30-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new detections to enhance protection against a specific GitLab path traversal vulnerability, alongside advanced generic rules targeting HTTP request smuggling, directory traversal, and command injection attempts.

**Key Findings**

  * CVE-2026-85706: A path traversal vulnerability affecting GitLab.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...cb14ded8| N/A| Broken Access Control - Directory Traversal| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...0364bd7e| N/A| HTTP Request Smuggling - Request Body Anomaly - Beta| Log| Block| This rule is merged into the original rule "HTTP/2 Request Smuggling - Request Body Anomaly" (ID: ...1489d892).  
Cloudflare Managed Ruleset| ...d498a69a| N/A| Command Injection - Generic 8 - body - Beta| Disabled| Disabled| This rule is merged into the original rule "Command Injection - Generic 8 - body" (ID: ...413592e2).  
Cloudflare Managed Ruleset| ...87ae8cfc| N/A| GitLab - Path Traversal- CVE:CVE-2026-85706| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...549f7356| N/A| Generic - Request routing cache inconsistency| N/A| Block| This is a new detection.  
  
Sep 29, 2026

## [Identify Mesh, Workers VPC, and Cloudflare Tunnel replicas in network logs](https://developers.cloudflare.com/changelog/post/2026-09-29-mesh-workers-vpc-network-logs/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

You can now tell a person on a laptop apart from a Mesh node or an AI agent running on Workers, without matching on connector email addresses or Mesh IP ranges — and see exactly which Cloudflare Tunnel and `cloudflared` replica received each session.

[Gateway network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs) and [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/) now identify two new kinds of traffic:

  * **Mesh** — Traffic sent from or delivered to a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node. Previously, Mesh nodes were logged the same way as devices running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), because Mesh nodes run the client in headless mode.
  * **Workers VPC** — Traffic sent by a Worker through a [Workers VPC](https://developers.cloudflare.com/workers-vpc/) binding. Previously, Workers VPC sessions were not recorded in Network Session Logs.

![Viewing Mesh and Workers VPC traffic in Gateway network logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1439,height=796,format=webp/_astro/2026-09-28-mesh-workers-vpc-network-logs.iGvLKYk7.gif)

#### Gateway network logs

To view these values in the dashboard, go to **Zero Trust** > **Insights & Logs** > **Logs** > **Network logs** , select **Columns** , and turn on **Traffic Source** and **Traffic Destination**. Both values also appear under **Network query details** when you open a log entry.

#### Network Session Logs

The `zero_trust_network_sessions` dataset, available through [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/), includes the following fields:

Field | Description  
---|---  
`OnrampType` | How the session entered Cloudflare One. Values: `CF1_CLIENT`, `MESH`, `WORKERS_VPC`, `MAGIC`, `OTHER`.  
`Offramp` | Where the session was routed. Sessions routed to a Mesh node report `MESH`.  
`SourceName` | Name of the Worker that started the session. Only populated for Workers VPC sessions.  
`SourceID` | Stable identifier of the Worker that started the session. Only populated for Workers VPC sessions.  
`DestinationReplicaID` | The replica that served the session, such as a specific replica of a Mesh node or a `cloudflared` replica of a Cloudflare Tunnel.  
  
For example, `OnrampType = 'WORKERS_VPC' AND Offramp = 'MESH'` returns every session where a Worker reached a service behind a Mesh node, and `SourceName` tells you which Worker it was.

Redeploy your Workers

`SourceName` and `SourceID` are only populated for Workers deployed after 29 September 2026. To include them for an existing Worker, redeploy it — for example, with `npx wrangler deploy`. No code changes are required.

#### See which tunnel and replica received a session

With `DestinationReplicaID`, you can now confirm which [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and which `cloudflared` replica received traffic for a specific session. Combine it with the existing `DestinationTunnelID` field to trace a session to an exact tunnel replica — or Mesh node replica — when you run multiple replicas for high availability. The replica ID matches the **Connector ID** shown in the dashboard, so you can [stream that replica's logs](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) with `cloudflared tail --connector-id`.

Sessions logged before this change are not backfilled. For all available fields, refer to [Zero Trust Network Session Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/).

Sep 25, 2026

## [WAF Release - 2026-09-25 - Emergency](https://developers.cloudflare.com/changelog/post/2026-09-25-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This update provides immediate defense against critical vulnerabilities affecting WordPress and JFrog Artifactory, including path traversal, local file inclusion (LFI), cross-site scripting (XSS), and authentication bypass exploits.

**Key Findings**

  * CVE-2026-87902: A high-severity Path Traversal and Local File Inclusion (LFI) vulnerability affecting WordPress. Unauthenticated attackers can exploit this flaw to read arbitrary files on the host server, potentially exposing sensitive configuration data or system files.

  * CVE-2026-42018 & CVE-2026-82329: Critical authentication bypass vulnerabilities affecting JFrog Artifactory. Successful exploitation allows unauthenticated attackers to bypass security controls and achieve unauthorized access to the Artifactory instance.




**Impact**

We strongly recommend that administrators apply the latest vendor patches for WordPress and JFrog Artifactory to fully secure origin servers.

Detailed Rule Changes

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...70a43f96| N/A| Wordpress - Path Traversal, Local File Inclusion - CVE:CVE-2026-87902| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...909a4db4| N/A| Wordpress - XSS - Comment| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...c797ef03| N/A| JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-42018| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a813ac74| N/A| JFrog Artifactory - Authentication Bypass - CVE:CVE-2026-82329| N/A| Block| This is a new detection.  
  
Sep 22, 2026

## [concat() now supports up to 32 arguments](https://developers.cloudflare.com/changelog/post/2026-09-22-concat-argument-limit/)

[Rules](https://developers.cloudflare.com/rules/)

The `concat()` function in Cloudflare Rules now accepts up to 32 arguments, increased from 16. This allows you to build richer dynamic values directly in Rules expressions and simplify configurations that combine request data.

A common use case is adding a request header that sends context to your origin. The following Rulesets API request adds a Request Header Transform Rule to an existing `http_request_late_transform` phase ruleset. Its 18-argument expression combines request and network information into one header value:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID/rules" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "ref": "add_request_context_header",
        "description": "Add request context for the origin",
        "expression": "true",
        "action": "rewrite",
        "action_parameters": {
          "headers": {
            "X-Request-Context": {
              "operation": "set",
              "expression": "concat(\"ip=\", to_string(ip.src), \";country=\", ip.src.country, \";host=\", http.host, \";method=\", http.request.method, \";path=\", http.request.uri.path, \";query=\", http.request.uri.query, \";ray-id=\", cf.ray_id, \";asn=\", to_string(ip.src.asnum), \";user-agent=\", http.user_agent)"
            }
          }
        }
      }'

For more information, refer to the [`concat()` function reference](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#concat) and [HTTP request header modification](https://developers.cloudflare.com/rules/transform/request-header-modification/).

Sep 22, 2026

## [WAF Release - 2026-09-22](https://developers.cloudflare.com/changelog/post/2026-09-22-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new threat detections to enhance protection against Server-Side Request Forgery (SSRF) attempts using non-standard IP notations or jar loopback payloads, alongside new defenses against Server-Side Template Injection (SSTI) targeting Jinja environments.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...5f21b651| N/A| SSRF - Cloud,Link-Local non-standard IP notation| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...0f0313d6| N/A| SSRF - Block jar HTTP loopback payload| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...75cd912a| N/A| SSRF - Local non-standard IP notation| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a1ba83f6| N/A| SSTI - Jinja Dangerous Globals Chain| Log| Block| This is a new detection.  
  
Sep 18, 2026

## [cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

Sep 17, 2026

## [Validate Rulesets changes before deployment](https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration.

The Cloudflare dashboard performs this validation automatically when you create or update rules from **Security** > **Security rules** or **Rules** > **Overview**.

Supported Rulesets API mutation endpoints now also accept the `dry_run=true` query parameter. A dry run performs the same authorization and server-side validation checks as the requested change, but does not persist or publish it. Successful operations that normally return a `200` response return `result: null`. Operations that normally return `204` continue to do so.

#### API example

Add `dry_run=true` to a Rulesets API request to validate it without creating the ruleset:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets?dry_run=true" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Custom firewall rules",
        "kind": "zone",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "action": "block",
            "expression": "ip.src.country eq \"GB\"",
            "description": "Block requests from the United Kingdom",
            "enabled": true
          }
        ]
      }'

For more information, refer to [Validate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/).

Sep 16, 2026

## [Control JavaScript Detections API results](https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/)

[Bots](https://developers.cloudflare.com/bots/)

Enterprise Bot Management customers can control whether Cloudflare uses results created through the JavaScript Detections API for bot scoring and detections.

Turn **JavaScript Detections for API traffic** on or off in **Security** > **Settings**. You can also configure the zone through the Bot Management API by setting `jsd_api_results_enabled`:
    
    
    {
    	"jsd_api_results_enabled": true
    }

This setting is separate from zone-wide script injection. When it is off, the API script can still execute and return `success` to the callback, but Cloudflare does not consume the result.

For more information, refer to [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#api).

Sep 15, 2026

## [WAF Release - 2026-09-15](https://developers.cloudflare.com/changelog/post/2026-09-15-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...ca453d31| N/A| SSRF - Cloud - 3| Log| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...e540f17f| N/A| Version Control - Information Disclosure - Beta| Log| Block| This rule is merged into the original rule "Version Control - Information Disclosure" (ID: ...0550c529).  
Cloudflare Managed Ruleset| ...ba458b4b| N/A| Command Injection - Generic 10| Log| Block| This is a new detection.  
  
Sep 10, 2026

## [WAF Release - 2026-09-10 - Emergency](https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.

**Key Findings**

  * Adobe Commerce and Magento RCE (CVE-2026-75650 / "StyleSmuggler"): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.



**Impact**

This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin [APSB26-146](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146) and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...440f5c55| N/A| Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650| N/A| Block| This is a new detection.  
  
Sep 8, 2026

## [WAF Release - 2026-09-08](https://developers.cloudflare.com/changelog/post/2026-09-08-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...c76ba662| N/A| Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta| Log| Block| This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID: ...80256efe).  
Cloudflare Managed Ruleset| ...208457cf| N/A| Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta| Log| Block| This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID: ...2ca6cce3).  
  
Sep 7, 2026

## [Enforce positive security with Application Profiles](https://developers.cloudflare.com/changelog/post/2026-09-07-application-profiles/)

[WAF](https://developers.cloudflare.com/waf/)

Application Profiles add a positive-security layer to Cloudflare WAF. Instead of looking only for requests that resemble known attacks, Application Profiles learn what valid requests to your application look like and identify traffic that deviates from the expected structure.

The first available profile type, Schema Profiles, can learn path variables, query parameters, headers, cookies, JSON bodies, and form-encoded bodies. Profiles model field types and constraints such as numeric ranges, string lengths, and character classes. After a profile becomes available, an always-on detection classifies requests as conforming or non-conforming without blocking traffic.

Use **Profile Analysis** in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) to review conformance trends and sampled violation details before enforcing a profile. When you are ready to mitigate traffic, use a [Custom Rule](https://developers.cloudflare.com/waf/custom-rules/) to scope enforcement by hostname, path, operation, or other security signals such as Attack Score.

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is also opening a closed beta to invited Enterprise customers without API Security. Contact your Cloudflare account team to express interest.

For more information, refer to [Application Profiles](https://developers.cloudflare.com/waf/detections/application-profiles/).

Sep 7, 2026

## [Attack Signature Detection is now available in Early Access](https://developers.cloudflare.com/changelog/post/2026-09-07-attack-signature-detection/)

[WAF](https://developers.cloudflare.com/waf/)

Attack Signature Detection is now available in Early Access. It evaluates requests against Cloudflare attack signatures and records matches without applying a mitigation action, allowing you to investigate detected traffic before deciding how to respond.

In **Security Analytics** > **Attack Analysis** , you can review matching signature references, categories, confidence levels, and request outcomes. You can then use these fields in [Security Rules](https://developers.cloudflare.com/security/rules/) and combine them with request properties such as hostname, path, and HTTP method to apply scoped mitigation.

Attack Signature Detection uses the same signature definitions as [Cloudflare Managed Rules](https://developers.cloudflare.com/waf/managed-rules/), but it does not inherit your Managed Rules actions, overrides, or deployment configuration. Managed Rules remain the recommended baseline protection during Early Access.

Contact your Cloudflare account team to request access. For more information, refer to [Attack Signature Detection](https://developers.cloudflare.com/waf/detections/attack-signature-detection/).

Sep 2, 2026

## [Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once](https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

  * **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
  * **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
  * **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.



The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).

Sep 1, 2026

## [Updated PII detection for AI Security for Apps](https://developers.cloudflare.com/changelog/post/2026-09-01-ai-security-for-apps-pii-detection/)

[WAF](https://developers.cloudflare.com/waf/)

AI Security for Apps now supports an updated set of categories for detecting personally identifiable information (PII) in incoming prompts.

The values available in [`cf.llm.prompt.pii_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_categories/) have changed. Existing WAF custom rules remain valid, but rules that reference a removed or renamed category will no longer match that category. Review any rules that use this field and update their expressions to use the currently supported values.

For the complete category list and configuration guidance, refer to [PII detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/).

Sep 1, 2026

## [WAF Release - 2026-09-01](https://developers.cloudflare.com/changelog/post/2026-09-01-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.

**Key Findings**

  * SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...bcfa0966| N/A| SQLi - WHERE Comparison With WITH Clause| Log| Block| This is a new detection.  
  
← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/application-security/2/)…[9](https://developers.cloudflare.com/changelog/product-group/application-security/9/)

[Next →](https://developers.cloudflare.com/changelog/product-group/application-security/2/)
