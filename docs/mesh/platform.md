---
url: https://developers.cloudflare.com/mesh/platform/
title: Platform \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:21.810061+00:00
---

# Platform · Cloudflare Docs

> Source: https://developers.cloudflare.com/mesh/platform/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)
  3. /Platform



# Platform

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/mesh/platform/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlatform requirements

Cloudflare Mesh is available in beta to Cloudflare One accounts, including accounts on the Free plan.

## Platform requirements

  * Mesh nodes require a [supported Linux distribution](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#linux) or the [`cloudflare/mesh` container image](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/).
  * Client devices can use any [operating system supported by the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).
  * Mesh nodes must use the MASQUE device tunnel protocol. Hostname routes, IPv6 CIDR routes, and high availability do not work with WireGuard.
  * Using Cloudflare Mesh with Cloudflare WAN requires [Unified Routing mode](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing).



For deployment recommendations and interoperability constraints, refer to [Best practices](https://developers.cloudflare.com/mesh/best-practices/).

[PreviousBest practices](https://developers.cloudflare.com/mesh/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/mesh/platform/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
