---
url: https://developers.cloudflare.com/kv/reference/data-security/
title: Data security \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:41.828380+00:00
---

# Data security · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/reference/data-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Reference
  4. /Data security



# Data security

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/kv/reference/data-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEncryption at RestEncryption in TransitCompliance

This page details the data security properties of KV, including:

  * Encryption-at-rest (EAR).
  * Encryption-in-transit (EIT).
  * Cloudflare's compliance certifications.



## Encryption at Rest

All values stored in KV are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of KV.

Values are only decrypted by the process executing your Worker code or responding to your API requests.

Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.

Objects are encrypted using [AES-256 ↗︎](https://www.cloudflare.com/learning/ssl/what-is-encryption/), a widely tested, highly performant and industry-standard encryption algorithm. KV uses GCM (Galois/Counter Mode) as its preferred mode.

## Encryption in Transit

Data transfer between a Cloudflare Worker, and/or between nodes within the Cloudflare network and KV is secured using the same [Transport Layer Security ↗︎](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (TLS/SSL).

API access via the HTTP API or using the [wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) command-line interface is also over TLS/SSL (HTTPS).

## Compliance

To learn more about Cloudflare's adherence to industry-standard security compliance certifications, refer to Cloudflare's [Trust Hub ↗︎](https://www.cloudflare.com/trust-hub/compliance-resources/).

[PreviousData location](https://developers.cloudflare.com/kv/reference/data-location/)[NextFAQ](https://developers.cloudflare.com/kv/reference/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/reference/data-security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
