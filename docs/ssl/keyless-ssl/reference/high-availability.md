---
url: https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/
title: High availability \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:42.647677+00:00
---

# High availability · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/)

  4. /Reference
  5. /High availability



# High availability

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Keyless SSL server runs as a single binary with minimal dependencies and is designed to be robust and reliable. However, the network between your key server and Cloudflare may not be, which could prevent new TLS connections.

For this reason, we strongly recommend that you run at least two key servers in a high availability configuration behind a load balancer. Set up health checks for each key server on the configured TCP port—2407 by default and failover as necessary or round-robin between active (healthy) key servers.

From a network availability and performance perspective, advertise the IP address of your key server from multiple data centers (an anycast setup) so the Cloudflare global network can route to the closest key server via BGP. When you use anycast routing, you can also safely take a data center offline to perform maintenance.

[PreviousUpgrade your key server](https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/)[NextScaling and benchmarking](https://developers.cloudflare.com/ssl/keyless-ssl/reference/scaling-and-benchmarking/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/keyless-ssl/reference/high-availability.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
