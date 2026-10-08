---
url: https://developers.cloudflare.com/changelog/product/vectorize/
title: Vectorize Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:50.458545+00:00
---

# Vectorize Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/vectorize/

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

Aug 4, 2026

## [Vectorize indexes now support up to 20 million vectors](https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.

Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the [Vectorize limits documentation](https://developers.cloudflare.com/vectorize/platform/limits/) for complete details.

Jul 1, 2026

## [Reduced end-to-end latency for vector changes](https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

We have greatly improved the throughput of the Vectorize [write-ahead log (WAL) ↗︎](https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal). As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.

![Vectorize p99 WAL batch end-to-end latency improved](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2542,height=1184,format=webp/_astro/vectorize-p99-wal-batch-end-to-end-latency-improvement.k8gtzlG7.png)

This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.

For more information, refer to the [Vectorize documentation](https://developers.cloudflare.com/vectorize/).

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

Mar 16, 2026

## [Return up to 50 query results with values or metadata](https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now set `topK` up to `50` when a Vectorize query returns values or full metadata. This raises the previous limit of `20` for queries that use `returnValues: true` or `returnMetadata: "all"`.

Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the [Vectorize API reference](https://developers.cloudflare.com/vectorize/reference/client-api/) for query options and current `topK` limits.

Jan 23, 2026

## [Vectorize indexes now support up to 10 million vectors](https://developers.cloudflare.com/changelog/post/2026-01-23-increased-index-capacity/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.

Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the [Vectorize limits documentation](https://developers.cloudflare.com/vectorize/platform/limits/) for complete details.

Aug 26, 2025

## [List all vectors in a Vectorize index with the new list-vectors operation](https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/)

[Vectorize](https://developers.cloudflare.com/vectorize/)

You can now list all vector identifiers in a Vectorize index using the new `list-vectors` operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.

The operation is available via Wrangler CLI and REST API. Refer to the [list-vectors best practices guide](https://developers.cloudflare.com/vectorize/best-practices/list-vectors/) for detailed usage guidance.

Apr 7, 2025

## [Create fully-managed RAG pipelines for your AI applications with AutoRAG](https://developers.cloudflare.com/changelog/post/2025-04-07-autorag-open-beta/)

[AI Search](https://developers.cloudflare.com/ai-search/)[Vectorize](https://developers.cloudflare.com/vectorize/)

[AutoRAG](https://developers.cloudflare.com/ai-search/) is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to [R2](https://developers.cloudflare.com/r2/get-started/), and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.

With AutoRAG, you can:

  * **Customize your pipeline:** Choose from [Workers AI](https://developers.cloudflare.com/workers-ai) models, configure chunking strategies, edit system prompts, and more.
  * **Instant setup:** AutoRAG provisions everything you need from [Vectorize](https://developers.cloudflare.com/vectorize), [AI gateway](https://developers.cloudflare.com/ai-gateway), to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.
  * **Keep your index fresh:** AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.
  * **Ask questions:** Query your data and receive grounded responses via a [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/) or [API](https://developers.cloudflare.com/ai-search/api/search/rest-api/).



Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.

Get started in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/autorag) or check out the [guide](https://developers.cloudflare.com/ai-search/get-started/) for instructions on how to build your RAG pipeline today.
