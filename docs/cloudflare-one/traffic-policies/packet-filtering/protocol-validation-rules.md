---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/protocol-validation-rules/
title: Protocol validation rules \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:15.309044+00:00
---

# Protocol validation rules · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/protocol-validation-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

  4. /Packet filtering
  5. /Protocol validation rules



# Protocol validation rules

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/protocol-validation-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Network Firewall can validate [Session Initiation Protocol (SIP) ↗︎](https://datatracker.ietf.org/doc/html/rfc2543) traffic — the protocol used to set up voice and video calls over IP networks (VoIP). This lets you inspect whether SIP packets are properly formatted and enforce a positive security model (only allow well-formed SIP traffic, block everything else).

You can use the `sip` field when creating a rule to check whether packets contain valid SIP data, a Layer 7 (L7) protocol. The `sip` field evaluates to `true` for well-formed SIP packets. Refer to [Cloudflare Network Firewall fields](https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/), specifically the `sip` field, for more information on this topic.

Currently, SIP is the only protocol supported for deep validation. Contact your account manager if you need Cloudflare Network Firewall to support additional protocols.

[PreviousForm expressions](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/form-expressions/)[NextRuleset logic](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/ruleset-logic/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/packet-filtering/protocol-validation-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
