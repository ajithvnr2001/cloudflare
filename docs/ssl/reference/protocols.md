---
url: https://developers.cloudflare.com/ssl/reference/protocols/
title: TLS protocols \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:45.567154+00:00
---

# TLS protocols · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/reference/protocols/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /Reference
  4. /TLS protocols



# TLS protocols

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/reference/protocols/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUnderstand TLS versionsDecide which version to useRelated resources

Cloudflare supports the following TLS protocols:

  * TLS 1.0
  * TLS 1.1
  * TLS 1.2
  * TLS 1.3



TLS 1.0 is the [version that Cloudflare sets by default](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/) for all customers using certificate-based encryption.

For information about which cipher suites are supported between clients and the Cloudflare network, refer to [Cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/).

## Understand TLS versions

A higher TLS version implies a stronger cryptographic standard. TLS 1.2 includes fixes for known vulnerabilities found in previous versions.

As of June 2018, TLS 1.2 is the version required by the Payment Card Industry (PCI) Security Standards Council. Cloudflare recommends migrating to TLS 1.2 to comply with the PCI requirement.

[TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/), which offers additional security and performance improvements, was approved by the Internet Engineering Task Force (IETF) in May 2018.

PayPal's TLS 1.2 requirement

Using Cloudflare does not affect PayPal's TLS 1.2 requirement. However, note that PayPal IPN (Instant Payment Notification) might not support [TLS version 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/). If you are encountering issues with PayPal IPN when the traffic is proxied by Cloudflare, try setting the [Minimum TLS version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/) to 1.2.

## Decide which version to use

TLS 1.3 has become widely adopted. As a general rule, Cloudflare recommends setting TLS to 1.3, as it will provide the best security.

However, not all browser versions support TLS 1.2 and above. Depending on your particular business situation, this may present some limitations in using stronger encryption standards:

  * Consider using TLS 1.0 or 1.1 for sites with a broad user base, particularly non-transactional sites. In this way, you minimize the possibility that some clients cannot connect to your site securely.

  * For a narrow user base and sites that run internal applications or business and productivity applications, Cloudflare recommends TLS 1.2. These sites might already have more stringent security requirements or might be subject to [PCI compliance](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/). You also need to ensure that your users upgrade to a TLS 1.2 compliant browser.




## Related resources

  * [PCI compliance and vulnerabilities mitigation](https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/)
  * [Transport Layer Security ↗︎](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)
  * [PCI Security Standards Council ↗︎](https://www.pcisecuritystandards.org/)



[PreviousPQC and Cloudflare One](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-and-zero-trust/)[NextCertificate and hostname priority](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/reference/protocols.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
