---
url: https://developers.cloudflare.com/changelog/product/analytics/
title: Analytics Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.888343+00:00
---

# Analytics Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/analytics/

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

Aug 14, 2026

## [WebSocket reporting now includes full connection data transfer and duration](https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/)

[Analytics](https://developers.cloudflare.com/analytics/)

Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial `101 Switching Protocols` handshake for some WebSocket connections.

Customers with WebSocket traffic will see the correct **Data Transfer** in the dashboard and `EdgeResponseBytes` in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.

The separate [WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/) continues to provide per-connection directional byte counts, timestamps, and close details.

For more information about HTTP Traffic Analytics, refer to [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/#http-traffic).

Apr 22, 2026

## [Custom dashboards available to all customers](https://developers.cloudflare.com/changelog/post/2026-04-22-custom-dashboards-ga/)

[Analytics](https://developers.cloudflare.com/analytics/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.

This update significantly expands the data available for visualization. Build charts based on any of the **100+ datasets** available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.

#### Log Explorer integration

Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.

#### Key benefits

  * **Unified visibility** : Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.
  * **Flexible monitoring** : Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.
  * **Expanded limits** : Log Explorer customers can create up to **100 dashboards** (up from 25 for standard customers).

![Custom Dashboards home page showing dashboard list and chart previews](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1079,height=793,format=webp/_astro/customdashboardshome.BIpSvImM.jpg)

To get started, refer to the [Custom Dashboards documentation](https://developers.cloudflare.com/analytics/custom-dashboards/).

Feb 18, 2026

## [New cfWorker metric in Server-Timing header](https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/)

[Analytics](https://developers.cloudflare.com/analytics/)

The Server-Timing header now includes a new `cfWorker` metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.

Previously, Worker execution time was included in the `edge` metric, making it harder to identify true edge performance. The new `cfWorker` metric provides this visibility:

Metric | Description  
---|---  
`edge` | Total time spent on the Cloudflare edge, including Worker execution  
`origin` | Time spent fetching from the origin server  
`cfWorker` | Time spent in Worker execution, including subrequests but excluding origin fetch time  
  
#### Example response
    
    
    Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7

In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.

#### Availability

The `cfWorker` metric is enabled by default if you have [Real User Monitoring (RUM)](https://developers.cloudflare.com/web-analytics/) enabled. Otherwise, you can enable it using [Rules](https://developers.cloudflare.com/rules/).

This metric is particularly useful for:

  * **Performance debugging** : Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.
  * **Optimization targeting** : Identify which component of your request path needs optimization.
  * **Real User Monitoring (RUM)** : Access detailed timing breakdowns directly from response headers for client-side analytics.



For more information about Server-Timing headers, refer to the [W3C Server Timing specification ↗︎](https://www.w3.org/TR/server-timing/).

Dec 18, 2025

## [Improved accuracy of cached request classification in analytics](https://developers.cloudflare.com/changelog/post/2025-12-18-cached-request-classification/)

[Analytics](https://developers.cloudflare.com/analytics/)

The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.

Previously, requests were classified as "cached" based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.

The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in [HTTP Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/), so only requests genuinely served from cache are counted as cached.

**What changed:**

  * **Zone Overview** — Cache ratios now reflect actual cache performance.
  * **HTTP Analytics** — No change. HTTP Analytics already used the correct classification logic.
  * **Historical data** — This fix applies to new requests only. Previously logged data is not retroactively updated.



Oct 1, 2025

## [New Confidence Intervals in GraphQL Analytics API](https://developers.cloudflare.com/changelog/post/2025-10-01-confidence-intervals/)

[Analytics](https://developers.cloudflare.com/analytics/)

The GraphQL Analytics API now supports confidence intervals for `sum` and `count` fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.

  * **Supported datasets** : Adaptive (sampled) datasets only.
  * **Supported fields** : All `sum` and `count` fields.
  * **Usage** : The confidence `level` must be provided as a decimal between 0 and 1 (e.g. `0.90`, `0.95`, `0.99`).
  * **Default** : If no confidence level is specified, no intervals are returned.



For examples and more details, see the [GraphQL Analytics API documentation](https://developers.cloudflare.com/analytics/graphql-api/features/confidence-intervals/).

May 23, 2025

## [New GraphQL Analytics API Explorer and MCP Server](https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/)

[Analytics](https://developers.cloudflare.com/analytics/)

We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:

#### GraphQL API Explorer

The new [GraphQL API Explorer ↗︎](https://graphql.cloudflare.com/explorer) helps you build, test, and run queries directly in your browser. Features include:

  * In-browser schema documentation to browse available datasets and fields
  * Interactive query editor with autocomplete and inline documentation
  * A "Run in GraphQL API Explorer" button to execute example queries from our docs
  * Seamless OAuth authentication — no manual setup required

![GraphQL API Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2626,height=974,format=webp/_astro/graphql-api-explorer.CPUNZZ5B.png)

#### GraphQL Model Context Protocol (MCP) Server

MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our [blog post ↗︎](https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/) for details on how they work and which servers are available. The new [GraphQL MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql) helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:

  * Explore what data is available to query
  * Generate and refine queries using natural language, with one-click links to run them in the API Explorer
  * Build dashboards and visualizations from structured query outputs



Example prompts include:

  * “Show me HTTP traffic for the last 7 days for example.com”
  * “What GraphQL node returns firewall events?”
  * “Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”



We’re continuing to expand these tools, and your feedback helps shape what’s next. [Explore the documentation](https://developers.cloudflare.com/analytics/graphql-api/) to learn more and get started.
