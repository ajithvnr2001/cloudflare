---
url: https://developers.cloudflare.com/use-cases/apis/
title: APIs and microservices \u00b7 Use cases \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:09.497766+00:00
---

# APIs and microservices · Use cases · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/apis/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /APIs and microservices



# APIs and microservices

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArchitecture patterns Secure API gateway Edge-native APIs Microservices meshPrerequisites Create a new application Use an existing applicationRelated resources

Build, secure, and manage Application Programming Interfaces (APIs) with rate limiting, authentication, and observability. Cloudflare Workers deploys API handlers globally with automatic scaling. API Shield validates requests against your OpenAPI specification. Rate Limiting prevents abuse. mTLS authenticates machine-to-machine communication. Cloudflare Tunnel and Access secure internal microservices. Logpush and Workers Analytics Engine provide monitoring.

  * [Deploy APIs at the edge](https://developers.cloudflare.com/use-cases/apis/deploy-apis/)
  * [Protect your APIs](https://developers.cloudflare.com/use-cases/apis/protect-apis/)
  * [Connect your internal network services](https://developers.cloudflare.com/use-cases/apis/internal-services/)
  * [Monitor your APIs](https://developers.cloudflare.com/use-cases/apis/monitor-apis/)



## Architecture patterns

### Secure API gateway

Protect your APIs with defense in depth:

  * **API Shield** validates requests against your OpenAPI schema
  * **Security rules** managed rulesets block SQL injection, XSS, and OWASP Top 10 vulnerabilities
  * **Rate Limiting** prevents abuse and Distributed Denial of Service (DDoS) attacks
  * **mTLS** (mutual TLS) authenticates known clients with certificates



### Edge-native APIs

Build APIs that run entirely on Cloudflare:

  * **Workers** handles request routing and business logic
  * **D1** or **KV** stores application data
  * **Queues** handles async processing and webhooks



### Microservices mesh

Connect and secure internal services:

  * **Cloudflare Tunnel** exposes services without public IPs
  * **Access** enforces identity-based policies between services
  * **Workers** acts as an API gateway for external consumers



* * *

## Prerequisites

### Create a new application

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up).
  * [Node.js ↗︎](https://nodejs.org/) (version 16.17.0 or later) installed on your machine.
  * [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) installed.



### Use an existing application

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up).
  * A domain [added to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/) with DNS records proxied through Cloudflare. This is required for API Shield, rate limiting, and application security.
  * For securing internal services with Cloudflare Tunnel and Access: a [Cloudflare One organization](https://developers.cloudflare.com/cloudflare-one/setup/) created in the Cloudflare dashboard.



* * *

## Related resources

### [API Shield documentation](https://developers.cloudflare.com/api-shield/)

Complete documentation for API discovery, schema validation, and security.

### [Workers examples](https://developers.cloudflare.com/workers/examples/)

Code examples for building APIs with Workers.

[PreviousSecure your application](https://developers.cloudflare.com/use-cases/web-apps/security/)[NextDeploy APIs at the edge](https://developers.cloudflare.com/use-cases/apis/deploy-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/apis/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
