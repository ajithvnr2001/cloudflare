---
url: https://developers.cloudflare.com/changelog/post/2026-06-17-pqc-mldsa-aop-cots/
title: Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.465314+00:00
---

# Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-17-pqc-mldsa-aop-cots/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 17, 2026

## Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-17-pqc-mldsa-aop-cots/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now accepts [ML-DSA ↗︎](https://csrc.nist.gov/pubs/fips/204/final) (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.

ML-DSA is supported in two origin-facing features:

  * [Authenticated Origin Pulls](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/) (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.
  * [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/) (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under [Full (strict) encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/).



Refer to [Post-quantum signatures](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures) for certificate generation and setup guidance, and to [PQC in Cloudflare products](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-cloudflare-products/) for the current post-quantum deployment status across Cloudflare.
