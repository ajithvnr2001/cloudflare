---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/
title: High availability replica management for Cloudflare Mesh \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.670473+00:00
---

# High availability replica management for Cloudflare Mesh · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-mesh-ha-replica-ui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## High availability replica management for Cloudflare Mesh

[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) dashboard now shows per-replica details for [high availability](https://developers.cloudflare.com/mesh/features/high-availability/) nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.

![Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1155,format=webp/_astro/mesh-ha-replicas.Dvf1GMmQ.gif)

#### What's new

  * **Replica tabs** on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.
  * **Active/passive badges** identify which replica is currently routing traffic.
  * **Manual failover** — promote a passive replica to active with a single click. The previous active replica switches to standby.
  * **HA badge** in the overview table identifies nodes running multiple replicas.
  * **Active replica IP** shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.



#### Manual failover

To manually promote a passive replica:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/mesh), go to **Networking** > **Mesh**.
  2. Select an HA-enabled node.
  3. Select the passive replica tab.
  4. Select **Promote to active** and confirm.



Traffic reroutes to the promoted replica immediately. Refer to [High availability](https://developers.cloudflare.com/mesh/features/high-availability/) for details on failover behavior.
