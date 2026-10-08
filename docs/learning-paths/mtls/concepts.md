---
url: https://developers.cloudflare.com/learning-paths/mtls/concepts/
title: Introducing mTLS \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:50.951052+00:00
---

# Introducing mTLS · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/mtls/concepts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Mtls
  4. /Introducing mTLS



# Introducing mTLS

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/mtls/concepts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Mutual TLS (mTLS)](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/) authentication is a common security practice that uses client certificates to ensure traffic between client and server is bidirectionally secure and trusted. mTLS also allows requests that do not authenticate via an identity provider — such as Internet-of-things (IoT) devices — to demonstrate they can reach a given resource.

[TLS (Transport Layer Security) ↗︎](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) is a widely-used protocol to ensure secure communication over a network. It ensures confidentiality and integrity by encrypting data and validating the server using digital certificates.

Mutual TLS (mTLS) adds an extra layer by authenticating both parties involved in the communication. The client presents a certificate to the server (in this case Cloudflare) and vice versa.

[NextBenefits of mTLS](https://developers.cloudflare.com/learning-paths/mtls/concepts/benefits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/mtls/concepts/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
