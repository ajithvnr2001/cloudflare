---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/
title: Create an Advanced DDoS Protection rule \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:45.602051+00:00
---

# Create an Advanced DDoS Protection rule · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systems

  4. /How to
  5. /Create a rule



# Create a rule

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-rule/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate an Advanced DNS Protection ruleCreate an Advanced TCP Protection ruleCreate a Programmable Flow Protection rule

## Create an Advanced DNS Protection rule

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection** > **Advanced DNS Protection**.

  3. Select **Create Advanced DNS Protection rule**.

  4. In **Mode** , select a [mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#mode) for the rule.

  5. Under **Set scope** , select a [scope](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#scope) to determine the range of packets that will be affected by the rule.

  6. Under **Sensitivity** , define the [burst sensitivity](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#burst-sensitivity), [rate sensitivity](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#rate-sensitivity), and [profile sensitivity](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#profile-sensitivity) to determine when to initiate mitigation. 9. Select **Deploy**.




* * *

## Create an Advanced TCP Protection rule

To create a [SYN flood rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/#syn-flood-protection) or an [out-of-state TCP](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/#out-of-state-tcp-protection) rule:

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection** > **Advanced TCP Protection**.

  3. Depending on the rule you are creating, do one of the following:

     * Under **SYN Flood Protection** , select **Create SYN flood rule**.
     * Under **Out-of-state TCP Protection** , select **Create out-of-state TCP rule**.
  4. In **Mode** , select a [mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#mode) for the rule.

  5. Under **Set scope** , select a [scope](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#scope) for the rule. If you choose to apply the rule to a subset of incoming packets, select a region or a data center.

  6. Under **Sensitivity** , define the [burst sensitivity](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#burst-sensitivity) and [rate sensitivity](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#rate-sensitivity) of the rule (by default, _Medium_). The sensitivity levels are based on the initially configured thresholds for your specific case.

  7. Select **Deploy**.




Note

Filters take precedence over rules. For details on how the execution mode is determined, refer to [Determining the execution mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#determining-the-execution-mode).

* * *

## Create a Programmable Flow Protection rule

To create a [Programmable Flow Protection rule](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection):

  1. In the Cloudflare dashboard, go to the **L3/4 DDoS protection** page.

[ Go to **DDoS Managed Rules** ↗ ](https://dash.cloudflare.com/?to=/:account/network-security/ddos)
  2. Go to **Advanced Protection** > **Programmable Flow Protection**.

  3. In **General Settings** , select a program. The chosen program must have a status of `success`, indicating it has successfully compiled and passed verification. This field is required.

  4. In **General Settings** , select a [mode](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#mode) for the rule. This field is required.

  5. Under **Set scope** , optionally select a [scope](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/concepts/#scope) for the rule. If you choose to apply the rule to a subset of incoming packets, select a region or a data center. The default scope setting is global.

  6. Under **Set scope** , optionally select a packet filter expression. If you choose to apply a rule to a subset of incoming packets, select the IP and UDP characteristics to filter on. The default setting applies a rule to all UDP packets.

  7. Select **Deploy**.




[PreviousAdd an IP or prefix to the allowlist](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/)[NextCreate a filter](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/how-to/create-filter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/how-to/create-rule.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
