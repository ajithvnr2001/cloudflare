---
url: https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/
title: DNS filtering for private network onramps \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:22.553496+00:00
---

# DNS filtering for private network onramps · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 11, 2025

## DNS filtering for private network onramps

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Magic WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering) and [WARP Connector](https://developers.cloudflare.com/mesh/features/routes/#dns-filtering) users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.

Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including [Internal DNS](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/#internal-dns) and [hostname-based policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites).

To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, `172.64.36.1` and `172.64.36.2`. Once you configure DNS resolution and filtering, you can use _Source Internal IP_ as a traffic selector in your [resolver policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/resolver-policies/) for routing private DNS traffic to your [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/).
