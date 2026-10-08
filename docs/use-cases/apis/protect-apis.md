---
url: https://developers.cloudflare.com/use-cases/apis/protect-apis/
title: Protect your APIs \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:09.631202+00:00
---

# Protect your APIs · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/apis/protect-apis/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /[APIs and microservices](https://developers.cloudflare.com/use-cases/apis/)
  4. /Protect your APIs



# Protect your APIs

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/apis/protect-apis/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSolutions API Shield Rate Limiting mTLS Application Security Access WorkersGet started

APIs are exposed to abuse, injection attacks, and unauthorized access. Cloudflare provides defense in depth with API Shield schema validation, per-endpoint rate limiting, mutual TLS (mTLS) client authentication, and security rules.

## Solutions

### API Shield

Discover, secure, and monitor your APIs. [Learn more about API Shield](https://developers.cloudflare.com/api-shield/).

  * **Schema validation** \- Reject requests that do not conform to your OpenAPI specification before they reach your origin



### Rate Limiting

Limit request rates based on flexible matching criteria. [Learn more about Rate Limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/).

  * **Rate limiting** \- Prevent abuse and volumetric attacks with per-IP or per-API-key request limits



### mTLS

Mutual TLS client certificate authentication. [Learn more about mTLS](https://developers.cloudflare.com/ssl/client-certificates/).

  * **Client authentication** \- Require mutual TLS certificates for machine-to-machine communication



### Application Security

Get automatic protection from vulnerabilities and create your own custom rules. [Learn more about Application Security](https://developers.cloudflare.com/waf/).

  * **Attack protection** \- Application security's managed rulesets block SQL injection, Cross-Site Scripting (XSS), and other injection attacks



### Access

Zero Trust access control for applications and infrastructure. [Learn more about Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

  * **Identity providers** \- Integrate with Okta, Azure AD, Google Workspace, and other identity providers (IdPs) to gate API access
  * **Service tokens** \- Issue long-lived credentials for machine-to-machine authentication between services



### Workers

Build and deploy serverless applications on Cloudflare's global network. [Learn more about Workers](https://developers.cloudflare.com/workers/).

  * **JWT validation** \- Verify and decode JSON Web Tokens (JWTs) at the edge before requests reach your backend
  * **Custom auth logic** \- Build any authentication scheme — API keys, Hash-based Message Authentication Code (HMAC) signatures, custom headers — directly at the edge



## Get started

  1. [API Shield get started](https://developers.cloudflare.com/api-shield/get-started/)
  2. [Configure rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/)
  3. [Set up mTLS authentication](https://developers.cloudflare.com/ssl/client-certificates/)
  4. [Configure applications with Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)
  5. [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)
  6. [Workers get started](https://developers.cloudflare.com/workers/get-started/)



[PreviousDeploy APIs at the edge](https://developers.cloudflare.com/use-cases/apis/deploy-apis/)[NextConnect your internal network services](https://developers.cloudflare.com/use-cases/apis/internal-services/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/apis/protect-apis.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
