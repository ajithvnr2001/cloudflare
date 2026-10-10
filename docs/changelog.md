---
url: https://developers.cloudflare.com/changelog/
title: Changelogs | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:04.871253+00:00
---

# Changelogs | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/

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

Oct 10, 2026

## [Cloudflare API MCP server serves Cloudflare skills](https://developers.cloudflare.com/changelog/post/2026-10-10-cloudflare-mcp-skills/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now serves [Cloudflare skills ↗︎](https://github.com/cloudflare/skills) through the [Skills over MCP extension ↗︎](https://modelcontextprotocol.io/extensions/skills/overview). MCP clients that support the extension discover the skills with `skills/list` and read their files at `skill://<name>/<path>`.

To use them, add `https://mcp.cloudflare.com/mcp` to an [MCP client that supports the extension ↗︎](https://modelcontextprotocol.io/extensions/client-matrix).

Oct 9, 2026

## [Improved HTTP/3 client cancellation reporting](https://developers.cloudflare.com/changelog/post/2026-10-09-http3-499-reporting-improvement/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare has improved how it handles and reports client-cancelled HTTP/3 requests across Free, Pro, Business, and Enterprise plans. Customers now get a clearer view of client behavior in Cloudflare analytics and, where available, logs.

Previously, Cloudflare did not always stop an HTTP/3 request when the client cancelled its request stream. Some cancellations were already recorded as `499`, while others continued to the origin and showed the eventual upstream status.

Cloudflare now stops affected requests sooner, reducing unnecessary origin work, and records them as `499`. Customers may notice more `499` status codes for HTTP/3 traffic. This reflects more consistent reporting of existing cancellations, not an increase in failed requests.

Customers who use `499` status codes in availability calculations should consider excluding them from server-side error rates because they represent requests cancelled by clients.

For more information, refer to [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/).

Oct 9, 2026

## [More efficient Markdown for Agents conversion](https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now converts HTML with an in-process streaming engine at the edge. It processes content as it arrives instead of buffering the HTML response and sending it to a separate conversion service. This reduces conversion overhead and memory use.

This release also changes the conversion limit and response headers:

  * Conversion supports up to 6 MiB (6,291,456 bytes) of decompressed HTML, increased from 2 MiB (2,097,152 bytes). The limit applies after decompression, not to the compressed response size.
  * Converted responses no longer generate the `x-markdown-tokens` or `x-original-tokens` headers. Clients that use these values need to calculate token counts themselves.
  * `Content-Length` is removed from converted responses rather than recalculated, because the Markdown body is streamed.



For more information, refer to the [Markdown for Agents documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).

Oct 9, 2026

## [R2 bandwidth by Cloudflare location](https://developers.cloudflare.com/changelog/post/2026-10-09-r2-bandwidth-by-location/)

[R2](https://developers.cloudflare.com/r2/)

You can now view R2 bandwidth by the Cloudflare location that served each request in the Cloudflare UI. This helps you see which locations consume the most bandwidth with options to select a specific bucket and download (read) vs upload (write) bandwidth.

[ Go to **R2 overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 bandwidth by location chart showing throughput for the top five Cloudflare locations](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=665,height=427,format=webp/_astro/r2-bandwidth-by-location.JMiyoI-0.png)

By default, the chart shows the top five locations by total bandwidth consumed during the selected time range. Use the **Top 5 locations** dropdown to select other locations, up to six at a time.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

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

Oct 9, 2026

## [Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) is now available on Workers AI. Clef-omni is a decision model that takes audio (WAV or MP3) and video (MP4 or WebM) input alongside text and images. It joins [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/) in the Clef family of open-weight decision models. We also cut the price of Clef-flash, so it now costs less than Jev, and made Clef faster.

#### Clef-omni: one decision model for every modality

Previously, making a decision about a voice recording or a video meant chaining models together: transcribe the speech, split the audio and visual tracks, then pass the results to a text decision model. Clef-omni reads every modality directly in one request. A video's soundtrack is aligned with its frames, so the model can reason over what is seen and heard at the same time.

Clef-omni is built on a 30B-parameter mixture-of-experts (MoE) backbone with 3B active parameters. Like the rest of the Clef family, it does not generate text. It scores every allowed answer in a single pass, so decisions return quickly:

  * Text requests: about 20 ms
  * Image or audio inputs: under 100 ms
  * A 21-second video clip with sound: about 300 ms



Pass media as base64 data URLs in the `images`, `audio`, and `videos` fields:
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });

Clef-omni scores highest of the Clef family on BANKING77, CLINC150+OOS, and Amazon ESCI:

Benchmark | Clef-omni | Clef | Clef-flash | Jev  
---|---|---|---|---  
BFCL (case exact) | 98.2 | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.8** | 94.20 | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.7** | 97.43 | 66.77 | 89.27  
Amazon ESCI (macro-F1) | **57.8** | 57.48 | 57.39 | 55.21  
PhishNChips (accuracy) | 73.2 | **79.60** | 75.05 | 62.55  
  
#### Clef-flash is now cheaper

Clef-flash now costs **$0.038 per million input tokens** , down from $0.090, which makes it cheaper than Jev. To offer this price, the hosted Clef-flash context window is now 24K tokens, down from 64K. Based on usage data, only 0.24% of requests exceed 24K input tokens. If you need a larger context window, use Clef, which keeps its 64K context window.

The Clef-flash weights on Hugging Face are unchanged and support up to a 256K context window if you self-host.

Model | Price | Context window  
---|---|---  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | $0.038 per M input tokens | 24K tokens  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | $0.240 per M input tokens | 64K tokens  
[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) | $0.150 per M input tokens | 64K tokens  
  
All Clef models convert image inputs to input tokens, and Clef-omni does the same for audio and video. For details on how each input type is tokenized, refer to the [Clef](https://developers.cloudflare.com/workers-ai/models/clef/), [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [Clef-omni](https://developers.cloudflare.com/workers-ai/models/clef-omni/) model pages.

#### Clef is now faster

We optimized how Clef is served on Workers AI, so it now returns decisions up to 2x faster. The model weights are unchanged.

Input size | Before: median / p95 (ms) | Now: median / p95 (ms) | Median speedup  
---|---|---|---  
~800 tokens | 262 / 438 | 152 / 351 | 1.7x  
~3,400 tokens | 616 / 777 | 305 / 531 | 2.0x  
~16,000 tokens | 2,721 / 3,250 | 1,635 / 1,805 | 1.7x  
  
Part of this speedup comes from moving Clef to [SGLang ↗︎](https://github.com/sgl-project/sglang). Clef support is coming to SGLang in version 0.5.22 ([PR #42721 ↗︎](https://github.com/sgl-project/sglang/pull/42721)). If you self-host Clef, launch commands are available in the [Clef collection on Hugging Face ↗︎](https://huggingface.co/collections/Cloudflare/clef).

#### Get started

Clef-omni follows the same System One API as Clef and Clef-flash, and works with [AI Gateway](https://developers.cloudflare.com/ai-gateway/). To try it, change the model ID to `@cf/cloudflare/clef-omni` and set the `model` selector to `clef-omni`.

For more information, refer to the [Clef-omni model page](https://developers.cloudflare.com/workers-ai/models/clef-omni/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Oct 8, 2026

## [Create Workflow instance batches by count or list](https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

[`createBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch) now accepts an options object that creates up to 100 Workflow instances in one call. The result lists the created instances and explains why any others were not created. To use this form in local development and get its types from `wrangler types`, use Wrangler 4.148.0 or later.

To create instances that share the same options, pass `count`. Each instance receives a generated ID:
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });

To give each instance its own ID or options, pass `instances`:
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }

`created` contains the created instances. `errors` contains each entry that was not created, identified by its position in the input. IDs that already exist and IDs repeated within the batch are reported as errors instead of being skipped silently.

Passing an array to `createBatch()` is deprecated. Existing code that uses the array form continues to work.

For more information, refer to [`createBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch).

Oct 7, 2026

## [Cloudflare One Client for macOS (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster connects and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Oct 7, 2026

## [Cloudflare One Client for Windows (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across tunnel reconnections.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved connection reliability on devices with very large hosts files. The client now detects a large hosts file, allows more time for its initial DNS check, and shows a banner letting the user know that connecting may take longer.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * A service recovery mechanism, backed by a Windows scheduled task, now starts the client service on system unlock if it is not already running. This is enabled by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client service failing to restart after an unexpected termination.
  * Fixed the client UI getting stuck in a connecting state after sleep and wake even though the tunnel was connected.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While this release includes a fix to mitigate this issue, users may still experience reduced DNS performance and connectivity check failures.



Oct 7, 2026

## [Cloudflare One Client for Linux (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Oct 7, 2026

## [Query Log Explorer datasets from Observability Logs](https://developers.cloudflare.com/changelog/post/2026-10-07-log-search-in-observability-logs/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer datasets are now queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The Logs page brings Log Explorer and Workers Observability datasets together with a shared filter builder, SQL editor, and visualizations.

As part of this change, the **Log Explorer** menu is no longer shown in the dashboard navigation.

  * Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page.
  * To manage datasets, open the dataset selector on the Logs page and select **Configure** next to the Log Explorer datasets.
  * The previous Log Search page remains available at its direct URL.



For more information, refer to [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and the [Logs overview](https://developers.cloudflare.com/observability/logs/).

Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 7, 2026

## [Updated unsafe topic detection for AI Security for Apps](https://developers.cloudflare.com/changelog/post/2026-10-07-ai-security-for-apps-unsafe-topic-detection/)

[WAF](https://developers.cloudflare.com/waf/)

AI Security for Apps now supports an updated set of categories for detecting unsafe topics in incoming prompts.

The values available in [`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) have changed. Existing WAF custom rules remain valid, but rules that reference a removed or renamed category will no longer match that category. Review any rules that use this field and update their expressions to use the currently supported values.

For category descriptions and configuration guidance, refer to [Unsafe topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/).

Oct 6, 2026

## [Standardize provider credential error responses in AI Gateway](https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to [`POST /ai/run` ↗︎](https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT_ID%7D/ai/run).

Scenario | Previous AI Gateway response | New AI Gateway response  
---|---|---  
ElevenLabs | Provider-specific `UserCredentialsError` with HTTP `403` | HTTP `401` with error code `2009`  
Google Vertex | HTTP `500` for rejected credentials, with upstream retries | HTTP `401` with error code `2009`; the request fails without retrying the provider  
All other providers | HTTP `402` or another provider-specific status for rejected credentials | HTTP `401` with error code `2009`  
When using [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), the provider rejects the credentials | Provider-specific authentication error | HTTP `503`  
  
Update applications that handle AI Gateway REST API errors to treat HTTP `401` as an invalid or rejected provider credential.

For details about providing provider credentials, refer to [Bring your own provider keys](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-key/).

Oct 6, 2026

## [Warnings when approaching your DNS records quota](https://developers.cloudflare.com/changelog/post/2026-10-06-dns-records-quota-warning/)

[DNS](https://developers.cloudflare.com/dns/)

The DNS records page in the Cloudflare dashboard now shows a warning once you have used 85% of your [DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#dns-records-quota).

The warning reflects the quota that applies to you. If your zone has its own quota, the warning shows that zone's usage. If your account uses an [account-level DNS records quota](https://developers.cloudflare.com/dns/manage-dns-records/#per-account-quota), the warning shows your usage across all zones in the account.

![Warning on the DNS records page showing that a domain has used 86% of its DNS record limit](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1520,height=226,format=webp/_astro/dns-records-quota-warning.iH_msM4_.png)

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
  
Oct 5, 2026

## [Detect organization-specific risks with CASB custom finding types](https://developers.cloudflare.com/changelog/post/2026-10-05-casb-custom-findings/)

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

[Cloudflare CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) now supports [**custom finding types**](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/), giving security teams full control over the security conditions CASB detects across their SaaS and cloud integrations.

In addition to CASB's library of standard finding types, you can now write your own detection logic using [Rego ↗︎](https://www.openpolicyagent.org/docs/policy-language), the open-source policy language from Open Policy Agent (OPA). Use custom finding types to match your organization's own thresholds and exceptions, such as flagging admin accounts without two-factor authentication, and get higher-confidence findings to act on.

![Create a custom finding type with a name, severity, scope, and Rego detection logic](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1194,height=1194,format=webp/_astro/create-custom-finding-type.CF3GXoPZ.png)

#### Key capabilities

  * **Write your own detection logic** — Define exactly what CASB flags using Rego expressions evaluated against asset data from your connected integrations.
  * **Target any supported provider and asset class** — Scope a custom finding type to a provider (such as Google Workspace or Microsoft 365) and asset class (such as users, files, or groups), and apply it to all integrations for that provider or a selected subset.
  * **Built-in validation** — Select **Validate** to check your expression for syntax errors and schema issues before you create the finding type.
  * **Inspect and duplicate standard finding types** — Open any standard finding type to view its detection logic, then duplicate it as the starting point for a custom finding type.
  * **Works with CASB policies** — Use custom finding types in [CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) to send matching findings to Slack, ServiceNow, or any other webhook destination.



#### Get started

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com), go to **Cloud & SaaS findings** > **Findings library**.
  2. Select **Create finding**.
  3. Enter a name, description, and severity.
  4. Select a provider and asset class, then set the integration scope.
  5. Write your Rego expression and select **Validate**.
  6. Select **Create finding**.



CASB evaluates the custom finding type against assets as they are created or updated within the selected scope. Matching assets appear as posture finding instances under **Posture Findings**.

#### Learn more

  * Learn how to [create and manage custom finding types](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/custom-finding-types/) in Cloudflare One.
  * Learn how to [manage findings](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/manage-findings/) in Cloudflare One.
  * Learn how to [create and manage CASB remediation policies](https://developers.cloudflare.com/cloudflare-one/cloud-and-saas-findings/policies/) in Cloudflare One.



CASB custom finding types are now available in Cloudflare One.

Oct 5, 2026

## [BGP over IPsec and GRE tunnels generally available](https://developers.cloudflare.com/changelog/post/2026-10-05-bgp-over-tunnels-ga/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

BGP peering over IPsec and GRE tunnels is generally available for Cloudflare WAN and Magic Transit. You can use it for production workloads.

BGP peering exchanges routes dynamically between your devices and your Cloudflare virtual network routing table. You no longer need to update static routes manually as your network changes.

BGP over IPsec and GRE tunnels is available to all accounts that use [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing). No enablement is required. BGP over CNI remains in closed beta.

For configuration details, refer to:

  * [Configure BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
  * [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)



Oct 2, 2026

## [Introducing Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).

Oct 2, 2026

## [New strict service token authentication setting for Access](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).



Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

Oct 2, 2026

## [Run the Pi Durable harness on Cloudflare with the Agents SDK](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now provides first-class support for building agents using the Pi harness. You can build long-running agents using the combination of [Pi 1.0 ↗︎](https://earendil.com/posts/pi-1-0/), [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/), and the new `PiHarness` class that the Cloudflare Agents SDK provides, ensuring your agent's work is durably persisted, even if interrupted mid-turn.

Built with [Earendil ↗︎](https://earendil.com/), this integration is our first step toward first-class support for third-party agent harnesses on Cloudflare.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi)

Beta

`PiHarness` is in beta. [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) is a new, experimental package, and the `PiHarness` API will likely change as Pi Durable matures.

`PiHarness` is a new "Lifecycle capability" provided by the Cloudflare Agents SDK. Pi Durable provides the agent harness and the Lifecycle is responsible for keeping the agent running in the Durable Object. The Lifecycle is a core concept in the Agents SDK ensuring that long-running work can run in a Durable Object, surviving restarts, crashes, and network issues. We will share more on Lifecycle capabilities in the near future.

#### Install

npmyarnpnpmbun
    
    
    npm i agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    yarn add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    pnpm add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    bun add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai

Both Pi packages are optional peer dependencies of `agents`, so you only install them if you use the harness.

#### Use it in an Agent

Creating a Pi agent requires configuring the Pi `Harness` with a model, skills, and tools, then registering the `PiHarness` with the `Agent` class.
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent<Env> {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt: string) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }

The `agents/models/pi-ai` entry point supports AI Gateway and Workers AI models, so you can get started with Cloudflare models right away or use your existing Pi AI provider.

#### Add tools with extensions

Both tools and system prompt sections are provided to the Pi `Harness` via extensions.
    
    
    import { Type } from "@earendil-works/pi-ai";
    
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));
    
    
    import { Type } from "@earendil-works/pi-ai";
    import type { ToolRegistration } from "@earendil-works/pi-durable";
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount: ToolRegistration<typeof WordCount> = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));

For more information on creating and configuring extensions, refer to [Extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/).

#### Learn more

  * [Pi harness documentation](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Pi harness extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/)
  * [pi-ai model provider](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi), with WebSockets, a browser UI, and a `@cloudflare/computer` Workspace for the model's tools
  * [Lifecycle ↗︎](https://github.com/cloudflare/agents/blob/main/docs/agents/lifecycle.md)
  * [Pi Durable announcement ↗︎](https://earendil.com/posts/pi-durable/) from Earendil



Oct 2, 2026

## [30 days of analytics data on every plan](https://developers.cloudflare.com/changelog/post/2026-10-02-30-days-analytics-on-every-plan/)

[Analytics](https://developers.cloudflare.com/analytics/)

Every plan now gets at least 30 days of analytics data. Adaptive analytics datasets, such as HTTP requests, security events, and DNS analytics, retain at least 31 days of data for Free and Pro domains, and you can query up to 30 days in a single request. Previously, Free and Pro domains could see between 24 hours and 8 days of history depending on the dataset.

A full month of history lets you investigate an issue after it happens, compare today with the same day in previous weeks, and tell a one-time spike from a longer trend. The change applies in the Cloudflare dashboard, in [Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/), and through the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Domain analytics also now live in one place. In the Cloudflare dashboard, select a domain and go to **Analytics** to see Traffic, Performance, Security, Cache, Origin, DNS, and Visitors as tabs that share one time range and one set of filters. Account-level analytics are under **Observability** > **Analytics**.

This change does not alter which datasets or fields your plan can access. Aggregated datasets, such as `httpRequests1hGroups`, keep their existing per-plan limits. To check the exact retention and query window for a zone or account, query the [settings](https://developers.cloudflare.com/analytics/graphql-api/features/discovery/settings/) for each dataset.

For plan-specific limits, refer to [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/#availability), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/#availability), and [GraphQL Analytics API limits](https://developers.cloudflare.com/analytics/graphql-api/limits/#node-limits-and-availability).

Oct 2, 2026

## [Workers Observability logs and traces in Custom Dashboards](https://developers.cloudflare.com/changelog/post/2026-10-02-workers-observability-in-custom-dashboards/)

[Analytics](https://developers.cloudflare.com/analytics/)

You can now build Custom Dashboards charts from Workers Observability data. Two new datasets, **Workers Observability — Logs** and **Workers Observability — Traces (OTel)** , let you chart Worker invocations, log levels, errors, CPU and wall time, span counts, and durations next to HTTP traffic, security events, and other analytics datasets.

This gives you one dashboard for an application that spans Cloudflare's network and your Workers. For example, you can put request volume, WAF blocks, and Worker error rates on the same view, filter all three by time range, and spot whether a spike in errors lines up with a change in traffic.

The datasets are available for every Worker in your account that has [Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/) or [Workers Traces](https://developers.cloudflare.com/workers/observability/traces/) turned on. Custom Dashboards also now allow up to 100 dashboards for every account.

To get started, refer to [Workers Observability data in Custom Dashboards](https://developers.cloudflare.com/analytics/custom-dashboards/#workers-observability-data).

Oct 2, 2026

## [United States jurisdiction](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/)

[D1](https://developers.cloudflare.com/d1/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

← Prev

1[2](https://developers.cloudflare.com/changelog/2/)…[54](https://developers.cloudflare.com/changelog/54/)

[Next →](https://developers.cloudflare.com/changelog/2/)
