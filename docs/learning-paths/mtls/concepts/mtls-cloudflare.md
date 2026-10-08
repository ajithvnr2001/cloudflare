---
url: https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/
title: Use mTLS with Cloudflare protected resources \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.974753+00:00
---

# Use mTLS with Cloudflare protected resources · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Mtls

  4. /[Introducing mTLS](https://developers.cloudflare.com/learning-paths/mtls/concepts/)
  5. /mTLS with Cloudflare



# Use mTLS with Cloudflare protected resources

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/mtls/concepts/mtls-cloudflare/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In this implementation guide we will be focusing on the L7 / Application Layer security for HTTP/S requests targeting [proxied](https://developers.cloudflare.com/dns/proxy-status/) hostnames, including the [first connection](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/) between client and Cloudflare.

Some common mTLS use cases are:

  * Protect and verify legitimate API traffic by verifying Client Certificates provided during TLS/SSL handshakes.
  * Check IoT devices' identity by verifying Client Certificates they provide during TLS/SSL handshakes.



There are two main ways to use mTLS at Cloudflare, either by using the Application Security offering (optionally including [API Shield](https://developers.cloudflare.com/api-shield/)) or [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). Below is a non-exhaustive overview table of their differences:

Feature | Application Security (Client Certificate + WAF) | Cloudflare Access (mTLS)  
---|---|---  
Mainly used for | External Authentication (that is, APIs) | Internal Authentication (that is, employees)  
Availability | By default, 100 Client Certificates per Zone are included for free. For more certificates or [API Shield features](https://developers.cloudflare.com/api-shield/), contact your account team. | Zero Trust Enterprise only feature.  
[Certificate Authority (CA)](https://developers.cloudflare.com/ssl/concepts/#certificate-authority-ca) | Cloudflare-managed or customer-uploaded (BYO CA). There's a soft-limit of up to [five customer-uploaded CAs](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/#availability). | Customer-uploaded only (BYO CA). There's a soft-limit of up to [50 CAs](https://developers.cloudflare.com/cloudflare-one/account-limits/#access).  
Client Certificate Details | Forwarded to the origin server via [Cloudflare API](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/#cloudflare-api), [Cloudflare Workers](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/#cloudflare-workers), and [Managed Transforms](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/#managed-transforms). | Forwarded to the origin server via [Cloudflare API](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-api), [Cloudflare Workers](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-workers), and [Managed Transforms](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#managed-transforms). Client Certificate headers and [Cf-Access-Jwt-Assertion](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/) JWT header can be forwarded to the origin server.  
Client Certificates Revocation | Use the WAF [Custom Rules](https://developers.cloudflare.com/waf/custom-rules/) to check for [_cf.tls_client_auth.cert_revoked_](https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/), which only applies to Cloudflare-managed CA.   
  
For BYO CAs, it would be the same approach as with Cloudflare Access. | Generate a [Certificate Revocation List (CRL)](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#create-a-crl) and enforce the revocation in a Cloudflare Worker.  
  
[PreviousBenefits of mTLS](https://developers.cloudflare.com/learning-paths/mtls/concepts/benefits/)[NextOverview](https://developers.cloudflare.com/learning-paths/mtls/mtls-app-security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/mtls/concepts/mtls-cloudflare.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
