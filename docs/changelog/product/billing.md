---
url: https://developers.cloudflare.com/changelog/product/billing/
title: Billing Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:10.748121+00:00
---

# Billing Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/billing/

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

Jul 20, 2026

## [Budget alerts now on by default for Pay-as-you-go accounts](https://developers.cloudflare.com/changelog/post/2026-06-15-budget-alerts-default-on/)

[Billing](https://developers.cloudflare.com/billing/)[Workers](https://developers.cloudflare.com/workers/)

We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.

We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.

The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.

Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.

Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.

You can change the threshold, add additional alerts, or remove the default alert entirely from **Manage Account** > **Billing** > **Billable Usage** , or from your Notifications settings. If you already configured your own budget alert, nothing changes.

Enterprise contract accounts are not in scope.

For more information, refer to the [Budget alerts documentation](https://developers.cloudflare.com/billing/manage/budget-alerts/).

May 21, 2026

## [Modernized Billing Profile with new payment options](https://developers.cloudflare.com/changelog/post/2026-05-21-modernised-billing-profile/)

[Billing](https://developers.cloudflare.com/billing/)

The [Billing Profile](https://developers.cloudflare.com/billing/get-started/update-billing-info/) now has a modern UI and a single space that unifies billing information, payment method management and an enhanced subscriptions view under a single **Subscriptions** tab.

#### What changed

The **Subscriptions** tab brings billing information, payment method management, and your subscriptions together in one place. The payment management and **Pay overdue balances** flows now use the latest checkout as product purchase flows, so you can pay with Apple Pay, Google Pay, Link, and [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/) alongside cards and PayPal.

New cards complete 3D Secure authentication when the issuer requires it — for example, the EU under PSD2 and India under RBI.

![Modernized Billing Profile with the Subscriptions tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=909,height=676,format=webp/_astro/2026-05-21-modernised-billing-profile.D6PysUnl.png)

For details, refer to the [Billing Home](https://developers.cloudflare.com/billing/) documentation.
