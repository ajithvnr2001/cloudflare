---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/security/
title: Enable security filters \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:39.924297+00:00
---

# Enable security filters · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors

  4. /[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)
  5. /Security filters



# Security filters

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Once your traffic flows through Cloudflare's network, you can apply security policies to it without deploying additional hardware. Cloudflare WAN (formerly Magic WAN) integrates with two primary security services, each operating at different layers of the network stack.

**[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)** filters traffic at layers 3 and 4 of the [OSI model ↗︎](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) — the network and transport layers. You can allow or block traffic based on packet characteristics such as source and destination IP addresses, ports, protocols, and packet length. All Cloudflare WAN customers have [automatic access to Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/plans/).

**[Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/cloudflare-gateway/)** inspects traffic at higher layers, including DNS queries, network sessions, and HTTP requests. Use Gateway to set up policies that control Internet-bound traffic and access to your private network infrastructure. Refer to [Connect to Cloudflare Gateway with Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/cloudflare-gateway/) to learn how to filter Cloudflare WAN traffic with Gateway policies.

[PreviousCustom IKE ID for IPsec](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
