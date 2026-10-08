---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/
title: Managed rulesets \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:53.157833+00:00
---

# Managed rulesets · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /Managed rulesets



# Managed rulesets

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProactive false positive detection for new rules

The DDoS Attack Protection managed rulesets provide comprehensive protection against a [variety of DDoS attacks](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/) across L3/4 (network layer) and L7 (application layer) of the [OSI model ↗︎](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/).

The available managed rulesets are:

  * **[HTTP DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/)**

    * This ruleset includes rules to detect and mitigate DDoS attacks over HTTP and HTTPS.
  * **[Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/)**

    * This ruleset includes rules to detect and mitigate DDoS attacks on L3/4 of the OSI model such as UDP floods, SYN-ACK reflection attacks, SYN Floods, and DNS floods.



* * *

## Proactive false positive detection for new rules

Note

Only available on Business and Enterprise plans.

When Cloudflare creates a new managed rule, we check the rule impact against the traffic of Business and Enterprise zones while the rule is not blocking traffic yet.

If a [false positive](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive) is detected, we proactively reach out to the affected customers and help them make configuration changes (for example, to lower the sensitivity level of the new rule) before the rule starts mitigating traffic. This prevents the new rule from causing service disruptions and outages to your Internet properties.

[PreviousAttack coverage](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/)[NextOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
