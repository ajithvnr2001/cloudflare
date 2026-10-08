---
url: https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/
title: Faster, more reliable UDP traffic for Cloudflare Tunnel \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:16.867534+00:00
---

# Faster, more reliable UDP traffic for Cloudflare Tunnel · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 15, 2025

## Faster, more reliable UDP traffic for Cloudflare Tunnel

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Your real-time applications running over [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) are now faster and more reliable. We've completely re-architected the way `cloudflared` proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.

This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.

**What’s new:**

  * **Faster UDP performance** : We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.
  * **Greater reliability for mixed traffic** : UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.



Learn more about running [TCP or UDP applications](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-applications) and [private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/) through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).
