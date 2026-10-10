---
url: https://developers.cloudflare.com/changelog/product/security-overview/
title: Security Overview Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.794028+00:00
---

# Security Overview Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/security-overview/

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

Apr 20, 2026

## [Archive and audit security action items](https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/)

[Security Overview](https://developers.cloudflare.com/security/overview/)

#### Archive and audit security action items

Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.

* * *

#### Why this matters

Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.

With these new archiving options—**False Positive** , **Accept Risk** , and **Other** —you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.

#### Key features

  * **Structured Archiving:** Choose from specific categories to define why an action item is being moved.
  * **Required Rationale:** For "Accept Risk" and "Other" categories, users must provide documentation, ensuring accountability for security decisions.
  * **Audit Log Transparency:** New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.
  * **Reversible Actions:** Any archived item can be moved back to the active list at any time if the security context changes.



:::note Archiving a suspicious activity item will remove it from the Security Overview page, but the activity will remain visible in your Security Analytics dashboard for deeper forensic analysis. :::

* * *

#### Example: Retrieve audit logs via API

To review the history and rationale of a specific archived issue at the account level, you can use the following API command:
    
    
    curl "[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log" \
         -H "Authorization: Bearer <API_TOKEN>" \
         -H "Content-Type: application/json"

Mar 17, 2026

## [New Security Overview UI](https://developers.cloudflare.com/changelog/post/2026-03-17-new-security-overview-ui/)

[Security Overview](https://developers.cloudflare.com/security/overview/)

The Security Overview has been updated to provide Application Security customers with more actionable insights and a clearer view of their security posture.

Key improvements include:

  * **Criticality for all Insights** : Every insight now includes a criticality rating, allowing you to prioritize the most impactful security action items first.
  * **Detection Tools Section** : A new section displays the security detection tools available to you, indicating which are currently enabled and which can be activated to strengthen your defenses.
  * **Industry Peer Comparison** (Enterprise customers): A new module from Security Reports benchmarks your security posture against industry peers, highlighting relative strengths and areas for improvement.

![New Security Overview UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1921,height=958,format=webp/_astro/overview-ui.D7FzaCLm.png)

For more information, refer to [Security Overview](https://developers.cloudflare.com/security/overview/).
