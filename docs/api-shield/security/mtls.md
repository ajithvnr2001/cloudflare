---
url: https://developers.cloudflare.com/api-shield/security/mtls/
title: Mutual TLS (mTLS) \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.967340+00:00
---

# Mutual TLS (mTLS) · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/mtls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /[Security](https://developers.cloudflare.com/api-shield/security/)
  4. /Mutual TLS (mTLS)



# Mutual TLS (mTLS)

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/mtls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupAvailabilityLimitations

Note

While API Shield is not required to use mTLS, many teams may use mTLS to protect their APIs.

[Mutual TLS (mTLS)](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/) authentication is a common security practice that uses client certificates to ensure traffic between client and server is bidirectionally secure and trusted. mTLS also allows requests that do not authenticate via an identity provider — such as Internet-of-things (IoT) devices — to demonstrate they can reach a given resource.

Use mTLS when you need to verify the identity of API clients, such as mobile applications, IoT devices, or services that connect to your API.

![mTLS sequence diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=900,height=1256,format=webp/_astro/api-shield-call-sequence.DjXyNgan.png)

mTLS also supports [gRPC ↗︎](https://grpc.io/docs/what-is-grpc/introduction/)-based APIs, which use binary formats such as protocol buffers rather than JSON.

## Setup

To set up mTLS for one or more hosts using the dashboard, refer to [Configure mTLS](https://developers.cloudflare.com/api-shield/security/mtls/configure/).

## Availability

All Cloudflare plans can set up mTLS with a Cloudflare-managed certificate authority (CA). Enterprise customers can [upload up to five non-Cloudflare CAs](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/). For higher limits, contact your account team.

## Limitations

When using Yubikeys, the browser may prompt for unlocking the key due to a problem in Yubikey's PKCS#11 library.

[PreviousEnhance Request Header Transform Rules](https://developers.cloudflare.com/api-shield/security/jwt-validation/transform-rules/)[NextConfigure mTLS](https://developers.cloudflare.com/api-shield/security/mtls/configure/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/mtls/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
