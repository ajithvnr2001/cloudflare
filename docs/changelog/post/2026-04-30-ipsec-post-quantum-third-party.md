---
url: https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/
title: Post-quantum IPsec interoperability with third-party devices \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:50.770313+00:00
---

# Post-quantum IPsec interoperability with third-party devices · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 30, 2026

## Post-quantum IPsec interoperability with third-party devices

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-30-ipsec-post-quantum-third-party/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. [Cisco ↗︎](https://www.cisco.com/) and [Fortinet ↗︎](https://www.fortinet.com/) are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

Post-quantum IPsec uses [RFC 9370 ↗︎](https://datatracker.ietf.org/doc/rfc9370/) and [draft-ietf-ipsecme-ikev2-mlkem ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) to negotiate hybrid key agreement during the IKEv2 `IKE_INTERMEDIATE` phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against [harvest-now, decrypt-later ↗︎](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) attacks.

Key details:

  * Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.
  * Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.
  * Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.
  * No additional licensing required.



Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.

For supported key exchange methods and the list of validated platforms, refer to [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability).
