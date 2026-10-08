---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/traffic-types/
title: Traffic types \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:15.568514+00:00
---

# Traffic types · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/traffic-types/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

  4. /Packet filtering
  5. /Traffic types



# Traffic types

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/traffic-types/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Network Firewall enables you to allow or block traffic on a variety of packet characteristics, including:

  * **Source and destination IP** — the sender's and receiver's IP addresses
  * **Source and destination port** — the numeric port identifying the specific service (for example, port 80 for HTTP)
  * **Protocol** — the communication method, such as TCP or UDP
  * **Packet length** — the size of the packet in bytes
  * **Bit field match** — inspect individual flags within packet headers



Cloudflare Network Firewall operates at OSI layers 3 and 4 — the network layer (IP addressing and routing) and transport layer (port-based connections). It supports protocols such as TCP (reliable, ordered connections), UDP (fast, connectionless messages), and ICMP (network diagnostic messages like ping). You can write rules against any layer 3 or 4 protocol, not only TCP and UDP.

To see the full list of fields you can use when writing filter expressions, refer to [Cloudflare Network Firewall fields](https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/).

[PreviousRuleset logic](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/ruleset-logic/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/packet-filtering/traffic-types.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
