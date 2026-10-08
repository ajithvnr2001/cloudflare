---
url: https://developers.cloudflare.com/durable-objects/reference/data-security/
title: Data security \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:09.895115+00:00
---

# Data security · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/reference/data-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Reference
  4. /Data security



# Data security

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/reference/data-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEncryption at RestEncryption in TransitCompliance

This page details the data security properties of Durable Objects, including:

  * Encryption-at-rest (EAR).
  * Encryption-in-transit (EIT).
  * Cloudflare's compliance certifications.



## Encryption at Rest

All Durable Object data, including metadata, is encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of Durable Objects.

Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.

Encryption at rest is implemented using the Linux Unified Key Setup (LUKS) disk encryption specification and [AES-256 ↗︎](https://www.cloudflare.com/learning/ssl/what-is-encryption/), a widely tested, highly performant and industry-standard encryption algorithm.

## Encryption in Transit

Data transfer between a Cloudflare Worker, and/or between nodes within the Cloudflare network and Durable Objects is secured using the same [Transport Layer Security ↗︎](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (TLS/SSL).

API access via the HTTP API or using the [wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) command-line interface is also over TLS/SSL (HTTPS).

## Compliance

To learn more about Cloudflare's adherence to industry-standard security compliance certifications, visit the Cloudflare [Trust Hub ↗︎](https://www.cloudflare.com/trust-hub/compliance-resources/).

[PreviousDurable Object class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/)[NextData location](https://developers.cloudflare.com/durable-objects/reference/data-location/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/reference/data-security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
