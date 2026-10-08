---
url: https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/magic-transit-egress/
title: Magic Transit egress \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:06.732440+00:00
---

# Magic Transit egress · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/magic-transit-egress/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /[Best practices](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/)
  4. /Magic Transit egress



# Magic Transit egress

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/magic-transit-egress/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The suggestions in the [Minimal ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/minimal-ruleset/) and [Extended ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/extended-ruleset/) are recommendations for ingress traffic.

For Magic Transit egress traffic, consider the following information:

  * The Cloudflare Network Firewall (formerly Magic Firewall) rules will apply to both Magic Transit ingress and egress traffic passing via Cloudflare.
  * Network Firewall is not stateful for your Magic Transit egress traffic.
  * Network Firewall is not stateful in both directions after DDoS mitigations.
  * If you have a Network Firewall "default drop" catchall rule for ingress traffic, you will need to add an earlier rule to permit traffic sourced from your Magic Transit prefix with the destination as **any** to allow outbound egress traffic.



[PreviousExtended ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/extended-ruleset/)[NextGraphQL Analytics](https://developers.cloudflare.com/cloudflare-network-firewall/tutorials/graphql-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/best-practices/magic-transit-egress.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
