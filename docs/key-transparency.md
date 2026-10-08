---
url: https://developers.cloudflare.com/key-transparency/
title: Overview \u00b7 Cloudflare Key Transparency Auditor docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.258797+00:00
---

# Overview · Cloudflare Key Transparency Auditor docs

> Source: https://developers.cloudflare.com/key-transparency/

  1. [Home](https://developers.cloudflare.com/)
  2. /Key Transparency Auditor



# Key Transparency Auditor

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/key-transparency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRelated products

Secure the distribution of public keys in your end-to-end encrypted (E2EE) messaging systems

Cloudflare's Key Transparency Auditor aims to secure the distribution of public keys for end-to-end encrypted (E2EE) messaging systems like [WhatsApp ↗︎](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/). It achieves this by building a verifiable append-only data structure called a Log, similar to [Certificate Transparency ↗︎](https://developer.mozilla.org/en-US/docs/Web/Security/Certificate_Transparency).

Cloudflare acts as an auditor of Key Transparency Logs to ensure the transparency of end-to-end encrypted messaging public keys. Cloudflare provides an API for anyone to monitor the verification work we perform, and verify the state of its associated Logs locally.

## Related products

[Certificate Transparency Monitoring](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/)

Certificate Transparency (CT) Monitoring is an opt-in feature in public beta that aims to improve security by allowing you to double-check any SSL/TLS certificates issued for your domain.

[Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/)

Cloudflare OHTTP Relay (formerly Privacy Gateway) is a managed service deployed on Cloudflare's global network that implements part of the [Oblivious HTTP (OHTTP) IETF ↗︎](https://www.ietf.org/archive/id/draft-thomson-http-oblivious-01.html) standard. The goal of Cloudflare OHTTP Relay and Oblivious HTTP is to hide the client's IP address when interacting with an application backend.

[NextAuditor](https://developers.cloudflare.com/key-transparency/api/auditor-information/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/key-transparency/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
