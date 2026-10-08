---
url: https://developers.cloudflare.com/r2/reference/data-security/
title: Data security \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:48.541645+00:00
---

# Data security · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/reference/data-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Reference
  4. /Data security



# Data security

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/reference/data-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEncryption at RestEncryption in TransitCompliance

This page details the data security properties of R2, including encryption-at-rest (EAR), encryption-in-transit (EIT), and Cloudflare's compliance certifications.

## Encryption at Rest

All objects stored in R2, including their metadata, are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of R2.

Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.

Objects are encrypted using [AES-256 ↗︎](https://www.cloudflare.com/learning/ssl/what-is-encryption/), a widely tested, highly performant and industry-standard encryption algorithm. R2 uses GCM (Galois/Counter Mode) as its preferred mode.

## Encryption in Transit

Data transfer between a client and R2 is secured using the same [Transport Layer Security ↗︎](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (TLS/SSL) supported on all Cloudflare domains.

Access over plaintext HTTP (without TLS/SSL) can be disabled by connecting a [custom domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#custom-domains) to your R2 bucket and enabling [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/).

Note

R2 custom domains use Cloudflare for SaaS certificates and cannot be customized. Even if you have [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/), the advanced certificate will not be used due to [certificate prioritization](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/).

## Compliance

To learn more about Cloudflare's adherence to industry-standard security compliance certifications, visit the Cloudflare [Trust Hub ↗︎](https://www.cloudflare.com/trust-hub/compliance-resources/).

[PreviousData location](https://developers.cloudflare.com/r2/reference/data-location/)[NextDurability](https://developers.cloudflare.com/r2/reference/durability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/reference/data-security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
