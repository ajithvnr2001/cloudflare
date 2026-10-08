---
url: https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/
title: Hostname routing for Cloudflare Mesh \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.026077+00:00
---

# Hostname routing for Cloudflare Mesh · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 2, 2026

## Hostname routing for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now add [hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes) to a Cloudflare Mesh node, in addition to CIDR routes.

  1. [Client device](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Requests `wiki.internal.local`

  2. DNS query↓
  3. [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Returns a token IP, then rewrites the destination to the real private IP.

`172.64.128.0/20`

  4. [Hostname route](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes)↓
  5. [Mesh node](https://developers.cloudflare.com/mesh/)

Forwards traffic to the host on the local network

  6. ↓
  7. Private host

`wiki.internal.local` · `10.0.0.50`




Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:

  * **Private hostname** (for example, `wiki.internal.local`) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.
  * **Public hostname** (for example, `www.example.com`) — route that hostname's traffic through the node and egress via the node's public IP.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)

For setup steps, prerequisites, and DNS options, refer to [Hostname routes](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).
