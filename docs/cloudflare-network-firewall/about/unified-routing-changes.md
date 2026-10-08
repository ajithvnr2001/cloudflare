---
url: https://developers.cloudflare.com/cloudflare-network-firewall/about/unified-routing-changes/
title: Unified Routing behavior changes \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:06.554840+00:00
---

# Unified Routing behavior changes · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/about/unified-routing-changes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /[About](https://developers.cloudflare.com/cloudflare-network-firewall/about/)
  4. /Unified Routing behavior changes



# Unified Routing behavior changes

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/about/unified-routing-changes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewip.geoip.countryRule evaluation for Layer 3 trafficRule evaluation for Layer 4 traffic

Cloudflare Network Firewall rules can behave differently depending on whether your account uses Legacy Routing or [Unified Routing](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/#how-to-upgrade-to-unified-routing). Review the following changes before you upgrade to Unified Routing.

## `ip.geoip.country`

The `ip.geoip.country` field is no longer supported on Unified Routing. Before upgrading you must either remove these rules or rewrite any rule that uses `ip.geoip.country` with the [`ip.src.country` and `ip.dst.country`](https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/#ipsrccountry) fields instead.

Match type | Rule using `ip.geoip.country` | Equivalent rule  
---|---|---  
Equals | `ip.geoip.country eq "US"` | `ip.src.country eq "US" or ip.dst.country eq "US"`  
Does not equal | `ip.geoip.country ne "US"` | `ip.src.country ne "US" and ip.dst.country ne "US"`  
In a list | `ip.geoip.country in {"UK" "FR"}` | `ip.src.country in {"UK" "FR"} or ip.dst.country in {"UK" "FR"}`  
Not in a list | `not ip.geoip.country in {"UK" "FR"}` | `not ip.src.country in {"UK" "FR"} and not ip.dst.country in {"UK" "FR"}`  
  
## Rule evaluation for Layer 3 traffic

Legacy Routing has limited support for Layer 3 protocols. IPv6 support is limited to the `ip.src` and `ip.dst` fields. A rule is either exclusively applied to IPv4 packets or exclusively applied to IPv6 packets, based on the address family of the literal used in the rule.

On Unified Routing, as a first step to supporting IPv6 more broadly, a rule that only matched IPv6 traffic in Legacy Routing may also be evaluated against IPv4 traffic.

Rule | Routing mode | Behavior for IPv4 | Behavior for IPv6  
---|---|---|---  
`ip.src ne fe80::/64` | Legacy | IPv4 packets skip this rule | Matches for all traffic not sourced from `fe80::/64`  
`ip.src ne fe80::/64` | Unified | Matches for all traffic | Matches for all traffic not sourced from `fe80::/64`  
  
To restrict the rule to only match IPv6 traffic, update the expression to `ip.src in {::/0} and ip.src ne fe80::/64`.

IPv6 behavior is unchanged from Legacy Routing.

## Rule evaluation for Layer 4 traffic

On Legacy Routing, the Layer 4 protocol is inferred from the expression and only applied to packets of that protocol. `tcp.srcport eq 80` and `tcp.srcport ne 80` both apply only to TCP traffic. Packets of other protocols, for example UDP, will not match the expression.

On Unified Routing, Cloudflare Network Firewall does not infer the protocol, and rules must specify a protocol in the expression explicitly. `tcp.srcport eq 80` still only applies to TCP traffic, but `tcp.srcport ne 80` now matches both TCP and UDP traffic. To restrict the rule to only match TCP traffic, update the expression to `ip.proto eq "tcp" and tcp.srcport eq 80`.

[PreviousTraffic types](https://developers.cloudflare.com/cloudflare-network-firewall/about/traffic-types/)[NextForm expressions](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/form-expressions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/about/unified-routing-changes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
