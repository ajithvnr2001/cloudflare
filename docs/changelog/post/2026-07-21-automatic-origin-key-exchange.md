---
url: https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/
title: Faster and more secure TLS handshakes to your origins, automatically \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.537506+00:00
---

# Faster and more secure TLS handshakes to your origins, automatically · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-21-automatic-origin-key-exchange/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 21, 2026

## Faster and more secure TLS handshakes to your origins, automatically

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first `ClientHello`, helping avoid a `HelloRetryRequest` and one extra network round trip.

Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum `X25519MLKEM768` hybrid key agreement.

To change this behavior, go to **SSL/TLS** > **Overview** > **Origin connection & post-quantum encryption**. Turn off **Automatic key exchange** to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.

**Compliance requirements** apply only to TLS 1.3 connections. The **Post-quantum hybrid** option requires hybrid post-quantum key agreements support on your origin server. The **Federal Information Processing Standards (FIPS)** option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.

For requirements, configuration options, and rollout details, refer to [Automatic key exchange to origins](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/).
