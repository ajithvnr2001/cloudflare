---
url: https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/
title: Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.366373+00:00
---

# Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-20-tunnel-core-dashboard/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 20, 2026

## Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) is now available in the main Cloudflare Dashboard at [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels), bringing first-class Tunnel management to developers using Tunnel for securing origin servers.

![Manage Tunnels in the Core Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=894,format=webp/_astro/tunnel-core-dashboard.BGPqaHfo.gif)

This new experience provides everything you need to manage Tunnels for [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), including:

  * **Full Tunnel lifecycle management** : Create, configure, delete, and monitor all your Tunnels in one place.
  * **Native integrations** : View Tunnels by name when configuring [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) and [Workers VPC](https://developers.cloudflare.com/workers-vpc/) — no more copy-pasting UUIDs.
  * **Real-time visibility** : Monitor [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) and Tunnel [health status](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status) directly in the dashboard.
  * **Routing map** : Manage all ingress routes for your Tunnel, including [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/), [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/), [private CIDRs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/), and [Workers VPC services](https://developers.cloudflare.com/workers-vpc/), from a single interactive interface.



#### Choose the right dashboard for your use case

**Core Dashboard** : Navigate to [Networking > Tunnels ↗︎](https://dash.cloudflare.com/?to=/:account/tunnels) to manage Tunnels for:

  * Securing origin servers and [public applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) with CDN, WAF, Load Balancing, and DDoS protection
  * Connecting [Workers to private services](https://developers.cloudflare.com/workers-vpc/) via Workers VPC



**Cloudflare One Dashboard** : Navigate to [Zero Trust > Networks > Connectors ↗︎](https://one.dash.cloudflare.com/?to=/:account/networks/connectors) to manage Tunnels for:

  * Securing your public applications with [Zero Trust access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)
  * Connecting users to [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/)
  * Building a [private mesh network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks)



Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.

#### Get started

New to Tunnel? Learn how to [get started with Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) or explore advanced use cases like [securing SSH servers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/) or [running Tunnels in Kubernetes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/).
