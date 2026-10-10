---
url: https://developers.cloudflare.com/changelog/product-group/analytics/
title: Analytics Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:26.440672+00:00
---

# Analytics Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/analytics/

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

Oct 7, 2026

## [Query Log Explorer datasets from Observability Logs](https://developers.cloudflare.com/changelog/post/2026-10-07-log-search-in-observability-logs/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer datasets are now queried from the [Logs](https://developers.cloudflare.com/observability/logs/) page under **Observability** in the Cloudflare dashboard. The Logs page brings Log Explorer and Workers Observability datasets together with a shared filter builder, SQL editor, and visualizations.

As part of this change, the **Log Explorer** menu is no longer shown in the dashboard navigation.

  * Your enabled datasets, saved queries, and SQL queries continue to work on the Logs page.
  * To manage datasets, open the dataset selector on the Logs page and select **Configure** next to the Log Explorer datasets.
  * The previous Log Search page remains available at its direct URL.



For more information, refer to [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) and the [Logs overview](https://developers.cloudflare.com/observability/logs/).

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

Sep 30, 2026

## [Logpush is now available on all plans with usage-based pricing](https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

  * **Internal exports** : 25 GB per month, then $0.03 per additional GB.
  * **External exports** : 25 GB per month, then $0.10 per additional GB.
  * **Transformations** : 1 GB per month, then $0.04 per additional GB.



R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 30, 2026

## [Transformers are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

Sep 18, 2026

## [Filter DDoS attack traffic from Logpush jobs](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/)

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:
    
    
    {
    	"filter_attack_traffic": true
    }

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).

Sep 8, 2026

## [Radar search now includes Internet events](https://developers.cloudflare.com/changelog/post/2026-09-08-radar-search-events/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.

![Radar search results showing Internet outage events associated with locations and autonomous systems](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2512,height=1130,format=webp/_astro/radar-search-events.DpZAk59G.png)

Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through [WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/).

Aug 28, 2026

## [Improved dataset configuration in Log Explorer](https://developers.cloudflare.com/changelog/post/2026-08-28-dataset-configuration/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.

  * **Grouped field selection** organizes fields by category and shows the number selected in each group.
  * **Field details** identify each field's data type and mark required or deprecated fields.
  * **Bulk controls** let you select all fields or reset the selection to the dataset defaults.
  * **Ingestion filters** let you ingest all events or only events that match your conditions.



These controls are available when you add a dataset or select **Actions** > **Edit** for an enabled dataset.

For more information, refer to [Configure fields and filters](https://developers.cloudflare.com/log-explorer/manage-datasets/#configure-fields-and-filters).

Aug 26, 2026

## [Delete Log Explorer datasets](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/)

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete** , and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.

Aug 26, 2026

## [Azure Functions-based Microsoft Sentinel connector deprecation](https://developers.cloudflare.com/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/)

[Logpush Connectors](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Enterprise customers using the [Azure Functions-based Microsoft Sentinel connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview) must migrate to the [Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector ↗︎](https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview) by 2026-09-14.

Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.

To migrate, follow the [Microsoft Sentinel integration setup guide](https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/).

#### Additional resources

  * [Download Cloudflare's CCF Sentinel Solution ↗︎](https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview)
  * [Microsoft Sentinel data lake overview ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)
  * [About the CCF platform ↗︎](https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector)



For more information, refer to Microsoft's [Azure Monitor HTTP Data Collector API deprecation notice ↗︎](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell).

Aug 26, 2026

## [Radar Researcher adds richer sources and URL Scanner explanations](https://developers.cloudflare.com/changelog/post/2026-08-26-radar-researcher-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) expands the [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) beta with richer sources and new ways to investigate Internet data.

#### Connected insights

Radar Researcher responses can now link to relevant Radar pages, reports, and Cloudflare Blog posts.

![Radar Researcher response linking to the IP Address Information and Network Quality Test pages](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=798,height=668,format=webp/_astro/radar-researcher-page-links.D74GzYoL.png)

#### URL Scanner report explanations

Select **Explain with AI** on a [URL Scanner report ↗︎](https://radar.cloudflare.com/scan) to have Radar Researcher explain its findings and answer follow-up questions about the scanned site.

![Radar Researcher explaining findings from an example.com URL Scanner report](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=696,height=1250,format=webp/_astro/radar-researcher-url-scanner-explanation.BBCehcJx.png)

#### Improved shared sessions

Shared conversations now open in fullscreen, while the share URL remains available until you close the panel or start a new conversation.

Open [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=) to explore these improvements.

Aug 24, 2026

## [RPKI ASPA path validation on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-08-24-radar-aspa-validation/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) adds an [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) to its [Routing section ↗︎](https://radar.cloudflare.com/routing). Enter a BGP `AS_PATH` and the tool checks it against the [Autonomous System Provider Authorization (ASPA) ↗︎](https://blog.cloudflare.com/aspa-secure-internet/) records currently published in the RPKI, returning a verdict of `Valid`, `Invalid`, or `Unknown`. An `Invalid` verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.

Validation follows [draft-ietf-sidrops-aspa-verification ↗︎](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/), so verdicts match those produced by validators implementing the same draft. The draft is still a work in progress and not yet an RFC.

#### Enter a path

Paths are read in BGP wire order: the rightmost AS is the origin, and the leftmost AS is the one closest to the collector or router that observed the route. AS numbers can be separated by spaces, commas, or hyphens, with or without an `AS` prefix. The full ASPA snapshot is loaded into the browser once, so the verdict, graph, and trace update as the path is edited, with no further requests. A set of example paths covers the interesting cases, including a route leak with an AS0 ASPA, where an AS declares that it has no providers at all.

#### Choose an algorithm

The draft defines two verification algorithms that differ only in whether a down-ramp is permitted:

  * **Upstream** ([section 5.4 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.4)) — for routes received from a customer, peer, route server client, or route server. Only an up-ramp is permitted.
  * **Downstream** ([section 5.5 ↗︎](https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.5)) — for routes received from a provider. Both an up-ramp and a down-ramp are permitted.



An **up-ramp** is the run of consecutive customer-to-provider hops from the origin to the apex of the path, and a **down-ramp** is the equivalent run from the announcing neighbor back to that apex. The tool evaluates both algorithms at once and labels each with its verdict, so a path that is legitimate when received from one session type and a leak when received from another is visible without switching modes. Selecting an algorithm drives the graph and the trace.

#### Read the result

The **ASPA validation graph** draws the path hop by hop, labeling each AS with its role, whether it publishes an ASPA, and how many providers that ASPA authorizes. Every hop is marked `Provider+`, `Not Provider+`, or `No attestation`, and the maximum and minimum bounds of each ramp are drawn against the length of the path. Hops that no ramp reaches are highlighted, because a path the ramps cannot cover end to end is `Invalid`. The accompanying **ASPA records** table lists every AS in the path with its ASPA status and its authorized providers, each linked to its Radar AS page.

![ASPA validation graph for the path 1003 6939 1299 553, showing a Valid verdict under the downstream algorithm, the Provider+, Not Provider+, and No attestation outcome on each hop, and the up-ramp and down-ramp bounds that together cover the path](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1222,format=webp/_astro/aspa-validation-graph.DQUq8KCm.png)

#### Follow the algorithm

The **Algorithm step by step** section shows the derivation rather than just the answer. Two columns run the same scans under different stopping rules: the upper bounds, which test for `Invalid` and stop only on `Not Provider+`, and the lower bounds, which test for `Unknown` and also stop on `No Attestation`. A hop is `Not Provider+` when the AS publishes an ASPA that does not list the next AS as a provider, and `No Attestation` when the AS publishes no ASPA at all. Each column lists the outcome for every hop scanned, marks where the scan stopped, gives the resulting ramp length, and then evaluates the verdict rule with the numbers filled in.

![Step-by-step trace for the same path, with the upper-bound and lower-bound columns each listing the up-ramp and down-ramp scans, the ramp lengths they produce, and the verdict rule that neither Invalid nor Unknown satisfies, leaving a Valid verdict](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1392,height=586,format=webp/_astro/aspa-validation-algorithm-trace.Bb8SM4wT.png)

#### Share a validation

The path and the selected algorithm are kept in the URL, so a link reproduces a result exactly — for example, this [route leak with an AS0 ASPA ↗︎](https://radar.cloudflare.com/routing/aspa-validation?path=22652-1299-9498-149765-14789). Appending `&mode=upstream` pins the link to the upstream algorithm. The graph is a standard Radar widget, so it can also be embedded or shared as an image.

The records behind the tool are the same ones served by the [`/bgp/rpki/aspa/snapshot`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/) endpoint of the [`ASPA`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/) API, and the number of records loaded and the snapshot timestamp are shown alongside the input.

Try the [ASPA validation tool ↗︎](https://radar.cloudflare.com/routing/aspa-validation) with a path of your own.

Aug 21, 2026

## [Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)](https://developers.cloudflare.com/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. **Update: this update is complete as of 2026-09-04.**

**This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.** The extent of these variances depend on your front-end architecture and visitor traffic patterns.

Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.

Any client-side navigation counts as a soft navigation, including navigations intercepted by [the Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API) or triggered by [the History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.

The main improvement comes from [Google Chrome's new Soft Navigation API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations). It natively measures [Largest Contentful Paint (LCP)](https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics) on soft navigations, removing a blind spot in perceived loading speed across pageviews.

We've extended our `navigationType` values to segment these different types of navigations:

`navigationType` | New? | Description  
---|---|---  
`navigate` | ❌ | Hard navigations that traditional websites (or "Multi Page Applications") perform when clicking links or submitting forms  
`soft-navigation` | ✅ | Where [the new Soft Navigation API ↗︎](https://developer.chrome.com/docs/web-platform/soft-navigations) is available and a visitor makes a client-side navigation, we record these events  
`routing-apis` | ✅ | Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using [the Navigation API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API) or [History API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/History_API). We cannot collect LCP for these, but the other Core Web Vitals are present.  
  
Prior to this change, we only used History API and all navigations were bucketed into `navigate`.

For more information, refer to the [Navigation Types](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/#navigation-types) and [Web Analytics SPA](https://developers.cloudflare.com/web-analytics/get-started/web-analytics-spa/) documentation pages.

Aug 20, 2026

## [New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-08-20-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **Account Abuse Protection Events** : A new dataset with fields including `AuthenticationIdentityProvider`, `AuthenticationMethod`, `AuthenticationStatus`, `BotScore`, `ClientASN`, `ClientCity`, `ClientCountry`, `ClientIP`, `Email`, `EphemeralID`, `EventSource`, `EventType`, `FraudEmailRisk`, `Host`, `JA4`, `RayID`, `Timestamp`, `UserAgent`, and `UserID`.
  * **Magic BGP Logs** : A new dataset with fields including `Direction`, `EventData`, `EventKind`, `EventTimestamp`, `TunnelID`, and `TunnelName`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `AISecurityCustomTopicCategories`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.
  * **Gateway HTTP** (added): `ExperimentalFeatures` and `PackageInfo`.
  * **HTTP requests** (added): `AISecurityCustomTopicCategories`, `ClientTLSKeyExchangeGroup`, `WAFRequestSignatureCategories`, and `WAFRequestSignatureRefs`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Aug 20, 2026

## [Per-zone post-quantum visibility in Logpush and Log Explorer](https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/)

[Logs](https://developers.cloudflare.com/logs/)[Log Explorer](https://developers.cloudflare.com/log-explorer/)

[Cloudflare Radar ↗︎](https://radar.cloudflare.com/post-quantum) publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the [`http_requests`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset — also queryable in [Log Explorer](https://developers.cloudflare.com/log-explorer/) — includes a new `ClientTLSKeyExchangeGroup` field.

The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as `X25519MLKEM768`, and classical connections appear as `X25519`, `P-256`, or another named group. A value of `UNK` means the group could not be determined, and `NONE` means either RSA key exchange was used or TLS was not used.

With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/).

Aug 14, 2026

## [WebSocket reporting now includes full connection data transfer and duration](https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/)

[Analytics](https://developers.cloudflare.com/analytics/)

Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial `101 Switching Protocols` handshake for some WebSocket connections.

Customers with WebSocket traffic will see the correct **Data Transfer** in the dashboard and `EdgeResponseBytes` in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.

The separate [WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/) continues to provide per-connection directional byte counts, timestamps, and close details.

For more information about HTTP Traffic Analytics, refer to [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/#http-traffic).

Aug 7, 2026

## [AS-level connectivity and upstream providers on Cloudflare Radar](https://developers.cloudflare.com/changelog/post/2026-08-07-radar-as-connectivity-upstreams/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) expands its [Routing section ↗︎](https://radar.cloudflare.com/routing) with two widgets on AS pages, such as [AS13335 ↗︎](https://radar.cloudflare.com/routing/as13335), that describe how a network reaches the rest of the Internet: the paths it takes toward the [Tier-1 ↗︎](https://en.wikipedia.org/wiki/Tier_1_network) networks, and the mix of direct upstreams carrying its routes. Both are derived from [RouteViews ↗︎](https://www.routeviews.org/) RIB snapshots, unioned across selected collectors.

#### AS-level connectivity

The **AS-level connectivity** graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors. It reads from left to right, starting at the queried AS and ending at the Tier-1 networks, and each node is labeled with its AS number, country, and organization name. Tier-1 nodes are marked so they stand apart from the intermediate networks that lead to them.

By default, the graph shows the network's direct connections to Tier-1 networks plus the indirect paths, which keeps the view readable. A **Show full paths** toggle expands it to every observed path, including transit through Tier-1 networks the AS already connects to. An IP version selector switches between IPv4 and IPv6, because the paths reaching Tier-1 networks may differ between the two address families.

![AS-level connectivity graph for AS13335, showing Tier-1 networks it reaches directly alongside paths that reach others through intermediate networks](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=1526,format=webp/_astro/as-level-connectivity-graph.DGv8lrUx.png)

This is the AS-level counterpart to the **Real-time connectivity** graph on prefix pages, such as the one for [1.1.1.0/24 ↗︎](https://radar.cloudflare.com/routing/prefix/1.1.1.0/24). Instead of covering a single prefix, it covers the union of paths for all prefixes an AS announces, which makes it a fast way to read a network's transit hierarchy: which providers it depends on, how many hops separate it from the core, and whether its paths to the core are diverse or concentrated. For more information on the prefix-level graph, refer to [BGP real-time routes](https://developers.cloudflare.com/radar/glossary/#bgp-real-time-routes).

#### Upstream providers

The **Upstream providers** widget tracks the share of an AS's observed paths carried by each of its direct upstream networks over time, drawn as a stacked area chart. Up to 10 upstreams appear as their own series and the remaining ones are grouped into **Other**. Transit changes such as adding a provider, dropping one, or moving traffic between them appear as movement between bands rather than as a single aggregate number. As with the connectivity graph, an IP version selector switches between IPv4 and IPv6.

![Stacked area chart of the share of AS13335's observed paths carried by each of its top 10 direct upstreams, with the remainder grouped into Other](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=976,format=webp/_astro/as-upstream-providers-timeseries.BUc6CJaT.png)

#### API endpoints

The data behind both widgets is also available through two new endpoints on the [`BGP`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/) API:

  * [`/bgp/routes/paths/{asn}`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/) — Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors, alongside the name and country of every ASN in the response. Pass `collector` to scope the result to a single RouteViews collector.
  * [`/bgp/routes/upstreams/{asn}/timeseries`](https://developers.cloudflare.com/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/) — Returns the share of an AS's observed paths carried by each direct upstream over time. Use `limit` to control how many upstreams come back as separate series before the rest are grouped into an `OTHER` series, and `ipVersion` to select the address family.



Visit the [AS13335 routing page ↗︎](https://radar.cloudflare.com/routing/as13335) to explore both widgets, or swap in any other AS number.

Aug 7, 2026

## [Radar Researcher beta and WebMCP support now available](https://developers.cloudflare.com/changelog/post/2026-08-07-radar-researcher-and-webmcp/)

[Radar](https://developers.cloudflare.com/radar/)

[**Cloudflare Radar**](https://developers.cloudflare.com/radar/) now includes [Radar Researcher ↗︎](https://radar.cloudflare.com/?prompt=), a beta AI-powered assistant for exploring Internet trends and traffic data in plain language. Open Researcher from the header on any Radar page to ask questions by voice or text, receive explanations, and view interactive charts based on Radar API data.

![Screenshot of the Radar Researcher panel alongside the Radar overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1430,height=780,format=webp/_astro/radar-researcher-panel.B7QqJlGo.webp)

To ask about a specific chart, select **Explain with AI** to start a conversation with its underlying data and context.

![Screenshot of the Explain with AI option in a Radar chart menu](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=434,height=302,format=webp/_astro/radar-explain-with-ai.Dgw4ghVh.webp)

You can explore further with suggested follow-up questions, find earlier conversations through searchable history, and share conversations through shareable links.

Alongside the user-facing Researcher experience, Radar now supports [WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/), allowing browser-based AI agents to navigate Radar, search data, and use tools such as URL scanning and domain lookup.

To get started, visit [Cloudflare Radar ↗︎](https://radar.cloudflare.com/).

Jul 14, 2026

## [Improved reliability for account-wide Web Analytics dashboards](https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.

For larger accounts (with >100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.

Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.

If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.

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

Jul 7, 2026

## [New WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/)

[Logs](https://developers.cloudflare.com/logs/)

Enterprise customers can now push per-connection WebSocket analytics to any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) using the new `websocket_analytics` dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.

Key fields include:

  * **`ConnectionCloseReason`** — why the connection ended: `peerReset`, `peerNoError`, `timedOut`, `upstreamReset`, `protocolViolation`, `unspecifiedError`, or `none`.
  * **`ConnectionCloseSource`** — which side initiated the close: `upstream`, `downstream`, `me`, or `both`.
  * **`ConnectionTransportCloseCode`** — the TLS alert code or TCP-level close code for additional precision.
  * **`RayID`** — correlate WebSocket connection events with your existing HTTP Request logs.



The dataset also includes directional byte counts (`BytesSentClient`, `BytesReceivedClient`, `BytesSentOrigin`, `BytesReceivedOrigin`), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.

This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (`ConnectionCloseReason == "peerReset"`) grouped by host and data center — directly in your existing log analysis tools.

For the full list of available fields, refer to [WebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/).

Jul 2, 2026

## [Updated fields across multiple Logpush datasets in Cloudflare Logs](https://developers.cloudflare.com/changelog/post/2026-07-02-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### Updated fields in existing datasets

  * **Gateway DNS** (added): `AppliedMaxTTL` and `UpstreamRecordTTLs`.
  * **Gateway HTTP** (added): `Warnings`.
  * **HTTP requests** (added): `CacheLockWaitedMs`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Jun 30, 2026

## [Account-scoped firewall events dataset in Logpush](https://developers.cloudflare.com/changelog/post/2026-06-30-account-level-firewall-events/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare Logpush now supports [firewall events as an account-scoped dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/). Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.

The dataset includes a new [`ZoneName`](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename) field so you can identify which zone each event came from when consuming logs in your downstream pipeline.

#### What's available

  * A new account-scoped `firewall_events` dataset, configurable via the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/) or the Cloudflare dashboard.
  * The same fields and filter expressions supported by the existing [zone-scoped firewall events dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/), plus the new `ZoneName` field.
  * Support for all existing Logpush destinations.



Jun 24, 2026

## [New WebSocket Analytics Logpush dataset and updated fields](https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/)

[Logs](https://developers.cloudflare.com/logs/)

Cloudflare has updated [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/):

#### New datasets

  * **WebSocket Analytics** : A new dataset with fields including `BytesReceivedClient`, `BytesReceivedOrigin`, `BytesSentClient`, `BytesSentOrigin`, `ClientASN`, `ClientIP`, `ClientRequestHost`, `ClientRequestPath`, `ClientRequestUserAgent`, `ColoCode`, `ConnectionCloseReason`, `ConnectionCloseSource`, `ConnectionID`, `ConnectionTransportCloseCode`, `EdgeEndTimestamp`, `EdgeStartTimestamp`, and `RayID`.



#### Updated fields in existing datasets

  * **Firewall events** (added): `ZoneName`. The Firewall events dataset is now also available for [account-scope Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/firewall_events/), in addition to the existing zone scope.
  * **Email Security Alerts** (added): `BCC`, `DKIMResult`, `DMARCPolicy`, `DMARCResult`, and `SPFResult`.



For the complete field definitions for each dataset, refer to [Logpush datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).

Jun 24, 2026

## [Precise IP location and richer AS details on the Cloudflare Radar IP page](https://developers.cloudflare.com/changelog/post/2026-06-24-radar-ip-page-improvements/)

[Radar](https://developers.cloudflare.com/radar/)

[**Radar**](https://developers.cloudflare.com/radar/) now plots your IPv4 and IPv6 locations on the [IP page ↗︎](https://radar.cloudflare.com/ip), shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.

#### Your IP location on the map

The map of your connection now shows:

  * **IP location markers** — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.
  * **Cloudflare data center markers** — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.
  * **Data center connectors** — Each line connects your IP markers to their respective data centers.

![Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3136,height=1305,format=webp/_astro/ip-page-geolocation.BJ53oUtj.png)

Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.

#### Extended AS information

The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.

Visit the [Cloudflare Radar IP page ↗︎](https://radar.cloudflare.com/ip) to explore more details about your IP.

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/analytics/2/)…[6](https://developers.cloudflare.com/changelog/product-group/analytics/6/)

[Next →](https://developers.cloudflare.com/changelog/product-group/analytics/2/)
