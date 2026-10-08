---
url: https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/
title: New accounts assigned a single IPv4 anycast address \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:53.466285+00:00
---

# New accounts assigned a single IPv4 anycast address · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 12, 2026

## New accounts assigned a single IPv4 anycast address

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.

Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.

To request additional anycast IP addresses for your account, contact your account team.

For tunnel configuration guidance, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/) for Cloudflare WAN or [Configure tunnel endpoints](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/) for Magic Transit.
