---
url: https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/
title: UDP and ICMP Monitor Support for Private Load Balancing Endpoints \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:11.183307+00:00
---

# UDP and ICMP Monitor Support for Private Load Balancing Endpoints · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 6, 2025

## UDP and ICMP Monitor Support for Private Load Balancing Endpoints

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing now supports **UDP (Layer 4)** and **ICMP (Layer 3)** health monitors for **private endpoints**. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.

#### What you can do:

  * Set up **ICMP ping monitors** to check if your private endpoints are reachable.
  * Use **UDP monitors** for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.
  * Gain better visibility and uptime guarantees for services running behind **Private Network Load Balancing** , without requiring public IP addresses.



This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with [**Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [**WARP**](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), and [**Magic WAN**](https://developers.cloudflare.com/cloudflare-wan/) to create a secure and observable private network.

Learn more about [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) or view the full list of [supported health monitor protocols](https://developers.cloudflare.com/load-balancing/monitors/#supported-protocols).
