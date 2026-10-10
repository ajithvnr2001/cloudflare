---
url: https://developers.cloudflare.com/changelog/product/kv/
title: KV Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:06.882550+00:00
---

# KV Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/kv/

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

## [Workers KV namespace jurisdictions are now generally available](https://developers.cloudflare.com/changelog/post/2026-10-02-kv-jurisdictions-ga/)

[KV](https://developers.cloudflare.com/kv/)

Jurisdictions for [Workers KV](https://developers.cloudflare.com/kv/) namespaces are now generally available. When you create a namespace, you can set a [jurisdiction](https://developers.cloudflare.com/kv/reference/data-location/) to make sure the namespace's data is only durably stored within that region. Jurisdictions can help you comply with data localization regulations such as GDPR or FedRAMP. Supported jurisdictions are `eu`, `us`, and `fedramp`.

A jurisdiction can only be set when a namespace is created, using the Cloudflare dashboard, Wrangler, the `cf` CLI, or the REST API, and cannot be added or changed afterwards.
    
    
    npx wrangler@latest kv namespace create <NAMESPACE_NAME> --jurisdiction=eu
    
    
    cf kv namespaces create --title <NAMESPACE_NAME> --jurisdiction eu
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/storage/kv/namespaces" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "title": "<NAMESPACE_NAME>",
        "jurisdiction": "eu"
      }'

Workers can still access a namespace restricted to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction on Cloudflare's network. The jurisdiction only controls where the namespace's data is durably stored.

To learn more, refer to [Data location](https://developers.cloudflare.com/kv/reference/data-location/).

Jul 15, 2026

## [Deprecate legacy Workers KV namespace API routes](https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/)

[KV](https://developers.cloudflare.com/kv/)

The legacy Workers KV API routes under `/accounts/{account_id}/workers/namespaces/*` are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented [Workers KV API](https://developers.cloudflare.com/api/resources/kv/) routes under `/accounts/{account_id}/storage/kv/namespaces/*` before that date.

The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from `/workers/namespaces/` to `/storage/kv/namespaces/`.

#### What you need to do

Update any integration that calls a route under `/accounts/{account_id}/workers/namespaces/` to use the equivalent route under `/accounts/{account_id}/storage/kv/namespaces/`. The migration is a direct URL path substitution — request parameters and response payloads are identical:

  * `GET` and `POST /accounts/{account_id}/workers/namespaces` → `GET` and `POST /accounts/{account_id}/storage/kv/namespaces`
  * `GET`, `PUT`, and `DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}` → `GET`, `PUT`, and `DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}`
  * `GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys` → `GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys`
  * `GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}` → `GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}`
  * `GET`, `PUT`, and `DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}` → `GET`, `PUT`, and `DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`



For more information about the deprecation timeline, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

Jan 30, 2026

## [Reduced minimum cache TTL for Workers KV to 30 seconds](https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/)

[KV](https://developers.cloudflare.com/kv/)

The minimum `cacheTtl` parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both `get()` and `getWithMetadata()` methods.

This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.

The `cacheTtl` parameter defines how long a KV result is cached at the global network location it is accessed from:
    
    
    // Read with custom cache TTL
    const value = await env.NAMESPACE.get("my-key", {
    	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)
    });
    
    // getWithMetadata also supports the reduced cache TTL
    const valueWithMetadata = await env.NAMESPACE.getWithMetadata("my-key", {
    	cacheTtl: 30, // Cache for minimum 30 seconds
    });

The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds `cacheTtl`.

This change affects all KV read operations using the binding API. For more information, consult the [Workers KV cache TTL documentation](https://developers.cloudflare.com/kv/api/read-key-value-pairs/#cachettl-parameter).

Jan 20, 2026

## [New Workers KV Dashboard UI](https://developers.cloudflare.com/changelog/post/2026-01-20-kv-dash-ui-homepage/)

[KV](https://developers.cloudflare.com/kv/)

[Workers KV](https://developers.cloudflare.com/kv/) has an updated dashboard UI with new dashboard styling that makes it easier to navigate and see analytics and settings for a KV namespace.

The new dashboard features a **streamlined homepage** for easy access to your namespaces and key operations, with consistent design with the rest of the dashboard UI updates. It also provides an **improved analytics view**.

![New KV Dashboard Homepage](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3444,height=1968,format=webp/_astro/kv-dash-ui-homepage.BT5hNntj.png)

The updated dashboard is now available for all Workers KV users. Log in to the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/) to start exploring the new interface.

Aug 22, 2025

## [Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance](https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/)

[KV](https://developers.cloudflare.com/kv/)

Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.

![Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1486,height=796,format=webp/_astro/kv-hybrid-providers-performance-improvements.D6MBO22S.png)

#### Performance improvements

The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:

  * **p95 latency** : Reduced from ~150ms to ~50ms (67% decrease)
  * **p99 latency** : Reduced from ~350ms to ~250ms (29% decrease)



Apr 17, 2025

## [Read multiple keys from Workers KV with bulk reads](https://developers.cloudflare.com/changelog/post/2025-04-10-kv-bulk-reads/)

[KV](https://developers.cloudflare.com/kv/)

You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.

This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by [Workers simultaneous connection limits](https://developers.cloudflare.com/workers/platform/limits/#simultaneous-open-connections).
    
    
    // Read single key
    const key = "key-a";
    const value = await env.NAMESPACE.get(key);
    
    // Read multiple keys
    const keys = ["key-a", "key-b", "key-c", ...] // up to 100 keys
    const values : Map<string, string?> = await env.NAMESPACE.get(keys);
    
    // Print the value of "key-a" to the console.
    console.log(`The first key is ${values.get("key-a")}.`)

Consult the [Workers KV Read key-value pairs API](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) for full details on Workers KV's new bulk reads support.

Jan 28, 2025

## [Workers KV namespace limits increased to 1000](https://developers.cloudflare.com/changelog/post/2025-01-27-kv-increased-namespaces-limits/)

[KV](https://developers.cloudflare.com/kv/)

You can now have up to 1000 Workers KV namespaces per account.

Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.

Consult the [Workers KV limits documentation](https://developers.cloudflare.com/kv/platform/limits/) for the rest of the limits. This increased limit is available for both the Free and Paid [Workers plans](https://developers.cloudflare.com/workers/platform/pricing/).
