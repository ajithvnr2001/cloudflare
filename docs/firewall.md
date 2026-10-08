---
url: https://developers.cloudflare.com/firewall/
title: Cloudflare Firewall Rules (deprecated) \u00b7 Cloudflare Firewall Rules (deprecated) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.586105+00:00
---

# Cloudflare Firewall Rules (deprecated) · Cloudflare Firewall Rules (deprecated) docs

> Source: https://developers.cloudflare.com/firewall/

  1. [Home](https://developers.cloudflare.com/)
  2. /Firewall Rules (deprecated)



# Cloudflare Firewall Rules

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/firewall/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMain featuresAvailabilityNext stepsRelated resources

Cloudflare Firewall Rules allows you to create rules that inspect incoming traffic and block, challenge, log, or allow specific requests.

Deprecation notice

Cloudflare Firewall Rules has been deprecated. Cloudflare has moved existing firewall rules to [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/). For more information on this change, refer to the [upgrade guide](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/).

## Main features

  * **Rule-based protection** : Use pre-defined rulesets provided by Cloudflare, or define your own firewall rules. Create rules in the Cloudflare dashboard or via API.
  * **Complex custom rules** : Each rule's expression can reference multiple fields from all the available HTTP request parameters and fields, allowing you to create complex rules.



## Availability

This table outlines the Firewall Rules features and entitlements available with each customer plan:

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Number of rules | 5 | 20 | 100 | 1,000  
Supported actions | All except Log | All except Log | All except Log | All  
Regex support | No | No | Yes | Yes  
  
## Next steps

  * Unless you are already an advanced user, refer to [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/) and [Actions](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/) to learn more about the basic elements of firewall rules.

  * To start building your own firewall rules, refer to one of the following pages:

    * [Manage firewall rules in the dashboard](https://developers.cloudflare.com/firewall/cf-dashboard/create-edit-delete-rules/)
    * [Manage firewall rules via the APIs](https://developers.cloudflare.com/firewall/api/)
  * You can also manage firewall rules through Terraform. For more information, refer to [Getting Started with Terraform ↗︎](https://blog.cloudflare.com/getting-started-with-terraform-and-cloudflare-part-1/).




## Related resources

  * [Cloudflare Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)



[NextOverview](https://developers.cloudflare.com/firewall/cf-firewall-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/firewall/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
