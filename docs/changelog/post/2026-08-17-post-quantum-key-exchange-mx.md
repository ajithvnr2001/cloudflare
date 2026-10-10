---
url: https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/
title: Post-quantum key exchange for MX deployments \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.802614+00:00
---

# Post-quantum key exchange for MX deployments · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-17-post-quantum-key-exchange-mx/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 17, 2026

## Post-quantum key exchange for MX deployments

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.

Inbound MX connections and outbound delivery connections now negotiate the [X25519MLKEM768](https://developers.cloudflare.com/ssl/post-quantum-cryptography/#hybrid-key-agreement) hybrid key agreement when the peer supports it, protecting SMTP traffic against [harvest-now, decrypt-later ↗︎](https://blog.cloudflare.com/pq-2024/) attacks.

Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.

This applies to all Email Security packages:

  * **Advantage**
  * **Enterprise**
  * **Enterprise + PhishGuard**


