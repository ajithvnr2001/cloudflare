---
url: https://developers.cloudflare.com/changelog/product/flagship/
title: Flagship Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:08.127837+00:00
---

# Flagship Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/flagship/

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

Aug 26, 2026

## [Create app-scoped API tokens for Flagship](https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/)

[Flagship](https://developers.cloudflare.com/flagship/)

You can now create **app-scoped API tokens** for [Flagship](https://developers.cloudflare.com/flagship/). These tokens grant access only to the Flagship apps you select, instead of every app in the account.

When you create a custom token, open the resource dropdown (it defaults to **Entire Account**) and select **Specified Flagship apps**. Then choose the app and a **Flagship App** permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.

Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.

To create a token, refer to [API tokens](https://developers.cloudflare.com/flagship/api-tokens/) or [open the app-scoped token form ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&scope=specified_flagship_app) in the dashboard.

Jul 16, 2026

## [Manage Flagship from the command line with Wrangler](https://developers.cloudflare.com/changelog/post/2026-07-16-wrangler-commands/)

[Flagship](https://developers.cloudflare.com/flagship/)

**[Wrangler](https://developers.cloudflare.com/workers/wrangler/)** now includes `wrangler flagship`, a command suite for managing [Flagship](https://developers.cloudflare.com/flagship/) apps and feature flags from your terminal.

Create an app and, if you use it from a Worker, add it to your `wrangler.json` or `wrangler.jsonc` file as a binding:
    
    
    wrangler flagship apps create "My Worker App" \
      --binding FLAGS \
      --update-config

Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:
    
    
    wrangler flagship flags create <APP_ID> new-checkout
    
    wrangler flagship flags create <APP_ID> checkout-flow \
      --variation control=old-checkout \
      --variation treatment=new-checkout \
      --default control \
      --type string

After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:
    
    
    wrangler flagship flags update <APP_ID> checkout-flow --default treatment
    wrangler flagship flags disable <APP_ID> checkout-flow
    wrangler flagship flags enable <APP_ID> checkout-flow

For release workflows, use `rollout`, `split`, and `rules` to change exposure without redeploying your Worker:
    
    
    wrangler flagship flags rollout <APP_ID> new-checkout \
      --to on \
      --percentage 25 \
      --by user_id
    
    wrangler flagship flags split <APP_ID> checkout-flow \
      --weight control=80 \
      --weight treatment=20 \
      --by user_id
    
    wrangler flagship flags rules update <APP_ID> checkout-flow \
      --priority 1 \
      --when "country equals US"

These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.

Refer to the [`wrangler flagship` command reference](https://developers.cloudflare.com/flagship/reference/wrangler-commands/) for the full command guide.

Jun 10, 2026

## [Flagship API reference now available](https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/)

[Flagship](https://developers.cloudflare.com/flagship/)

The **[Flagship API reference](https://developers.cloudflare.com/api/resources/flagship/)** is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.

For example, create a new boolean flag with the API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -d '{
        "key": "new-checkout",
        "enabled": true,
        "default_variation": "off",
        "variations": {
          "off": false,
          "on": true
        },
        "rules": []
      }'

To create an API token, go to [Account API Tokens ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens) in the Cloudflare dashboard and search for Flagship.

The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the [Flagship reference in the Cloudflare skill ↗︎](https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship) to create and manage Flagship resources.

Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/) to learn more about evaluating feature flags from your applications.

May 26, 2026

## [Flagship now in public beta](https://developers.cloudflare.com/changelog/post/2026-05-26-public-beta/)

[Flagship](https://developers.cloudflare.com/flagship/)

**[Flagship](https://developers.cloudflare.com/flagship/)** is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.

Evaluate a flag from a Worker in a few lines of code:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const showNewCheckout = await env.FLAGS.getBooleanValue(
    			"new-checkout",
    			false,
    		);
    
    		return new Response(showNewCheckout ? "New checkout" : "Standard checkout");
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const showNewCheckout = await env.FLAGS.getBooleanValue("new-checkout", false);
    
    		return new Response(
    			showNewCheckout ? "New checkout" : "Standard checkout",
    		);
    	},
    } satisfies ExportedHandler<Env>;

Start creating flags from the Cloudflare dashboard today. Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/get-started/) to get started.
