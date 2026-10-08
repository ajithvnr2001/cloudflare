---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/
title: Configure Network-layer DDoS Attack Protection in the dashboard \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:54.152407+00:00
---

# Configure Network-layer DDoS Attack Protection in the dashboard · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)[Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/)

  4. /[Overrides](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/)
  5. /Configure in the dashboard



# Configure in the dashboard

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a DDoS override Delete a DDoS override

Configure the Network-layer DDoS Attack Protection managed ruleset by defining [overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) in the Cloudflare dashboard. DDoS overrides allow you to customize the **action** and **sensitivity** of one or more rules in the managed ruleset.

You define overrides for the Network-layer DDoS Attack Protection managed ruleset at the account level.

For more information on the available parameters and allowed values, refer to [Ruleset parameters](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/override-parameters/).

## Create a DDoS override

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Network-layer DDoS Protection**.

  3. Select **Deploy a DDoS override**.

  4. In **Set scope** , specify if you wish to apply the override to all incoming packets or to a subset of the packets.

  5. If you are creating an override for a subset of the incoming packets, define the [custom expression](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/override-expressions/) that matches the incoming packets you wish to target in the override, using either the Rule Builder or the Expression Editor.

  6. Select **Next**.

  7. Depending on what you wish to override, refer to the following sections (you can perform both configurations on the same override):

Configure all the rules in the ruleset (ruleset override)

     8. Select **Next**.
     9. Enter a name for your override in **Execution name**.
     10. To always apply a given action for all the rules in the ruleset, select an action in **Ruleset action**.
     11. To set the sensitivity level for all the rules in the ruleset, select a value in **Ruleset sensitivity**.

Configure one or more rules

     12. Search for the rules you wish to override using the available filters. You can search for tags.
     13. To override a single rule, select the desired value for a field in the displayed dropdowns next to the rule.

To configure more than one rule, select the rules using the row checkboxes and update the fields for the selected rules using the dropdowns displayed before the table. You can also configure all the rules with a given tag. For more information, refer to [Configure a managed ruleset](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset). 14\. Select **Next**. 15\. Enter a name for your override in **Execution name**.

Notes

     * Tag and rule overrides have priority over ruleset overrides.
     * The managed ruleset includes some read-only rules that you cannot override.

  8. To save and deploy the override, select **Deploy**. If you are not ready to deploy your override, select **Save as Draft**.




### Delete a DDoS override

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to the **Network-layer DDoS Protection** tab.

  3. Select the override.

  4. Select **Delete deployment**.




[PreviousOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/)[NextConfigure via API](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
