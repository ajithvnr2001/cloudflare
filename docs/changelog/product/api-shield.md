---
url: https://developers.cloudflare.com/changelog/product/api-shield/
title: API Shield Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:11.716406+00:00
---

# API Shield Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/api-shield/

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

## [Increased limits for JWT validation configurations](https://developers.cloudflare.com/changelog/post/2026-08-27-jwt-validation-limits/)

[API Shield](https://developers.cloudflare.com/api-shield/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports 32 token configurations per zone by default. Each token configuration can contain up to 16 keys.

These increased limits support more JWT configurations and provide additional capacity for key rotation.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/) for configuration details.

Aug 25, 2026

## [Symmetric key support for JWT validation](https://developers.cloudflare.com/changelog/post/2026-08-25-symmetric-jwt-validation/)

[API Shield](https://developers.cloudflare.com/api-shield/)

API Shield [JSON Web Token validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) now supports symmetric keys that use the `HS256`, `HS384`, and `HS512` algorithms. You can configure HMAC verification keys in the Cloudflare dashboard or with the Cloudflare API.

Cloudflare never stores symmetric credentials in plaintext. API responses do not include the credential.

Refer to [Configure JWT validation via the API](https://developers.cloudflare.com/api-shield/security/jwt-validation/api/#credentials) for supported key formats and credential requirements.

Mar 23, 2026

## [Web Assets fields now available in GraphQL Analytics API](https://developers.cloudflare.com/changelog/post/2026-03-23-web-assets-graphql-fields/)

[API Shield](https://developers.cloudflare.com/api-shield/)

Two new fields are now available in the `httpRequestsAdaptive` and `httpRequestsAdaptiveGroups` [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) datasets:

  * `webAssetsOperationId` — the ID of the [saved endpoint](https://developers.cloudflare.com/api-shield/management-and-monitoring/) that matched the incoming request.
  * `webAssetsLabelsManaged` — the [managed labels](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#managed-labels) mapped to the matched operation at the time of the request (for example, `cf-llm`, `cf-log-in`). At most 10 labels are returned per request.



Both fields are empty when no operation matched. `webAssetsLabelsManaged` is also empty when no managed labels are assigned to the matched operation.

These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/) did or did not flag a request.

Refer to [Endpoint labeling service](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#analytics) for GraphQL query examples.

Mar 9, 2026

## [New Vulnerability Scanner for API Shield](https://developers.cloudflare.com/changelog/post/2026-03-09-vulnerability-scanner/)

[API Shield](https://developers.cloudflare.com/api-shield/)

Introducing Cloudflare's Web and API Vulnerability Scanner (Open Beta)

Cloudflare is launching the [Open Beta of the **Web and API Vulnerability Scanner** ↗︎](https://blog.cloudflare.com/vulnerability-scanner) for all [API Shield](https://developers.cloudflare.com/api-shield/) customers. This new, stateful Dynamic Application Security Testing (DAST) platform helps teams proactively find logic flaws in their APIs.

The initial release focuses on detecting Broken Object Level Authorization (BOLA) vulnerabilities by building API call graphs to simulate attacker and owner contexts, then testing these contexts by sending real HTTP requests to your APIs.

The scanner is now available via the Cloudflare API. To scan, set up your target environment, owner and attacker credentials, and upload your OpenAPI file with response schemas. The scanner will be available in the Cloudflare dashboard in a future release.

**Access** : This feature is only available to API Shield subscribers via the Cloudflare API. We hope you will use the API for programmatic integration into your CI/CD pipelines and security dashboards.

**Documentation** : Refer to the [developer documentation](https://developers.cloudflare.com/api-shield/security/vulnerability-scanner/) to start scanning your endpoints today.

Nov 25, 2025

## [New Zombie API detection for API Shield](https://developers.cloudflare.com/changelog/post/2025-11-25-zombie-endpoint-risk-label/)

[API Shield](https://developers.cloudflare.com/api-shield/)

API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the `cf-risk-zombie` [risk label](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#risk-labels) is applied.

The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.

Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a [fallthrough rule](https://developers.cloudflare.com/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule) to prevent communication with endpoints removed from Endpoint Management.

Nov 12, 2025

## [New BOLA Vulnerability Detection for API Shield](https://developers.cloudflare.com/changelog/post/2025-11-12-bola-attack-detection/)

[API Shield](https://developers.cloudflare.com/api-shield/)

Now, API Shield automatically searches for and highlights **Broken Object Level Authorization (BOLA) attacks** on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.

You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.

On the Security Overview card, select the suggestion > **View details** to review the top attacked API endpoints, endpoint details, and the attack summary: ![BOLA attack Overview card](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1546,height=816,format=webp/_astro/bola-overview-card.hwcSeAkb.png)![BOLA attack Overview drawer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1246,height=1078,format=webp/_astro/bola-overview-drawer.DD2c0bxS.png)

From the endpoint details, you can select **View attack** to find details about the BOLA attacker’s sessions.

![BOLA attack endpoint details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2050,height=630,format=webp/_astro/bola-endpoint-attack.UQP3MDkp.png)

From here, select **View in Analytics** to observe attacker traffic over time for the last seven days.

![BOLA attack analytics drawer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1156,height=1176,format=webp/_astro/bola-analytics-drawer.DXzC6EJU.png)

Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.

At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.

![Suspicious Activity card](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1252,height=722,format=webp/_astro/bola-suspicious-card._B3GB3s4.png)

We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.

In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.

Mar 18, 2025

## [New API Posture Management for API Shield](https://developers.cloudflare.com/changelog/post/2025-03-18-api-posture-management/)

[API Shield](https://developers.cloudflare.com/api-shield/)

Now, API Shield **automatically** labels your API inventory with API-specific risks so that you can track and manage risks to your APIs.

View these risks in [Endpoint Management](https://developers.cloudflare.com/api-shield/management-and-monitoring/) by label:

![A list of endpoint management labels](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2172,height=936,format=webp/_astro/endpoint-management-label.BDmf8Ai1.png)

...or in [Security Center Insights](https://developers.cloudflare.com/security/security-insights/):

![An example security center insight](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2250,height=1316,format=webp/_astro/posture-management-insight.7vB7mzGI.png)

API Shield will scan for risks on your API inventory daily. Here are the new risks we're scanning for and automatically labelling:

  * **cf-risk-sensitive** : applied if the customer is subscribed to the [sensitive data detection ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/) and the WAF detects sensitive data returned on an endpoint in the last seven days.
  * **cf-risk-missing-auth** : applied if the customer has configured a session ID and no successful requests to the endpoint contain the session ID.
  * **cf-risk-mixed-auth** : applied if the customer has configured a session ID and some successful requests to the endpoint contain the session ID while some lack the session ID.
  * **cf-risk-missing-schema** : added when a learned schema is available for an endpoint that has no active schema.
  * **cf-risk-error-anomaly** : added when an endpoint experiences a recent increase in response errors over the last 24 hours.
  * **cf-risk-latency-anomaly** : added when an endpoint experiences a recent increase in response latency over the last 24 hours.
  * **cf-risk-size-anomaly** : added when an endpoint experiences a spike in response body size over the last 24 hours.



In addition, API Shield has two new 'beta' scans for **Broken Object Level Authorization (BOLA) attacks**. If you're in the beta, you will see the following two labels when API Shield suspects an endpoint is suffering from a BOLA vulnerability:

  * **cf-risk-bola-enumeration** : added when an endpoint experiences successful responses with drastic differences in the number of unique elements requested by different user sessions.
  * **cf-risk-bola-pollution** : added when an endpoint experiences successful responses where parameters are found in multiple places in the request.



We are currently accepting more customers into our beta. Contact your account team if you are interested in BOLA attack detection for your API.

Refer to the [blog post ↗︎](https://blog.cloudflare.com/cloudflare-security-posture-management/) for more information about Cloudflare's expanded posture management capabilities.
