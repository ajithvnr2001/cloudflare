---
url: https://developers.cloudflare.com/changelog/product/load-balancing/
title: Load Balancing Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:07.066075+00:00
---

# Load Balancing Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/load-balancing/

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

Aug 31, 2026

## [Load Balancing now supports pool sets](https://developers.cloudflare.com/changelog/post/2026-08-31-pool-sets/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.

Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.

For example, this pool set uses Dynamic Latency steering for traffic from Germany:
    
    
    {
    	"pool_sets": [
    		{
    			"name": "germany-lowest-latency",
    			"match": { "topology": { "countries": ["DE"] } },
    			"overrides": {
    				"pools": [
    					"0930eec54a4c7ae6616985b79f678210",
    					"c8b4f5a6d7e84910a2b3c4d5e6f70819"
    				],
    				"steering_policy": "dynamic_latency"
    			}
    		}
    	]
    }

Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.

For configuration details and more examples, refer to [Pool sets](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/pool-sets/).

Aug 17, 2026

## [Load balancing analytics now filters by pool name](https://developers.cloudflare.com/changelog/post/2026-08-17-pool-name-analytics-filter/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.

Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.

The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:

  * **Requests over time** , filtering the chart series to the selected pool.
  * **Pool distribution** , showing only the selected pool segment.
  * **Top endpoints** , displaying cards for origins in the selected pool.
  * **Latency** , showing latency data for the selected pool.



The **Logs** view and health event filtering are unchanged.

To use this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same pool filter appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

For more information about analytics filters and metrics, refer to [Load Balancing Analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/).

Aug 7, 2026

## [Load Balancing health notifications now resolve automatically](https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/) health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.

As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.

This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by [Health Checks](https://developers.cloudflare.com/health-checks/) notifications.

Two things to keep in mind:

  * A recovery notification is matched to the earlier unhealthy notification for the **same pool or endpoint**. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.
  * If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.



Refer to [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/) to learn more about routing Load Balancing health notifications to an incident management tool.

Aug 3, 2026

## [See fallback pool traffic separately in load balancing analytics](https://developers.cloudflare.com/changelog/post/2026-08-03-fallback-pool-analytics/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Load balancing analytics now shows traffic served by your [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) separately from traffic routed to the same pool by normal steering.

Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.

Fallback traffic is now labeled with the pool name followed by `(Fallback)`. A pool named `eu-west`, for example, is shown as `eu-west (Fallback)`. This label appears as its own entry in:

  * **Requests over time** , as a separate series in the chart.
  * **Pool distribution** , as a separate segment.
  * **Top endpoints** , as a separate card for the pool.



The **Latency** view and the health event **Logs** are unchanged.

To see this, go to **Traffic** > **Load Balancing Analytics** for a zone. The same breakdown appears in the analytics view for an individual load balancer under **Load Balancing** at the account level.

Refer to [load balancing analytics](https://developers.cloudflare.com/load-balancing/reference/load-balancing-analytics/) to learn more.

Oct 16, 2025

## [Monitor Groups for Advanced Health Checking With Load Balancing](https://developers.cloudflare.com/changelog/post/2025-08-15-monitor-groups-for-load-balancing/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.

With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.

#### What you can do:

  * **Combine Multiple Monitors** : Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific `/login` service.
  * **Isolate Monitors for Observation** : Mark a monitor as "monitoring only" to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.
  * **Improve Steering Intelligence** : Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.



This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.

For detailed information and API configuration guides, please visit our [developer documentation](https://developers.cloudflare.com/load-balancing/monitors/monitor-groups) for Monitor Groups.

Aug 15, 2025

## [Steer Traffic by AS Number in Load Balancing Custom Rules](https://developers.cloudflare.com/changelog/post/2025-08-15-asnum-support-in-custom-rules/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.

This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.

![Create a Load Balancing Custom Rule using AS Num](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2554,height=1472,format=webp/_astro/asnum-custom-rule.CtcHu_zj.png)

To get started, create a [Custom Rule ↗︎](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) in your Load Balancer and select **AS Num** from the **Field** dropdown.

Aug 6, 2025

## [Improvements to Monitoring Using Zone Settings](https://developers.cloudflare.com/changelog/post/2025-08-06-zone-monitoring-improvements/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.

All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.

#### What you can expect:

  * More reliable application of zone settings to monitoring requests, including 
    * Authenticated Origin Pulls
    * Aegis Egress IP Pools
    * Argo Smart Routing
    * HTTP/2 to Origin
  * Improved support and bug fixes for retries, redirects, and proxied origin resolution
  * Improved performance and reliability of monitoring requests within the Cloudflare network
  * Unrelated CDN or WAF configuration changes should have no risk of impact to pool health



Jun 4, 2025

## [New Account-Level Load Balancing UI and Private Load Balancers](https://developers.cloudflare.com/changelog/post/2025-06-04-account-load-balancing-ui/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

We've made two large changes to load balancing:

  * Redesigned the user interface, now centralized at the **account level**.
  * Introduced [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.



This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.

![Load Balancing UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=822,format=webp/_astro/account-load-balancing-ui.CoCi7gPb.png)

**Key Enhancements:**

  * **Account-Level UI Consolidation:**

    * **Unified Management:** Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.

    * **Improved Efficiency:** This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.

  * **Private Network Load Balancing:**

    * **Secure Internal Application Access:** Create [**Private Load Balancers**](https://developers.cloudflare.com/load-balancing/private-network/) to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.

    * **WARP & Magic WAN Integration:** Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.

    * **Enhanced Security for Internal Resources:** Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.


![Private Load Balancers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=744,format=webp/_astro/private-load-balancer.yti20m_p.png)

May 6, 2025

## [UDP and ICMP Monitor Support for Private Load Balancing Endpoints](https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Cloudflare Load Balancing now supports **UDP (Layer 4)** and **ICMP (Layer 3)** health monitors for **private endpoints**. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.

#### What you can do:

  * Set up **ICMP ping monitors** to check if your private endpoints are reachable.
  * Use **UDP monitors** for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.
  * Gain better visibility and uptime guarantees for services running behind **Private Network Load Balancing** , without requiring public IP addresses.



This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with [**Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [**WARP**](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), and [**Magic WAN**](https://developers.cloudflare.com/cloudflare-wan/) to create a secure and observable private network.

Learn more about [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) or view the full list of [supported health monitor protocols](https://developers.cloudflare.com/load-balancing/monitors/#supported-protocols).
