---
url: https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/
title: Verify WARP Connector connectivity with a simple ping \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:33.857053+00:00
---

# Verify WARP Connector connectivity with a simple ping · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 15, 2026

## Verify WARP Connector connectivity with a simple ping

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have made it easier to validate connectivity when deploying [WARP Connector](https://developers.cloudflare.com/mesh/) as part of your [software-defined private network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks).

You can now `ping` the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.

Starting with [version 2025.10.186.0](https://developers.cloudflare.com/changelog/2026-01-13-warp-linux-ga/), WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.

Learn more about deploying [WARP Connector](https://developers.cloudflare.com/mesh/) and building private network connectivity with [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).
