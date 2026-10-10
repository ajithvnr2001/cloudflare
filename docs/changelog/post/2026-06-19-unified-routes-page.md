---
url: https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/
title: Manage all your routes from one page in the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.199282+00:00
---

# Manage all your routes from one page in the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-19-unified-routes-page/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 19, 2026

## Manage all your routes from one page in the dashboard

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **Routes** page in the Cloudflare dashboard now shows the routes across all of your connectors — [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) and [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) routes alongside [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) and [Magic Transit](https://developers.cloudflare.com/magic-transit/) static routes — in a single table, instead of a separate routes view per product.

![The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/2026-06-19-unified-routes.B3igBY20.gif)

From the unified Routes page you can:

  * **Visualize your network with an interactive map** that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.
  * **See every route in one table** , with its destination, type, connector, priority, and source, and filter or sort to find what you need.
  * **Create, edit, and delete routes** of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by **connector name** instead of typing its IP.
  * **Manage[virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/)** from a dedicated tab.
  * **Test a route** to see which connector and next hop a destination resolves to before you commit a change.



To find it, go to **Networking** > **Routes** in the dashboard sidebar.

[ Go to **Routes** ↗ ](https://dash.cloudflare.com/?to=/:account/magic-networks/routes)

Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to [add routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) and [manage virtual networks](https://developers.cloudflare.com/cloudflare-one/networks/virtual-networks/).
