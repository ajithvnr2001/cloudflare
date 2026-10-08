---
url: https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/
title: IPv6 CIDR routes for Cloudflare Mesh \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:51.504724+00:00
---

# IPv6 CIDR routes for Cloudflare Mesh · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 6, 2026

## IPv6 CIDR routes for Cloudflare Mesh

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-06-mesh-ipv6-routes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.

![IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2906,height=1352,format=webp/_astro/mesh-ipv6-routes.CC-jlZkw.png)

To add an IPv6 route, follow the same steps as [adding an IPv4 route](https://developers.cloudflare.com/mesh/features/routes/#add-a-route) — enter the IPv6 CIDR (for example, `fd00::/64`) when configuring the route in the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/mesh) or via the API.
