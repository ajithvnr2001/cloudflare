---
url: https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/
title: Best practices \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:06.583983+00:00
---

# Best practices · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /Best practices



# Best practices

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

By default, Cloudflare Network Firewall (formerly Magic Firewall) permits all ingress traffic that has passed through Cloudflare's core DDoS mitigations. To proactively mitigate attacks and minimize your attack surface and leakage of attack traffic into your environment, we recommend implementing your Cloudflare Network Firewall rules using the following guidelines.

The best approach is to replicate your current ingress perimeter firewall rules in Network Firewall. If you are unable to export your current perimeter firewall rules, contact your Implementation Manager for help translating the rules into Cloudflare Network Firewall rules.

  * [Minimal ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/minimal-ruleset/)
  * [Extended ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/extended-ruleset/)
  * [Magic Transit egress](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/magic-transit-egress/)



[PreviousCollect PCAPs](https://developers.cloudflare.com/cloudflare-network-firewall/packet-captures/collect-pcaps/)[NextMinimal ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/minimal-ruleset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/best-practices/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
