---
url: https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/
title: Automatic Platform Optimization Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.015581+00:00
---

# Automatic Platform Optimization Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/automatic-platform-optimization/

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

Aug 27, 2026

## [APO caches more crawler and bot traffic again](https://developers.cloudflare.com/changelog/post/2026-08-27-accept-header-caching/)

[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)

We fixed a regression where Automatic Platform Optimization (APO) stopped caching some HTML requests that did not send an explicit `Accept: text/html` header — commonly crawlers, bots, and uptime monitors. These requests were being served from your origin (`cf-cache-status: DYNAMIC`) instead of the cache.

APO now caches these requests again. No action is needed. If you added a Transform Rule to set `Accept: text/html` as a workaround, you can remove it.

For details on how APO decides what to cache, refer to [About APO](https://developers.cloudflare.com/automatic-platform-optimization/about/).
