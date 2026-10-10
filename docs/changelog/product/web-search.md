---
url: https://developers.cloudflare.com/changelog/product/web-search/
title: Web Search API Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:02.242103+00:00
---

# Web Search API Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/web-search/

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

## [Introducing Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).
