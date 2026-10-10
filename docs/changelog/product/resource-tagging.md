---
url: https://developers.cloudflare.com/changelog/product/resource-tagging/
title: Resource Tagging Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:05.307812+00:00
---

# Resource Tagging Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/resource-tagging/

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

Apr 27, 2026

## [Resource Tagging enters public beta](https://developers.cloudflare.com/changelog/post/2026-04-27-resource-tagging-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)

Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.

#### What's included

  * **Broad resource type support** — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the [full list of supported resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/).
  * **Powerful filtering** — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.
  * **Account and zone-level endpoints** — Full CRUD operations across both scopes.
  * **Token-based authentication** — Tagging supports [Account Owned Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) that persist independently of individual users, so your automation keeps running through credential rotations and team changes.
  * **Flexible role support** — Super Administrators, Workers Admins, and Tag Admins can all manage tags.



#### API-first by design

The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.

#### Dashboard UI

You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to **Manage Account** > **Resource Tagging** to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.

![Tagged Resources dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2874,height=1234,format=webp/_astro/tagged-resources-dashboard.Dg5WvwiN.png)

#### What's coming next

In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.

#### Current limitations

  * `PUT` replaces all tags on a resource (no partial update). Use the [GET, merge, PUT workflow](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/#add-a-single-tag) to modify individual tags safely.
  * `DELETE` removes all tags from a resource. To remove a single tag, PUT the remaining tags back.
  * Querying tags for a resource that has never been tagged returns `500` instead of `404`. This is a known beta limitation.



To get started, refer to the [Resource Tagging documentation](https://developers.cloudflare.com/resource-tagging/).
