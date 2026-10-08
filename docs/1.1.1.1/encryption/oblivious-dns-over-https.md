---
url: https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/
title: Oblivious DNS over HTTPS \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.644925+00:00
---

# Oblivious DNS over HTTPS · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Encryption](https://developers.cloudflare.com/1.1.1.1/encryption/)
  4. /Oblivious DoH



# Oblivious DNS over HTTPS

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow ODoH worksCloudflare and third-party productsRelated resources

With standard [DNS over HTTPS (DoH)](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/), your DNS queries are encrypted, but the resolver still sees both your IP address and the domain you are looking up. Oblivious DNS over HTTPS (ODoH) adds a privacy layer so that no single entity can see both pieces of information at the same time.

Caution

ODoH is defined in [RFC 9230 ↗︎](https://www.rfc-editor.org/rfc/rfc9230.html). This RFC is experimental and is not endorsed by the IETF.

## How ODoH works

ODoH introduces two roles between your device and the DNS resolver:

  * **Proxy** — Forwards your encrypted DNS query to the target. The proxy can see your IP address but cannot read the query because it is encrypted.
  * **Target** — Receives and decrypts the DNS query, then sends it to the upstream resolver. The target can read the query but only sees the proxy's IP address, not yours.



Because the query is encrypted before it reaches the proxy, and the target never learns your IP address:

  * The proxy has no visibility into the DNS messages, with no ability to identify, read, or modify either the query being sent by the client or the answer being returned by the target.
  * The target only has access to the encrypted query and the proxy's IP address, while not having visibility over the client's IP address.
  * Only the intended target can read the content of the query and produce a response, which is also encrypted.



This means that, as long as the proxy and the target do not collude, no single entity can have access to both the DNS messages and the client IP address at the same time. Clients are in complete control of proxy and target selection, so you can choose a proxy and target operated by different organizations to reduce collusion risk.

Clients encrypt their query for the target using Hybrid Public Key Encryption ([HPKE ↗︎](https://blog.cloudflare.com/hybrid-public-key-encryption/)), a standard for encrypting messages to a recipient using their public key. A target's public key is obtained via DNS, where it is bundled into an HTTPS resource record and protected by DNSSEC.

## Cloudflare and third-party products

Cloudflare 1.1.1.1 supports ODoH by acting as a target that can be reached at `odoh.cloudflare-dns.com`.

To make ODoH queries you can use open source clients such as [dnscrypt-proxy ↗︎](https://github.com/DNSCrypt/dnscrypt-proxy).

[iCloud Private Relay ↗︎](https://support.apple.com/102602) uses similar privacy-separation principles and uses [Cloudflare as one of their partners ↗︎](https://blog.cloudflare.com/icloud-private-relay/).

## Related resources

  * [HPKE: Standardizing public-key encryption ↗︎](https://blog.cloudflare.com/hybrid-public-key-encryption/) blog post
  * [Cloudflare OHTTP Relay (formerly Privacy Gateway)](https://developers.cloudflare.com/ohttp-relay/)



[PreviousConnect to 1.1.1.1 using DoH clients](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/)[NextDNSKEY](https://developers.cloudflare.com/1.1.1.1/encryption/dnskey/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/encryption/oblivious-dns-over-https.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
