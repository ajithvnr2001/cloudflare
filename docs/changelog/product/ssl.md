---
url: https://developers.cloudflare.com/changelog/product/ssl/
title: SSL/TLS Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:04.217865+00:00
---

# SSL/TLS Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/ssl/

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

Aug 13, 2026

## [Certificate Transparency Monitoring is now Generally Available](https://developers.cloudflare.com/changelog/post/2026-08-13-ct-monitoring-ga/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Certificate Transparency Monitoring is now [generally available ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) across all Cloudflare plans.

Alerts for certificates Cloudflare issues on your behalf (Universal SSL renewals, backup certificates, Advanced Certificate Manager, Total TLS) are now automatically filtered out. Alert emails are also clearer and more actionable, with structured certificate details and a direct link to manage CT Monitoring in the Cloudflare dashboard.

Learn more in the [launch blog post ↗︎](https://blog.cloudflare.com/certificate-transparency-monitoring-ga) or the [CT Monitoring docs](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/).

Jul 21, 2026

## [Faster and more secure TLS handshakes to your origins, automatically](https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first `ClientHello`, helping avoid a `HelloRetryRequest` and one extra network round trip.

Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum `X25519MLKEM768` hybrid key agreement.

To change this behavior, go to **SSL/TLS** > **Overview** > **Origin connection & post-quantum encryption**. Turn off **Automatic key exchange** to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.

**Compliance requirements** apply only to TLS 1.3 connections. The **Post-quantum hybrid** option requires hybrid post-quantum key agreements support on your origin server. The **Federal Information Processing Standards (FIPS)** option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.

For requirements, configuration options, and rollout details, refer to [Automatic key exchange to origins](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/).

Jun 17, 2026

## [Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store](https://developers.cloudflare.com/changelog/post/2026-06-17-pqc-mldsa-aop-cots/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare now accepts [ML-DSA ↗︎](https://csrc.nist.gov/pubs/fips/204/final) (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.

ML-DSA is supported in two origin-facing features:

  * [Authenticated Origin Pulls](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.
  * [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/) (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under [Full (strict) encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/).



Refer to [Post-quantum signatures](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures) for certificate generation and setup guidance, and to [PQC in Cloudflare products](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-cloudflare-products/) for the current post-quantum deployment status across Cloudflare.

Apr 7, 2026

## [Manage mTLS and BYO CA certificates from the Cloudflare dashboard](https://developers.cloudflare.com/changelog/post/2026-04-07-mtls-byoca-dashboard/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

You can now manage mutual TLS (mTLS) and Bring Your Own Certificate Authority (BYO CA) configurations directly from the Cloudflare dashboard — no API required.

Previously, these advanced workflows required the Cloudflare API. The following are now available in the dashboard:

  * **AOP certificate management** — Upload and manage your own certificate authorities for [Authenticated Origin Pulls (AOP)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) directly from the dashboard.
  * **BYO Client mTLS certificate management** — Upload and manage your own CA certificates for [client mTLS enforcement](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/) without needing API access.
  * **CDN hostname to client mTLS certificate mapping** — Associate client mTLS certificates with specific hostnames directly from the dashboard.



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

Feb 14, 2025

## [Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname](https://developers.cloudflare.com/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/)

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.

Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.
    
    
    curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \
        -H 'Content-Type: application/json' \
        -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
        -H "X-Auth-Key: $CLOUDFLARE_API_KEY" \
        -d '{
        "hostname": "hostname",
        "ssl": {
            "custom_cert_bundle": [
                {
                    "custom_certificate": "RSA Cert",
                    "custom_key": "RSA Key"
                },
                {
                    "custom_certificate": "ECDSA Cert",
                    "custom_key": "ECDSA Key"
                }
            ],
            "bundle_method": "force",
            "wildcard": false,
            "settings": {
                "min_tls_version": "1.0"
            }
        }
    }’

You can also:

  * [Upload](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/) an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.

  * [Replace](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/) the RSA or ECDSA certificate with a certificate of its same type.

  * [Delete](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/) the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).




This feature is available for Business and Enterprise customers who have purchased custom certificates.
