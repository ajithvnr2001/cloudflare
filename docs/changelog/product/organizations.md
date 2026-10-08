---
url: https://developers.cloudflare.com/changelog/product/organizations/
title: Organizations Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:48.186674+00:00
---

# Organizations Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/organizations/

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

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 2, 2026

## [Organizations support increased account and zone limits](https://developers.cloudflare.com/changelog/post/2026-10-02-organization-account-zone-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations now support up to **20,000 accounts** and **200,000 zones**. For MSSP/Distributors using sub-organizations, these limits are applied at the root Organization.

If you require a higher limit, reach out to your account team. The new limits apply to enterprise and MSSP/Distributor Organizations. Legacy reseller partner and brand partner tenants retain their existing quota behavior.

For more information, refer to [Account and zone limits](https://developers.cloudflare.com/fundamentals/organizations/limitations/#account-and-zone-limits).

Jul 17, 2026

## [Distributor, MSSP, and Agency partners can manage Organization members directly](https://developers.cloudflare.com/changelog/post/2026-07-17-distributor-mssp-self-serve-members/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Distributor, MSSP, and Agency partners on Cloudflare [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.

Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard **Add member** flow was blocked for these Organizations.

Now, Organization admins can add members themselves from **Organization** > **Members** > **Add member** , with no beta enrollment required.

New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The **Accounts** list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.

Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.

Distributor, MSSP, and Agency Organizations are currently in beta.

For more information, refer to [Manage Organization members](https://developers.cloudflare.com/fundamentals/organizations/manage-members/).

Apr 6, 2026

## [Organizations is now in public beta for enterprises](https://developers.cloudflare.com/changelog/post/2026-04-06-organizations-public-beta/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

We're announcing the public beta of **Organizations** for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.

**What's New**

**Organizations [BETA]** : [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.

**Self-serve onboarding** : Enterprise customers can [create an Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/) in the dashboard and assign accounts where they are already Super Administrators.

**Centralized Account Management** : At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly. **Shared policies** : Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) policies across multiple accounts within your Organization to simplify centralized policy management. **Implicit access** : Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.

**Unified analytics** : View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.

**Terraform provider support** : Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the [Cloudflare Terraform provider ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization).

**Shared policies** : Share [WAF](https://developers.cloudflare.com/waf/custom-rules/) or [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) policies across multiple accounts within your Organization to simplify centralized policy management.

Note

Organizations is in Public Beta. You must have an Enterprise account to create an organization, but once created, you can add accounts of any plan type where you are a Super Administrator.

For more info:

  * [Get started with Organizations](https://developers.cloudflare.com/fundamentals/organizations/)
  * [Set up your Organization](https://developers.cloudflare.com/fundamentals/organizations/setup/)
  * [Review limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/)


