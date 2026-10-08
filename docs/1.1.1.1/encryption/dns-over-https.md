---
url: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/
title: DNS over HTTPS \u00b7 Cloudflare 1.1.1.1 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:03.327531+00:00
---

# DNS over HTTPS · Cloudflare 1.1.1.1 docs

> Source: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/

  1. [Home](https://developers.cloudflare.com/)
  2. /[1.1.1.1 (DNS Resolver)](https://developers.cloudflare.com/1.1.1.1/)
  3. /[Encryption](https://developers.cloudflare.com/1.1.1.1/encryption/)
  4. /DNS over HTTPS



# DNS over HTTPS

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS over HTTPS (DoH) encrypts DNS queries by wrapping them inside regular HTTPS requests. This prevents attackers from forging or altering your DNS traffic.

DoH sends DNS traffic over port `443` — the default port for HTTPS web traffic. Because DoH queries use the same port and protocol as normal web browsing, they are difficult to distinguish from other HTTPS traffic on the network.

DoH supports the HTTP, HTTP/2, and HTTP/3 protocols.

  * [Make API requests to 1.1.1.1](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/)
  * [Configure DoH on your browser](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/encrypted-dns-browsers/)
  * [Connect to 1.1.1.1 using DoH clients](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/)



[PreviousDNS over TLS](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-tls/)[NextOverview](https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/make-api-requests/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/1.1.1.1/encryption/dns-over-https/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
