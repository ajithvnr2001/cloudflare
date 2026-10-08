---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/rule-categories/
title: Rule categories \u2014 Network-layer DDoS \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:54.383998+00:00
---

# Rule categories — Network-layer DDoS · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/rule-categories/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)

  4. /[Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/)
  5. /Rule categories



# Rule categories

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/rule-categories/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The main categories (or tags) of Network-layer DDoS Attack Protection managed rules are the following:

Name | Description  
---|---  
`gre` | Rules for DDoS attacks over Generic Routing Encapsulation (GRE) that usually target GRE endpoints.  
`esp` | Rules for DDoS attacks related to the Encapsulating Security Payload (ESP) protocol, which is part of the IPsec secure network protocol suite.  
`advanced` | Rules related to features available to Enterprise customers, such as [Adaptive DDoS Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/).  
`generic` | Rules for detecting and mitigating floods of packets. These rules are useful for mitigating attacks that have no known signatures, but they may also trigger on unusually high volumes of legitimate traffic. To reduce the risk of false positives, their packet per second (pps) activation threshold is higher. These rules rate-limit traffic by default, but you can override them to block traffic if necessary.  
`read-only` | Highly targeted rules for mitigating DDoS attacks with a high confidence rate. These rules are read-only — you cannot override their sensitivity level or action.  
`test` | Rules used for testing the detection, mitigation, and alerting capabilities of Cloudflare's DDoS protection products.  
  
There are other rule categories based on the attack vector/protocol, such as `dns`, `quic`, and `sip`. The categories list is dynamic and may change over time.

[PreviousParameters](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/override-parameters/)[NextOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/network/rule-categories.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
