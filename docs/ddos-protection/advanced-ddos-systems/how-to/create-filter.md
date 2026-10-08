---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/
title: Create a filter for Advanced TCP Protection \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.716880+00:00
---

# Create a filter for Advanced TCP Protection · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /How to
  5. /Create a filter



# Create a filter

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcedure

A filter modifies Advanced TCP Protection's [execution mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#mode) — monitoring, mitigation (enabled), or disabled — for all incoming packets matching an expression.

Each protection system component (SYN flood protection or out-of-state TCP protection) should have at least one [rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#rule), but filters are optional.

Note

Filters only apply to Advanced TCP Protection.

## Procedure

To create a [filter](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#filter) for one of the system components:

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection** > **Advanced TCP Protection**.

  3. Under the system component for which you are creating the filter (**SYN Flood Protection** or **Out-of-state TCP Protection**), select **Create** next to the type of filter you want to create:

     * **Mitigation Filter** : The protection system will drop packets matching the filter expression. - **Monitoring Filter** : The protection system will log packets matching the filter expression.
     * **Off Filter** : The protection system will ignore packets matching the filter expression.
  4. Under **When incoming packets match** , define a filter expression using the Expression Builder (specifying one or more values for **Field** , **Operator** , and **Value**), or manually enter an expression using the Expression Editor. For more information, refer to [Edit rule expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/).

  5. Select **Save**.




Note

Filters take precedence over rules. For details on how the execution mode is determined, refer to [Determining the execution mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#determining-the-execution-mode).

[PreviousCreate a rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/)[NextExclude a prefix](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/exclude-prefix/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/how-to/create-filter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
