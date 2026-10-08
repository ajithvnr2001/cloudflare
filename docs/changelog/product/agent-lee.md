---
url: https://developers.cloudflare.com/changelog/product/agent-lee/
title: Agent Lee Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:39.006118+00:00
---

# Agent Lee Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/agent-lee/

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

Aug 12, 2026

## [Export the code Agent Lee generates](https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/)

[Agent Lee](https://developers.cloudflare.com/agent-lee/)

When Agent Lee generates a project for you — a starter static site, a Worker, a scaffold — you can now take the source with you. Agent Lee packages the generated files into a temporary repository and gives you a one-time command to clone it to your own machine.

Previously, generated code lived only in the conversation. You had to copy files out of the chat by hand, which is tedious for anything larger than a single snippet and easy to get wrong.

#### How it works

  * Ask Agent Lee to build something, then ask it to export the code.
  * An export card appears listing the files and a countdown to expiry.
  * Select **Copy clone command**. Agent Lee fetches a fresh command and copies it to your clipboard.
  * Run it in your terminal, then point the repository at your own Git host and push:


    
    
    git remote set-url origin https://your-git-host.example/you/your-repo.git
    git push -u origin main

#### Good to know

  * **The export is temporary.** The repository expires about 36 hours after it is created and is then deleted automatically. The clone credential expires about an hour after it is issued. Clone promptly, then push to a repository you control.
  * **No credential appears in the chat.** The clone command and its read-only credential are delivered only when you select **Copy clone command** — never in the message text or conversation history.
  * **Nothing is written to your account.** The temporary repository lives in Cloudflare-managed storage, and connecting a GitHub or GitLab account is not required.
  * **Intended for small projects.** An export can include up to 50 files, up to 100 KB per file and 2 MB in total.



Agent Lee remains in beta. Features and behaviors may change as the product evolves.

For details, see [Export generated code](https://developers.cloudflare.com/agent-lee/take-home-code/).
