---
url: https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/
title: Post-quantum encryption support for Cloudflare One Appliance \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:44.020627+00:00
---

# Post-quantum encryption support for Cloudflare One Appliance · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 11, 2026

## Post-quantum encryption support for Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One Appliance version 2026.2.0 adds [post-quantum encryption](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).

The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.

This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.

For more information, refer to [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/).
