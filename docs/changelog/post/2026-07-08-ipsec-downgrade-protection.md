---
url: https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/
title: IPsec downgrade protection (beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.301535+00:00
---

# IPsec downgrade protection (beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-08-ipsec-downgrade-protection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 8, 2026

## IPsec downgrade protection (beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare IPsec now supports the [`IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` ↗︎](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/) IKEv2 extension to protect against downgrade attacks on IPsec tunnels.

IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable [on-path attacker ↗︎](https://www.cloudflare.com/learning/security/threats/on-path-attack/) can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.

Key details:

  * Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.
  * Cloudflare sends the `IKE_SA_INIT_FULL_TRANSCRIPT_AUTH` notification unconditionally as a responder when the feature flag is enabled.
  * Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.
  * This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.



Refer to [Downgrade protection](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta) for more details.
