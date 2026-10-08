---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/form-expressions/
title: Form an expression \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:14.993156+00:00
---

# Form an expression · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/form-expressions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

  4. /Packet filtering
  5. /Form expressions



# Form expressions

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/form-expressions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCapabilitiesRestrictions

Rules are written using the Cloudflare Rules language - a domain-specific language (DSL) intended to mimic Wireshark semantics. For more information, refer to the [Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/) documentation.

To start with a simple case, review below how you would match a source IP. In this expression, `ip.src` refers to the source IP address of the incoming packet, and `==` means "equals":
    
    
    ip.src == 192.0.2.0

Expressions can be more complex by joining multiple clauses via a logical operator (`&&` means AND, `||` means OR). The following expression matches packets from `192.0.2.1` that also have the TCP push or reset flag set:
    
    
    ip.src == 192.0.2.1 && (tcp.flags.push || tcp.flags.reset)

## Capabilities

You can use Cloudflare Network Firewall to skip or block packets based on source or destination IP, source or destination port, protocol, packet length, or bit field match.

## Restrictions

The expression engine supports CIDR notation (IP address ranges like `192.0.2.0/24`), but only inside curly-brace sets. A bare comparison will not work as expected:
    
    
    ip.src == 192.0.2.0/24  # bad
    ip.src in { 192.0.2.0/24 }  # good

Expressions have a complexity limit that is easily reached when many joined or nested clauses are in the expression. Here's an example:
    
    
    (tcp.dstport == 1000 || tcp.dstport == 1001) && (tcp.dstport == 1002 || tcp.dstport == 1003) && (tcp.dstport == 1004 || tcp.dstport == 1005) && (tcp.dstport == 1006 || tcp.dstport == 1007) && (tcp.dstport == 1008 || tcp.dstport == 1009) && (tcp.dstport == 1010 || tcp.dstport == 1011) && (tcp.dstport == 1012 || tcp.dstport == 1013) && (tcp.dstport == 1014 || tcp.dstport == 1015) && (tcp.dstport == 1016 || tcp.dstport == 1017)

If the limit is reached, the response will have a `400` status code and an error message of `ruleset exceeds complexity constraints`. Split the expression across multiple rules and try again. Each rule can handle a subset of the conditions, and the firewall evaluates them in order.

[PreviousEnable Managed Rulesets](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/enable-managed-rulesets/)[NextProtocol validation rules](https://developers.cloudflare.com/cloudflare-one/traffic-policies/packet-filtering/protocol-validation-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/packet-filtering/form-expressions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
