---
url: https://developers.cloudflare.com/changelog/product/speed/
title: Speed Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.378661+00:00
---

# Speed Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/speed/

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

Jun 23, 2026

## [Cloudflare AMP/SXG is now end of life.](https://developers.cloudflare.com/changelog/post/2026-06-23-amp-sxg-end-of-life/)

[Speed](https://developers.cloudflare.com/speed/)

Cloudflare Accelerated Mobile Pages (AMP) and Signed Exchanges (SXG) support has reached end of life. The features have been disabled since October 2025, so customers who had them configured should see no change to their traffic.

Customers will no longer be able to configure AMP/SXG through API or rulesets. The Zone API will start throwing errors. Rulesets with the SXG configuration will fail to save until SXG has been removed.

Jun 18, 2026

## [Cloudflare Fonts error handling and security improvements](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/)

[Speed](https://developers.cloudflare.com/speed/)

Cloudflare Fonts now forwards `/cf-fonts` requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.

Apr 30, 2026

## [Shared dictionaries passthrough now in open beta](https://developers.cloudflare.com/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/)

[Speed](https://developers.cloudflare.com/speed/)

[Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/) ([RFC 9842 ↗︎](https://www.rfc-editor.org/rfc/rfc9842.html)) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.

#### What changed

In passthrough mode, Cloudflare:

  * Forwards the `Use-As-Dictionary` and `Available-Dictionary` headers between client and origin without modification.
  * Treats `dcb` (Dictionary-Compressed Brotli) and `dcz` (Dictionary-Compressed Zstandard) as valid `Content-Encoding` values end to end, without recompressing them.
  * Extends the cache key to vary on `Available-Dictionary` and `Accept-Encoding` so each delta-compressed variant is cached correctly.



Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching `Use-As-Dictionary` headers, and producing deltas in response to `Available-Dictionary` requests. Cloudflare handles the transport and the cache.

In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.

Shared dictionaries work with browsers that advertise `dcb` or `dcz` in `Accept-Encoding`. Today, this includes Chrome 130 or later and Edge 130 or later.

#### Get started

Turn on passthrough for your zone with a single API call:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"value": "passthrough"
    	}'

You can also turn it on under **Speed** > **Settings** > **Content Optimization** in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization). For full origin setup instructions and a working test recipe, refer to [Shared dictionaries](https://developers.cloudflare.com/speed/optimization/content/shared-dictionaries/), or try the live demo at [canicompress.com ↗︎](https://canicompress.com/).
