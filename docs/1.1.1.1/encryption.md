---
url: https://developers.cloudflare.com/1.1.1.1/encryption/
title: Encrypt DNS traffic \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.569271+00:00
---

# Encrypt DNS traffic · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/encryption/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /Encryption



# Encryption

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you visit a website, your device first sends a DNS query to translate the domain name (for example, `example.com`) into an IP address. Traditionally, these queries are sent in plaintext — unencrypted and readable by anyone on the network path.

Unencrypted DNS queries can be monitored, modified, or used for tracking by ISPs, network operators, or malicious actors.

To protect your DNS traffic, 1.1.1.1 supports three encryption standards:

  * [DNS over TLS (DoT)](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/) — Encrypts DNS queries over a dedicated TLS connection on port `853`.
  * [DNS over HTTPS (DoH)](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/) — Encrypts DNS queries inside regular HTTPS traffic on port `443`.
  * [Oblivious DNS over HTTPS (ODoH)](https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/) — Adds a privacy layer to DoH so that no single entity can see both your identity and your query.



You can also [configure your browser](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/) to secure your DNS queries.

To secure connections on your smartphone, refer to the 1.1.1.1 [iOS](https://developers.cloudflare.com/1.1.1.1/setup/ios/) or [Android](https://developers.cloudflare.com/1.1.1.1/setup/android/) apps.

[PreviousWindows](https://developers.cloudflare.com/1.1.1.1/setup/windows/)[NextDNS over TLS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/encryption/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
