---
url: https://developers.cloudflare.com/byoip/concepts/irr-entries/
title: IRR Overview \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.766966+00:00
---

# IRR Overview · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/concepts/irr-entries/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Concepts
  4. /Internet Routing Registry



# Internet Routing Registry (IRR)

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/concepts/irr-entries/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Internet Routing Registry (IRR)](http://www.irr.net/index.html) is a globally distributed database of routing information which contains announced routes and routing policies in a common format. Network operators use this information, as well as [RPKI](https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/), to configure backbone routers.

IRR entries serve as a public record of which networks are authorized to announce specific IP prefixes. When Cloudflare advertises your IP prefixes on your behalf, other networks check IRR records to verify that Cloudflare has permission to do so. Without accurate IRR entries, your traffic may not be properly routed on the Internet.

The IRR consists of many individual [routing registries ↗︎](http://www.irr.net/docs/list.html), some managed by regional entities such as the American Registry for Internet Numbers (ARIN) and the Regional Internet Registry for Europe, Middle East and Central Asia (RIPE). Each routing registry contains IRR entries that provide information about IP prefixes and the [autonomous systems ↗︎](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) authorized to announce them.

To announce your IP prefixes through Cloudflare, you must have accurate IRR entries for your prefixes and autonomous system numbers (ASNs).

When you configure network infrastructure for services such as [Magic Transit](https://developers.cloudflare.com/magic-transit/about/), or before onboarding your IPs to Cloudflare, [verify your IRR entries](https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/#verify-an-irr-entry).

[PreviousBest practices](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/)[NextManage IRR entries](https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/concepts/irr-entries/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
