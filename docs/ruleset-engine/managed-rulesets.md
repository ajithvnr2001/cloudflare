---
url: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/
title: Work with managed rulesets \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:01.335820+00:00
---

# Work with managed rulesets · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/managed-rulesets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /Work with managed rulesets



# Work with managed rulesets

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMore resources

Managed rulesets are preconfigured rulesets provided by Cloudflare that you can deploy. Only Cloudflare can modify these rulesets.

The rules in a managed ruleset have a default configuration. However, you can define [overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/) that change this default configuration.

Several Cloudflare products include managed rulesets:

  * [Web Application Firewall (WAF)](https://developers.cloudflare.com/waf/managed-rules/)
  * [DDoS Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)
  * [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-managed-rulesets/)



Check each product's documentation for details on the available managed rulesets.

## More resources

To view available managed rulesets, refer to [View rulesets](https://developers.cloudflare.com/ruleset-engine/basic-operations/view-rulesets/).

To deploy a managed ruleset to a phase, refer to [Deploy a managed ruleset](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/deploy-managed-ruleset/).

To adjust the behavior of a managed ruleset, do one of the following:

  * Customize the behavior of one or more rules by using [overrides](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/override-managed-ruleset/).
  * Skip one or more managed rules by adding [exceptions](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/create-exception/).



Exceptions (only supported by the WAF) have priority over overrides.

[PreviousDeploy rulesets](https://developers.cloudflare.com/ruleset-engine/basic-operations/deploy-rulesets/)[NextDeploy a managed ruleset](https://developers.cloudflare.com/ruleset-engine/managed-rulesets/deploy-managed-ruleset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ruleset-engine/managed-rulesets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
