---
url: https://developers.cloudflare.com/use-cases/application-security/
title: Application security \u00b7 Use cases \u00b7 Cloudflare use cases
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:09.564427+00:00
---

# Application security · Use cases · Cloudflare use cases

> Source: https://developers.cloudflare.com/use-cases/application-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Use cases](https://developers.cloudflare.com/use-cases/)
  3. /Application security



# Application security

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/use-cases/application-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArchitecture patterns Web application security API security Client-side defensePrerequisitesRelated resources

Protect your website or application from attacks, bots, and abuse. Cloudflare's application security (also known as Web Application Firewall or WAF) blocks SQL injection, XSS, and OWASP Top 10 vulnerabilities. DDoS Protection mitigates volumetric and application-layer attacks automatically. Bot Security uses machine learning to score every request. API Shield validates API traffic against your OpenAPI specification. Client-side security monitors third-party scripts for malicious behavior.

  * [Block application attacks](https://developers.cloudflare.com/use-cases/application-security/block-attacks/)
  * [Mitigate DDoS attacks](https://developers.cloudflare.com/use-cases/application-security/ddos/)
  * [Stop malicious bots](https://developers.cloudflare.com/use-cases/application-security/bots/)
  * [Protect against client-side threats](https://developers.cloudflare.com/use-cases/application-security/client-side/)
  * [Secure API endpoints](https://developers.cloudflare.com/use-cases/application-security/api-endpoints/)



## Architecture patterns

### Web application security

Protect a website or web application from common attacks:

  * **SSL/TLS** encrypts all traffic between visitors and Cloudflare
  * **Security rules** managed rulesets block SQL injection, XSS, and OWASP Top 10 vulnerabilities
  * **DDoS Protection** mitigates volumetric and application-layer attacks automatically
  * **Bot Security** scores every request and blocks automated threats



### API security

Secure Application Programming Interface (API) endpoints with schema enforcement and authentication:

  * **API Shield** validates requests against your OpenAPI specification
  * **Rate Limiting** prevents abuse with per-endpoint request limits
  * **mTLS** authenticates known clients with mutual TLS certificates



### Client-side defense

Protect visitors from threats that execute in the browser:

  * **Client-side security** monitors third-party scripts loading on your pages
  * **Turnstile** replaces CAPTCHAs on forms with a privacy-preserving challenge
  * **Content security rules** block requests from known malicious sources



* * *

## Prerequisites

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up).
  * A domain [added to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/). All solutions in this use case require your domain's DNS records to be proxied through Cloudflare so that traffic passes through Cloudflare's network before reaching your origin.



* * *

## Related resources

### [Security best practices](https://developers.cloudflare.com/learning-paths/application-security/)

Structured learning path for application security.

### [Security Analytics](https://developers.cloudflare.com/waf/analytics/)

Analyze security events and fine-tune your configuration.

### [Security case studies](https://www.cloudflare.com/case-studies/)

Explore how companies secure their applications with Cloudflare.

[PreviousStop account takeover](https://developers.cloudflare.com/use-cases/solutions/stop-account-takeover-attacks/)[NextBlock application attacks](https://developers.cloudflare.com/use-cases/application-security/block-attacks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/use-cases/application-security/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
