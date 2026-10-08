---
url: https://developers.cloudflare.com/learning-paths/data-center-protection/enable-network-firewall/
title: Enable Cloudflare Network Firewall \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:47.420134+00:00
---

# Enable Cloudflare Network Firewall · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/data-center-protection/enable-network-firewall/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Data Center Protection
  4. /Enable Cloudflare Network Firewall



# Enable Cloudflare Network Firewall

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/data-center-protection/enable-network-firewall/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Transit customers are automatically provided with the [standard features](https://developers.cloudflare.com/cloudflare-network-firewall/plans/#standard-features) of Cloudflare Network Firewall, Cloudflare's firewall-as-a-service product.

Cloudflare recommends creating a ruleset customized to your environment and needs. Without any rules configured, Cloudflare Network Firewall will pass on all traffic after mitigations are applied to your tunnels.

The [Extended ruleset](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/extended-ruleset/) is the best practice for reducing your attack surface by adopting a positive security model. If possible, use your current Edge Firewall policies to help you decide what ports to permit/block.

If you cannot use the extended ruleset, then use the [minimal ruleset guidance](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/minimal-ruleset/) to create a customized ruleset to block known unwanted traffic and common vectors for attack.

[PreviousConfigure DDoS protection](https://developers.cloudflare.com/learning-paths/data-center-protection/configure-ddos/)[NextEnable Notifications](https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/data-center-protection/enable-network-firewall.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
