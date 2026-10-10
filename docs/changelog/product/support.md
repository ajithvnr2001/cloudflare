---
url: https://developers.cloudflare.com/changelog/product/support/
title: Support Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.432261+00:00
---

# Support Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/support/

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

Aug 11, 2026

## [New Cloudflare Status page](https://developers.cloudflare.com/changelog/post/2026-08-11-new-status-page/)

[Support](https://developers.cloudflare.com/support/)

The Cloudflare Status page at [www.cloudflarestatus.com ↗︎](https://www.cloudflarestatus.com/) has been rebuilt. It is available at the same address, and every previously documented [Status API ↗︎](https://www.cloudflarestatus.com/api) endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.

#### Notifications that fire even when Cloudflare is down

The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.

The **Maintenance Notification** and **Incident Alerts** in [Cloudflare Notifications](https://developers.cloudflare.com/notifications/) remain supported, and deliver to the destinations already configured on your account.

#### Markdown for AI agents

Every page on the status page returns Markdown when requested with an `Accept: text/markdown` header, so agents can read the current status without parsing HTML:
    
    
    curl -H "Accept: text/markdown" https://www.cloudflarestatus.com/locations

#### Separate feeds for incidents and maintenance

Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:
    
    
    https://www.cloudflarestatus.com/api/v3/incidents.rss
    https://www.cloudflarestatus.com/api/v3/incidents.atom
    https://www.cloudflarestatus.com/api/v3/maintenance.rss
    https://www.cloudflarestatus.com/api/v3/maintenance.atom

For more information, refer to [Cloudflare Status](https://developers.cloudflare.com/support/cloudflare-status/).

Apr 28, 2026

## [Direct access to Support from the dashboard](https://developers.cloudflare.com/changelog/post/2026-04-28-direct-support-navigation/)

[Support](https://developers.cloudflare.com/support/)

#### Direct access to Support from the dashboard

The **Support** button in the dashboard global navigation header now takes you directly to the [Cloudflare Support Portal ↗︎](https://support.cloudflare.com), eliminating the previous dropdown menu.

This change ensures that when you need help, you spend less time navigating the UI and more time getting the answers you need.

#### What changed?

  * **Previous behavior** : Selecting **? Support** opened a dropdown menu with various links (Help Center, Cloudflare Community, etc.).
  * **New behavior** : Selecting **Support** immediately redirects your current tab to the Support Portal.



To learn more about the resources available to you, refer to the [Cloudflare Support documentation ↗︎](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Apr 7, 2026

## [Redesigned Support Portal for faster, personalized help](https://developers.cloudflare.com/changelog/post/2026-04-06-redesigned-support-portal/)

[Support](https://developers.cloudflare.com/support/)

#### Redesigned "Get Help" Portal for faster, personalized help

Cloudflare has officially launched a redesigned "Get Help" Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.

The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as "Ask AI", "Chat with a human", or "Community" — without the manual triage.

#### What's New

  * **One Page, Clear Choices** : No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.
  * **A Radically Simpler Support Form** : We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.
  * **AI-Driven Triage** : Using [Cloudflare Workers AI ↗︎](https://developers.cloudflare.com/workers-ai/) and [Vectorize ↗︎](https://developers.cloudflare.com/vectorize/), the portal now automatically generates case subjects and predicts product categories.



#### Moving complexity to the backend

Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.

By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.

To learn more, refer to the [Support documentation](https://developers.cloudflare.com/support/contacting-cloudflare-support/) or select **Get Help** directly in the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com/).
