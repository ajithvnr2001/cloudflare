---
url: https://developers.cloudflare.com/changelog/product/web-analytics/
title: Cloudflare Web Analytics Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:02.573467+00:00
---

# Cloudflare Web Analytics Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/web-analytics/

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

Jul 14, 2026

## [Improved reliability for account-wide Web Analytics dashboards](https://developers.cloudflare.com/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.

For larger accounts (with >100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.

Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.

If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.

May 13, 2026

## [/cdn-cgi/rum endpoint now returns 405 for non-POST requests](https://developers.cloudflare.com/changelog/post/2026-05-13-rum-405-method-not-allowed/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

The `/cdn-cgi/rum` beacon endpoint now returns `405 Method Not Allowed` for non-POST requests instead of `404 Not Found`. The response includes an `Allow: POST, OPTIONS` header per [RFC 9110 §15.5.6 ↗︎](https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6).

Previously, sending a `GET` or other non-POST request to this endpoint returned a `404`, which was misleading because it suggested the endpoint did not exist. The new `405` response clearly indicates that the endpoint exists but only accepts `POST` requests.

The Web Analytics beacon (`beacon.min.js`) already uses `POST` for all metric submissions, so this change does not affect normal beacon operation. `OPTIONS` requests for CORS preflight continue to work as before.

For more information, refer to the [Web Analytics FAQ](https://developers.cloudflare.com/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum).

Apr 30, 2026

## [Web Analytics adds Navigation Type filtering and reporting](https://developers.cloudflare.com/changelog/post/2026-04-30-rum-navigation-types/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

Cloudflare Web Analytics now supports **Navigation Type** reporting and filtering.

This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.

Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of "Back-forward" navigations versus "Back-forward Cache", those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.

The same applies for regular "Navigate" entries — where "Navigate Cache", "Navigate Prefetch Cache" and "Prerender" would provide instant document retrieval — and "Reload", where "Reload cache" would be more optimal.

A high volume of "Reload" entries can also indicate a potential stability problem with your website.

By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.

For more information, refer to [Navigation Types](https://developers.cloudflare.com/web-analytics/data-metrics/dimensions/#navigation-types).

#### Key benefits

  * **Monitor Cache Effectiveness:** See how often your site is served from the HTTP cache or bfcache.
  * **Identify Performance Bottlenecks:** Filter by the different types to understand performance opportunity of improving browser cache hit ratio.



#### Analyze navigation types in the Cloudflare dashboard

You can now find the **Navigation Type** dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using "equals", "does not equal", "in", or "not in" matchers.

![Navigation Type filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2646,height=1040,format=webp/_astro/dash-web_analytics-navigation-type-filter.Cculflhp.png)

To check the list of popular navigation types, select **Page views** on the Web Analytics sidebar and scroll down to the bottom:

![Navigation Types list in Page Views tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2076,height=500,format=webp/_astro/dash-web_analytics-navigation-types-list.CWaiEQzO.png)

Feb 26, 2024

## [Easily Exclude EU Visitors from RUM](https://developers.cloudflare.com/changelog/post/2025-02-25-rum-exclude-eu/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.

![RUM Enablement UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1101,height=1061,format=webp/_astro/2025-02-26-rum-eu.X0ZtbXWA.png)

Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.

To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.

You can learn more about what metrics are reported by Web Analytics and how it is collected [in the Web Analytics documentation](https://developers.cloudflare.com/web-analytics/data-metrics/). You can enable Web Analytics on any hostname by going to the [Web Analytics ↗︎](https://dash.cloudflare.com/?to=/:account/web-analytics/sites) section of the dashboard, selecting "Manage Site" for the hostname you want to monitor, and choosing the appropriate enablement option.
