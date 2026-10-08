---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/override-parameters/
title: Network-layer DDoS Attack Protection parameters \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:54.443861+00:00
---

# Network-layer DDoS Attack Protection parameters · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/override-parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)

  4. /[Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/)
  5. /Parameters



# Parameters

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/override-parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActionSensitivity Level

Define overrides for the Network-layer DDoS Attack Protection managed ruleset to change the action applied to a given attack or modify the sensitivity level of the detection mechanism. You can [define overrides in the Cloudflare dashboard](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/) or [define overrides via Rulesets API](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-api/).

The available parameters are the following:

  * Action
  * Sensitivity Level



## Action

API property name: `"action"`.

The action performed for packets that match specific rules of Cloudflare's DDoS mitigation services. The available actions are:

  * **Log**

    * API value: `"log"`.
    * Only available on Enterprise plans. Logs requests that match the expression of a rule detecting network layer DDoS attacks. Recommended for validating a rule before committing to a more severe action. 

Refer to the [Analytics documentation](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/#view-logged-or-monitored-traffic) for more information on how to view logged or monitored traffic.

  * **Block**

    * API value: `"block"`.
    * Blocks IP packets that match the rule expression given the sensitivity levels.
  * **DDoS Dynamic**

    * API value: _N/A_ (internal rule action that you cannot use in overrides).
    * Performs a specific action according to a set of internal guidelines defined by Cloudflare. The executed action can be _Block_ or an undisclosed mitigation action.



## Sensitivity Level

API property name: `"sensitivity_level"`.

Defines how sensitive a rule is. Affects the thresholds used to determine if an attack should be mitigated. A higher sensitivity level means having a lower threshold, while a lower sensitivity level means having a higher threshold.

The available sensitivity levels are:

UI value | API value  
---|---  
_High_ | `"default"`  
_Medium_ | `"medium"`  
_Low_ | `"low"`  
_Essentially Off_ | `"eoff"`  
  
The default sensitivity level is _High_.

In most cases, when you select the _Essentially Off_ sensitivity level the rule will not trigger for any of the selected actions, including _Log_. However, if the attack is extremely large, Cloudflare's protection systems will still trigger the rule's mitigation action to protect Cloudflare's network.

_Essentially Off_ means that we have set an exceptionally low sensitivity level so in most cases traffic will not be mitigated for you. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.

**Log** means that requests will not be mitigated but only logged and shown on the dashboard. However, attack traffic will be mitigated at exceptional levels to ensure the safety and stability of the Cloudflare network.

[PreviousOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/)[NextRule categories](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/rule-categories/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/network/override-parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
