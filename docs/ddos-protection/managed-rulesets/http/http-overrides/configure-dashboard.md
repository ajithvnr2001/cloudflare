---
url: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/
title: Configure HTTP DDoS Attack Protection in the dashboard \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:53.533741+00:00
---

# Configure HTTP DDoS Attack Protection in the dashboard · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)[HTTP DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/)

  4. /[Overrides](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/)
  5. /Configure in the dashboard



# Configure in the dashboard

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccess Create a DDoS override Delete a DDoS override

Configure the HTTP DDoS Attack Protection managed ruleset by defining [overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) in the Cloudflare dashboard. DDoS overrides allow you to customize the **action** and **sensitivity** of one or more rules in the managed ruleset.

For more information on the available parameters and allowed values, refer to [Ruleset parameters](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/override-parameters/).

Number of available overrides

If you are an Enterprise customer with the Advanced DDoS Protection subscription, you can define up to 10 overrides. These overrides can have a custom expression so that the override only applies to a subset of incoming requests. If you do not have the Advanced DDoS Protection subscription, you can only deploy one override which will always apply to all incoming requests.

If you cannot deploy any additional overrides, consider editing an existing override to adjust rule configuration.

Create multiple rules in the `ddos_l7` phase entry point ruleset to define different overrides for different sets of incoming requests. Set each rule expression according to the traffic whose HTTP DDoS protection you wish to customize.

Rules in the phase entry point ruleset, where you create overrides, are evaluated in order until there is a match for a rule expression and sensitivity level, and Cloudflare will apply the first rule that matches the request. Therefore, the rule order in the entry point ruleset is very important.

## Access

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Go to the **DDoS protection** tab.

  3. On **HTTP DDoS attack protection** , select **Create override**.




### Create a DDoS override

  1. Enter a descriptive name for the override in **Override name**.

  2. If you are an Enterprise customer with the Advanced DDoS Protection subscription:

     1. Under **Override scope** , review the scope of the override — by default, all incoming requests for the current zone.
     2. If necessary, select **Edit scope** and configure the [custom filter expression](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-expressions/) that will determine the override scope.
  3. Depending on what you wish to override, refer to the following sections (you can perform both configurations on the same override):

Configure all the rules in the ruleset (ruleset override)

     4. To always apply a given action for all the rules in the ruleset, select an action in **Ruleset action**.
     5. To set the sensitivity level for all the rules in the ruleset, select a value in **Ruleset sensitivity**.

Configure one or more rules

     4. Under **Rule configuration** , select **Browse rules**.

     5. Search for the rules you wish to configure using the available filters. You can search by [tag](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/rule-categories/) (also known as category).

     6. To configure a single rule, select the desired value for a field in the displayed dropdowns next to the rule.

To configure more than one rule, select the rules using the row checkboxes and update the fields for the selected rules using the dropdowns displayed before the table. You can also configure all the rules with a given tag. For more information, refer to [Configure a managed ruleset](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset).

     7. Select **Next**.

Notes

     * Tag and rule overrides have priority over ruleset overrides.
     * The managed ruleset includes some read-only rules that you cannot override.

  4. Select **Save**.




### Delete a DDoS override

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Go to the **DDoS protection** tab.

  3. Select the override.

  4. Select **Delete deployment**.




[PreviousOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/)[NextConfigure via API](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/configure-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
