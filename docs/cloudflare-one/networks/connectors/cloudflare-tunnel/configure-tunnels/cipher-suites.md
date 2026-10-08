---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/
title: Cipher suites \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:10.982009+00:00
---

# Cipher suites · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Configure a tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/)
  5. /Cipher suites



# Cipher suites

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Tunnel connections use the cipher suites supported by `cloudflared`, which relies on the Go TLS library for its TLS implementation. These cipher suites apply to both the TLS connection between Cloudflare's network and `cloudflared`, and the HTTPS connection between `cloudflared` and your origin. In both cases, `cloudflared` negotiates the most secure cipher suite supported by both sides. All tunnel connections use TLS 1.3 and post-quantum encryption by default.

The following table lists the cipher suites supported by `cloudflared`:

Protocol support | Cipher suites  
---|---  
TLS 1.3 only | `TLS_AES_128_GCM_SHA256`  
`TLS_AES_256_GCM_SHA384`  
`TLS_CHACHA20_POLY1305_SHA256`  
TLS 1.2 only | `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`  
`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`  
`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`  
`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`  
`TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`  
`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`  
Up to and including TLS 1.2 | `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`  
`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`  
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`  
`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`  
  
[PreviousTunnel permissions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/remote-tunnel-permissions/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
