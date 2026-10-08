---
url: https://developers.cloudflare.com/changelog/product/dex/
title: Digital Experience Monitoring Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:44.376949+00:00
---

# Digital Experience Monitoring Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/dex/

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

Jul 9, 2026

## [Wi-Fi signal and network performance analytics for Cloudflare One Client devices](https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment.

The **Device Monitoring** page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.

![Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1652,height=664,format=webp/_astro/dex-device-monitoring-summary.CBxeSd6b.png)

A summary at the top of the page shows the health of each category at a glance, using **Good** , **Fair** , and **Poor** labels:

  * **Connection** — connection status, Cloudflare One Client mode, and tunnel type over time
  * **Wi-Fi signal strength** — signal measured in dBm over time, with thresholds that flag a weak signal
  * **Traffic performance** — upstream and downstream performance, including network throughput on the active interface
  * **Device health** — hardware metrics such as CPU, memory, and disk

![Wi-Fi signal strength and network throughput charts on the Device Monitoring page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1666,height=732,format=webp/_astro/dex-device-monitoring-wifi-network.CoEBznAm.png)

You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.

These analytics are available to all Cloudflare One customers at no additional cost.

To learn more, refer to the [DEX monitoring documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/).

Apr 29, 2026

## [Digital experience tests to authenticated resources and enhanced configuration](https://developers.cloudflare.com/changelog/post/2026-04-29-dex-tests-to-auth/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital experience tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via [Cloudflare Secret Store](https://developers.cloudflare.com/secrets-store/).

Digital experience tests also have enhanced configuration options including:

  * New HTTP methods (DELETE, PATCH, POST, PUT)
  * Secret Store headers, custom plain text headers, and custom request bodies
  * Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates

![Digital experience test configuration for Cloudflare Access applications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1374,format=webp/_astro/dex_test_auth_config.CD3G3zb_.png)![Digital experience enhanced test configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2840,height=1496,format=webp/_astro/dex_test_enhanced_config.Nsv7Vcob.png)

Apr 28, 2026

## [Internet outage notifications for devices](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-internet-outage-notification/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/) will display a dashboard notification when an Internet outage or traffic anomaly may impact a [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) device based on its geographic location or network connection.

This Internet outage and traffic anomaly data is pulled from [Cloudflare Radar ↗︎](https://radar.cloudflare.com/). All Internet outage and traffic anomaly observations can be viewed in the [Radar Outage Center ↗︎](https://radar.cloudflare.com/outage-center).

![Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=314,format=webp/_astro/dex_radar_ux_notification.CpdrUVYA.png)![Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2068,height=909,format=webp/_astro/dex_radar_analytics.GaPxWM6C.png)

Apr 28, 2026

## [Cloudflare One Client speed tests](https://developers.cloudflare.com/changelog/post/2026-04-28-dex-speed-test/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

IT teams can now remotely run speed tests from the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) to Cloudflare's network edge.

Each speed test includes the following metrics:

  * Internet speed: download and upload throughput
  * Latency: download, upload, unloaded latency, and jitter
  * Network quality score: video streaming, webchat/real-time communication (RTC)



In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Digital experience** > **Diagnostics** and select **Run diagnostics** to use the feature today.

![Cloudflare One client speed test result](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2906,height=1730,format=webp/_astro/dex_speed_test.DukupcRs.png)

Apr 15, 2026

## [Last seen timestamp for Cloudflare One Client devices is more consistent](https://developers.cloudflare.com/changelog/post/2026-04-15-dex-consistent-last-seen-timestamps/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

The last seen timestamp for [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.

Feb 19, 2026

## [DEX Supports EU Customer Metadata Boundary](https://developers.cloudflare.com/changelog/post/2026-02-19-dex-supports-cmb-eu/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into [WARP](https://developers.cloudflare.com/warp-client/) device connectivity and performance to any internal or external application.

Now, all DEX logs are fully compatible with Cloudflare's [Customer Metadata Boundary](https://developers.cloudflare.com/data-localization/metadata-boundary/) (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.

If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via [LogPush](https://developers.cloudflare.com/logs/logpush/), and build their own analytics and dashboards.

If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: "DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets."

![Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2143,height=1221,format=webp/_astro/dex_supports_cmb.6YOLXjHN.png)

Nov 12, 2025

## [DEX Logpush jobs](https://developers.cloudflare.com/changelog/post/2025-11-12-dex-logpush-jobs/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.

We've released four new WARP and DEX device data sets that can be exported via [Cloudflare Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.

  1. [DEX Application Tests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/)
  2. [DEX Device State Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_device_state_events/)
  3. [WARP Config Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_config_changes/)
  4. [WARP Toggle Changes](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/)



To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard > Analytics & Logs > Logpush to get started.

![DEX logpush job creation dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2549,height=1283,format=webp/_astro/dex_logpush_datasets.CtCk36pX.png)

Aug 29, 2025

## [DEX MCP Server](https://developers.cloudflare.com/changelog/post/2025-08-29-dex-mcp-server/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device connectivity and performance across your Cloudflare SASE deployment.

We've released an MCP server [(Model Context Protocol) ↗︎](https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) for DEX.

The DEX MCP server is an AI tool that allows customers to ask a question like, "Show me the connectivity and performance metrics for the device used by carly‌@acme.com", and receive an answer that contains data from the DEX API.

Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.

Customers can test the new DEX MCP server in less than one minute. To learn more, read the [DEX MCP server documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/dex-mcp-server/).

Mar 7, 2025

## [Cloudflare One Agent now supports Endpoint Monitoring](https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/)

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.

Device health metrics are now automatically collected, allowing administrators to:

  * View the last network a user was connected to
  * Monitor CPU and RAM utilization on devices
  * Identify resource-intensive processes running on endpoints

![Device endpoint monitoring dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1226,height=675,format=webp/_astro/cloudflare-one-agent-health-monitoring.XXtiRuOp.gif)

This feature complements existing DEX features like [synthetic application monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) and [network path visualization](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/), creating a comprehensive troubleshooting workflow that connects application performance with device state.

For more details refer to our [DEX](https://developers.cloudflare.com/cloudflare-one/insights/dex/) documentation.

Jun 16, 2024

## [Explore product updates for Cloudflare One](https://developers.cloudflare.com/changelog/post/2024-06-16-cloudflare-one/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/)[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/)[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)[Network Flow](https://developers.cloudflare.com/network-flow/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Network Interconnect](https://developers.cloudflare.com/network-interconnect/)[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Welcome to your new home for product updates on [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

Our [new changelog](https://developers.cloudflare.com/changelog/) lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.

If you are looking for older product updates, refer to the following locations.

Older product updates

  * [Access](https://developers.cloudflare.com/cloudflare-one/changelog/access/)
  * [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/changelog/browser-isolation/)
  * [CASB](https://developers.cloudflare.com/cloudflare-one/changelog/casb/)
  * [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/changelog/tunnel/)
  * [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/changelog/dlp/)
  * [Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/changelog/dex/)
  * [Email security](https://developers.cloudflare.com/cloudflare-one/changelog/email-security/)
  * [Gateway](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/)
  * [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/changelog/)
  * [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/changelog/)
  * [Magic Network Monitoring](https://developers.cloudflare.com/network-flow/changelog/)
  * [Magic Transit](https://developers.cloudflare.com/magic-transit/changelog/)
  * [Magic WAN](https://developers.cloudflare.com/cloudflare-wan/changelog/)
  * [Network Interconnect](https://developers.cloudflare.com/network-interconnect/changelog/)
  * [Risk score](https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/)
  * [Cloudflare One Client](https://developers.cloudflare.com/changelog/cloudflare-one-client/)


