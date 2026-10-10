---
url: https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/
title: Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.713430+00:00
---

# Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 2, 2026

## Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create multiple [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) routes from the Routes page in a single action, instead of submitting one route at a time.

![Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1034,format=webp/_astro/2026-09-01-tunnel-mesh-bulk.zu4fOWN3.gif)

When creating a route, you can now:

  * **Add multiple destinations at once** — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.
  * **Queue up multiple routes** — Select **Add another** to stage additional routes, including different types or connectors, before creating them all in one action.
  * **Retry only what failed** — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.



The same Routes UI already supports bulk creation for [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

For setup steps, refer to [Add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/).
