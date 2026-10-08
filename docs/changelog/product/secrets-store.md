---
url: https://developers.cloudflare.com/changelog/product/secrets-store/
title: Secrets Store Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:49.426125+00:00
---

# Secrets Store Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/secrets-store/

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

Aug 25, 2025

## [Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store](https://developers.cloudflare.com/changelog/post/2025-08-25-secrets-store-ai-gateway/)

[Secrets Store](https://developers.cloudflare.com/secrets-store/)[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through [Bring Your Own Key ↗︎](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/). Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.

You can now create a secret directly from your AI Gateway [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/ai-gateway) by navigating into your gateway -> **Provider Keys** -> **Add**.

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1842,format=webp/_astro/add-secret-ai-gateway.B-SIPr6s.png)

You can also create your secret with the newly available **ai_gateway** scope via [wrangler ↗︎](https://developers.cloudflare.com/workers/wrangler/commands/), the [Secrets Store dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), or the [API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/).

Then, pass the key in the request header using its Secrets Store reference:
    
    
    curl -X POST https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic/v1/messages \
     --header 'cf-aig-authorization: ANTHROPIC_KEY_1 \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{"model": "claude-3-opus-20240229", "messages": [{"role": "user", "content": "What is Cloudflare?"}]}'

Or, using Javascript:
    
    
    import Anthropic from '@anthropic-ai/sdk';
    
    
    const anthropic = new Anthropic({
     apiKey: "ANTHROPIC_KEY_1",
     baseURL: "https://gateway.ai.cloudflare.com/v1/<ACCOUNT_ID>/my-gateway/anthropic",
    });
    
    
    const message = await anthropic.messages.create({
     model: 'claude-3-opus-20240229',
     messages: [{role: "user", content: "What is Cloudflare?"}],
     max_tokens: 1024
    });

For more information, check out the [blog ↗︎](https://blog.cloudflare.com/ai-gateway-aug-2025-refresh)!

Jul 29, 2025

## [Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets](https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/)

[Workers](https://developers.cloudflare.com/workers/)[Secrets Store](https://developers.cloudflare.com/secrets-store/)

Any template which uses [Worker environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), or [Secrets Store secrets](https://developers.cloudflare.com/secrets-store/) can now be deployed using a [Deploy to Cloudflare button](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

Define environment variables and secrets store bindings in your Wrangler configuration file as normal:
    
    
    {
      "name": "my-worker",
      "main": "./src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
      "vars": {
        "API_HOST": "https://example.com",
      },
    	"secrets_store_secrets": [
    		{
    			"binding": "API_KEY",
    			"store_id": "demo",
    			"secret_name": "api-key"
    		}
    	]
    }
    
    
    name = "my-worker"
    main = "./src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [vars]
    API_HOST = "https://example.com"
    
    [[secrets_store_secrets]]
    binding = "API_KEY"
    store_id = "demo"
    secret_name = "api-key"

Add secrets to a `.dev.vars.example` or `.env.example` file:

.dev.vars.exampleini
    
    
    COOKIE_SIGNING_KEY=my-secret # comment

And optionally, you can add a description for these bindings in your template's `package.json` to help users understand how to configure each value:

package.jsonjson
    
    
    {
    	"name": "my-worker",
    	"private": true,
    	"cloudflare": {
    		"bindings": {
    			"API_KEY": {
    				"description": "Select your company's API key for connecting to the example service."
    			},
    			"COOKIE_SIGNING_KEY": {
    				"description": "Generate a random string using `openssl rand -hex 32`."
    			}
    		}
    	}
    }

These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in [our documentation](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

May 27, 2025

## [Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans](https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)[Secrets Store](https://developers.cloudflare.com/secrets-store/)

With upgraded limits to [all free and paid plans ↗︎](https://www.cloudflare.com/plans/), you can now scale more easily with [Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and [Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/).

[Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the [limit for custom hostnames ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/) on a Cloudflare for SaaS Pay-as-you-go plan has been **raised from 5,000 custom hostnames to 50,000 custom hostnames.**

With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. [Custom origin server ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/) is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.

You can enable custom origin server on a per-custom hostname basis [via the API ↗︎](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) or the UI:

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1896,height=1636,format=webp/_astro/custom-origin-server.B-BXcG-1.png)

Currently [in beta with a Workers integration ↗︎](https://blog.cloudflare.com/secrets-store-beta/), [Cloudflare Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/) allows you to store, manage, and deploy account level secrets from a secure, centralized platform your [Cloudflare Workers ↗︎](https://developers.cloudflare.com/workers/). Now, you can create and deploy **100 secrets per account**. Try it out [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), with [Wrangler ↗︎](https://developers.cloudflare.com/secrets-store/integrations/workers/), or [via the API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/) today.

Apr 9, 2025

## [Cloudflare Secrets Store now available in Beta](https://developers.cloudflare.com/changelog/post/2025-04-09-secrets-store-beta/)

[Secrets Store](https://developers.cloudflare.com/secrets-store/)[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1914,height=1536,format=webp/_astro/secrets-store-landing-page.BQoEWsq8.png)

To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store) or use this Wrangler command:
    
    
    wrangler secrets-store store create <name> --remote

The following are supported in the Secrets Store beta:

  * Secrets Store UI & API: create your store & create, duplicate, update, scope, and delete a secret
  * Workers UI: bind a new or existing account level secret to a Worker and deploy in code
  * Wrangler: create your store & create, duplicate, update, scope, and delete a secret
  * Account Management UI & API: assign Secrets Store permissions roles & view audit logs for actions taken in Secrets Store core platform



For instructions on how to get started, visit our [developer documentation](https://developers.cloudflare.com/secrets-store/).
