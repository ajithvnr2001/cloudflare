---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/magic-transit-egress/
title: Magic Transit egress \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:14.315637+00:00
---

# Magic Transit egress · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/magic-transit-egress/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)Packet filtering

  4. /[Best practices](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/)
  5. /Magic Transit egress



# Magic Transit egress

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/magic-transit-egress/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The suggestions in the [Minimal ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/minimal-ruleset) and [Extended ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/extended-ruleset) are recommendations for ingress (incoming) traffic. This page covers the additional consideration needed for egress (outgoing) traffic.

Cloudflare Network Firewall does not track connection state (it is not "stateful"). A stateful firewall automatically allows return traffic for active connections — for example, if you send a request outbound, the response is allowed back in. Because Network Firewall is not stateful, each packet — whether ingress or egress — is evaluated independently against your rules. This means ingress block rules can inadvertently block egress traffic.

For Magic Transit egress traffic, consider the following:

  * Network Firewall rules apply to both Magic Transit ingress and egress traffic passing through Cloudflare.

  * If you have a "default drop" catchall rule (a final rule that blocks all traffic not matched by earlier rules) for ingress traffic, you must add an earlier rule to permit traffic sourced from your Magic Transit prefix with the destination as **any** to allow outbound egress traffic.

For example, place the following allow rule before any default-drop catchall rule:

**Match** : `ip.src in {<YOUR_MAGIC_TRANSIT_PREFIX>}`   
**Action** : Allow




[PreviousExtended ruleset](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/best-practices/extended-ruleset/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/packet-filtering/best-practices/magic-transit-egress.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
